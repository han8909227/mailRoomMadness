"""Pesudo coding for the mail room madness problem"""



def main():
    donor_list = {'donar1': [100.00], 'donar2': [100.00]}
    user_choice = input('Choose 1:\'Thank You\' or 2:\'Create Report\' enter the corresponding number ')
    user_choice = user_input_validate(user_choice, validator_for_main, 'Choose 1:\'Thank You\' or 2:\'Create Report\' enter the corresponding number')
    if user_choice == 'quit':
        return

    if user_choice == '1':
        send_thank_you(donor_list)

    if user_choice == '2':
        user_report(donor_list)


def send_thank_you(donor_list):
    name_input = input('Enter a name or type \'list\' for a list of names')

    name_input = user_input_validate(name_input, validator_for_thank_you, 'Enter a name or type \'list\' for a list of names')

    if name_input == 'quit':
        return



    if name_input.lower() == 'list':
        print (list(donor_list.keys()))
    else:
        if name_input not in donor_list:
            donor_list[name_input] = []
        donation_input = input('Enter a donation amount')

        donation_input = user_input_validate(donation_input, validator_for_thank_you_donation, 'Enter a donation amount')

        if donation_input == 'quit':
            return

        donor_list[name_input].append(float(donation_input))
        email_string = """email""".format(donation_input)
        print (email_string)


def user_report(donor_list):
    list_of_donars = list(donor_list.keys()).sort(total_donation_amount)
    for donors in list_of_donars:
        print ('{} {} {} {}'.format(donar, total_donated_amount, num_donation, avg_donation))


def user_input_validate(user_input, validator, question):
    while not validator(user_input):
        print('Invalid user input,  input again')
        user_input = promopt(question)
    return user_input


def validator_for_main(user_input):
    return user_input == '1' or user_input == '2' or name_input.lower() == 'quit'


def validator_for_thank_you(name_input):
    return name_input.isprintable() or name_input.lower() == 'quit'


def validator_for_thank_you_donation(donation_input):
    return donation_input.validFloat() or name_input.lower() == 'quit'

