filePath = "input.txt"

def calculateSum(filePath):
    totalSum = 0

    # Open file and read lines
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()     # Remove any extra space or blank lines

            firstDigit  = None
            lastDigit = None

            # Iterate over characters in the line to find the first and last digits
            for char in line:
                if char.isdigit():
                    if firstDigit is None:
                        firstDigit = char
                    lastDigit = char

            # Ensure both first and last digits are found
            if firstDigit is not None and lastDigit is not None:
                # Combine both digits and add
                calibrationValue = int(firstDigit + lastDigit)
                totalSum += calibrationValue

    return totalSum

    
result = calculateSum(filePath)

print(result)

# Answer -> 54990