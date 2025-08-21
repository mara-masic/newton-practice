#Univariate Newton's Method (Completed)

def deriv(f, x, eps=1e-5):
    # if x < 5:
    #    raise RuntimeError("fake error")
    return (f(x + eps) - f(x)) / eps


def deriv2(f, x, eps=1e-5):
    return (deriv(f, x + eps, eps) - deriv(f, x, eps)) / eps


def optimize(x0, f, tol=1e-4):
    """Run Newton's method to minimize a function.

    Parameters
    ----------
    x0: starting value
    f: function to minimize
    tol: blah blah blah
    """
    x_new = x0 - deriv(f, x0) / deriv2(f, x0)
    x = x0
    while abs(x_new - x) > tol:
        x = x_new
        x_new = x - deriv(f, x) / deriv2(f, x)
    return {"x": x_new, "value": f(x_new)}



#Multivariate Newton's Method (in progress)

def f(params):
    x, y = params
    return (x - 1)**2 + (y - 2)**2
    

def multivariate_newton(f, x0, tol, max_itter):

    '''
    f: scalar vlaued fucniton
    x0: numpy array initila guess
    tol: convergence tolerance
    itter: number itterations

    algorithm:  x_new = x - H'g 
    '''
    
    grad = nd.Gradient(f)
    hess = nd.Hessian(f)

    x = np.array(x0, float)

    for i in range(max_itter):
        g = grad(x)
        h = hess(x)

        if np.linalg.norm(g) < tol:
            return x

        else:
            delta = np.linalg.solve(h, g)
            x_new = x - delta

    return x_new











