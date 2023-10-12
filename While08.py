def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if int(str(s[i]))%2==1 :
            k+=1
        i+=1
    return k
print(main("1567534"))