

class mahmoud98():
    def pr():
        print("Hi\nTravis CI test lang:python ")
        print("Happy new year : ", 1398, " :) ")
        print("\n")

    def nump():

        import numpy as np
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        arr2 = np.power(arr, 2)
        print(arr2)

    def op(a, b):
        if a == b:
            return('a = b')
        else:
            raise ValueError("Error a != b")


if __name__ == '__main__':
    mahmoud98.pr()
    # nump()
    mahmoud98.op(5, 3)
