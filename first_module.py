"""
If Python runs a file, it sets a few special variables before running any code. __name__ is one of those. If Python runs a file directly, it sets the name variable equal to __main__

When you import a module, it will set the __name__ variable to the name of the file. 

the following prints "First module's name: first_module" when run here

print("First module's name: {__name__}")  # prints __main__ """

# prints "First Module's name: __main__"


def main():
    print("First module's name: {__name__}")


# this asks if this file is run directly by Python or being imported.
# main() is not run when you run second_module.py that imports first_module, and therefore sets name to "first_module" and not "main"
if __name__ == '__main__':
    main()
