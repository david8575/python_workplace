m, n = map(int, input().split())
m_fac, n_fac, m_n_fac = 1, 1, 1
for i in range(m):
    m_fac *= (i+1)
for i in range(n):
    n_fac *= (i+1)
for i in range(m-n):
    m_n_fac *= (i+1)
print(m_fac // (n_fac*m_n_fac))
print(m_fac)
print(n_fac)
print(m_n_fac)