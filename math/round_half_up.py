from decimal import Decimal, ROUND_HALF_UP


def round_half_up(n: int, ndigits: int) -> int:
    '''整数nを右からndigits桁の位置で四捨五入する'''
    assert ndigits >= 0
    unit = 10 ** ndigits
    sign = 1 if n >= 0 else -1
    return sign * ((abs(n) + unit // 2) // unit * unit)


def round_half_up_float(n: float, ndigits=0) -> float:
    '''小数nを小数点以下ndigits桁へ四捨五入する'''
    unit = Decimal(1).scaleb(-ndigits)
    return float(Decimal(str(n)).quantize(unit, rounding=ROUND_HALF_UP))


def round_half_up_float_simple(n: float, ndigits=0) -> float:
    '''微小値を加えて四捨五入する簡易版（負数や値の大きさによっては不正確）'''
    return round(n + 0.000000005, ndigits)


def example():
    # 整数版のndigitsは、右から何桁を0にするかを指定
    print(round_half_up(125, 1))       # 130: 10の位へ丸める
    print(round_half_up(149, 2))       # 100: 100の位へ丸める
    print(round_half_up(-150, 2))      # -200: ちょうど半分は0から遠ざける

    # float版のndigitsは、残す小数点以下の桁数を指定
    print(round_half_up_float(2.675, 2))   # 2.68
    print(round_half_up_float(-2.675, 2))  # -2.68
    print(round_half_up_float(125.0, -1))  # 130.0: 10の位へ丸める

    # 誤差を許容できる場面では、元の軽量な簡易版も利用可能
    print(round_half_up_float_simple(2.675, 2))  # 2.68


if __name__ == '__main__':
    example()
