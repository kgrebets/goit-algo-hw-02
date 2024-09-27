from collections import deque


def is_palindrome(s: str) -> bool:
    dq = deque(s)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def main():
    test_strs = [
        "civic",
        "123321",
        "Hello",
    ]

    for s in test_strs:
        result = is_palindrome(s)
        print(f'"{s}" - {( "is" if result else "is not") } palindrome')

if __name__ == "__main__":
    main()