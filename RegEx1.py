import re
import os


def mline():
    user = os.getlogin()
    with open('C:/Users/'+user+'/Desktop/Python/CourseraRegEx.txt', 'r') as pros:
        s = 0
        r = pros.read()
        l = re.findall('[0-9]+', r)
        for _ in l:
            s += int(_)
        print(s)


def main():
    mline()


if __name__ == "__main__":
    main()