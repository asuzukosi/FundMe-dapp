from brownie import FundMe, network
from.helpers import get_account, get_contract

def funder(contract):
    fund_me = contract
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee + 100})
    print("Account has been funded successfully.")

def withdraw(contract):
    fund_me = contract
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Account has been withdraw successfully.")