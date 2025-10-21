class employee:
    def __init__(self, Name):
        self.Name = Name
    def __del__(self):
        print(self.Name, "successfully fired")

Joe = employee('Joe')
print(Joe.Name)
del Joe