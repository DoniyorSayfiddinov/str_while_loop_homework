def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if s[i].isdigit() and int(str(s[i]))%2==1 :
            k+=int(str(s[i]))
        i+=1
    return k
print(main("98421"))