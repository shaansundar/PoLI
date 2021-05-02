from web3 import Web3
import json

url="https://eth-mainnet.alchemyapi.io/v2/E6cSIEaRt3rtEqX-f4RfgP5M17GQzREl"
tezos_url="https://api.tzstats.com"
test_url="https://eth-ropsten.alchemyapi.io/v2/E6cSIEaRt3rtEqX-f4RfgP5M17GQzREl"
test_url2="https://ropsten.infura.io/v3/eecce0fb50ab42d380100756f803f929"
g_url="HTTP://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(test_url2))
print(web3.isConnected())

contract_add=#ENTER YOUR CONTRACT ADDRESS HERE
node_acc2=#ENTER YOUR WALLET ADDRESS HERE
web3.eth.defaultAccount=node_acc2
nonce=web3.eth.getTransactionCount(node_acc2)
print(nonce)

contractAbi=json.loads('[{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"docLocation","outputs":[{"internalType":"string","name":"dateStamp","type":"string"},{"internalType":"string","name":"hash","type":"string"},{"internalType":"address","name":"delegatorWallet","type":"address"},{"internalType":"uint256","name":"nodeLocation","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"read","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_hash","type":"string"},{"internalType":"string","name":"_dateStamp","type":"string"},{"internalType":"uint256","name":"_nodeLocation","type":"uint256"},{"internalType":"string[]","name":"_tags","type":"string[]"}],"name":"write","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
contractAdd=web3.toChecksumAddress(contract_add)
contract=web3.eth.contract(abi=contractAbi,address=contractAdd)


def writeContract(hash,dateStamp,nodeLocation,author,title,tags):
    print("Success!!!")
    contract.functions.write(hash,dateStamp,nodeLocation,tags,author,title,tags).transact()
    print(txhash)

