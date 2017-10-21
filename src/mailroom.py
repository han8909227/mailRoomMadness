"""Console script to keep track of donations.

Allows the user to keep track of donors by name and
a history of the donations from each. Script prompts
user to print a report of donor stats or to fill out a
form thank-you email. Enter 'quit' to exit script.
"""


def user_report(donor_dict):
    """Print a table of donation stats.

    Includes the donor's name, the total amount donated,
    the number of donations made, and the average
    donation amount.
    """
    list_of_donars = sort_donors(donor_dict)

    print ('Donation Report:\n{0:<20} {1:>10} {2:>4} {3:>8}\n{4}'
           .format('Name', 'Total $', '#', 'Avg $', '-' * 45))

    for donor in list_of_donars:
        total_donated_amount = sum(donor_dict[donor])
        num_donation = len(donor_dict[donor])
        avg_donation = cal_avg_donation(donor_dict[donor])

        print ('{0:<20} {1:>10.2f} {2:>4} {3:>8.2f}'.format(donor,
               total_donated_amount, num_donation, avg_donation))


def cal_avg_donation(donations):
    """Calculate the average given a list of donations."""
    if not donations:
        return 0
    return sum(donations) / len(donations)


def send_thank_you(donor_dict):
    """Ask to print a list of donors or a thank-you email."""
    question = 'Enter a name or type \'list\' for a list of names: '
    name_input = user_input_validator(validator_for_thank_you, question)

    if name_input == 'quit':
        return

    if name_input.lower() == 'list':
        for name in list(donor_dict):
            print(name)
    else:
        if name_input not in donor_dict:
            donor_dict[name_input] = []

        donation_input = user_input_validator(validator_for_thank_you_donation,
                                              'Enter a donation amount: ')

        if donation_input == 'quit':
            return

        donation_input = float(donation_input)

        donor_dict[name_input].append(donation_input)
        print (email_generator(name_input, donation_input))


def email_generator(name, amount):
    """Fill in a form thank-you email for a donation."""
    email_string = "Hi {}:\n\
Thank you very much for your generous donation of ${:.2f}.\n\
We appreciate your donation!!\nCheers,\nTeam".format(name, amount)
    return email_string


def sort_donors(donor_dict):
    """Sort the list of donors by total amount donated.

    Returns a list of only the donors' names.
    """
    return sorted(list(donor_dict), key=lambda x: -sum(donor_dict[x]))


def user_input_validator(validator, question):
    """Validate a user input until it passes a validator function.

    validator: function, test for user input. Returns a truthy
               value for a valid input, falsey for invalid.
    question: str, prompt for user to answer
    """
    user_input = input(question)

    while not validator(user_input) and user_input.lower() != 'quit':
        print('Invalid user input,  input again')
        user_input = input(question)
    return user_input


def validator_for_main(user_input):
    """Check that input is '1' or '2'."""
    return user_input == '1' or user_input == '2'


def validator_for_thank_you(name_input):
    """Check that input is made only of letters and spaces."""
    if not name_input:
        return False
    for name in name_input.split():
        if not name.isalpha():
            return False
    return True


def validator_for_thank_you_donation(donation_input):
    """Check that input can be a float."""
    try:
        float(donation_input)
        return True
    except ValueError:
        return False
