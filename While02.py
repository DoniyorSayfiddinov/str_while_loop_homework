def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answeris
    """
    i=0
    k=0
    while i<len(s):
         if s[i].isalpha():
            k+=1
         i+=1   
    return k
print(main("e324xE"))