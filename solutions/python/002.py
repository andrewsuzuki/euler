def solution():
    sum = 0
    nl = 1
    n = 2
    while (n < 4e6):
        if (n % 2 == 0):
            sum += n
        new = nl + n
        nl = n
        n = new
    return sum

if __name__ == "__main__":
    print(solution())
