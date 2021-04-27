#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *

def exponentiation_by_squaring(x, n) :
    """
    This function is able to calculate the exponentiation by squaring.
    """
    if n == 1 :
        return x
    elif n%2 == 0 :
        return exponentiation_by_squaring(x * x, (n) / 2)
    return x * exponentiation_by_squaring(x * x, (n-1) / 2)
    

def binary_search(lst, x) :
    """
    Perform a binary search of the value x in a sorted array.
    """
    def binary_search_aux(lst, l, r, val) :
        if r >= l :
            mid = l + (r - 1) // 2
            if lst[mid] == val :
                return (True, mid)
            elif lst[mid] > x :
                return binary_search_aux(lst, l, mid-1, x)
            return binary_search_aux(lst, mid+1, r, x)
        return (False, -1)
    return binary_search_aux(lst, 0, len(lst) - 1, x)
    

def generate_random_array() :
    """
    Generate an array of a random size, with sorted values.
    """
    lst = []
    val = 0
    for i in range(randint(150, 1000)) :
        val = val + randint(0, 12)
        lst.append(val)
    return lst
        

def main() :
    """
    Main function of the first practical work.
    """
    print(exponentiation_by_squaring(2, 2600))
    print(binary_search(generate_random_array(), 6))
    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
