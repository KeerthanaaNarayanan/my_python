# Given an integer array A of size N, find sum of elements in it.
# Input:
# First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of
# input. First line contains N the size of the array A. The second line contains the elements of the array.
# Output:
# For each testcase, print the sum of all elements of the array in separate line.
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= Ai <= 100
# Example:
# Input:
# 2
# 3
# 3 2 1
# 4
# 1 2 3 4
# Output:
# 6
# 10

T = int(input())
for i in range(0, T):
    N = int(input())
    A = []
    inp = input()
    for i in range(0, N):
        element = int(inp[i])
        A.append(element)
    print(A)
    # print(T, N, A)
    if (T >= 1) & (T <= 100) & (N >= 1) & (N <= 100):
        print (True)
    else:
        print(False)
