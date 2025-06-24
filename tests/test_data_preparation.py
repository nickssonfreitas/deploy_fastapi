import pandas as pd
import numpy as np
from src.ml.data_preparation import process_data

def test_process_data():
    data = pd.DataFrame({
        'age': [25, 32],
        'workclass': ['Private', 'Self-emp'],
        'education': ['Bachelors', 'Masters'],
        'marital-status': ['Never-married', 'Married'],
        'occupation': ['Tech-support', 'Exec-managerial'],
        'relationship': ['Not-in-family', 'Husband'],
        'race': ['White', 'Black'],
        'sex': ['Male', 'Female'],
        'native-country': ['United-States', 'Canada'],
        'salary': ['<=50K', '>50K']
    })

    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    X, y, encoder, lb = process_data(
        data, categorical_features=cat_features, label="salary", training=True
    )

    assert X.shape[0] == data.shape[0]
    assert len(y) == data.shape[0]
    assert encoder is not None
    assert lb is not None