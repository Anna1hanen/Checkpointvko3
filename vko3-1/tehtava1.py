import requests
import os
from google.oauth2 import service_account
from google.cloud import storage

sr = requests.get(' https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = sr.json()

parametrilista = []

for d in data['items']:
    parametrilista.append(d["parameter"])

with open("checkpoint.txt", "w") as tiedosto:
    for i in parametrilista:
        tiedosto.write(i + "\n")

def tiedosto_buckettiin(bucket_name, source_file_name, destination_blob_name):


    credentials = service_account.Credentials.from_service_account_file("C:/Users/35840/.vscode/python_harkat/uusiprojektivko2-keys.json")
    valimies = storage.Client()

    bucket = valimies.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "Tiedosto {} ladattu bukettiin {}.".format(
            source_file_name, destination_blob_name
        )
    )


if __name__ == "__main__":
    tiedosto_buckettiin("checkpointvko3",r"C:\Users\35840\vscode\Git\vko3-1\checkpoint.txt", "Checkpoint1")


def luo_bucket(bucket_nimi :str):

    credentials = service_account.Credentials.from_service_account_file("C:/Users/35840/.vscode/python_harkat/uusiprojektivko2-keys.json")
    valimies = storage.Client(credentials=credentials)

    # Luo uuden bucketin
    bucket = valimies.create_bucket(bucket_nimi)

    print("Loi bucketin {} .".format(bucket.name))

if __name__ == "__main__":

    luo_bucket("checkpointvko3")

