
def traffic_signal(func):
    print("RED : STOP" )
    func()
    print("GREEN : Go")
    
        

@traffic_signal
def traffic_sig():
    print("YELLOW : SLOW DOWN")



# def print1():
#     print("down fuction")
# print1()
def highest_sum(input_str):
    # Convert the input string into a list of integers
    nums = [int(char) for char in input_str]

    prev = 0
    total_sum = 0

    # Iterate through the list
    while nums:
        num = nums.pop(0)

        # If the number is equal to the previous number, remove it from the list and add it to the sum
        if num == prev:
            total_sum += num
        # If the number is not equal to the previous number, add it to the sum and update the previous number
        else:
            total_sum += num
            prev = num

    return total_sum

print(highest_sum('1211'))