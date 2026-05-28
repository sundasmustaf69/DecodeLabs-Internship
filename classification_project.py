# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_data.csv")

# Show dataset
print("Dataset:")
print(data)

# Features (Input)
X = data[["study_hours", "attendance", "sleep_hours", "previous_marks"]]

# Target (Output)
y = data["result"]

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nPredictions:")
print(predictions)

print("\nActual Results:")
print(y_test.values)

print("\nModel Accuracy:")
print(accuracy * 100, "%")

# Custom student data
custom_data = pd.DataFrame(
    [[5, 80, 7, 60]],
    columns=["study_hours", "attendance", "sleep_hours", "previous_marks"]
)

# Predict custom result
prediction = model.predict(custom_data)

print("\nCustom Student Prediction:")
print(prediction[0])