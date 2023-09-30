import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the HAM10000 dataset from a CSV file
df = pd.read_csv('C:/Users/ELCOT/Desktop/mini project paper/HAM10000_metadata.csv')

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

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the validation set
y_val_pred = model.predict(X_val)

# Evaluate the model on the validation set
accuracy = accuracy_score(y_val, y_val_pred)
report = classification_report(y_val, y_val_pred)

# Print the evaluation metrics
print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)

# Now, you can fine-tune the model, evaluate it on the test set, and make predictions for real-world data.
