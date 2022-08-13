def roman2arab(str):
    """Converts a number in roman notation to integer form and prints the result

    Parameters
    ----------
    str : str 
        String of number in roman notation
        
    Returns
    -------
    int
        Integer form of roman number
    """

    roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    result = 0

    for i in range(len(str)):
        if i + 1 < len(str) and roman[str[i]] < roman[str[i+1]]:
            result -= roman[str[i]]
        else:
            result += roman[str[i]]
            
    print(result)
    return result