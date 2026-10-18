import numpy as np


Funciones_Evaluar = [
    {
        'Nombre': "Polinomica_(Raiz simple)",
        'f': lambda x: x**3 - x - 2,
        'g': lambda x: np.cbrt(x +  2),
        'a': 1.0,
        'b': 2.0,
    },
    {
        'Nombre': "Polinomica_(Raiz doble)",
        'f': lambda x: (x-2)**2,
        'g': None,
        'a': 1.2,
        'b': None,
    },
    {
        'Nombre': "Logaritmica",
        'f': lambda x: np.log(x)+x-4,
        'g': lambda x:4 - np.exp(4-x),
        'a': 2.0,
        'b': 3.0,
    },
    {
        'Nombre': "Exponencial",
        'f': lambda x: np.exp(-x)-x,
        'g': lambda x: np.exp(-x),
        'a': 0.0,
        'b': 1.0,
    },
    {
        'Nombre': "Trigonometrica",
        'f': lambda x: np.cos(x) - x,
        'g': lambda x: np.cos(x),
        'a': 0.0,
        'b': 1.0,
    },
    {
        'Nombre': "Mixta",
        'f': lambda x: np.sqrt(x) - np.cos(x),
        'g': lambda x: np.cos(x)*np.cos(x),
        'a': 0.1,
        'b': 1.0,

    }
]
