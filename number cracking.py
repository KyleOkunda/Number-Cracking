number = input('Enter number: ')


if len(number) != 4:
    print('The number has to be four digits.')
else:
    digit_list = []
    for digit in number:
        digit_list.append(int(digit))
    print(digit_list)

    def dig_0():
        for digit_0 in range(10):
            while digit_0 == digit_list[0]:
                digit_0 = digit_list[0]
                return(digit_0)
                
    
    def dig_1():
        for digit_1 in range(10):
            while digit_1 == digit_list[1]:
                digit_1 = digit_list[1]
                return(digit_1)
               
    
    def dig_2():
        for digit_2 in range(10):
            while digit_2 == digit_list[2]:
                digit_2 = digit_list[2]
                return(digit_2)
               
    def dig_3():
        for digit_3 in range(10):
            while digit_3 == digit_list[3]:
                digit_3 = digit_list[3]
                return(digit_3)
               
    
   
   
    digit_0 = str(dig_0())
    digit_1 = str(dig_1())
    digit_2 = str(dig_2())
    digit_3 = str(dig_3())
    
    number_guess = digit_0 + digit_1 +digit_2 + digit_3
    print(number_guess)
    


        

    
   
    
    
    
            

       
   
    
