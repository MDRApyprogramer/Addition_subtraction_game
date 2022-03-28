def number_game():
    print('be soalat zir pasokh dahid')


    def number_game1(min,max):
        import random

        print(f'javab beyn {min + min} va {max + max} hast')

        number1 = random.randint(min,max)
        number2 = random.randint(min,max)
        
        def number_gamer(komak):
            
            number3 = number1 + number2
            number4 = int(input(f'{number1} + {number2} = '))

            if number4 == number3 :
                print('javab shoma dorost bood')
                print(f'shoma {komak} shans digar dashtid')
                komak = 5

            else :
                komak -= 1
                
                if komak == 0 :
                    import sys

                    print('shoma 5 bar eshtebah javab dadid')
                    print('shoma bakhtid')
                    print(f'javab {number3} bood')

                    exit()
                print('shoam eshtebah javab dadid')
                print(f'shoma {komak} shans digar darid')

                number_gamer(komak)

        number_gamer(5)


    def number_game2(min,max):
        import random

        print(f'javab beyn {min - min} va {min - max} hast')

        number1 = random.randint(min,max)
        number2 = random.randint(min,max)
        
        number3 = number1 - number2

        def number_gamer(komak):

            number3 =number1 - number2
            number4 = int(input(f'{number1} - {number2} = '))

            if number4 == number3 :
                print('javab shoma dorost bood')
                print(f'shoma {komak} shans digar dashtid')
                komak = 5

            else :
                komak -= 1

                if komak == 0 :
                    import sys

                    print('shoma 5 bar eshtebah javab dadid')
                    print('shoma bakhtid')
                    print(f'javab {number3} bood')

                    exit()
                print('shoam eshtebah javab dadid')
                print(f'shoma {komak} shans digar darid')

                number_gamer(komak)

        number_gamer(5)
    while True :
        import random

        number_game = random.randint(1,20)

        if number_game == 1 :
            number_game1(50,1500)
        elif number_game == 2 :
            number_game1(10,100)
        elif number_game == 3 :
            number_game1(1000,10000)
        elif number_game == 4 :
            number_game1(200,1000)
        elif number_game == 5 :
            number_game1(500,4000)
        elif number_game == 6 :
            number_game2(50,1500)
        elif number_game == 7 :
            number_game2(10,100)
        elif number_game == 8 :
            number_game2(1000,10000)
        elif number_game == 9 :
            number_game2(200,1000)
        elif number_game == 10 :
            number_game2(500,4000)
        else :
            pass

def number_gamer():
    print('be soalat zir pasokh dahid')

    def number_game1(min,max):
        import random

        print(f'javab beyn {min + min} va {max + max} hast')

        number1 = random.randint(min,max)
        number2 = random.randint(min,max)
        
        number3 = number1 + number2
        number4 = int(input(f'{number1} + {number2} = '))

        komak = 5

        while number3 != number4 :
            print()
            komak -= 1
            print('shoam eshtebah javab dadid')
            print(f'shoma {komak} shans digar darid')

            number4 = int(input(f'{number1} + {number2} = '))

            if komak == 0 :
                import sys

                print('shoma 5 bar eshtebah javab dadid')
                print('shoma bakhtid')
                print(f'javab {number3} bood')

                exit()

        if number4 == number3 :
            print('javab shoma dorost bood')
            print(f'shoma {komak} shans digar dashtid')
            komak = 5


    def number_game2(min,max):
        import random

        print(f'javab beyn {min - min} va {min - max} hast')

        number1 = random.randint(min,max)
        number2 = random.randint(min,max)
        
        number3 = number1 - number2

        number4 = int(input(f'{number1} - {number2} = '))

        komak = 5

        while number3 != number4 :
            print()
            komak -= 1
            print('shoam eshtebah javab dadid')
            print(f'shoma {komak} shans digar darid')

            number4 = int(input(f'{number1} + {number2} = '))

            if komak == 0 :
                import sys

                print('shoma 5 bar eshtebah javab dadid')
                print('shoma bakhtid')
                print(f'javab {number3} bood')

                exit()

        if number4 == number3 :
            print('javab shoma dorost bood')
            print(f'shoma {komak} shans digar dashtid')
            komak = 5


    while 0 < 1 :
        import random

        number_game = random.randint(1,20)

        if number_game == 1 :
            number_game1(50,1500)
            
        elif number_game == 2 :
            number_game1(10,100)
            
        elif number_game == 3 :
            number_game1(1000,10000)
            
        elif number_game == 4 :
            number_game1(200,1000)
            
        elif number_game == 5 :
            number_game1(500,4000)
            
        elif number_game == 6 :
            number_game2(50,1500)
            
        elif number_game == 7 :
            number_game2(10,100)
            
        elif number_game == 8 :
            number_game2(1000,10000)
            
        elif number_game == 9 :
            number_game2(200,1000)
            
        elif number_game == 10 :
            number_game2(500,4000)
        else :
            pass
 
import random

a = random.randint(1,2)
if a == 1 :
    number_gamer()
if a == 2 :
    number_game()