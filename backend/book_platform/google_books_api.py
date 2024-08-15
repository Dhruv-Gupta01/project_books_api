import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

GOOGLE_BOOKS_API_KEY = 'YOUR_API_KEY'
GOOGLE_BOOKS_API_CREDENTIALS = 'path/to/credentials.json'

def get_google_books_api_client():
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_BOOKS_API_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/books']
    )
    client = build('books', 'v1', credentials=credentials)
    return client

def search_books(query):
    client = get_google_books_api_client()
    response = client.volumes().list(q=query).execute()
    return response.get('items', [])

def get_book_details(volume_id):
    client = get_google_books_api_client()
    response = client.volumes().get(volumeId=volume_id).execute()
    return response