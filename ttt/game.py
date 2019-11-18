
def main():
    exit = False
    while not exit:
        user_input = input("Ask player X for something: ")
        print("Player entered:", user_input)
        # TODO: Now do something with the input?
        if user_input == "exit":
            exit = True


if __name__ == "__main__":
    main()
