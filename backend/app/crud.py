import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_books():
    response = supabase.table("books").select("*").limit(5).execute()
    return response.data


print(get_books())