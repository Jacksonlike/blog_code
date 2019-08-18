class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Father(metaclass=Singleton):
    def __init__(self):
        print('Creating Father')


class Son(Father):
    def __init__(self):
        print('Creating Son')


if __name__ == '__main__':
    a = Father()
    b = Father()
    print(a is b)

    c = Son()
    d = Son()
    print(c is d)
