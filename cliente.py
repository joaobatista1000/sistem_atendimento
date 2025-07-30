class Cliente:
    def __init__(self, name, vip=False):
        self.name = name
        self.vip = vip

    def __str__(self):
        return f"{'[VIP] ' if self.vip else ''}{self.name}"