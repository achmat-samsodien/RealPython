

pos_int = int(raw_input("Enter a positive integer:"))
for divisor in range(1, pos_int+1):
    if pos_int % divisor == 0:
        print "{} is a divisor of {}".format(divisor, pos_int)


