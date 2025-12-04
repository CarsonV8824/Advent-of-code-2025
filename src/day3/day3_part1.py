"""def staircase(filename):
    with open(filename, "r") as file:
        file_lines = file.readlines()
        
    file_lines = [line.replace("\n","") for line in file_lines]
    
    sum_of_numbers = 0
    for big_num in file_lines:
        first_num = 0
        first_num_index = 0
        
        second_num = 0
        second_num_index = 0
        
        for index, num in enumerate(big_num):
            if int(num) > int(first_num):
                first_num = int(num)
                first_num_index = int(index)
        
        if first_num_index == (len(str(big_num)) - 1):
            for index in range(0, len(str(big_num)) - 2):
                if int(big_num[index]) > int(second_num):
                    second_num = int(big_num[index])
                    second_num_index = int(index)
        else:
            for index in range(first_num_index+1, len(str(big_num)) -1):
                if int(big_num[index]) > int(second_num):
                    second_num = int(big_num[index])
                    second_num_index = int(index)
        
        if second_num > first_num:
            first_num, second_num = second_num, first_num
        
        
        sum_of_numbers += int(str(first_num) + str(second_num))
        break
    return sum_of_numbers"""
    
def staircase(filename):
    with open(filename, "r") as file:
        file_lines = file.readlines()
        
    file_lines = [line.replace("\n","") for line in file_lines]
    file_lines = [line.strip() for line in file_lines]
    sum_of_numbers = 0
    list_of_values = []
    for big_num in file_lines:
        
        first_num = 0 
        first_num_index = 0
        
        second_num = 0
        second_num_index = 0
        
        for index, f_num in enumerate(big_num):
            if int(f_num) > int(first_num):
                first_num = int(f_num)
                first_num_index = int(index)
        
        if first_num_index == len(big_num) - 1:
            for index in range(0, len(big_num) - 1):
                if int(big_num[index]) > int(second_num):
                    second_num = int(big_num[index])
                    second_num_index = index
            first_num, second_num = second_num, first_num
        
        else:
            for index, s_num in enumerate(big_num):
                if (int(s_num) > int(second_num)) and (int(s_num) <= first_num) and (first_num_index < index):
                    second_num = int(s_num)
                    second_num_index = int(index)

        
        sum_of_numbers += int(str(first_num) + str(second_num))
        list_of_values.append(str(first_num) + str(second_num))
    print((list_of_values))
    return sum_of_numbers
            
        
    
if __name__ == "__main__":
    print(staircase("src/day3/day3.txt"))