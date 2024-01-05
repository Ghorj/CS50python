class Jar:
    def __init__(self, capacity=12):

        #__init__ should initialize a cookie jar with the given capacity
        #which represents the maximum number of cookies that can fit in the cookie jar
        self.capacity = int(capacity)
        self.size = 0


    def __str__(self):
        #__str__ should return a str with n 🍪 (cookies in jar)
        return "🍪" * self.size

    def deposit(self, n):
        try:
            #If adding that many would exceed the cookie jar’s capacity raise ValueError
            if (self.size + n) <= self.capacity and n >= 0:
                self.size += n
            else:
                raise ValueError
        except TypeError:
            raise ValueError



    def withdraw(self, n):
        try:
            #If there aren’t that many cookies raise ValueError
            if n > self.size or n < 0:
                raise ValueError

            #remove n cookies from the cookie jar.
            else:
                self.size -= n
        except TypeError:
            raise ValueError

    #capacity getter
    @property
    def capacity(self):
        #capacity should return the cookie jar’s capacity.
        return self._capacity

    #capacity setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity.is_integer() == True and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError

    #size getter
    @property
    def size(self):
        #size returns the number of cookies actually in the cookie jar, initially 0
        return self._size

    #size setter
    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar(input("Size of the jar: "))

    while True:

        action = input("deposit or withdraw? (d/w/e): ")

        if action.lower() == "e":
            print("Goodbye!")
            break

        if action.lower() == "d":
            try:
                jar.deposit(int(input("How many cookies do you want to deposit?: ")))
            except ValueError:
                print("The jar is too small!")

        elif action.lower() == "w":
            try:
                jar.withdraw(int(input("How many cookies do you want to eat?: ")))
            except ValueError:
                print("Too greedy!")

        else:
            print("Invalid action")

        print(jar)



if __name__ == "__main__":
    main()
