# import copy
# def show_copy_difference():

#     original = [[1, 2], [3, 4]]
#     print("Original:", original) 

#     shallow = copy.copy(original)  
#     print("Shallow copy:", shallow)
    
#     shallow[0].append(99)

#     print("Shallow copy after modification:", shallow) 
#     print("Original after shallow copy modification:", original) 

# show_copy_difference()

import copy 
def show_copy_difference():

    original = [[1, 2], [3, 4]]
    print("Original:", original) 

    deepcopy = copy.deepcopy(original)  
    print("Deep copy:", deepcopy)
    
    deepcopy[0].append(100)

    print("Deep copy after modification:", deepcopy) 
    print("Original after shallow copy modification:", original) 

show_copy_difference()