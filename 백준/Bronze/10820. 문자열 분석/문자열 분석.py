while True:
    try:
        a = input()
        print(sum(b.islower() for b in a), sum(b.isupper() for b in a), sum(b.isnumeric() for b in a), a.count(' '))
    except EOFError:
        break