class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"最大的是的{self.r}"

    def __lt__(self, other):
        return self.r < other.r


list_color = [Color(102, 178, 120), Color(135, 156, 129),
              Color(110, 137, 117)]

print(max(list_color))
# list_color.remove(Color(102, 178, 120))
# for i in list_color:
#     print(i)
