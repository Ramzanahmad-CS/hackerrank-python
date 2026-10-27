if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = set(arr)
    print(sorted(scores)[-2])
