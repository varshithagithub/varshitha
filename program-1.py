class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = float(input('Enter First number : '))
b = float(input('Enter Second number : '))        
obj=cal(a,b)
while True:
    def menu():
        x = ('a. Add \n b. Sub \n c. Multiply \n d. Divide') 
        print(x)
    menu()
    choice = (input('Please select one of the following : ')) 
    if choice == 'a':
        print("Result: ",obj.add())
    elif choice == 'b':
        print("Result: ",obj.sub())
    elif choice == 'c':
        print("Result: ",obj.multiply())    
    elif choice == 'd':
        print("Result: ",obj.divide())
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option') 
        break       
print()

