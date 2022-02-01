from brownie import MockV3Aggregator
from brownie import accounts, config, network
from web3 import Web3


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 2 * 10e10


def get_account():
    if (
        network.show_active()
        in LOCAL_BLOCKCHAIN_ENVIRONMENTS + FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            # DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},
        )
