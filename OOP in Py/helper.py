#When to use class methodds & When to use Static Methods  ?

class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should do something that
        must have relationship with class
        but not something that
        must bw unique per instance !
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually those are used to
        manipulate different structures of data to
        instantiate objects, like  we have done with CSV.
        '''

# however these also could be called from an instance.

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()