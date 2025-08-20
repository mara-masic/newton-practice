max_itter = 100
h = 1e-5


def function(x):
    return x**2


# Derivatives


def first_derivative(f, x, h=1e-5):
    df = (f(x + h) - f(x)) / h
    return df


def second_derivative(f, x, h=1e-5):
    df1 = first_derivative(f, x + h, h)
    df0 = first_derivative(f, x, h)
    ddf = (df1 - df0) / h
    return ddf


# Newton's Method


def newtons_method(x_0, f, tol=1e-7, max_iter=100):
    x = x_0
    df = first_derivative(f, x, h=1e-5)
    ddf = second_derivative(f, x, h=1e-5)

    for i in range(max_itter):
        if (x - h) > 0.1:
            x_1 = x - (df / ddf)
        return x_1
