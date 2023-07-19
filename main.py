from problems import example, pb1, pb2, pb3

def main():
    pass
    # print('ding dong')
    # example.testFunc()

    # Test Cases

    # Problem #1: Replace Spaces
    sentence = "Test  This is a test   Testing "
    sentence2 = pb1.replace_spaces(sentence, "_")
    # print(sentence2)

    # Problem #2: Max Values
    # print(pb2.max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
    # print(pb2.max_values([-5, -2, -1, -11])) # -> [1, 2]  

    # Problem #3: Youngest Student
    students1 = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
    students2 = {"Bob": 20, "Charlie": 19, "David": 22, "Jay": 20, "Alice": 18, "Drake": 16, "Mary": 25}
    # print(pb3.youngest_student(students1))  # Expected output: "Alice"
    # print(pb3.youngest_student(students2))  # Expected output: "Drake"


if __name__ == '__main__':
    main()
