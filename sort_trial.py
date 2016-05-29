import random

num = randomint(1000,100000)


lista = list(range(20))

listb = [x for x in lista if x %2 != 0]





def bubbleSort(list0):

    #冒泡

    list0.insert(i,list0.pop(j)) for i in range(len(list0)) for j in range(i) if list0[i] < list0[j]

    #list0.insert(i,list0.pop(j))

    #for each in list0.pop

	pass


    

def insertionSort(list0):

#插入

    pass


def mergeSortRescur(list0):

    #小到大并归排序,递归

	if len(list0) <4:

		return mergeFuncCurrying(list0[:1],list0[1:])

	else:

		return mergeFuncCurrying(mergeSortRescur(list0[:int(len(list0)/2)]),mergeSortRescur(list0[int(len(list0)/2):]))

        

def mergeSortIter(list0):

    #小到大并归排序,迭代

    if len(list0) <4:

        

    pass

def mergeSortCurrying(list0):

    pass


def mergeFuncRescursion(lista,listb):

    #并归操作,递归

    listmerge = []

    if len(lista)==0:

        listmerge.extend(listb)

    elif len(listb)==0:

		listmerge.extend(lista)

	elif lista[0]>listb[0]:

		listmerge.append(listb.pop(0))

		listmerge.extend(mergeFuncRescursion(lista,listb))

	else:

		listmerge.append(lista.pop(0))

		listmerge.extend(mergeFuncRescursion(lista,listb))

	return listmerge


def mergeFuncIter(listmerge,lista,listb):

    #并归操作,迭代

	if len(lista)==0:

		listmerge.extend(listb)

		return listmerge

	elif len(listb)==0:

		listmerge.extend(lista)

		return listmerge

	elif lista[0]>listb[0]:

		listmerge.append(listb.pop(0))

		return mergeFuncIter(listmerge,lista,listb)

	else:

		listmerge.append(lista.pop(0))

		return mergeFuncIter(listmerge,lista,listb)

 

 def mergeFuncCurrying(lista,listb):

    listmerge = []

    return mergeFuncIter(listmerge,lista,listb)

 

    