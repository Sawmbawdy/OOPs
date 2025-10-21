class IOstring:
    def __init__(self):
            self.str1 = ''

    def get_string(self):
          self.str1 = input("Enter the string: \n")

    def convert_string(self):
          print("The upper cased format is: \n", self.str1.upper())

st1 = IOstring()
st1.get_string()
st1.convert_string()
