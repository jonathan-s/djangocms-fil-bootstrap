import os

__version__ = "0.0.1"


def bootstrap():
    from factory.random import reseed_random
    reseed_random(0)
    from .bootstrap import Bootstrap
    from .components import Collections, Groups, Pages, Permissions, Users, Workflows

    bootstrap = Bootstrap(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    )
    bootstrap(Users, Groups, Permissions, Pages, Workflows, Collections)
