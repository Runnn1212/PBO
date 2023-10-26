from sys import path
path.append('D:\\Kuliah\\Semester 3\\Pemrogaman Ber Orientasi Objek\\PER 4 ES 2')

print('\nStep 7 ')
import extra.iota
print(extra.iota.funI())

import extra.good.best.sigma
from extra.good.best.tau import funT
 
print(extra.good.best.sigma.funS())
print(funT())

print('\nStep 8')
import extra.good.best.sigma as sig
import extra.good.alpha as alp
 
print(sig.funS())
print(alp.funA())

print('\nStep 9')
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB
 
print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
