"""
Task

 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Constraints





Output Format

Print the amount of money earned by .

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
count = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]: 
        y[size] -= 1
        total += rate
print(total)