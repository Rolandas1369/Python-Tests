class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")
    # def setup_module(module):
    #     print("Setup module!")
    #
    # def teardown_module(module):
    #     print("Teardown module!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method == self.test2:
            print("\nTeariing down test2!")
        else:
            print("\nTearing down unknown test!")

    # def setup_function(function):
    #     if function == test1:
    #         print("\nSetting up test1!")
    #     elif function == test2:
    #         print("\nSetting up test2!")
    #     else:
    #         print("\nSetting up unknown test!")
    #
    # def teardown_function(function):
    #     if function == test1:
    #         print("\nTearing down test1!")
    #     elif function == test2:
    #         print("\nTeariing down test2!")
    #     else:
    #         print("\nTearing down unknown test!")

    def test1(self):
        print("Execurting test1!")
        assert True

    def test2(self):
        print("Execurting test2")
        assert True

#pytest -v -s test_fi
