"""Reusable MongoDB CRUD module for animal shelter records."""

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """Provide create, read, update, and delete operations."""

    def __init__(
        self,
        username,
        password,
        host="localhost",
        port=27017,
        database_name="aac",
        collection_name="animals",
        auth_source="admin"
    ):
        """Connect using the supplied credentials and database settings."""

        # Your aacuser account was created in the admin database.
        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource=auth_source,
            serverSelectionTimeoutMS=5000
        )

        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """Insert one document; return True on success, otherwise False."""

        if not isinstance(data, dict) or not data:
            return False

        try:
            # Copy the dictionary so insert_one does not alter caller data.
            result = self.collection.insert_one(data.copy())
            return result.acknowledged
        except PyMongoError as error:
            print(f"Create operation failed: {error}")
            return False

    def read(self, query):
        """Return matching documents as a list, or [] on failure."""

        if not isinstance(query, dict):
            return []

        try:
            # find returns a cursor, which is converted into a list.
            return list(self.collection.find(query))
        except PyMongoError as error:
            print(f"Read operation failed: {error}")
            return []

    def update(self, query, update_data):
        """Update matching documents; return the number modified."""

        # Require a filter to prevent accidental collection-wide changes.
        if not isinstance(query, dict) or not query:
            return 0

        if not isinstance(update_data, dict) or not update_data:
            return 0

        # Require MongoDB update operators, such as $set.
        if not all(
            isinstance(key, str) and key.startswith("$")
            for key in update_data
        ):
            return 0

        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except PyMongoError as error:
            print(f"Update operation failed: {error}")
            return 0

    def delete(self, query):
        """Delete matching documents; return the number removed."""

        # Require a filter to prevent accidental collection-wide deletion.
        if not isinstance(query, dict) or not query:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as error:
            print(f"Delete operation failed: {error}")
            return 0

    def close(self):
        """Release the MongoDB connection."""
        self.client.close()