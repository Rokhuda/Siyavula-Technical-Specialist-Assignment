from xmlrpc.client import boolean


def real_roots(a, b, c) -> boolean:
    if type(a) != int and type(b) != int and type(c) != int:
        return False
    else:
        if a == 0:
            return False
        delta = b**2 - 4 * a * c

        if delta > 0:
            return True
        elif delta == 0:
            return True
        else:
            return False

