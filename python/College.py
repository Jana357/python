from university import univ
class College(univ):
    def getcolldet(self):
        self.cname=input("Enter College Name :")
        self.cloc=input("Enter Location :")
    def discolldet(self):
        print("-"*50)
        print("College Name :".format(self.cname))
        print("College Location :".format(self.cloc))
        print("-"*50)