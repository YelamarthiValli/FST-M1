import pytest

@pytest.fixture
def wallet_amount():
   amount = 0
   return amount

@pytest.mark.parametrize("Earned, Expenses, Balance", [ (30, 10, 20), (20, 2, 18), ])
def test_transactions(wallet_amount, Earned, Expenses, Balance):

    wallet_amount = wallet_amount + Earned
 
    wallet_amount = wallet_amount - Expenses
 
    assert wallet_amount == Balance