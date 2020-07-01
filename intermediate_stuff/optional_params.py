# # optional parameters

#  give param a default value
#  this makes param optional 

#  works with multiple params

# depending on situation, better than using if-statements 
# to check if user entered all params

class car(object):
    # give default condition and kms
    def __init__(self, make, model, year, condition="New", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    # if user calls display without specifying param, won't break
    def display(self, showAll=False):
        if showAll:
            print("This car is a %s %s %s in %s condition with %s kms on the clock." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s %s." %(self.make, self.model, self.year))

fox = car("Volks Wagen", "Fox", 1996, "decent", 15000)
fox.display(True)