Funciones_Evaluar = [
    {
        'Nombre': "Polinomica (Raiz simple)",
        'f': lambda x: x**3 - x - 2,
        'a': 1.0,
        'b': 2.0,
    },
    {
        'Nombre': "Polinomica (Raiz doble)",
        'f': lambda x: (x-2)**2,
        'a': 1.2,
        'b': None,
    },
    {
        'Nombre': "Logaritmica",
        'f': lambda x: np.log(x)+x-4,
        'a': 2.0,
        'b': 3.0,
    },
    {
        'Nombre': "Exponencial",
        'f': lambda x: np.exp(-x)-x,
        'a': 0.0,
        'b': 1.0,
    },
    {
        'Nombre': "Trigonometrica",
        'f': lambda x: np.cos(x) - x,
        'a': 0.0,
        'b': 1.0,
    },
        {
        'Nombre': "Mixta",
        'f': lambda x: np.sqrt(x) - np.cos(x),
        'a': 0.1,
        'b': 1.0,
    },
]