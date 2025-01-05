class univ():
    def getunidet(self):
        self.uname=input("Enter University Name:")
        self.uloc=input("Enter University Location:")

    def disunidet(self):
            print("-"*50)
            print("University : {}".format(self.uname))
            print("Location : {}".format(self.uloc))
            print("-"*50)