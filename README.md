# Proof of Low Infringement
PoLI is a proposed consensus mechanism which runs by hashing the uniqueness of a given document. The blockchain's ultimate goal is to make sure all documents contained have as little infringement as possible.

**This particular repository, however, instead of implementing an entire blockchain, works on top of the Ethereum blockchain for simplicity puropses.**

The Infringement algorithm, the code, smart contract, etc. are open and free to use. Feel free to mention me if you like it xD

**Update v1.0.1: Tezos integration now supported:** Change url from `test_url` to `tezos_mainnet` to continue working with Tezos mainnet



## Procedure of implementation

1. Clone the repo in a local directory:

```git clone [add_the_url_here] PoLI```

2. Navigate to ON_CHAIN and copy the contents of `token.sol` to a new remix file [remix.ethereum.org](remix.ethereum.org)

3. Setup Remix to **Ropsten Testnet** and deploy the contract

4. Copy the contract code to ```OFF_CHAIN/src/ethacc.py``` under **"PASTE YOUR CONTRACT ADDRESS HERE"** comment.

5. Copy your local Ethereum wallet PubKey to **"PASTE YOUR WALLET ADDRESS HERE"** in the same document.

6. Paste two documents and rename them *paper1.pdf* and *paper2.pdf*. Remember *paper1.pdf* will be published to the blockchain whereas the other is for infringement checking.

7. Run ```core.py```

## Author

Shaan Sundar, 

Twitter: @notthatsundar

email: shaan.idtindia@gmail.com
