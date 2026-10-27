if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second = sorted(set(s[1] for s in students))[1]
    for name in sorted(s[0] for s in students if s[1] == second):
        print(name)
