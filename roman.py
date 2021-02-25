def to_roman(n):
    '''
    Convert any integer between 0 and 1000 to roman numerals.

    Parameters
    ----------
        n : int
            Integer between 0 and 1000. This input will be converted to roman numerals.
    GitHub
    ------
        https://github.com/ArturoSbr/
    '''
    try:
        if n >= 0 and n <= 1000:
            d = [{'0':'','1':'M'},
                 {'0':'','1':'C','2':'CC','3':'CCC','4':'DC','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'MC'},
                 {'0':'','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'CX'},
                 {'0':'','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}]
            x = str('0000' + str(n))[-4:]
            r = ''
            for i in range(4):
            r = r + d[i][x[i]]
            return r
        else:
            return '`n` is out of bounds.'
    except:
        print('Is this real life?\nIs `n` even an integer?')
