import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

print("SUPABASE_URL:", os.environ.get("SUPABASE_URL"))  # 🔍 Debug
print("SUPABASE_KEY:", os.environ.get("SUPABASE_KEY"))  # 🔍 Debug

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)