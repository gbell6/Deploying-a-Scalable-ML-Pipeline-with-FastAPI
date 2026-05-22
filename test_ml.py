import pytest
import os
import numpy as np
import pandas as pd
# TODO: add necessary import
from ml.model import save_model, load_model, inference
from ml.data import process_data, apply_label

@pytest.fixture
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data

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


def test_data_processing_output_format(data):
    """
    This test checkes that the output values returned by data.process_data() are the expected numpy arrays.

    input:
        - data:
            taken from the pytest.fixture above, which returns the census.csv data as a Pandas.DataFrame
    """
    test_feats, test_label, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label='salary',
    )

    assert all(isinstance(i, np.ndarray) for i in [test_feats, test_label])



# Fixture for the arrange/teardown phases of the test_save_model_function()
@pytest.fixture
def save_path():
    test_data = 'simple testing of save_model functionality'
    test_path = os.getcwd()
    save_path = os.path.join(test_path, 'test.pkl')

    save_model(test_data, save_path)

    yield save_path

    os.remove(save_path)


def test_save_model_function(save_path):
    """
    Test to make sure that save_model properly saves the file the specified place within the project directory.
    The fixture above will automatically remove the test file once the test is executed.
    """
    assert os.path.exists(save_path) == True



@pytest.fixture
def pred():
    dummy_data = pd.DataFrame([{
        'age': 29,
        'workclass': 'Private',
        'fnlgt': 160187,
        'education': 'Bachelors',
        'education-num': 12,
        'marital-status': 'Unmarried',
        'occupation': 'Other-service',
        'relationship': 'Single',
        'race': 'black',
        'sex': 'male',
        'capital-gain': 10,
        'capital-loss': 0,
        'hours-per-week': 55,
        'native-country': "United States"
    }])
    mod_path = os.path.join(os.getcwd(), 'model', 'model.pkl')
    model = load_model(mod_path)
    enc_path = os.path.join(os.getcwd(), 'model', 'encoder.pkl')
    encoder = load_model(enc_path)
    X, _, _, _ = process_data(
        dummy_data,
        categorical_features=cat_features,
        training=False,
        encoder=encoder
    )
    pred = inference(model, X)
    return pred


def test_label_application(pred):
    """
    This test checks that apply_label works properly given the output of inference(). The fixture above creates some dummy data, and runs a quick inference on that dummy data to provide a prediction, which is passed to test_label_application(). test_label_application() then runs the prediction straight into apply_label() and checks that the output is a string (instead of an integer, which is returned by inference()).
    """
    # Your code here
    pred_str = apply_label(pred)
    assert type(pred_str) is str
    
