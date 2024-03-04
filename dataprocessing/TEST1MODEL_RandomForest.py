from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Sample data (replace with your dataset)
# code_snippets = [
#     "$b = $_GET['q']; $sql = `SELECT * FROM table WHERE id = ${b}`;",  # SQL Injection
#     "$input = $_POST['name']; echo 'Hello, ' . $input;",  # No vulnerability
#     "$user_input = $_GET['query']; echo 'Search results for: ' . $user_input;",  # XSS
#     "$cmd = $_GET['cmd']; system($cmd);",  # Command Injection
#     "$username = $_POST['username']; $password = $_POST['password']; login($username, $password);"  # Bypassing input validation,
#     "var test_string = \"Bad characters: $@#\";var bad_pattern = /^(\w+\s?)*$/i;var result = test_string.search(bad_pattern);", # Bypassing input validation
# ]

# # 0: No vulnerability, 1: XSS, 2: Command/Code Injection, 3: Prototype Pollution, 4: File Inclusion, 5: SQL Injection, 6: Bypassing input validation, 7: Excessive data exposure
# labels = [2, 0, 1, 3, 4, 4]  

# Generate 200 unique code snippets with 5 different labels including non-vulnerable code

# use datasets.csv
code_snippets = []
labels = []
with open('datasets.csv', 'r') as file:
    data = file.readlines()
    # separate the data by ::::: delimiter
    for line in data:
        line = line.split(':::::')
        code_snippets.append(line[0])
        labels.append(int(line[1]))


# shuffle the data
from sklearn.utils import shuffle
code_snippets, labels = shuffle(code_snippets, labels, random_state=0)

# Feature extraction
vectorizer = CountVectorizer(binary=True, ngram_range=(1, 2), token_pattern=r'\b\w+\b')
X = vectorizer.fit_transform(code_snippets)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Evaluate model
y_pred = rf_classifier.predict(X_val)
print("Classification Report:")
print("LEGENDS: 0: No vulnerability, 1: XSS, 2: Command/Code Injection, 3: Prototype Pollution, 4: File Inclusion, 5: SQL Injection, 6: Bypassing input validation, 7: Excessive data exposure\n")
print(classification_report(y_val, y_pred))

print("="*50)
print("TEST SAMPLES:\n")
print("[5] - SQL injection Prediction Test & [0] - Non Vulnerable Prediction Test\n")
print("="*50)
print("PHP\n")
# Example prediction with SQL Injection in PHP
new_code_snippet = ["$a = $_GET['id']; $b = `SELECT * FROM users WHERE id = ${a}`"]
X_new = vectorizer.transform(new_code_snippet)
prediction = rf_classifier.predict(X_new)
print("Vulnerable Prediction:", prediction) # Output: [5] (SQL Injection)

# Example prediction with Non vulnerable code to SQL Injection  in PHP
new_code_snippet = "$username = $_POST['username']; $password = $_POST['password']; $stmt = $connection->prepare(\"SELECT * FROM users WHERE username=? AND password=?\");"
X_new = vectorizer.transform([new_code_snippet])
prediction = rf_classifier.predict(X_new)
print("None Vulnerable Prediction:", prediction)  # Output: [0] (No vulnerability)

print("="*50)
print("JavaScript\n")
# Example prediction with SQL Injection in JavaScript
new_code_snippet = ["var id = req.params.id; var query = 'SELECT * FROM users WHERE id = ' + id;"]
X_new = vectorizer.transform(new_code_snippet)
prediction = rf_classifier.predict(X_new)
print("Vulnerable Prediction:", prediction)  # Output: [5] (SQL Injection)

# Example prediction with Non vulnerable code to SQL Injection  in JavaScript
new_code_snippet = "var id = req.params.id; var query = 'SELECT * FROM users WHERE id = ?';"
X_new = vectorizer.transform([new_code_snippet])
prediction = rf_classifier.predict(X_new)
print("None Vulnerable Prediction:", prediction)  # Output: [0] (No vulnerability)



