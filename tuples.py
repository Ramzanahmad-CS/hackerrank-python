if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    M = 2 ** 64
    x = 0x345678
    mult = 1000003
    length = len(t)
    for item in t:
        length -= 1
        x = ((x ^ (hash(item) % M)) * mult) % M
        mult = (mult + 82520 + length + length) % M
    x = (x + 97531) % M
    if x >= 2 ** 63:
        x -= M
    if x == -1:
        x = -2
    print(x)
