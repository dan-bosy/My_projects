class calculator: # calculator class

    # function for addition
    def add(self):
        try:
            while True:
                num1 = float(input('enter first number: '))
                num2 = float(input('enter second number: '))
                print('your result is', num1 + num2)
                break
        except Exception as e:
             print('an error occured', e)
     # function for subtraction        
    def sub(self):
           try:
                while True:
                    num1 = float(input('enter number to subract:  '))
                    num2 = float(input('enter second number: '))
                    print('your result is', num1 - num2)
                    break
           except Exception as e:
                print('an error occured', e)
 # funtion for divition               
    def div(self):
        try:
            while True:
                num1 = float(input('enter number to divide: '))
                num2 = float(input('enter second number: '))
                print('your result is', num1 / num2)
                break
        except Exception as e:
            print('an error occured', e)
   # funcion for multiplication         
    def mult(self):
        try:
            while True:
                num1 = float(input('enter first number: '))
                num2 = float(input('enter second number: '))
                print('your result is', num1 * num2)
                break
        except Exception as e:
            print('an error occured', e)
    # main function         
    def main(self):
        import time
        # print main menu settings
        main_menu_list = [
        '='*67,
'welcome to calculator app',
'='*67,
'main menu',
'1. addition',
'2. subtraction',
'3. division',
'4. multiplication',
'5. exit program',
'6. display main menu',
'='*67]
        for item in main_menu_list:
            print(item)
            time.sleep(0.05)
        try:
            while True:
                 choice = int(input('enter your choice (1-6): '))
                 if choice == 1:
                     self.add()
                 elif choice == 2:
                     self.sub()
                 elif choice == 3:
                     self.div()
                 elif choice == 4:
                     self.mult()
                 elif choice == 5:
                     print('existing program, bye')
                     break
                 elif choice == 6:
                     calculator.main()
                 else:
                     print('invalid option try again')
        except Exception as e:
            print('an error occured',e)
                    
my_app = calculator()
# initialize the app from main
if __name__ == '__main__':
    my_app.main()
