"""Daily Coding Problem ----- Problem #71 [EASY]
4/6/2021

This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) 
with uniform probability, implement a function rand5() that returns an integer 
from 1 to 5 (inclusive).

.. _Google Python Style Guide:   
http://google.github.io/styleguide/pyguide.html
"""
from random import randint

def rand7() -> int:
    """function to return integer from 1-7 (inclusive) with uniform probability
    
    Returns
    -------
    int
        random number [1-7]
    """
    return randint(1,7)


def rand5() -> int:
    """
    function to return integer from 1-5 (inclusive) with uniform probability
    extends existing rand7() function
    
    Returns
    -------
    int
        random number [1-7]
    """
    potential_nums = [
        [1,2,3,4,5,1,2],
        [3,4,5,1,2,3,4],
        [5,1,2,3,4,5,1],
        [2,3,4,5,1,2,3],
        [4,5,1,2,3,4,5],
        [1,2,3,4,5,1,2],
        [3,4,5,0,0,0,0]]

    num = potential_nums[rand7()-1][rand7()-1]

    while num==0:
        num = potential_nums[rand7()][rand7()]
    
    return num

def main():
    # print(rand7())
    print(rand5())
    return

if __name__=="__main__":
    main()


'''
Interesting Takeaways
---------------------

Rejection sampling is the technique employed above, we take a sample by
extending or contracting our initial random API, if not in our desired
range we reject the sample - this is non-deterministic so there is still
an existing probability that we take O(inf) time to do this


'''