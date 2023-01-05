import pymongo
import pandas as pd
import json
from marcket.config import mongo_client
from dotenv import load_dotenv

print(f"Loading environment vartaible from .env file")
load_dotenv()
# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb+srv://amitpatra:amit27@cluster0.cqlj9.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "Marketing_Campaign.csv"
DATABASE_NAME = "market"
COLLECTION_NAME = "marketing"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")
#Convert dataframe to json so that we can dump these records into mongodb
df.reset_index(drop=True,inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])
#insert converted json record to mongo db
#client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
#mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
