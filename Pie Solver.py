"""
Pie Chart Solver

39.3, 28.6

"""

def pie(nums):
    res = []
    for num in nums:
        numerator = 1
        denominator = 2
        while not (((numerator / denominator) > ((num-0.05)/100)) and ((numerator / denominator) < ((num+0.05)/100))):
            if ((numerator / denominator) < ((num-0.05)/100)):
                numerator += 1
            else:
                denominator += 1
        res.append(denominator)
    return max(res)
        
nums = [39.3, 28.6]
print(pie(nums))