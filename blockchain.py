blockchain = []


def get_last_block_chain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_tranaction=[1]):
    blockchain.append([last_tranaction, transaction_amount])


def get_user_input():
    user_input = float(input('Your Transaction Amount Please: '))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_block_chain_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_block_chain_value())

print(blockchain)
