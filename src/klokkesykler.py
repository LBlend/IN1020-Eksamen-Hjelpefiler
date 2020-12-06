"""
Anta at prosessoren har 100 instruksjoner igjen å utføre. 
Det tar én klokkesykel pr instruksjon, og man regner med å ha en minneaksessering på 80% og med cache-miss på 50%. 
En cache-miss fører til en total tidsbruk på 20 klokkesykler. 
Cache-hit bruker total én klykkesykel. 
Hva er total antall gjenstående klokkesykler?
"""


"""
Det er 100 instruksjoner.
(A) 20% av dem tar 1 klokkesykel
80% minneaksess hvor 50% (B) av dem ikke tar lengre enn 1 klokkesykel. Mens 50% (C) tar 20 klokkesykel

Det betyr
A + B + C
20 + 40 + (40*20) = 860
"""


def klokkesykler(instruksjoner, minneaksessering_prosent, cache_miss_prosent, cache_miss_penalty_instruksjoner):
    non_mem_instruksjoner = ((100 - minneaksessering_prosent) / 100) * instruksjoner
    mem_instruksjoner = (minneaksessering_prosent / 100) * instruksjoner

    non_penalty_mem_instruksjoner = ((100 - cache_miss_prosent) / 100) * mem_instruksjoner
    penalty_instruksjoner = mem_instruksjoner * (cache_miss_prosent / 100) * cache_miss_penalty_instruksjoner

    return int(non_mem_instruksjoner + non_penalty_mem_instruksjoner + penalty_instruksjoner)


print(klokkesykler(100, 80, 50, 20))
