class test4_class:
    b = 10
    def __init__(self):
        print('test_4_class')
        self.a = "test_4_var"

    def _print_a(self):
        print(self.a)
    
    def _print_b(self):
        print(f'b is {self.b}')

test4=test4_class()
test4._print_a()
test4._print_b()