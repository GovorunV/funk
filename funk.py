def test(*par): #передача кортежа
    res = 1
    i=1
    for i in par:
        res=res*i
    return res
s=test(5,3,4,1,10)
print(s)
'''
def test2(**par): #передача асоциированого(словаря) списка вывой ключей и значений
    for key,value in par.items():
        print("ключ",key,"значение",value)
test2(long="Peta",short='Pet',x=5)
'''
def test3(**par): #передача асоциированого списка вывод всех ключей
    for key in par:
        print("ключ",key)
test3(long="Peta",short='Pet',x=5)

mult = lambda a,b=2: a*b;  #анонимный цикл
print(mult(2))
