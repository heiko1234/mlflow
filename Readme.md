



# mlflow-azurite-postgres docker

This is a MLFLow image which works with a postgres DB and a local Azure Blob Storage Instance (Azurite).

This image is designed to track local created Machine Learning Models with MLFlow on your own machine.



# How to install and set it up

Download or copy the Repos to your computer.

Go to your folder and run 

```

docker-compose up --build

```




# Clean Up

If you need to remove all old work like blob storage data and MLFlow metadata (yes, pickle files and so on) from the PostgreSQL DB, you can use the following. 
Please go to your folder where your docker-compose file is and run

```
docker-compose down -v
```




It will be neccessary to push your model to this docker compose system. 

## Linux

```

export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://localhost:10000/devstoreaccount1;QueueEndpoint=http://localhost:10001/devstoreaccount1"

export MLFLOW_TRACKING_URI="http://localhost:5000"

```

## Windows
```
set AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://localhost:10000/devstoreaccount1;QueueEndpoint=http://localhost:10001/devstoreaccount1"


set MLFLOW_TRACKING_URI=http://localhost:5000

```


It is easyier to keep these things in an `.env` file that VS Code can use.


# Run a model training and store the artifacts

Go to your project folder set the variables like describted abouve for your system and run in your cmd shell (not python shell or powershell) while you have your .venv activated

```
(.venv) ~/mlflow/get_model_from_mlflow/Fast_Check_of_Registed_Models.py


```
A successful trainings run with storage can look like this when printing the model id. This id you can find in the mlflow tracking server as well.




# How to get used while MLFlow is in a docker on your machine

You can access MLFlow (Docker) via your webbrowser and `localhost:5000` as web adress.




# Trouble shooting

## Known Problems and Solutions

It can happen that the docker is created correctly but you cannot track your artifacts. One solution that worked was to rename the storage container e.g. azurite to blobstorage or postgres_db to postgres. Make sure you rename all these things. It is strongly depending on your docker version if this works or not. It was no error message available.

Certain packages cause problems in higher versions. Therefore mlflow was set to 1.14.1 and azure-blob-storage to 12.7.1. Higher versions of azure-blob-storage were not running correctly but without any error message. Keep track of your versions if you need or like to use more actuall versions.


Sometimes the storage of artifacts did not work while a problem was in the repo of the model while mlflow docker was working fine.





