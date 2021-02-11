# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0
# prefixed unless they are 0.
# Example:
# Given “25525511135”,
# return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)

# ip = input("Enter any IP without dots in it: ")
ip = '23232323'
length = len(ip)
print(length)
if length > 12:
    print("enter valid IP")
str_ip = str(ip)
print(str_ip)
# for i in str_ip:
