from collections import deque


def isPalindrome(num):
    num_deque = deque(str(num))
    while(len(num_deque) > 0):
        if(num_deque[0] == num_deque[-1]):
            num_deque.pop()
            if(len(num_deque) > 0):
                num_deque.popleft()
        else:
            return(False)
    return(True)

if __name__ == "__main__":
    palindromes = []
    left_mult = 999
    while (left_mult > 99):
        right_mult = 999
        while(right_mult > 99):
            product = left_mult * right_mult
            if(isPalindrome(product)):
                palindromes.append(product)
            right_mult = right_mult - 1
        left_mult = left_mult - 1

    print(max(palindromes))
