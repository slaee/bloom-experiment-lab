import pandas as pd
import re
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
from sklearn.model_selection import train_test_split
import numpy as np
import torch_geometric.transforms as T
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix

# Step 1: Load CSV data
df = pd.read_csv('dataprocessing_dataset.csv')

# Step 2: Extract features (X) and target labels (y)
X = torch.tensor(df.iloc[:, :-6].values, dtype=torch.float)
y = torch.tensor(df.iloc[:, -6:].values, dtype=torch.float)  # Convert target labels to float

# Step 3: Prepare the graph data
data = Data(x=X, y=y)
data = T.NormalizeFeatures()(data)
data = T.ToSparseTensor()(data)

# Define the number of features based on processed data
num_features = data.num_features

# Define the edges based on the complete graph approach
edges = []
for i in range(num_features):
    for j in range(i + 1, num_features):  # Connect nodes that are consecutive
        edges.append([i, j])

# Convert edges to a NumPy array
edges = np.array(edges).T

# Convert edges to PyTorch tensor with dtype=torch.long
edge_index = torch.tensor(edges, dtype=torch.long)

# Step 4: Define the GNN architecture
class GCN(nn.Module):
    def __init__(self):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(num_features, 64)  # Adjust input dimension
        self.conv2 = GCNConv(64, 64)
        self.fc = nn.Linear(64, 6)  # Adjust output dimension to match number of classes

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, training=self.training, p=0.2)  # Add dropout for regularization
        x = F.relu(self.conv2(x, edge_index))
        x = self.fc(x)
        return x

# Step 5: Train the GCN model
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the model
model = GCN()

# Define the loss function and optimizer (consider adjusting learning rate if needed)
criterion = nn.BCEWithLogitsLoss()  # Binary cross-entropy loss for multi-label classification
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    model.train()
    optimizer.zero_grad()
    output = model(X_train, edge_index)
    loss = criterion(output, y_train)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)  # Gradient clipping
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch: {epoch+1}, Loss: {loss:.4f}")

# Evaluate the model
model.eval()
with torch.no_grad():
    output = model(X_test, edge_index)
    pred = (torch.sigmoid(output) > 0.5).int()  # Threshold probabilities to get binary predictions
    correct = (pred == y_test).sum().item()
    total = y_test.size(0) * y_test.size(1)
    accuracy = correct / total
    print("Test Accuracy:", accuracy)

# Preprocess input function
def preprocess_input(input_string):
    # Convert input string to lowercase
    input_string = input_string.lower()
    
    # Tokenize input string (split by whitespace and special characters)
    tokens = re.findall(r"[\w']+|[.,!?;]", input_string)
    
    # Construct feature vector based on tokens
    features = torch.zeros(num_features)  # Initialize feature vector with zeros
    for token in tokens:
        # Update feature vector based on token presence
        if token in df.columns:
            features[df.columns.get_loc(token)] = 1  # Set the corresponding feature to 1 if token exists in the dataset
    return features

# Define function to predict vulnerabilities
def predict_vulnerability(input_string):
    # Preprocess input
    input_features = preprocess_input(input_string)
    
    # Perform prediction
    model.eval()
    with torch.no_grad():
        output = model(input_features.unsqueeze(0), edge_index)  # Unsqueeze to add batch dimension
        pred_probs = torch.sigmoid(output)
        predicted_classes = (pred_probs > 0.5).int().squeeze().tolist()
    return predicted_classes

# Define function to map predicted output to vulnerability types
def map_to_vulnerability(predicted_classes):
    vulnerabilities = ['SQL Injection', 'XSS', 'CSRF', 'Command Injection', 'Path Traversal', 'Remote Code Execution']
    detected_vulnerabilities = [vulnerabilities[i] for i, pred in enumerate(predicted_classes) if pred == 1]
    return detected_vulnerabilities

# Sample input
input_code = "$input = $_GET['id']; $sql = `SELECT * FROM users WHERE id = ${input}`"

# Predict vulnerabilities
predicted_classes = predict_vulnerability(input_code)

# Map predicted output to vulnerability types
detected_vulnerabilities = map_to_vulnerability(predicted_classes)

print("Detected Vulnerabilities:", detected_vulnerabilities)

