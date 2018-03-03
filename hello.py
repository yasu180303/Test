import sys

def hello(name):
    return "Hello, {0}".format(name)
    
def bye(name):
    return "Bye, {0}".format(name)
    
def main():
    name = sys.argv[1]
    print(hello(name))
    print(bye(name))
    
        
