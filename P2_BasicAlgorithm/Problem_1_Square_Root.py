def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    #: egde case
    if number == None:
        return None


    ceiling_flag = False #: to handle edge cases when first sq value is 1
    root = number//2
    sq = root**2
    if  sq == number:
        return root
    else:
        while True:
            if sq > number:  #: squared number is greater
                root -= 1    #: subtract one and then repeat
                if ceiling_flag is False:
                    ceiling_flag = True
                sq = root**2
            else:            #: squared number is lesser
                if ceiling_flag:
                    return root #: return root if we have seen a ceiling
                else:
                    root += 1    #: add one if we have not seen a ceiling
                    sq = root**2                     




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")
