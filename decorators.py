# a function and takes a function of input and modify it
# announces the function for decorators: Very powerful e.g. announces users logging in, etc.
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

#decorator
@announce
def hello():
    print("Hello, world!")

hello()