
def main(stdin, stdout):

    def prnt(msg, *args):
        msg = msg + " " + repr(args)
        stdout.write(msg + "\n")
    def inpt(prompt):
        stdout.write(prompt + " ")
        return stdin.readline().strip()

    exit = False
    while not exit:
        user_input = inpt("Ask player X for input:")
        prnt("Player entered:", user_input)
        # TODO: Now do something with the input?
        if user_input == "exit":
            exit = True


if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)
