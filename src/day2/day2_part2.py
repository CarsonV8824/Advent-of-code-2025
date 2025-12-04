import math

"""
I did not solve part 2 of day 2. I was, but I ran out of time!

"""

def id(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    ranges = []
    for l in lines:
        ranges.append(l.strip().replace("\n",""))
    ranges = str(ranges).replace("[","").replace("]","").replace("'","")
    id_ranges = ranges.split(",")

    ids = [(ida.split("-")) for ida in id_ranges]
    
    total = 0

    for each_id in ids:
        for num in range(int(each_id[0]), int(each_id[1]) + 1):
            temp_num = str(num)
            len_of_temp_num_half = math.ceil(len(temp_num) / 2)
            first_num = temp_num[0: len_of_temp_num_half]
            second_num = temp_num[len_of_temp_num_half: (len_of_temp_num_half * 2)]
            
            if first_num == second_num:
                number = str(first_num) + str(second_num)
                #print(number) 
                total += int(number)
    
    return f"the total sum of your id's is {total}"

if __name__ == "__main__":
    print(id("src/day2/day2.txt"))
