if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    empty_list = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a + b + c != n:
                    empty_list.append([a,b,c])
    print(empty_list)                  
