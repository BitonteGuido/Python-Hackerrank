if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    for i in student_marks:
        if query_name==i:
            prom=sum(student_marks[i])
            print("%.2f"%(prom/3))
