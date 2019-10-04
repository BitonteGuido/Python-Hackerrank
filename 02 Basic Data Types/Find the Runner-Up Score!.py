if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listnew=[]

    for i in arr:
        if i not in listnew:
            listnew.append(i)
    listnew.sort(reverse=True)
    print(listnew[1])
