'''
The python code has solved the hacker rank questioned mentioned in the URL: https://www.hackerrank.com/challenges/string-validators/
'''


if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper()for c in s))