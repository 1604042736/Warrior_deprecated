class Player:
    goods = [
        ["Wooden sword", 100, 10, 0, "nothing"],
        ["Iron sword", 200, 20, 0, "nothing"],
        ["Golden sword", 300, 30, 0, "nothing"],
        ["Bronze sword", 400, 40, 0, "nothing"],
        ["Diamond sword", 500, 50, 0, "nothing"],
        ["Leather Helmet", 100, 0, 10, "nothing"],
        ["Leather Armor", 100, 0, 13, "nothing"],
        ["Leather shinguard", 100, 0, 16, "nothing"],
        ["Leather Boots", 100, 0, 19, "nothing"],
        ["Iron helmet", 200, 0, 20, "nothing"],
        ["Iron armor", 200, 0, 23, "nothing"],
        ["Iron shinguard", 200, 0, 26, "nothing"],
        ["Iron boots", 200, 0, 29, "nothing"],
        ["Gold helmet", 300, 0, 30, "nothing"],
        ["Gold armor", 300, 0, 33, "nothing"],
        ["Gold shinguard", 300, 0, 36, "nothing"],
        ["Golden boots", 300, 0, 39, "nothing"],
        ["Bronze Helmet", 400, 0, 40, "nothing"],
        ["Bronze armor", 400, 0, 43, "nothing"],
        ["Bronze shinguard", 400, 0, 46, "nothing"],
        ["Bronze boots", 400, 0, 49, "nothing"],
        ["Diamond helmet", 500, 0, 50, "nothing"],
        ["Diamond armor", 500, 0, 53, "nothing"],
        ["Diamond Leggings", 500, 0, 56, "nothing"],
        ["Diamond Boots", 500, 0, 59, "nothing"],
        ["Arch", 300, 30, 0, "nothing"],
        ["Shield", 300, 0, 100, "nothing"],
        ["Arrow", 1, 0, 0, "nothing"]
    ]
    chant = [
        ["Damage increased(1)", 100, 10, 0],
        ["Damage increased(2)", 120, 30, 0],
        ["Damage increased(3)", 140, 50, 0],
        ["Damage increased(4)", 160, 70, 0],
        ["Damage increased(5)", 180, 90, 0],
        ["Increased defense(1)", 100, 0, 10],
        ["Increased defense(2)", 120, 0, 30],
        ["Increased defense(3)", 140, 0, 50],
        ["Increased defense(4)", 160, 0, 70],
        ["Increased defense(5)", 180, 0, 90],
        ["Comprehensive improvement(1)", 1000, 20, 20],
        ["Comprehensive improvement(2)", 2000, 40, 40],
        ["Comprehensive improvement(3)", 3000, 60, 60],
        ["Comprehensive improvement(4)", 4000, 80, 80],
        ["Comprehensive improvement(5)", 5000, 100, 100]
    ]

    def __init__(self, config):
        self.config = config

    def addmoney(self, add):
        self.config['money'] += add
