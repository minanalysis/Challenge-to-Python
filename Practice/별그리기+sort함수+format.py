# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
n = int(input('숫자를 적어주세요' ))
t = str(input('이름을 적어주세요' ))

a=list(range(1,n))
b=sorted(list(range(1,n)),reverse=True)

print("{}가 그려본".format(t))

for i in a:
    print(i*'*')
for ii in b : 
    if ii != n-1 :
        print(ii*'*')


# -

b.sort(reverse=True)
b

for i in range(1,8):
    i = 4-abs(4-i)
    print("{}".format(i*"*"))
