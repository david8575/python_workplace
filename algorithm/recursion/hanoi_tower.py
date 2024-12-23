# 하노이 탑 hanoi tower

# 기본
def hanoiTower(a,b,c,n,):
    if (n == 1):
        print(f"{a} {c}")
    else:
        hanoiTower(a,c,b,n-1)
        print(f"{a} {c}")
        hanoiTower(b,a,c,n-1)

# 특정 순서 정할 때
def hanoiTower2(a,b,c,n,m,cnt):
    if (m == cnt):
        print(f"{a} {c}")
        return None
    else:
        hanoiTower2(a,c,b,n-1,m,cnt+1)
        hanoiTower2(b,a,c,n-1,m,cnt+1)

hanoiTower("A", "B", "C", 3)