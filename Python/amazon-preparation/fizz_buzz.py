def fizz_buzz(n):
    print(f"el pinche numerito: {n}")
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":

    n = int(input('Incerte su pinche numero: '))

    fizz_buzz(n)
