from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProviveder(infura_url))

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
trans_info = json.loads(req_ethgas_data.content)


print('safelow', trans_info['safelow'])
print('average', trans_info['average'])
print('fast', trans_info['fast'])
print('fastest', trans_info['fastest'])
print('Block number', trans_info['blockNum'])


gas_price = web3.eth.gasPrice
print('Calculated gas price:', gas_price/10**9)
