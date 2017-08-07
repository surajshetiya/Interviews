my_str = raw_input()

"""
Time complexity: n^2.
Space complexity: n^2
"""

total = 0
string_dict = {}
for loc in range(0, len(my_str)):
    if my_str[loc] in string_dict:
        string_dict[my_str[loc]].append(loc)
    else:
        string_dict[my_str[loc]] = [loc]
        total = total + 1


for i in range(2, len(my_str) + 1):
    temp_dict = {}
    for k, v in string_dict.iteritems():
        for loc in v:
            if(loc + i - 1 < len(my_str)):
                if((k + my_str[loc+i-1]) in temp_dict):
                    temp_dict[k + my_str[loc+i-1]].append(loc)
                else:
                    temp_dict[k + my_str[loc + i - 1]] = [loc]
                    total = total + 1

print(total)