from src.real_world_data import fetch_real_world_data
from src.blockchain_connector import interact_with_blockchain

class CelonAgent:
    def __init__(self):
        print("Initializing Celon, the bridge between reality and blockchain...")

    def run(self):
        print("Fetching real-world data...")
        data = fetch_real_world_data()

        print("Pushing data to blockchain...")
        interact_with_blockchain(data)

        print("Celon operation complete!")
