from .methods import land
from litestar import Litestar

app = Litestar(route_handlers=[land])
