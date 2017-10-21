"""."""


def user_report(donor_dictionary):
    """."""
    list_of_donars = sort_donors(donor_dictionary)

    for donor in list_of_donars:
        total_donated_amount = sum(donor_dictionary[donor])
        num_donation = len(donor_dictionary[donor])
        avg_donation = cal_avg_donation(donor_dictionary[donor])
        print ('{0:<20} {1:>6.2f} {2:^3} {3:>6.2f}'.format(donor,
               total_donated_amount, num_donation, avg_donation))


def cal_avg_donation(donations):
    """."""
    if not donations:
        return 0
    return sum(donations) / len(donations)


def send_thank_you(donor_list):

    question = 'Enter a name or type \'list\' for a list of names'
    name_input = user_input_validator(validator_for_thank_you, question)

    if name_input == 'quit':
        return

    if name_input.lower() == 'list':
        print (list(donor_list))
    else:
        if name_input not in donor_list:
            donor_list[name_input] = []

        donation_input = user_input_validator(validator_for_thank_you_donation, 'Enter a donation amount')

        if donation_input == 'quit':
            return

        donation_input = float(donation_input)

        donor_list[name_input].append(donation_input)
        print (email_generator(name_input, donation_input))


def email_generator(name, amount):
    email_string = "Hi {}:\n\
Thank you very much for your generous donation of ${:.2f}.\n\
We appreciate your donation!!\nCheers,Team".format(name, amount)
    return email_string


def sort_donors(donor_dictionary):
    """."""
    return sorted(list(donor_dictionary), key=lambda x: -sum(donor_dictionary[x]))


def user_input_validator(validator, question):

    user_input = input(question)

    while not validator(user_input) and user_input.lower() != 'quit':
        print('Invalid user input,  input again')
        user_input = input(question)
    return user_input


def validator_for_main(user_input):
    return user_input == '1' or user_input == '2'


def validator_for_thank_you(name_input):
    if not name_input:
        return False
    for name in name_input.split():
        if not name.isalpha():
            return False
    return True


def validator_for_thank_you_donation(donation_input):
    try:
        float(donation_input)
        return True
    except ValueError:
        return False

