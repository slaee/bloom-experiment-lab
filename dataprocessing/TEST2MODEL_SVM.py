from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

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

# Feature extraction
vectorizer = CountVectorizer(binary=True, ngram_range=(1, 2), token_pattern=r'\b\w+\b')
X = vectorizer.fit_transform(code_snippets)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train SVM classifier
svm_classifier = SVC(kernel='linear', C=1, gamma='auto', random_state=42)
svm_classifier.fit(X_train, y_train)

# Evaluate model
y_pred = svm_classifier.predict(X_val)
print("Classification Report:")
print(classification_report(y_val, y_pred))

# Example prediction
new_code_snippet = ["$input = $_GET['id']; $sql = `SELECT * FROM users WHERE id = ${input}`"]
X_new = vectorizer.transform(new_code_snippet)
prediction = svm_classifier.predict(X_new)
print("Prediction:", prediction)  # Output: [3] (SQL Injection)
