from pathlib import Path

from bootstrap.bootstrap import bootstrap
from data_structures.seg_tree import SegTree


def load_graph_module(name, **dependencies):
    path = Path(__file__).parents[2] / 'graph' / f'{name}.py'
    source = path.read_text()
    source = source.replace('def bootstrap(func=None, stack=[]):\n    pass\n\n\n', '')
    source = source.replace('class SegTree:\n    pass\n\n\n', '')
    source = source.replace('class Dinic:\n    pass\n\n\n', '')
    namespace = {
        '__name__': f'test_{name}',
        'bootstrap': bootstrap,
        'SegTree': SegTree,
        **dependencies,
    }
    exec(compile(source, str(path), 'exec'), namespace)
    return namespace
