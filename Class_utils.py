class utils:
    def reversed (num_rev):
        original_num_rev = num_rev
        if not isinstance(num_rev, int):
            print("Error: " + str(original_num_rev) + " is not an integer")
            return
        
        negative = False
        if num_rev < 0:
            negative = True
            num_rev = abs(num_rev) 
        
        num_to_string = str(num_rev)
        reversed_string = num_to_string[::-1]
        string_to_num = int(reversed_string)

        if negative:
            ans = -string_to_num
        else:
            ans = string_to_num
        
        print(str(original_num_rev) + " reversed is " + str(ans))
        return ans

    def formatter (num_form):
        if not isinstance(num_form, int):
            print("Error: " + str(num_form) + " is not an integer")
            return
        
        base_2_ans = bin(num_form)
        base_8_ans = oct(num_form)

        print(str(num_form) + " is " + str(base_2_ans) + " as base 2 and " + str(base_8_ans) + " as base 8")

        return base_2_ans, base_8_ans
