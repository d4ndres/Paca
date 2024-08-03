from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
url = SUPABASE_URL
key = SUPABASE_KEY
supabase: Client = create_client(url, key)
