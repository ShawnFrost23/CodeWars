import unittest

def same_structure_as(original,other):
    print(original)
    print(other)
    if type(original) != type(other):
        return False
    elif len(original) != len(other):
        return False
    else:
        for i in range(0, len(original), 1):
            if type(original[i]) != type(other[i]):
                if type(original[i]) is list or type(other[i]) is list:
                    return False
            elif type(original[i]) is list and type(other[i]) is list:
                if same_structure_as(original[i], other[i]) == False:
                    return False
                elif len(original[i]) != len(other[i]): 
                    return False
        return True

# Test Cases
# (same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
# (same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")