from fasthtml.common import *

def not_found(req, exc):
    return Titled('Oh no!', P('We could not find that page :('))

