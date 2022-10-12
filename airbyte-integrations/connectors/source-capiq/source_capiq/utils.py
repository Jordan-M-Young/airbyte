import requests
import json
from base64 import b64encode
from cryptography.fernet import Fernet
from pymongo import MongoClient

def send_request(endpoint, credentials, fld, id, start, end):
    """Function that builds a json request body for querying capital iq's data and
    sends the request. Potential to futher configure this"""


    response = requests.post(
        url=endpoint,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json; charset=utf-8",
            'User-Agent': 'My User Agent 1.0'
        },
        data=json.dumps(
            {
                "inputRequests": [
                    {
                        "mnemonic": fld,
                        "function": "GDSHE",
                        "properties": {
                            "EndDate": end,
                            "StartDate": start,
                        },
                        "identifier": id,
                    }
                ]
            }
        ),
    )

    return response




def get_mongo_connection(fernet, password_string):
    mongo_string = password_string.encode()

    client = MongoClient(
        Fernet(fernet.encode()).decrypt(mongo_string).decode("utf-8"),
        replicaset="Production-shard-0",
        readPreference="secondaryPreferred",
    )

    return client


def get_ciq_credentials(fernet, password_string, user_name):

    password_string = password_string.encode()

    password = Fernet(fernet.encode()).decrypt(password_string).decode("utf-8")

    return b64encode(f"{user_name}:{password}".encode("utf-8")).decode()
