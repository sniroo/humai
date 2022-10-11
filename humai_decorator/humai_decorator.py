# -*- coding: utf-8 -*-

"""Main module."""
import functools
from numpy.random import choice, random

def anadir_ruido(noise_probability : float, noise_distribution : dict(str, float)):
    """
    Description: Función para añadir ruido aleatorio.

    Input:
    -> noise_probability: float
    -> noise_distribution: dictionary [str, float]

    Output:

    -> Modifica la funcion original

    """
    def inner_decorator(func):
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(   possible_noise_values,
                                                    noise_value_probabilities,
                                                    true_value
                            )
                return choice(vals, p=probs)
            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values, noise_value_probabilities, true_value):
    """
    ACA TENEMOS QUE PONER EL DOCSTRING
    """
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        z_num = sum(noise_value_probabilities)
        noise_value_probabilities = [x/z_num for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})

    def funcion_de_ejemplo(num_x):
        """
            ACA TENEMOS QUE PONER EL DOCSTRING
        """

        return 2*num_x
    for x in range(10):
        print(funcion_de_ejemplo(x))
