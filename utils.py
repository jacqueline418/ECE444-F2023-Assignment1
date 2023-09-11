class utils:
    
    def reversed(int_number):

        assert type(int_number) == int, "input not an integer"
        if(int_number>=0):
            reversed_str = str(int_number)[::-1]
            reversed_int = int(reversed_str)
        else:
            reversed_str = str(-int_number)[::-1]
            reversed_int = -int(reversed_str)
        return reversed_int
    
    def formatter(int_number):
        assert type(int_number) == int, "input not an integer"
        return bin(int_number), oct(int_number)
