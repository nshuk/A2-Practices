def PROCEDUREX (denary):
    if (denary == 0) or (denary==1):
        print(denary, end=" ")
    else:
        PROCEDUREX(int(denary/2))
        print(denary%2, end=" ")

PROCEDUREX(40)

# personal note
# use of end=" " to combine lines, so it is printed in the same line
# basically in pseudocode is procedure(n DIV 20) followed by output(n MOD 2)
# div truncates the decimals
# mod takes the remainder. say, 5 mod 2 will bring you 2,1/2. that 1 is the result