from web3 import Web3
import json
#from solc import compile_standard

url="https://eth-mainnet.alchemyapi.io/v2/E6cSIEaRt3rtEqX-f4RfgP5M17GQzREl"
test_url="https://eth-ropsten.alchemyapi.io/v2/E6cSIEaRt3rtEqX-f4RfgP5M17GQzREl"
test_url2="https://ropsten.infura.io/v3/eecce0fb50ab42d380100756f803f929"
g_url="HTTP://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(test_url2))
print(web3.isConnected())

node_acc2="0xc5c10FBdE6A086C6b2D1b24462D976743f14894A"
acc1="0xb62B4187Bd382bCfEdd4EEee19B9CfFd525EA489"
priv1="349940cf0bb5005adfcdcc96ba82064e3bf4fc53a01ff34c87706bd96d1e0597"
priv2="ce9bd2529470bb928987505e18c3dd7f68a983e2dbf818c0349b660b9e32a85c"
web3.eth.defaultAccount=node_acc2
nonce=web3.eth.getTransactionCount(node_acc2)
print(nonce)

contractAbi=json.loads('[{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"docLocation","outputs":[{"internalType":"string","name":"dateStamp","type":"string"},{"internalType":"string","name":"hash","type":"string"},{"internalType":"address","name":"delegatorWallet","type":"address"},{"internalType":"uint256","name":"nodeLocation","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"read","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_hash","type":"string"},{"internalType":"string","name":"_dateStamp","type":"string"},{"internalType":"uint256","name":"_nodeLocation","type":"uint256"},{"internalType":"string[]","name":"_tags","type":"string[]"}],"name":"write","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
contractAdd=web3.toChecksumAddress("0xfBBA874ce8AD57AF374534c1583E8dC8b7458E84")
contract=web3.eth.contract(abi=contractAbi,address=contractAdd)

# j=contract.caller().write("vscode", "34562020", 4, ["hello","hi"])
# k=contract.functions.write("vscode", "34562020", 4, ["hello","hi"]).transact(transaction=priv1)


def writeContract(hash,dateStamp,nodeLocation,author,title,tags):
    print("Success!!!")
    #Enable the next line after connecting solidity and remix to web3py
    '''contract.functions.write(hash,dateStamp,nodeLocation,tags,author,title,tags).transact()'''
    print(txhash)

