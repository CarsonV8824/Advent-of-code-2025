def password(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    list_of_passwords = [line.replace("\n", "").strip() for line in lines]

    starting = 50
    

    number_of_zeros = 0
    for index, combo in enumerate(list_of_passwords):
        
        if combo.count("R") == 1:
            number = int(combo.replace("R", ""))
            for i in range(number):
                starting += 1
                
                if starting == 100:
                    starting = 0

            if starting == 0 and list_of_passwords[index+1].count("L") == 1:
                number_of_zeros += 1
            
        elif combo.count("L") == 1:
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