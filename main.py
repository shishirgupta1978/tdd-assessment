class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0 # If the string is empty, return 0
        numbers = numbers.replace("\n", ",") # Replace new lines with commas
        num_list = numbers.split(",")
        return sum([int(num) for num in num_list])





if __name__==   "__main__":
    calculator = StringCalculator()
    print(calculator.add(""))
    print(calculator.add("1"))
    print(calculator.add("1,5"))
    print(calculator.add("1\n2,3"))