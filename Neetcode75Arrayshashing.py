# Encode and Decode Strings

# Problem:
# Given a list of strings, encode it into a single string.
# Then decode that single string back into the original list of strings.

# Restriction:
# The combined encoded string may contain other characters in the middle,
# so we need a reliable way to separate the strings when decoding.

# Solution:
# Use a delimiter format like: <length>#<string>
# This ensures even if the string contains '#' or digits, we can still parse it correctly.

# Example:
# Input: ["neet", "code", "love", "you"]
# Encoded: "4#neet4#code4#love3#you"
# Output after decoding: ["neet", "code", "love", "you"]

def encode(strs):
    """Encodes a list of strings to a single string."""
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    """Decodes a single string to a list of strings."""
    res, i = [], 0 # This give us a list to store the values and also i is the pointer that will 
    # loop throughout the string to separate the different smaller strings 

    while i < len(s): # the while loop will go on until every word is analyzed in string s 
        # everytime I see a while loop I should think that we are going to be doing a task
        # until the string. list , or iterable or condition is met. From i < len(s) 
        # while i is less than len(s) and i will grow eventually to make this statement false
        # Find the delimiter to extract length
        j = i  # as we loop through string s, the pointer will be on a letter i
        # and to this pointer i we will assign j aswell so that it will have the same letter starting point
        # but it will be located in a different variable 
        while s[j] != "#": # we are getting all the characters beside #
            j += 1 # and we are adding more and more index points until we reach another # 
        length = int(s[i:j]) # we are storing the length of the word from pointer i to pointer j 
        # because that is one word, and we used != # so it will be counting one word only
        # Extract the word using the length
        i = j + 1
        j = i + length

        res.append(s[i:j])
        # Move to the next encoded word
        i = j

    return res

# Example usage
input_list = ["neet", "code", "love", "you"]
encoded = encode(input_list)
print("Encoded:", encoded)  # Output: "4#neet4#code4#love3#you"
decoded = decode(encoded)
print("Decoded:", decoded)  # Output: ["neet", "code", "love", "you"]

# Contains Duplicate 

# Given an integer array nums, return true if any value appears more than once in the array
# otherwise return false. So there must be only unique characters if not its false

# One data Structure that always only has unique keys / values is a hashset

# If the input is an integer array nums, we must turn it into a set, after turning into a set
# only the unique values will be left, then we must make a comparison bewteen this and 
# the original integer array list. We can make this comparison by looking at their lengths
# because onviously the hash one will be shorter if there are not unique values 

def hasDuplicate(self, nums):
    return len(set(nums)) < len(nums) # if the length of the hashset is less than array it has duplicates so it is true 

# Valid Anagram
# Given two strings s and t return true if the two strings are anagrams of eachother
# What is an anagram? An anagram is when a word has the same amount of letters and 
# the same letters as another word like cat and tac 

# how can we find if they are anagrams?

# we are inputting s and t strings (words which are given to us and the output is a boolean value 

# first we would check if they have the same length even 
# then if they have the same length we can create a hashmap that contains each word and how many 
# times that word occurs 

def isAnagram(self, s: str, t: str) -> bool: 
    if len(s) != len(t): # if the length of s and t are not same then they are not anagrams
        return False # since they are not anagrams we return false 

    countS, countT = {}, {} # we are creating two hashmaps count s and count t

    for i in range(len(s)): # since we determined that the length of s and t is the same 
        # we are going from 0 to end of the lengths of s 
        countS[s[i]] = 1 + countS.get(s[i], 0)
        # in the hashmap count s and count t we are inputting every letter in strings s and t
        countT[t[i]] = 1 + countT.get(t[i], 0)
        # and 1 + hashmap.get(letter,0) to increment 1 on a particular letter in the hashmap after adding it
    return countS == countT
    # so far we have two different hashmaps and they are storing the letters and count of letters
    # to see if they are anagrams we must check if they have the same letters and same count
    # so we just check if they are equal to each other 

    # two sum 
    # given an array of integers nums and a target integer
    # return indices i and j where the indices on that array will help you reach the target value
    # i and j must not be equal 
    # I would begin to solve this by finding the difference of all the nums in the array from
    # the target and i would check if the difference could be found in the array 
    # I need a hash storage to store all the integers in nums and their indices 
    

def twoSum(self, nums: List[int], target: int) -> List[int]: # two sum function definition 
    prevMap = {} # we are creating a hashmap to store the indices as well as the values themselves 

    for i, n in enumerate(nums): # we are getting the values and indices in nums at once 
        diff = target - n # the difference is given from each value from the list and the target value 
        # btw we are currently iterating through nums so every value n is being analyzed by code individually
        if diff in prevMap: # and if that difference from taregt - n is in the prevmap
            return [prevMap[diff], i] # we will return [prevMap[diff], i] 
        # [prevMap[diff], i] gives us the index key value for a hashmap and i is the regular index we find as we for loop 
        prevMap[n] = i  # if the index of the difference doesnt exist in prev map, or in other words if the difference 
        # doesnt exist at all then we do prevMap[n] = i, we are adding that value n and setting it to i key in the prevMap hashmap

# Group Anagrams 
# Input is array of strings strs
# group all the anagrams together into sublists 
# An anagram is a string that contains the same characters as another string
# But the order of the characters can be different
# example is cat / tac

from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = {}  # using a dictionary 
    for s in strs: # going through all the words in the input string 
        count = [0] * 26 # creating one list with 26 different '0' elements
        for c in s: # for every letter in each word 
            count[ord(c) - ord('a')] += 1 # increasing the count for that letter 
        key = tuple(count) # making it into a tuple so that we can add it to the dictionary as a key
        if key not in res: # if that key is not in the dict
            res[key] = []  # manually initialize list if key is not present
        res[key].append(s) # the key is the jumble of list of letters and we are matching to it
        # the value, which is the word itself s 
    return list(res.values()) # res.values returns the values from the dictionary which is the words

        