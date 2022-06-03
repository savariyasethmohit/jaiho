"""# n=int(input("Enter the total days : "))
print("Mohit Sharma")
student=str(input("Give The Attendance :"))
countA=0
countP=0
countL=0
for i in student:
    if i=='A':
        countA+=1
    elif i=='P':
        countP+=1
    elif i=='L':
        countL+=1
    else:
        print("Please give right attendance")
        exit()

if countA>=2 or countL>=3:
    print("False")
    print("The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.")
else:
    print("True")
    print("The student has fewer than 2 absences and was never late 3 or more consecutive days.")

# print(countA)
# print(countP)
# print(countL)


print("Mohit Sharma")
def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ')
        num1 = num2
        num2 = series
        series = num1 + num2
num = int(input('Enter the number : '))
fibonacci(num)"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n == 0:
            return res

        for i in range(pow(2, n)):
            l = []
            for j in range(n):
                if i & (1 << j) > 0:
                    l.append(nums[j])
            res.append(l)
        return res

    nums=list(input())