def traverse_nested_dictionary(nested:dict):
    for key,value in nested.items():
        if type(value) is dict:
            traverse_nested_dictionary(value)
            #This is just a place holder but I can add any needed functionality 
            #below sunce I now have a way of traversing the dictionary
        print(f"{key}:{value}")
        
print(traverse_nested_dictionary({1:1}))
