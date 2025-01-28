# Object Oriented Programming using abstraction

from abc import ABC, abstractmethod
import re

# creation of the abstract method

class Equation(ABC):
    #  each class (equation) will have 2 classes variables: a degree and a type (name)
    degree: int
    type: str
    
#   initialisation runned after a class is created from this abstract class to create the self.coeficients attribute
    def __init__(self, *args):
        # Checking degree and argc
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # checking data types
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # checking degree != 0
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        # creating the coefficients attributes dictionnary depending number of arguments and their order (highest coefficient fist)
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    # Code run when a subclass (cls) is instancied: check if the new created class has a degree and a type attribute
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

# define the returned string of the class as the equation: take into consideration all possible degree
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                coefficient
            if n == 0:
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x')
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = ' '.join(terms) + ' = 0'
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))        

# definition d'une méthode abstraite: chaque sous classe devra implémenter sa méthode solve
    @abstractmethod
    def solve(self):
        pass
        
# definition d'une méthode abstraite: chaque sous classe devra implémenter sa méthode analyze
    @abstractmethod
    def analyze(self):
        pass


# creation d'une sous classe equation linéaire
class LinearEquation(Equation):
    degree = 1
    type = 'Linear Equation'

# solve method 
    def solve(self):
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

# methode analyze, pour retourner un dictionnaire des éléments constituant l'équation 
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


class QuadraticEquation(Equation):
    degree = 2
    type = 'Quadratic Equation'

# initialisation de la méthode pour creer un attribut d'instance "delta"
    def __init__(self, *args):
        super().__init__(*args)  # permet de lancer le code d'initialisaiton de la classe abstraite et de récupérer l'attribut coefficients de la classe abstraite
        a, b, c = self.coefficients.values() # stocke les valeurs du coefficients dans a, b, c
        self.delta = b**2 - 4 * a * c  # calcul du delta pour la classe

# solve method
    def solve(self):
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]

        return [x1, x2]
# analyze method
    def analyze(self):
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}

# création d'une méthode externe principale de résolution d'équation
def solver(equation):
    # vérification de l'objet equation et confirmation de l'instance à Equation.
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

# creation de la variable "output_string" pour générer le rapport (à l'aide de format string type f{X:})
    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'
    results = equation.solve()
    # match case to detect all the different result possibilities
    match results:
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']
    
    # integrating the result into the output_string report 
    for result in result_list:
        output_string += f'{result:^24}\n'
    output_string += f'\n{"Details":-^24}\n\n'
    
    details = equation.analyze()
    #  unpacking the details dictionnarie into a match case for different possibilities
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity}', f'{min_max} = {coord}']
    #  after saving the details in a correct string format in a list: concatenation with the output_list for report
    for detail in details_list:
        output_string += f'{detail}\n'
    return output_string


lin_eq = LinearEquation(2, 3)
quadr_eq = QuadraticEquation(1, 2, 1)
print(solver(quadr_eq))
