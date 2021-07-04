def isfloat(st: str):
    """Check if a string is a floating point number"""
    # check for numeric characters and '.'. Also, check if '.' appears just once
    if (i in st for i in "0123456789.") and st.count('.') == 1:
        return True
    else:
        return False


string = ".233"
print(isfloat(string))
print(float(string))
