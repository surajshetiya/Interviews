testcases = int(raw_input())
lookup = [[]]
text = ''

"""
DP solution that has a table of size n^2. Total time is n^3.
"""


def lookup_value(x, y, length):
    global lookup
    if(len(lookup[0]) != 0):
        return lookup[x][y]
    else:
        lookup = []
        for times in range(0,length):
            lookup.append([-1]*length)
        return lookup[x][y]

def solve(start, end):
    global text
    global lookup
    length = len(text)
    if(lookup_value(start, end, length) == -1):
        minimum = float('Inf')

        if(start == end):
            if(text[start] == 'x'):
                lookup[start][start] = 0
            else:
                lookup[start][start] = 1
            return lookup[start][start]

        # Add a character * to the end and run combinations of 0 to x and x+1 to n
        for mid in range(start, end):
            value = solve( start, mid ) + solve( mid+1, end ) + 1
            if( value < minimum ):
                minimum = value

        # Change a character at right end  to * if it is x
        if(text[end] == '*'):
            basic = 0
        else:
            basic = 1
        for mid in range(start, end):
            if(mid <= end - 2 ):
                value = solve(start, mid) + solve(mid + 1, end - 1)
            else:
                value = solve(start, mid - 1) + 1 # Add an 'x' char
            if(value + basic < minimum):
                minimum = value + basic

        # Check combinations of deletions and size from right and left
        for e in range(start, end):
            value = end - e + solve(start, e)
            if( value < minimum ):
                minimum = value
            value = e + 1 - start + solve(e + 1, end)
            if (value < minimum):
                minimum = value

        lookup[start][end] = minimum
        return minimum
    else:
        return lookup[start][end]

for t in range(0, testcases):
    global lookup
    global text
    lookup = [[]]
    text = raw_input()
    print(solve(0, len(text)-1))
