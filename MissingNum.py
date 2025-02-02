n=int(input())

numbers=list(map(int,input().split()))

total=n*(n+1)//2

currSum=sum(numbers)

missingNum=(total-currSum)

print(missingNum)
