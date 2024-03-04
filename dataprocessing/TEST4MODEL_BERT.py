from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, Dataset
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

# Sample data (replace with your dataset)
# code_snippets = [
#     "$b = $_GET['q']; $sql = `SELECT * FROM table WHERE id = ${b}`",  # SQL Injection
#     "$input = $_POST['name']; echo 'Hello, ' . $input;",  # No vulnerability
#     "$user_input = $_GET['query']; echo 'Search results for: ' . $user_input;",  # XSS
#     "$cmd = $_GET['cmd']; system($cmd);",  # Command Injection
#     "$username = $_POST['username']; $password = $_POST['password']; login($username, $password);"  # Bypassing input validation
# ]
# labels = [2, 0, 1, 3, 4]  # 0: No vulnerability, 1: XSS, 2: Command Injection, 3: SQL Injection, 4: Bypassing input validation

code_snippets = []
labels = []
with open('datasets.csv', 'r') as file:
    data = file.readlines()
    # separate the data by ::::: delimiter
    for line in data:
        line = line.split(':::::')
        code_snippets.append(line[0])
        labels.append(int(line[1]))

from sklearn.utils import shuffle
code_snippets, labels = shuffle(code_snippets, labels, random_state=0)

# Split data into training and validation sets
train_texts, val_texts, train_labels, val_labels = train_test_split(code_snippets, labels, test_size=0.2, random_state=42)

# Define a custom Dataset class
class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]

        encoding = self.tokenizer(text, add_special_tokens=True, truncation=True, max_length=self.max_length, padding='max_length', return_tensors='pt')
        input_ids = encoding['input_ids'].squeeze(0)
        attention_mask = encoding['attention_mask'].squeeze(0)

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': torch.tensor(label, dtype=torch.long)
        }

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(set(labels)))

# Define training parameters
batch_size = 4
max_length = 128
learning_rate = 2e-5
num_epochs = 3

# Create DataLoader for training and validation sets
train_dataset = CustomDataset(train_texts, train_labels, tokenizer, max_length)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = CustomDataset(val_texts, val_labels, tokenizer, max_length)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Define optimizer and loss function
optimizer = AdamW(model.parameters(), lr=learning_rate)
loss_fn = torch.nn.CrossEntropyLoss()

# Training loop
for epoch in range(num_epochs):
    model.train()
    for batch in train_loader:
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    val_preds = []
    val_true = []
    for batch in val_loader:
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']

        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits

        preds = np.argmax(logits.detach().numpy(), axis=1)
        val_preds.extend(preds)
        val_true.extend(labels.numpy())

    print("Epoch:", epoch + 1)
    print("Validation Report:")
    print(classification_report(val_true, val_preds))

# Prediction
new_code_snippet = ["$input = $_GET['id']; $sql = `SELECT * FROM users WHERE id = ${input}`"]
encoding = tokenizer(new_code_snippet, add_special_tokens=True, truncation=True, max_length=max_length, padding='max_length', return_tensors='pt')

with torch.no_grad():
    outputs = model(**encoding)
    logits = outputs.logits

prediction = np.argmax(logits.detach().numpy(), axis=1)
print("Prediction:", prediction)  # Output: [3] (SQL Injection)