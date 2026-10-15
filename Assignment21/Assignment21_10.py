import threading


sum_result = 0
product_result = 1


def calculate_sum(numbers):

    global sum_result

    for number in numbers:
        sum_result += number


def calculate_product(numbers):

    global product_result

    for number in numbers:
        product_result *= number


def main():

    Size = int(input("Enter how many No. u want in list : "))

    Arr = []

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    thread1 = threading.Thread(target=calculate_sum, args=(Arr,))
    thread2 = threading.Thread(target=calculate_product, args=(Arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Sum :", sum_result)
    print("Product :", product_result)


if __name__ == "__main__":
    main()