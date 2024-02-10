#!/usr/bin/python3

# from google.cloud import firestore
from firebase_admin import firestore, credentials, initialize_app


class StorageModel:
    """
    Class handles the storage functionalities
    """

    def __init__(self):
        """initialization"""
        cred = credentials.Certificate('key.json')
        default_app = initialize_app(cred)
        self.db = firestore.client()

    def add_document(self, collection_name, document_data):
        """
        Adds a document to the Firestore collections
        """
        collection_ref = self.db.collection(collection_name)
        doc_ref = collection_ref.document()
        doc_ref.set(document_data)
        return doc_ref.id

    def get_document(self, collection_name, document_id):
        """
        Retrieves documents from firestore collections
        """
        doc_ref = self.db.collection(collection_name).document(document_id)
        return doc_ref.get().to_dict()

    def update_document(self, collection_name, document_id, update_data):
        """
        updates the firestore collections
        """
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.update(update_data)

    def delete_document(self, collection_name, document_id):
        """
        Deletes documents from firestore collections
        """
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.delete()

    def query_collection(self, collection_name, filters=None):
        """
        query documents from firestore collections
        """
        collection_ref = self.db.collection(collection_name)
        if filters:
            for field, value in filters.items():
                collection_ref = collection_ref.where(field, '==', value)
        return [doc.to_dict() for doc in collection_ref.get()]
