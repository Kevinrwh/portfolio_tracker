def show_port(tracker):

    if tracker:
        print(tracker)
    else:
        print('Portfolio is empty.')

def show_balance(balance):
    print(f'Current Balance: {balance}')

def update_balance(tracker):
    running_balance = 0
    
    for balance in tracker.values():
        running_balance+=balance

    return running_balance

def update_port(tracker):
    # Prompt the user for a category
    while True:
        
        # TODO: Validate category is valid
        category = input('Please enter a category to update:\n')
        # TODO: Validate balance is float
        balance = input(f'Please enter the balance for {category}:\n')

        # Verify with the user
        # TODO: Validate response is y or n
        print(f'You\'ve entered a balance of ${balance} for {category}.')
        response = input('Is this correct (Y/N)?\n').lower()

        # TODO: Shouldn't delete if we had a previous value
        if response == 'y':
            # Update/create the value for the category input by the user
            tracker[category] = int(balance)
        
        continue_flag = input('Press X to exit or any key to continue.\n').lower()
        
        if continue_flag == 'x':
            break
        else:
            continue

def main():
    # Global variables: portfolio and our current balnace
    tracker = {}
    current_balance = 0

    # TODO: Create menu to choose whether we want to look at our balances or update our portfolio

    # Display initial portfolio and balance
    show_port(tracker)
    show_balance(current_balance)

    # Update portfolio
    update_port(tracker)

    # Display updated portfolio and balance
    print('Updated Portfolio:')
    show_port(tracker)
    current_balance = update_balance(tracker)
    show_balance(current_balance)

    # Exit program
    print('Program exit.')

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
    
