import pandas as pd

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

# User wants to update their portfolio. Ask for the category & balance and update in the tracker
# Input(s): Tracker/Portfolio object
# Output(s): Updated tracker
# TODO: Can make this method into multiple smaller validating methods
def update_port(tracker):
    
    continue_flag = True

    while continue_flag:
        
        # Prompt the user for a category & balance
        # TODO: Validate category is valid
        category = input('Please enter a category to update:\n').upper()
        # TODO: Validate balance is float
        balance = input(f'Please enter the balance for {category}:\n')

        # Display the user's entry and verify
        # TODO: Validate response is y or n
        print(f'You\'ve entered a balance of ${balance} for {category}.')
        response = input('Is this correct (Y/N)?\n').lower()

        # If the user verified the category and balance, add the cat-balance kv pair or update the value
        # if the cat exists already
        if response == 'y':
            # Update/create the value for the category input by the user
            tracker[category] = int(balance)
        
        response = input('Press X to exit or any other key to continue.\n').lower()
        
        # User has finished updating, so exit back to main
        if response == 'x':
            continue_flag = False

# TODO: Update from the previously created account_data.xlsx spreadsheet
# Note: If there is no tracker in this working session, we should populate from
# previous entry. 
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
            # TODO: Send to excel
            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(list(tracker.items()), columns=['Account', 'Integer'])
            # Specify the output Excel file name
            output_file = 'account_data.xlsx'
            # Save the DataFrame to an Excel file
            df.to_excel(output_file, index=False)

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
    
