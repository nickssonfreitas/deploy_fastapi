import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.ml.data_preparation import process_data
from src.ml.model import (
    save_model,
    train_model
)
# load the cencus.csv data
PROJECT_PATH = "/home/nicksson/Git/deploy_fastapi/"
DATA_PATH = os.path.join(PROJECT_PATH, "data", "census_cleaned_data.csv")

print(DATA_PATH)
data = pd.read_csv(DATA_PATH) # your code here
print(f"Sucessfully loaded the dataset from: {DATA_PATH}")
print(f"The shape of the dataset:", data.shape)
#print(f"The columns in the dataset:", data.columns)


# split the provided data to have a train dataset and a test dataset
# Split into Train (24,000) & Test (6,000)
# Stratification ensures class distribution is preserved in train and test sets.
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42, stratify=data['salary'])
print("The shape of the training data:", train_data.shape)
print("The shape of the test data:", test_data.shape)


# Save test data for evaluation
test_data_path = os.path.join(PROJECT_PATH, "data", "test_data.csv")
test_data.to_csv(test_data_path, index=False)
print("Train-Test Split Done! Test data saved for evaluation.")


# DO NOT MODIFY
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# use the process_data function provided to process the data.
X_train, y_train, encoder, lb = process_data(
    X=train_data,
    categorical_features=cat_features,
    label="salary",
    training=True
    )


# use the train_model function to train the model on the training dataset
# Best Parameters: {'colsample_bytree': 0.8, 'learning_rate': 0.2, 'max_depth': 3, 'n_estimators': 100, 'subsample': 0.8}
model = train_model(X_train, y_train)

print("Saving model of type:", type(model))


# save the model and the encoder
model_path = os.path.join(PROJECT_PATH, "model", "model.pkl")
save_model(model, model_path)
encoder_path = os.path.join(PROJECT_PATH, "model", "encoder.pkl")
save_model(encoder, encoder_path)
lb_path = os.path.join(PROJECT_PATH, "model", "label_encoder.pkl")
save_model(lb, lb_path)



