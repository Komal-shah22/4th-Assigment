
def countDown(number_list: list[int]):
    for i in number_list:
        print(i, end=" ")
    print("Liftoff!")

def countDown1():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("List off")

countDown1()

number_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

countDown(number_list)
countDown(number_list)