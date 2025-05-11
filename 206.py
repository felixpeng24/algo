"""
A permutation can be specified by an array P, 
where P[i] represents the location of the element at i in the permutation. 
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. 
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

"""

#cant we jsut intialiE pointers at the curr array plus the value, swap elements, and repeat for all elements

def permtoarr(perm, arr):
    # for i in range(len(perm)):
    #     arr[i], arr[perm[i]] = arr[perm[i]], arr[i]
    
    # return arr
    return [arr[perm[i]] for i in range(len(arr))]


perm = [2, 1, 0]
arr = ["a", "b", "c"]

print(permtoarr(perm, arr))