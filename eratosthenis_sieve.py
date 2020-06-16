##Sieve
def sieve(num):
    max_num = int(input(num))
    num_list = list(range(2, max_num + 1))
    i = 0
    while i < len(num_list):
        next_num = num_list[i] 
        multiples_of_next_num = list(range(next_num * 2, max_num + 1, next_num))
        num_list = list(set(num_list) - set(multiples_of_next_num))
        num_list.sort()
        i += 1

    return num_list
 
    

print(sieve("Enter a number: "))
