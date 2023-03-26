#IMPORTS
from secrets import *
from random import *
from math import *

def PREP_password(dataset,length,iteration):
    for i in range(iteration):
        datasetvalues=[]
        for i in range(21384):
            datasetvalues.append(dataset[randbelow(len(dataset))])
        shuffle(datasetvalues)
        largearray=[]
        for i in range(40000):
            largearray.append(datasetvalues[randbelow(len(datasetvalues)-36)
                                            +trunc(1+((randbelow(1000000)-1)%9))
                                            +trunc(1+((randbelow(1000000)-1)%9))
                                            +trunc(1+((randbelow(1000000)-1)%9))])
        shuffle(largearray)
        passwordarray=[]
        for i in range(length):
            passwordarray.append(largearray[randbelow(len(largearray)-36)
                                            +trunc(1+((randbelow(1000000)-1)%9))
                                            +trunc(1+((randbelow(1000000)-1)%9))
                                            +trunc(1+((randbelow(1000000)-1)%9))])
        password_string = ''.join(map(str, passwordarray))
        print(password_string)

PREP_password("01",256, 1000)