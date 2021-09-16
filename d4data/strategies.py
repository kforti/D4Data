

class Strategy:
    def __init__(self):
        self.actions = {}
        self.strategies = {}
        self.type_checks = []

    def traversal(self, actions=True, func=None,):
        pass

    def apply_one(self):
        pass

    def apply_all(self):
        pass

    def check_type(self, data):
        for func in self.type_checks:
            result = func(data)
            if result:
                return result

    def add_action(self, name, func):
        self.actions[name] = func

    def add_type_check(self, func):
        self.type_checks.insert(0, func)
