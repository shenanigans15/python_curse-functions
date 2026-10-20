# # Default parameter
# def hello(greet="Hola", name="Invitado"):
#     """
#     Info: esta es una función para devolver un saludo personalizado
#     Devuelve un string o un print
#     """
#     print(f"{greet}, {name}")


# # Keyword arguments
# hello(name="Ricardo", greet="Hola")


def multiply(a: float, b: float) -> float:
    """
    Info: multiplica dos números y devuelve el resultado
    """
    return a * b


print(multiply(2, 3))
