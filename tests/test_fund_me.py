import pytest
from scripts.deploy import get_price_feed_address
from scripts.helpers import get_account, get_contract
from brownie import FundMe



def test_can_fund_and_withdraw():
    account = get_account()

    # pass price feed address
    price_feed_address = get_price_feed_address(account)
    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    assert fund_me.getEntranceFee()
    fund_me.fund({"from": account})