import re
from toblibz.lib import findc


with open("./input","r") as finput:
    valid_password = 0
    for i in finput:

        finput_split=i.split(' ')
        interval = finput_split[0].split('-')
        character = finput_split[1].strip(':') #  ->
        password = list(finput_split[2])
        password.sort()

        interval_min = interval[0] # -> x
        interval_max = interval[1] # -> y

        regex_search_pattern = r"".join(
             [  "^",
                character, 
                "{", 
                interval_min, 
                ",", 
                interval_max, 
                "}", "$" ] ) # ==> "^c{x,y}$"

        # def findc(s,c): 
        #   return "".join( [s[i] for i,l in enumerate(s) if l==c] ), [i for i,l in enumerate(s) if l==c]
        password_sorted_searched_chars = findc("".join(password),character)[0]

        if re.search(regex_search_pattern, password_sorted_searched_chars):
            valid_password += 1
    print(valid_password)
    finput.close()