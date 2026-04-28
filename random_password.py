import secrets
symbols = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '1','2','3','4','5','6','7','8','9',
    '%','!','@','#','$','^','&','*'
]

while True:
    try:
        quantity = int(input("Enter the number of characters: "))
        password = ""
        if quantity > 0:
            for _ in range(quantity):
                password += secrets.choice(symbols)
            print(f'Your password: {password}')

        elif quantity <= 0:
            print("Enter a positive number")


    except ValueError:
        print('Enter number')
    except KeyboardInterrupt:
        print('yo!')
        break
