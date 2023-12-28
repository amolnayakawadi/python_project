### Creating a bank using Python

bank_name = 'ETHANS BANK'
width = 40
branch_name = 'wakad'
bank_db = {}

def print_header(mesg=None):
    head = '-' * width
    print(head)
    if mesg:
        print(mesg.center(width))
    print(f'{bank_name} {branch_name}'.center(width))
    print(head)
          
def first_screen():
    print('1) Login\n2) Create New Account\n3) Exit')
    choice = input('Enter your choice : ')
    return choice

def get_new_account_no():
    if bank_db:
        return max(bank_db) + 1
    else:
        return 1
    
def logged_in_user(ano):
    print_header(f'Welcome {bank_db[ano]["name"]}')
    print('1) Check balance\n2) Deposit\n3) Withdrawl')
    ch1 = input('Enter your choice : ')
    return ch1

def login_user():
    ano = int(input('Enter the account number : '))
    paswd = input('Enter the password : ')
    if ano in bank_db and bank_db[ano]['paswd'] == paswd:
        return True
    else:
        return False
    
    
def create_new_account():
    global bank_db
    name = input('Enter your name : ')
    paswd = input('Enter your password : ')
    acc_no = get_new_account_no()
    bank_db[acc_no] = { 'name'    : name,
                        'paswd' : paswd,
                        'balance' : 0}
    print(f'Account opened succesfully - {acc_no}')
          
          
def server():
    while True:
        print_header()
        ch = first_screen()
        if ch == '1':
            ano = login_user()
            if ano:
                logged_in_user(ano)
            else:
                print('invalid User found')
        elif ch == '2':
            create_new_account()
        elif ch == '3':
            print('Thanks for banking with us')
            break
          