import jmespath as jmp


# testing: alpha or digits
def ternar_expression():
    string = input("Please, enter string: ")
    result = True if string.isalpha() else False

    print(result)

    return string, result


def main():
    test_dict = {}
    string, bul_result = ternar_expression()
    number = len(string)
    for item in range(1, number + 1):
        test_dict[str(item)] = string[item - 1]
    test_dict[str(int(number / 2))] = {"123": "test", "train": {"123456": ["fhfhfh", "ruieiw"]}}
    print(test_dict)
    jmespath_value = jmp.search("train", test_dict)
    print(f"The result of the jmespath work: {jmespath_value}.")

    return test_dict, jmespath_value


if __name__ == "__main__":
    main()
