from web3 import Web3
import yaml

def interact_with_blockchain(data):
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    provider_url = config["blockchain_settings"]["provider_url"]
    web3 = Web3(Web3.HTTPProvider(provider_url))

    if web3.isConnected():
        print("Connected to blockchain!")
        # Example: Simulating data being sent to the blockchain
        print(f"Sending data to blockchain: {data}")
    else:
        print("Failed to connect to blockchain.")
