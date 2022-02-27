from brownie import FundMe, accounts, network, config, MockV3Aggregator
from .helpers import get_account
from web3 import Web3
from .fund_and_withdraw import funder, withdraw

def deploy_fund_me():
    account = get_account()

    # pass price feed address
    price_feed_address = get_price_feed_address(account)
    fund_me = FundMe.deploy(price_feed_address, {"from": account}) # publish_source=True
    print(f"Deployed fund me address is {fund_me.address}")

    print(f"Funding fund me contract")
    funder(contract=fund_me)
    withdraw(contract=fund_me)


def get_price_feed_address(account):
    if network.show_active() != "development":
        return config["networks"]["kovan"]["eth_usd_price_feed"]

    else:
        if len(MockV3Aggregator) <= 0 :
            print("The dev network is active deploying mock contracts")
            mock = MockV3Aggregator.deploy(18,Web3.toWei(2000, "ether"), {"from": account})
            print("Mocks deployed")
            return mock.address

        else:
            return MockV3Aggregator[-1]

def main():
    deploy_fund_me()