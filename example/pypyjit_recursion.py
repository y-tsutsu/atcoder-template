try:
    import pypyjit  # type: ignore
    pypyjit.set_param('max_unroll_recursion=-1')
except Exception:
    pass
