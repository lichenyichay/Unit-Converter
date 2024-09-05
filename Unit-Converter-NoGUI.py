# Author:Chay
# Time:2024/9/5 22:47
# Release:Alpha 1.0.0

# 长度单位换算函数
def mmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def mmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100.0


def mmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000.0


def mmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000000.0


def cmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def cmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100.0


def cmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100000.0


def dmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def dmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10000.0


def mtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000.0


def cmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def dmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100.0


def mtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000.0


def kmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000000.0


def dmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def mtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100.0


def kmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100000.0


def mtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def kmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10000.0


def kmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000.0


# 物理量换算函数


def ρ(V=0.0,m=0.0,g=9.8,h=0.0,p=0.0,Ffu=0.0) -> float:
    if V!=0.0 and m != 0.0:
        return m/V
    elif p!=0.0 and h != 0.0 and g != 0.0:
        return p/(g*h)
    elif Ffu != 0 and g!=0 and V!=0.0:
        return Ffu/(g*V)
    else:
        raise ValueError("参数无效！")


def m(G=0.0,g=9.8,V=0.0,ρ=0.0) -> float:
    if G!=0 and g!=0:
        return G/g
    elif V!=0 and ρ!=0:
        return ρ*V
    else:
        raise ValueError("参数无效！")


def Vtiji(m=0.0,ρ=0.0,g=9.8,Ffu=0.0) -> float:
    if m!=0 and ρ!=0:
        return m/ρ
    elif g!=0 and Ffu!=0 and ρ!=0:
        return Ffu/(g*ρ)
    else:
        raise ValueError("参数无效！")


def Vsudu(Slu=0.0,t=0.0) -> float:
    if Slu!=0 and t != 0:
        return Slu/t
    else:
        raise ValueError("参数无效！")
def p() -> float:
    pass
if __name__ == "__main__":
    pass

