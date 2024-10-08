import numpy as np
import matplotlib.pyplot as plt

class Function:
    """
    A class to represent a mathematical function using a lambda expression.
    
    Attributes:
    ----------
    func : lambda
        A lambda function representing a mathematical function.
    """

    def __init__(self, func):
        """
        Initializes the Function object with a given lambda function.
        
        Parameters:
        ----------
        func : lambda
            A lambda function to initialize the Function object.
        """
        self.func = func

    def __call__(self, x):
        """
        Makes the Function object callable.
        
        Parameters:
        ----------
        x : float or array-like
            Input value for the lambda function
        
        Returns:
        -------
        float or array-like
            The result of the lambda function
        """
        return self.func(x)

    def __add__(self, other):
        """
        Overload the addition operator
        """
        return Function(lambda x: self(x) + (other(x) if isinstance(other, Function) else other))

    def __sub__(self, other):
        """
        Overload the substration operator
        """
        return Function(lambda x: self(x) - (other(x) if isinstance(other, Function) else other))

    def __mul__(self, other):
        """
        Overload the multification operator
        """
        return Function(lambda x: self(x) * (other(x) if isinstance(other, Function) else other))

    def __truediv__(self, other):
        """
        Overload the division operator
        """
        return Function(lambda x: self(x) / (other(x) if isinstance(other, Function) else other))


class Plotter:
    """
    A class to handle the plotting of multiple mathematical functions using Matplotlib.
    
    Attributes:
    ----------
    domain_start : float
        Starting value of the domain.
    domain_end : float
        Ending value of the domain.
    step_size : float
        Step size for generating the domain values.
    functions : list
        List of tuples containing function labels and Function objects.
    """

    def __init__(self, domain_start, domain_end, step_size):
        """
        Initializes the Plotter object with domain range and step size.
        
        Parameters:
        ----------
        domain_start : float
            Start of the domain range.
        domain_end : float
            End of the domain range.
        step_size : float
            Step size for the domain range.
        """
        self.domain_start = domain_start
        self.domain_end = domain_end
        self.step_size = step_size
        self.functions = []

    def add_func(self, label, function_obj):
        """
        Adds a Function object to the Plotter for plotting.
        
        Parameters:
        ----------
        label : str
            Label of the function for the plot legend.
        function_obj : Function
            Function object to be added to the plot.
        """
        self.functions.append((label, function_obj))

    def plot(self):
        """
        Plots all the added functions using Matplotlib.
        """
        x_values = np.arange(self.domain_start, self.domain_end, self.step_size)
        
        for label, function_obj in self.functions:
            y_values = function_obj(x_values)
            plt.plot(x_values, y_values, label=label)
        
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Function Plotter')
        plt.legend()
        plt.show()


# Main block of code
if __name__ == "__main__":
    
    f1 = Function(lambda x: x ** 2)
    f2 = Function(lambda x: x + 3)
    f3 = Function(lambda x: np.sin(x))
    f4 = (f1 + f2) * f3 / 2.0

    plot = Plotter(0, 20, 0.1)
    
    plot.add_func("Function 1", f1)
    plot.add_func("Function 2", f2)
    plot.add_func("Function 3", f3)
    plot.add_func("Function 4", f4)
    plot.plot()
