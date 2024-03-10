class Dinic:
    pass


class BpMatch:
    def __init__(self, n0, n1, v0=1, v1=1):
        self._n0 = n0
        self._n1 = n1
        self._n = n0 + n1
        self._dinic = Dinic(self._n + 2)
        for i in range(self._n0):
            self._dinic.add_edge(self._n, i, v0)
        for i in range(self._n1):
            self._dinic.add_edge(self._n0 + i, self._n + 1, v1)

    def add_edge(self, fr, to, cap=1):
        self._dinic.add_edge(fr, self._n0 + to, cap)

    def flow(self):
        return self._dinic.flow(self._n, self._n + 1)
