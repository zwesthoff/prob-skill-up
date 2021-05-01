"""Daily Coding Problem ----- Problem #96 [EASY]
5/1/2021

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

.. _Google Python Style Guide:   
http://google.github.io/styleguide/pyguide.html
"""
from collections import deque

def permute(nums : list[int]) -> list[list[int]]:
    #Container for our soln
    res = []

    #base case
    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)

        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        
        res.extend(perms)

        nums.append(n)

    return res


def main():
    test = [1,2,3]

    res = permute(test)
    
    print(f"Result is : {res}")



if __name__=="__main__":
    main()


'''
Interesting Takeaways
---------------------
I definitely rate this a Medium for me atm but it is a great example of backtracking with DFS, link below isn't best for me to learn from
but, does include additional similar problems

Backtracking - https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
Given n distince items, total number of possible permutations are n!

Backtracking is a complete search technique and DFS is an ideal way to implement

Permutations refer to the permutation of n things, taken k at a time without repetition

This youtube video explains it very clearly -> https://www.youtube.com/watch?v=s7AvT7cGdSo&t=579s

'''