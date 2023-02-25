def palindrome (string):
    """
        Prints boolean, based on arguments passed
        Arguments:
        word for checking
    """
    if(string == string[::-1]):
        return(True)
    else:
        return(False)
print(palindrome("дід"))



