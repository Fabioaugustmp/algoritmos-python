class MyClass:
    # Class attribute
    class_variable = "I am a class variable"

    # Constructor (initializer)
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance variable

    # Instance method
    def instance_method(self):
        return f"Instance variable: {self.instance_variable}"
