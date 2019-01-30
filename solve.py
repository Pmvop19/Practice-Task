def solve(s, a, b, x):
    a, b = max(a, b), min(a, b)
    n = 0
    l = []
    while n != s // a + 1:  # находим все варианты размена S на A и B
        l.append([n, (s - n * a) // b, (s - n * a) % b, abs(x - n / (n + (s - n * a) // b) * 100)])
        n += 1
    mino = min(i[2] for i in l)  # ищем минимально возможный остаток
    lc = [x for x in l if x[2] == mino]  # находим все размены с наименьшим остатком
    minc = min(i[3] for i in l)  # находим минимальную разницу между X и процентным соотношением монет A от всех монет
    ans = [x for x in lc if x[3] == minc]  # находим необходимый размены
    an = ans[0][0]
    bn = ans[0][1]
    return an, bn
