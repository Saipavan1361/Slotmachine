import random
MAX_LINES=3
MAX_BET=1000
MIN_BET=25
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_line.append(line+1)
    return winnings,winnings>0,winning_line

def slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        amount=input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_no_of_lines():
    while True:
        lines=input(f"Enter number of lines you want to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <=3:
                break
            else:
                print(f"Enter valid number of lines (1-{MAX_LINES}).")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount=input("What would you like to bet on each line? ₹")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET}-₹{MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

def game():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        
        if balance < MIN_BET:
             print(f"Your balance is too low to place the minimum bet of ₹{MIN_BET}.")
             deposit_choice = input("Would you like to deposit more? (yes/no): ")
             if deposit_choice.lower() == 'yes':
                 balance += deposit()
                 continue
             else:
                 break

        lines = get_no_of_lines()
        
        while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough to make that bet. Your balance is ₹{balance}")
            else:
                break
        
        print(f"You are betting ₹{bet} on {lines} lines. Total bet is equal to ₹{total_bet}.")
        
        balance -= total_bet
        
        slots = slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        
        winnings, won, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        balance += winnings
        
        if won:
            print(f"Congrats! You won ₹{winnings}.")
            print(f"You won on lines:", *winning_lines)
        else:
            print("Sorry, you didn't win this time.")
            
        print(f"Your new balance is ₹{balance}")

        play_again_choice = input("Press Enter to play again (or 'no' to quit). ")
        if play_again_choice.lower() == "no":
            break
            
    print(f"You left with ₹{balance}. Thanks for playing!")


def play():
    sel=input("Do you want to play?")
    print("DISCLAIMER:Think before you spend you might loose money. This is only for entertainment.")
    if sel.upper()=='YES':
        game()
    else:
        print("Thankyou hope you will try your luck.")

if __name__ == "__main__":
    play()