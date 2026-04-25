# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Step 1: Create Dataset
# -----------------------------

data = {
    "study_hours": [2, 5, 1, 6, 3, 7, 4, 8, 2, 6, 1, 5, 3, 7, 2],
    "attendance": [50, 80, 40, 90, 60, 85, 70, 95, 55, 88, 45, 78, 65, 92, 50],
    "previous_grade": [40, 70, 35, 85, 60, 80, 65, 90, 50, 82, 30, 75, 68, 88, 45],
    "internet_access": [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    "family_income": [1, 3, 1, 3, 2, 3, 2, 3, 1, 3, 1, 2, 2, 3, 1],
    "dropout": [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())

# -----------------------------
# Step 2: Data Visualization
# -----------------------------
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Step 1: Create Dataset
# -----------------------------

data = {
    "study_hours": [2, 5, 1, 6, 3, 7, 4, 8, 2, 6, 1, 5, 3, 7, 2],
    "attendance": [50, 80, 40, 90, 60, 85, 70, 95, 55, 88, 45, 78, 65, 92, 50],
    "previous_grade": [40, 70, 35, 85, 60, 80, 65, 90, 50, 82, 30, 75, 68, 88, 45],
    "internet_access": [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    "family_income": [1, 3, 1, 3, 2, 3, 2, 3, 1, 3, 1, 2, 2, 3, 1],
    "dropout": [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())

# -----------------------------
# Step 2: Data Visualization
# -----------------------------

# Bar chart of dropout vs non-dropout
dropout_counts = df["dropout"].value_counts()

plt.figure()
dropout_counts.plot(kind='bar')
plt.title("Dropout vs Non-Dropout Students")
plt.xlabel("0 = Not Dropout, 1 = Dropout")
plt.ylabel("Count")
plt.savefig("dropout_distribution.png")
plt.show()


# Scatter plot: Study Hours vs Previous Grade
plt.figure()
plt.scatter(df["study_hours"], df["previous_grade"])

plt.xlabel("Study Hours")
plt.ylabel("Previous Grade")
plt.title("Study Hours vs Previous Grade")

plt.grid()
plt.show()
# -----------------------------
# Step 3: Prepare Data
# -----------------------------

X = df.drop("dropout", axis=1)
y = df["dropout"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Step 4: Train Model
# -----------------------------

model = LogisticRegression()
model.fit(X_train, y_train)

# -----------------------------
# Step 5: Predictions
# -----------------------------

y_pred = model.predict(X_test)

# -----------------------------
# Step 6: Evaluation
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# Step 7: Predict New Student
# -----------------------------

# Example new student
new_student = [[3, 60, 55, 1, 2]]  
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nPrediction: This student is at RISK of dropout")
else:
    print("\nPrediction: This student is NOT at risk")
# Bar chart of dropout vs non-dropout
dropout_counts = df["dropout"].value_counts()

plt.figure()
dropout_counts.plot(kind='bar')
plt.title("Dropout vs Non-Dropout Students")
plt.xlabel("0 = Not Dropout, 1 = Dropout")
plt.ylabel("Count")
plt.savefig("dropout_distribution.png")
plt.show()

# -----------------------------
# Step 3: Prepare Data
# -----------------------------

X = df.drop("dropout", axis=1)
y = df["dropout"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Step 4: Train Model
# -----------------------------

model = LogisticRegression()
model.fit(X_train, y_train)

# -----------------------------
# Step 5: Predictions
# -----------------------------

y_pred = model.predict(X_test)

# -----------------------------
# Step 6: Evaluation
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# Step 7: Predict New Student
# -----------------------------

# Example new student
new_student = [[3, 60, 55, 1, 2]]  
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nPrediction: This student is at RISK of dropout")
else:
    print("\nPrediction: This student is NOT at risk")