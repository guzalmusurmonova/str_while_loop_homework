def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """ 
    n=0
    i=0  
    while n<len(s): 
        if int(s[n])%2!=0:
            i=i+1 
        n=n+1  

    return i 
print(main("1567534"))
    