class Car:
    def __init__(self):
        self.mark=input("Enter Mark :")
        self.model=input("Enter Model :")
        self.year=int(input("Enter Year :"))

    def display(self):
        print("-"*50)
        print("Content of Car :")
        print("\tMark : {}".format(self.mark))
        print("\tModel : {}".format(self.model))
        print("\tYear : {}".format(self.year))
        print("-"*50)


c=Car()
c.display()
