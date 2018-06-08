from human import *


def main():
    a = Human()
    b = Female('El')
    c = a
    c.sex = Sex.MALE
    b.sex = Sex.MALE
    print(a)
    print(b)
    print(c)
    if a == c:
        print('a and c are same person')
    else:
        print('a and c are different person')


if __name__ == '__main__':
    main()
