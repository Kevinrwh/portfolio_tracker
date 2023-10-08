import pandas as pd
from datetime import date

menu_options = {
    '1.':'Show current portfolio and balance.',
    '2.':'Update portfolio.',
    '3.': 'Send to excel.'
}

# Display the menu to the user
def show_menu():

    for option, string in menu_options.items():
        print(f'{option} {string}')
    
    print('Or any other key to exit.')

    response = input('Selection: ')

    return response

# Show user's portfolio
def show_port(tracker):

    if tracker:
        print(tracker)
    else:
        print('Portfolio is empty.')

# Display the current balance
def show_balance(balance):
    print(f'Current Balance: {balance}')

# Update the balance my summing the balances in an updated tracker
def update_balance(tracker):
    running_balance = 0
    
    for balance in tracker.values():
        running_balance+=balance

    return running_balance

# User wants to update their portfolio. Ask for the account & balance and update in the tracker
# Input(s): Tracker/Portfolio object
# Output(s): Updated tracker2
# TODO: Can make this method into multiple smaller validating methods
def update_port(tracker):
    
    continue_flag = True

    while continue_flag:
        
        # Prompt the user for an account, balance, and category
        # TODO: Validate account is valid
        account = input('Please enter a balance to update:\n').upper()
        # TODO: Validate balance is float
        balance = input(f'Please enter the balance for {account}:\n')

        # TODO: Add category functionality. I will need to change dictionary to triplet

        # Display the user's entry and verify
        # TODO: Validate response is y or n
        print(f'You\'ve entered a balance of ${balance} for {account}.')
        response = input('Is this correct (Y/N)?\n').lower()

        # If the user verified the account and balance, add the acc-balance kv pair or update the value
        # if the acc exists already
        if response == 'y':
            # Update/create the value for the account input by the user
            tracker[account] = int(balance)
        
        response = input('Press X to exit or any other key to continue.\n').lower()
        
        # User has finished updating, so exit back to main
        if response == 'x':
            continue_flag = False

# TODO: Update from the previously created spreadsheet, if there is one
# TODO: Create a del_account method, which removes an account and its balance
# After showing the menu, the user is able to choose an action to take
#     1. Viewing portfolio and balance
#     2. Updating portfolio (today)
#     3. Sending to excel (probably not needed, should be auto-done
# NOTE: When updating from previous data, will need to decide to keep old values or start over each time. 
# We could assume we want to keep old values.
# Output(s): Excel file with updated balances
def main():

    # Initialize our tracker and balance
    tracker = {}
    current_balance = 0

    # Show menu to user
    response = show_menu()
    # print(f'{response} {type(response)}')

    while(response):

        # Display initial portfolio and balance
        if (response == '1'):   
            show_port(tracker)
            show_balance(current_balance)

        # Update portfolio
        elif (response == '2'):

            update_port(tracker)

            # Display portfolio and updated balance
            print('Updated Portfolio:')
            show_port(tracker)
            current_balance = update_balance(tracker)
            show_balance(current_balance)

        # Send to excel
        elif (response == '3'):

            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(list(tracker.items()), columns=['Account', 'Balance'])

            # Add the total balance to the dataframe and concatenate for the final output
            total_df = pd.DataFrame({'Account': ['Total'], 'Balance': [current_balance]})
            result_df = pd.concat([df, total_df])

            # Specify the output Excel file name
            today = date.today()
            output_file = f'{today}.xlsx'
            
            # Save the DataFrame to an Excel file
            result_df.to_excel(output_file, index=False)

            print('Spreadsheet updated')

        # Prompt the user for their next action
        response = show_menu()

        if (response != '1' and response != '2' and response != '3'):
            print(f'Exit for action code {response}')
            response = False

    # Exit program
    print('Program exit.')
    # response = False

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
    
