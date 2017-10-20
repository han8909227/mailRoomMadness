import pytest 
from faker import Faker
from random import uniform, randint

fake = Faker()
fake_donors = {fake.name(): [uniform(0, 1000) for _ in range(randint(1, 10))] for _ in range(20)}
small_donors = {'Joseph Ramos': [270.36, 609.35, 170.10], 
'Stephanie Jones': [70.13, 483.50, 29.23, 117.34, 594.88, 425.31, 730.61]}

@pytest.mark.parametrize('donor_dictionary', [(small_donors)])

def test_generate_user_report(donor_dictionary):
    from mailroom import user_report 
    user_report(donor_dictionary)

@pytest.mark.parametrize('donations, result', [([], 0), ([2,6], 4)])

def test_avg_donation(donations, result):
    from mailroom import avg_donation
    assert avg_donation(donations) == result


