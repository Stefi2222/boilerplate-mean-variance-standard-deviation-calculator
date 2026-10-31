import numpy as np


def calculate(numbers):

    # Verificar que la lista tenga exactamente 9 números
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir la lista en una matriz de 3 filas y 3 columnas
    matrix = np.array(numbers).reshape(3, 3)

    # Calcular las estadísticas
    calculations = {
        "mean": [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).item()
        ],

        "variance": [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).item()
        ],

        "standard deviation": [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item()
        ],

        "max": [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item()
        ],

        "min": [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item()
        ],

        "sum": [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item()
        ]
    }

    return calculations
