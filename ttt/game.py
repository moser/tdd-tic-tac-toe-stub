
def main(stdin, stdout):

    def prnt(msg, *args):
        msg = msg + " " + repr(args)
        stdout.write(msg + "\n")
    def inpt(prompt):
        stdout.write(prompt + "\n")
        return stdin.readline().strip()

    while True:
        user_input = inpt("Ask player X for input:")
        # TODO: Now do something with the input?
        if user_input == "exit":
            break
        prnt("Player entered:", user_input)


if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)
