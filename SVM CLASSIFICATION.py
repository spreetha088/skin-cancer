import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Load the HAM10000 dataset from a CSV file
df = pd.read_csv('C:/Users/ELCOT/Desktop/mini project paper/HAM10000_metadata.csv')  # Replace with your dataset path

# Handle missing values by dropping rows with missing data
df.dropna(inplace=True)

# Encode categorical columns (assuming 'dx' is your target variable)
df_encoded = pd.get_dummies(df, columns=['dx_type', 'sex', 'localization'])

# Scale the 'age' column to a range between 0 and 1
scaler = MinMaxScaler()
df_encoded['age'] = scaler.fit_transform(df_encoded[['age']])

# Assuming you want to classify 'mel' (malignant) vs. 'not mel' (not malignant)
# Create a binary target variable
df_encoded['is_mel'] = (df_encoded['dx'] == 'mel').astype(int)

# Drop the 'lesion_id' and 'image_id' columns as they are not relevant for classification
df_encoded.drop(columns=['lesion_id', 'image_id'], inplace=True)

# Split the data into features (X) and the binary target variable (y)
X = df_encoded.drop(columns=['dx', 'is_mel'])  # Features
y = df_encoded['is_mel']  # Target variable

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Create and train the SVM model
svm_classifier = SVC(kernel='linear', random_state=42)  # You can choose the appropriate kernel
svm_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_test_pred = svm_classifier.predict(X_test)

# Evaluate the model on the test set
test_accuracy = accuracy_score(y_test, y_test_pred)
test_report = classification_report(y_test, y_test_pred)

# Print the evaluation metrics for the test set
print(f'Test Accuracy: {test_accuracy}')
print('Test Classification Report:')
print(test_report)

# Oversampling using SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Undersampling using RandomUnderSampler
undersampler = RandomUnderSampler(random_state=42)
X_train_resampled, y_train_resampled = undersampler.fit_resample(X_train_resampled, y_train_resampled)

# Train the model on the resampled data
svm_classifier.fit(X_train_resampled, y_train_resampled)

# Make predictions on the test set with the resampled model
y_test_resampled_pred = svm_classifier.predict(X_test)

# Evaluate the resampled model on the test set
test_resampled_accuracy = accuracy_score(y_test, y_test_resampled_pred)
test_resampled_report = classification_report(y_test, y_test_resampled_pred)

# Print the evaluation metrics for the resampled test set
print(f'Resampled Test Accuracy: {test_resampled_accuracy}')
print('Resampled Test Classification Report:')
print(test_resampled_report)
