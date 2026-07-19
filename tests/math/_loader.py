from pathlib import Path

from bootstrap.bootstrap import bootstrap
from bootstrap.bootstrapmemo import bootstrapmemo


def load_math_module(name):
    path = Path(__file__).parents[2] / 'math' / f'{name}.py'
    source = path.read_text()
    source = source.replace('def bootstrap(func=None, stack=[]):\n    pass\n\n\n', '')
    source = source.replace(
        'def bootstrapmemo(func=None, stack=[], memo={}, args_list=[]):\n    pass\n\n\n',
        '',
    )
    namespace = {
        '__name__': f'test_{name}',
        'bootstrap': bootstrap,
        'bootstrapmemo': bootstrapmemo,
    }
    exec(compile(source, str(path), 'exec'), namespace)
    return namespace
