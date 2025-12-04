def password(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    list_of_passwords = [line.replace("\n", "") for line in lines]
    
    starting = 50
    
    number_of_zeros = 0
    for index, combo in enumerate(list_of_passwords):
        if combo[0].upper() == "R":
            
            number = int(combo.replace("R", ""))
            
            for i in range(number):
                starting += 1
                if starting == 100:
                    starting = 0
            
            if starting == 0:
                number_of_zeros += 1
        elif combo[0].upper() == "L":
            
            number = int(combo.replace("L", ""))
            
            for i in range(number):
                
                starting = starting - 1
                
                if starting == -1:
                    starting = 99
        
            if starting == 0:
                number_of_zeros += 1
    return number_of_zeros

print(password("src/day1/day1.txt"))
print(password("src/day1/test_day1.txt"))
