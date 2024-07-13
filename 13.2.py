class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < sself.min_value or start > self.max_value:
            raise ValueError("Початкове значення повинно бути в межах мініму та максимуму")
        self.current = start

    def set_max(self, max_max):
        if max_value < seslf.min_value:
            raise ValueError("Максимальне значення не може бути менще мінімільнго ")
        self.max_value = max_value
        if self.current > max_value:
            self.current = max_value

    def set_min(self, min_min):
        if min_value > self.max_value:
            raise ValueError("Mінімальне значення не може бути більше максимального")
        self.min_value = min_value
        if self.current < min_value:
            self.current = min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимум")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімум")
        self.counter -= 1

    def get_current(self):
        return self.current
