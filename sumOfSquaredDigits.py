def getSumOfSqaures(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)*int(digit)      
    return sum