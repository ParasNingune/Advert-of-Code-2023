import regex as re

filePath = "input.txt"

DIGIT_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
RE = r'\d|' + '|'.join(DIGIT_WORDS)  # Regex pattern for digits or spelled-out digit words

def calculateSum(filePath):
    totalSum = 0

    def get_digit_from_digit_or_word_digit(target):
        # Returns numeric value if target is in DIGIT_WORDS, else returns target
        return str(DIGIT_WORDS.index(target) + 1) if target in DIGIT_WORDS else target

    with open(filePath, 'r') as file:
        for line in file:
            line = line.strip()  # Remove extra spaces or newline characters
            if not line:  # Skip empty lines
                continue

            # Find all matches for digits or digit words
            matches = re.findall(RE, line, overlapped=True)
            if not matches:
                continue  # Skip lines without matches

            # Extract the first and last matches
            first_digit = matches[0]
            last_digit = matches[-1]

            # Convert spelled-out words to digits if necessary
            first_digit = get_digit_from_digit_or_word_digit(first_digit)
            last_digit = get_digit_from_digit_or_word_digit(last_digit)

            # Form the calibration value and add to the total
            calibrationValue = int(first_digit + last_digit)
            totalSum += calibrationValue

    return totalSum

result = calculateSum(filePath)
print(result)


# Answer -> 54473