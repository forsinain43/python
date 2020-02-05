# Michael Reid 119399591
# functions.py

def to_english(num):
    '''
        A function that takes an integer input between -999 and 999 and converts it to english words
        num = input
    '''
    units = ["", "one ", "two ", "three ", "four ",  "five ",
                 "six ", "seven ", "eight ", "nine "]

    teens = ["", "eleven ", "twelve ", "thirteen ",  "fourteen ",
                 "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

    tens = ["", "ten ", "twenty ", "thirty ", "forty ",
                "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    num = int(num)
                                                    # string version of the num for the - values
    stringnum = str(num)
    words = []                                      # make a list of the words to print
    if num == 0:                                    # if 0
        words.append("zero ")
    else:
        length = len(stringnum)
        i = 0

        if '-' in stringnum:                        # negative numbers

            words.append("minus ")
            if length == 4:                         # for hundreds;
                                                    # format into hundreds, tens and units
                hun = int(stringnum[i + 1])
                ten = int(stringnum[i + 2])
                unit = int(stringnum[i + 3])

            if length == 3:                         # for tens;
                hun = 0                             # format into tens and units
                ten = int(stringnum[i + 1])
                unit = int(stringnum[i + 2])

            if length == 2:                         # for units;
                hun = 0                             # format into units
                ten = 0
                unit = int(stringnum[i + 1])

        elif '-' not in stringnum:                  # positive numbers

            if length == 3:                         # for hundreds;
                    	                            # format into hundreds, tens and units
                hun = int(stringnum[i])
                ten = int(stringnum[i + 1])
                unit = int(stringnum[i + 2])

            if length == 2:                         # for tens;
                hun = 0                             # format into tens and units
                ten = int(stringnum[i])
                unit = int(stringnum[i + 1])

            if length == 1:                         # for units;
                hun = 0                             # format into units
                ten = 0
                unit = int(stringnum[i])

        if hun >= 1:                                # if 100 or greater
            words.append(units[hun])
            words.append("hundred ")

        if hun >= 1 and ten >= 1:                   # if not even hundreds
            words.append("and ")

        if hun >= 1 and ten == 0 and unit > 0:
            words.append("and ")

        if ten > 1:                                 # if 20 or greater
            words.append(tens[ten])

            if unit >= 1:                           # if not even tens
                words.append(units[unit])

        elif ten == 1:                              # if in teens
            if unit >= 1:                           # if not 10
                words.append(teens[unit])

            else:                                   # if 10
                words.append(tens[ten])

        else:
            if unit >= 1:                           # if not 0
                words.append(units[unit])

    output = ''                                     # make a string from the list
    for element in words:
        output += element

    return output.capitalize()


def sort_a_list(s):
    
    new_s = []

    while s:
        minimum = s[0]
        for value in s:
            if value < minimum:
                minimum = value
        new_s.append(minimum)
        s.remove(minimum)

    no_dupes = []
    for value in new_s:
        if value not in no_dupes:
            no_dupes.append(value)
            
    return no_dupes


def ascii_difference(m, n):

    combine = []  # combined ascii vals
    diff = []  # difference between ascii vals

    while len(m) < len(n):
        m.append("\0")
        
    while len(m) > len(n):
        n.append("\0")
     
      
    for i in range(len(m)):
        addedval = ord(str(m[i])) + ord(str(n[i]))
        combine.append(addedval)
        
        diffval = ord(str(m[i])) - ord(str(n[i]))
        diff.append(abs(diffval))

    return combine, diff
