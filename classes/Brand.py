class Brand:

    def __init__(self, name, slogan):
        self.name = name
        self.slogan = slogan

    def __str__(self):
        return f"[ Brand {self.name} with slogan {self.slogan} ]"