class Lister(object):
    def get_integer_list(self, start, stop, step):
        if step != 0:
            result = []
            for value in range(start, stop+1, step):
                result.append(value)
            return result
        return [0]

    def get_even_list(self, start, stop, step):
        result = []
        for value in self.get_integer_list(start, stop, step):
            is_even = value % 2 == 0
            if is_even:
                result.append(value)
        return result

    def get_odd_list(self, start, stop, step):
        result = []
        for value in self.get_integer_list(start, stop, step):
            is_odd = value % 2 == 1
            if is_odd:
                result.append(value)
        return result