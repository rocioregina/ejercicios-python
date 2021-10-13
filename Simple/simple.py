import random

def generate_list(amount):
    """
    Testea la funcion que genera una lista
    >>> random.seed(10)
    >>> generate_list(10)
    [{'id': 1, 'edad': 74}, {'id': 2, 'edad': 5}, {'id': 3, 'edad': 55}, {'id': 4, 'edad': 62}, {'id': 5, 'edad': 74}, {'id': 6, 'edad': 2}, {'id': 7, 'edad': 27}, {'id': 8, 'edad': 60}, {'id': 9, 'edad': 63}, {'id': 10, 'edad': 36}]
    >>> random.seed(20)
    >>> generate_list(10)
    [{'id': 1, 'edad': 93}, {'id': 2, 'edad': 88}, {'id': 3, 'edad': 99}, {'id': 4, 'edad': 20}, {'id': 5, 'edad': 34}, {'id': 6, 'edad': 87}, {'id': 7, 'edad': 82}, {'id': 8, 'edad': 13}, {'id': 9, 'edad': 42}, {'id': 10, 'edad': 74}]
    """
    list = []
    for i in range(1, amount + 1):
        dictionary = {"id": i, "edad": random.randint(1, 100)}
        list.append(dictionary)
    return list

def order_list(list):
    """
    Testea la funcion que ordena una lista
    >>> random.seed(10)
    >>> order_list(generate_list(10))
    Youngest person's id:  1
    Oldest person's id:  6
    [{'id': 1, 'edad': 74}, {'id': 5, 'edad': 74}, {'id': 9, 'edad': 63}, {'id': 4, 'edad': 62}, {'id': 8, 'edad': 60}, {'id': 3, 'edad': 55}, {'id': 10, 'edad': 36}, {'id': 7, 'edad': 27}, {'id': 2, 'edad': 5}, {'id': 6, 'edad': 2}]
    """
    list.sort(reverse=True, key = lambda dict: dict["edad"])
    print("Youngest person's id: ", list[0]["id"])
    print("Oldest person's id: ", list[len(list) - 1]["id"])
    return list

if(__name__ == "__main__"):
    import doctest
    doctest.testmod(verbose=True)
