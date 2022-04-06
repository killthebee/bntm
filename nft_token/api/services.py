import eth_utils

from bntm.settings import WALLET_PRIVATE_KEY, WALLET_ADDRESS, GAS
from bntm.utils import get_w3_instance, get_contract


def mint_token(owner, media_url, generated_hash):
    w3 = get_w3_instance()
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    contract = get_contract(w3)
    mint_token_transaction = contract.functions.mint(
        eth_utils.to_bytes(hexstr=owner),
        generated_hash,
        media_url,
    ).buildTransaction(
        {
            'chainId': 4,
            'gas': GAS,
            'maxFeePerGas': w3.toWei('2', 'gwei'),
            'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
            'nonce': nonce,
        }
    )
    signed_mint_token_transaction = w3.eth.account.sign_transaction(
        mint_token_transaction, private_key=WALLET_PRIVATE_KEY
    )
    transaction_hash = w3.eth.send_raw_transaction(signed_mint_token_transaction.rawTransaction)
    return transaction_hash.hex()
