#1) Bir listeyi düzleştiren (flatten) fonksiyon yazın.
#Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir

boskume=[]
def flatten(k):

    for x in k:
        if isinstance(x,list):
            flatten(x)
        else:
            boskume.append(x)
            

k =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten(k)

print(boskume)


#2) Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
#Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

kume=[[1, 2], [3, 4], [5, 6, 7]]

def ters(kume):
    for x in range(int(len(kume))):
     (kume[x])=(kume[x])[::-1]
     kume=kume[::-1]
    return kume 


print(ters(kume))   
