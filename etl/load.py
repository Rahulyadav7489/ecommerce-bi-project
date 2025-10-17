from pymongo import MongoClient

    # Replace with your actual connection string
MONGO_URI = "mongodb+srv://myself28072004:Yadavji28072004@cluster0.2vo3mcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "ecommerce_db"  # Replace with your desired database name
COLLECTION_NAME = "sales" # Replace with your desired collection name

    # Sample dictionary data to upload
from transform import sales_records as data_to_upload

try:
        # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    # Insert the dictionary data
    # Use insert_one() for a single dictionary or insert_many() for a list of dictionaries
    if isinstance(data_to_upload, list):
        result = collection.insert_many(data_to_upload)
        print(f"Inserted {len(result.inserted_ids)} documents.")
        print(f"Inserted IDs: {result.inserted_ids}")
    elif isinstance(data_to_upload, dict):
        result = collection.insert_one(data_to_upload)
        print(f"Inserted document with ID: {result.inserted_id}")
    else:
        print("Data to upload must be a dictionary or a list of dictionaries.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    if 'client' in locals() and client:
        client.close()
        print("MongoDB connection closed.")