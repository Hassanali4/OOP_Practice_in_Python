from Item import Item
from phone import Phone

item1 = Item("MyItem",750)
item1.apply_Increment(0.2)
item1.apply_Discount()
print(item1.price)

#-----Items for 12th step Learned the concept about Encapsulation as we added apply_Increment function in our Item.py file
#that Encapsulate all the working from the user and not allow to change most of the working of the class just giving readonly
#of the functions
#As by making the self.price to self.__price and using previouse knowledge to make its setter and also a discount increment
#applying function




#-----Items for 11th step Learned about @property & @[variable_name].setter decorator in python that makes attributes read only
#We can craete Getters like in OOP in Python using the @property Decorator with as a function with its name in it same for setters
#The best thing for these setters as when setting a variable they can become useful to impose conditions when creating a name
#as shown below


#In Item.py
        # @property
        #     #property Decorator = Read-Only Attribute
        #     def name(self):
        #         #print("Your trying to get the value of name variable")
        #         return self.__name
        #
        #     @name.setter
        #     def name(self,value):
        #         #print("Your trying to set the value of name variable")
        #         if len(value) > 10:
        #             raise Exception("The name of characters should not be longer them 10 characters")
        #         else:
        #             self.__name = value

#In main.py
            # item1 = Item("MyItem",750)
            # item1.name = "OtherItem12"
            # print(item1.name)



#-----Items for 10th step Made 2 seperate python files 1 for our mian item class
#2nd for the child class that inherited the properties of the item class Name Phone class
#And now using our main.py class for creating instances and logic for this mini project






# phone1 = Phone("jscPhonev19",500,5)
#
# print(Item.all)
# print(phone1.all)







#-----Items for 9th step Made inheritance to another child class named phone
#Added a new variable with name of broken_phones into it as some phone items can be broken in stock so thats a related
# variable to the item too
#Then learned about the super function that is used to get access to the Parent class(base class) variables
# inside new inherited class without hard coding them
#Adding the self.__class__.__name__ in the def __repr__() function to add the name of the instance of the
# class that is using it.

#The usage of super function inside every child class of a Parent class(base class) is verys useful as we have added a list type
#variable inside the Parent class(base class) to have the collection of every instance incheck using just one list variable, that
#would have caused problem as child classes can have their own unique set of collection but still they all are being derived
# from just a single pare


# class Phone(Item):
#     all = []
#     def __init__(self, name, price, quantity=0,broken_phones=0):
#         # Call to super function to access all the attributes / methods
#         super().__init__(
#             name, price, quantity
#         )
#         # Run validations to the recieved arguments
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} should be equal to or greater then zero!"
#
#         # Assigning to self object
#         self.broken_phones = broken_phones
#
#         # Actions to execute
#         Phone.all.append(self)
#
# phone1 = Phone("jscPhonev19",500,5)
# phone1.broken_phones = 1
# print(phone1.calculate_the_total())
# phone2 = Phone('jscPhonev20',700,5)
# phone1.broken_phones = 1






#-----Items for 8th step Made a static method in our class to remove the 10.0 float point zero presenting problem from
# our prices in this regard the static function can be helpful
#
# @staticmethod
#     def is_integer(num):
#         if isinstance(num,float):
#             #We will count out the floats that are point zero
#             #i.e 5.0 , 10.0
#             return num.is_integer()
#         elif isinstance(num,float):
#             return True
#         else:
#             return False


#-----Items for 7th step Made a class method in our class to get new instances data from a csv file and
# imported a csv package in our main.py file
#Also used 3 plugins like RainboCSV , ExcelReader 2.0 , CSV they will help to read the csv file according to our need
#For this reason maded a Class Method in our class using a Decorator(@classmethod) to instantiate the desired
# instances using the csv file with no problem
# Also used a Magic Function of python to learn to represent according to our needs __repr__(self).
# @classmethod
#     def instantiate_from_csv(cls):
#         with open('item.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#
#         for item in items:
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity')),
#             )
#
#     def __repr__(self):
#         #return "Item"
#         return f"Item('{self.name}','{self.price}','{self.quantity}')"
#
# Item.instantiate_from_csv()
# print(Item.all)


#-----Items for 6th step detial explaination of working on the instance level & class level attributes 
# item1 = item('Phone',100,5)
# item1.apply_Discount()
# print(item1.price)
# print(item1.calculate_the_total(item1.price,item1.quantity))

# item2 = item('Laptop',1000,3)
# item2.pay_rate = 0.7
# item2.apply_Discount()
# print(item2.price)



#----- 5th step: Learned about the class level attributes and Instance level attributes.
    #As the class level attributes are present only in class to use instances have to get ahead of their level to access the class level attributes if needed.
    #Also learned about Magic Methods in Python like __Dict__ that converts the level of a class & its instance into a dictionary then present it to user if choose to view it.

#----- 4th step: Used Assert built in python statement to make custom error statements that will apear if the user uses my class not according to its logic 


#----- 3rd step: Maded a cunstructor type known in python as __init__ fucntion, 
# passed some basic parameters through it as it is not mandatory to hard code everything we can utilize cunstructor ability in such cases.
#Printed the items to check its working
# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)



#----- 2nd step: developed a class method.
# Printed it by passing some parameters in it solving a problem.
# print(item2.calculate_the_total(item2.price,item2.quantity))



#----- 1st step: maded a class and printed its types to see custom class.
# And all of its types as int , str etc
# print(type(item1)) # item
# print(type(item1.name)) # str
# print(type(item1.price)) # int
# print(type(item1.quantity)) # int


