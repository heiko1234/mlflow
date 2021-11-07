
# Check if we can find a model
# https://www.mlflow.org/docs/latest/model-registry.html#fetching-an-mlflow-model-from-the-model-registry



# Imports
from dotenv import load_dotenv
from mlflow.tracking import MlflowClient
from pprint import pprint


# take environment variables from .env.
load_dotenv() 


# just run this locally to check if you have a registed model and set your env variables correctly
client = MlflowClient()
for rm in client.list_registered_models():
    pprint(dict(rm), indent=4)
