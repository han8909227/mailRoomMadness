"""Tests for the mailroom module."""
from faker import Faker
import pytest
from random import uniform, randint


fake = Faker()
fake_donors = {
    fake.name(): [uniform(0, 1000) for _ in range(randint(1, 10))]
    for _ in range(20)
}
small_donors = {
    'Joseph Ramos': [270.36, 609.35, 170.10],
    'Stephanie Jones': [70.13, 483.50, 29.23, 117.34, 594.88, 425.31, 730.61]
}


@pytest.mark.parametrize('donor_dictionary', [(small_donors)])
def test_generate_user_report(donor_dictionary):
    """Test that user_input does not raise any exceptions."""
    from mailroom import user_report
    user_report(donor_dictionary)


@pytest.mark.parametrize('donations, result', [([], 0), ([2, 6], 4)])
def test_cal_avg_donation(donations, result):
    """Test cal_avg_donation for proper output."""
    from mailroom import cal_avg_donation
    assert cal_avg_donation(donations) == result


@pytest.mark.parametrize('donor_dictionary, result',
                         [(small_donors, ['Stephanie Jones', 'Joseph Ramos'])])
def test_sort_donors(donor_dictionary, result):
    """Test sort_donors for proper output."""
    from mailroom import sort_donors
    assert sort_donors(donor_dictionary) == result


@pytest.mark.parametrize('user_input, result', [('1', True),
                         ('2', True), ('3', False), ('T', False)])
def test_validator_main(user_input, result):
    """Test validator_for_main for proper output."""
    from mailroom import validator_for_main
    assert validator_for_main(user_input) == result


@pytest.mark.parametrize('user_input, result', [('Joseph Ramos', True),
                         ('Michel', True), ('%', False), ('873', False),
                         ('', False)])
def test_validator_thank_you(user_input, result):
    """Test validator_for_thank_you for proper output."""
    from mailroom import validator_for_thank_you
    assert validator_for_thank_you(user_input) == result


@pytest.mark.parametrize('user_input, result', [('100.22336', True),
                         ('20', True), ('', False), ('letter', False),
                         ('***', False)])
def test_validator_thank_you_donation(user_input, result):
    """Test validator_for_thank_you_donation for proper output."""
    from mailroom import validator_for_thank_you_donation
    assert validator_for_thank_you_donation(user_input) == result


@pytest.mark.parametrize('name, amount, result', [('John', 20000, 'Hi John:\n\
Thank you very much for your generous donation of $20000.00.\n\
We appreciate your donation!!\nCheers,\nTeam')])
def test_email_generator(name, amount, result):
    """Test email_generator for proper output."""
    from mailroom import email_generator
    assert email_generator(name, amount) == result
