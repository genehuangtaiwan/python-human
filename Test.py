from human import Human


def main():
    a = Human()
    b = Human()
    c = a
    print(a)
    print(b)
    if a == c:
        print('a and c are same person')
    else:
        print('a and c are different person')


if __name__ == '__main__':
    main()