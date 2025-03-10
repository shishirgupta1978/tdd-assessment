class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0 # If the string is empty, return 0

        if numbers.startswith("//"): # If the string starts with a custom delimiter
            end = numbers.find("\n")
            delimiter = numbers[2:end]
            numbers = numbers[end + 1:]
            num_list = numbers.split(delimiter)
        else:
            numbers = numbers.replace("\n", ",") # Replace new lines with commas
            num_list = numbers.split(",")

        negatives = []
        total = 0
        for num in num_list:
            num = int(num)
            if num < 0:
                negatives.append(num)
            else:
                total += num
        
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        return total






if __name__==   "__main__":
    calculator = StringCalculator()
    print(calculator.add(""))
    print(calculator.add("1"))
    print(calculator.add("1,5"))
    print(calculator.add("1\n2,3"))
    print(calculator.add("//;\n1;2"))
    print(calculator.add("1,-2,3"))
    