from pyplates import capture_output


def test_capture_output():
    code = """
    def f(x):
        x = x + 1
        return x

    print 'This is my output.'
    """
    capture_output(code)
    print(f(4))
