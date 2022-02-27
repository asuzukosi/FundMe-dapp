from brownie import network, accounts, config

def get_account():
    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_wallet"])

def get_contract(contract_instance):
    if network.show_active() == "development" :
        return contract_instance

    else:
        return contract_instance[-1]