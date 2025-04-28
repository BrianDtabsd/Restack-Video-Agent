import os

from dotenv import load_dotenv
from restack_ai import Restack
from restack_ai.restack import CloudConnectionOptions

# Load environment variables from a .env file
load_dotenv()

# Use the cloud engine URL directly
engine_id = os.getenv("RESTACK_ENGINE_ID")
address = "https://reli5mem.clj5khk.gcp.restack.it"  # Your cloud engine URL
api_key = os.getenv("RESTACK_ENGINE_API_KEY")
api_address = "https://reli5mem.clj5khk.gcp.restack.it"  # Your cloud engine URL

connection_options = CloudConnectionOptions(
    engine_id=engine_id, address=address, api_key=api_key, api_address=api_address
)
client = Restack(connection_options)
