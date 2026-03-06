"""
Esse arquivo é responsável para ser o CRONÔMETRO da aplicação - extraindo o tempo de estudo
"""

import time

def time_logic(sec,min,hr):

    """
    lógica do tempo isolada
    """
    time.sleep(1)
    sec+=1

    if sec>=60:
        sec=0
        min+=1
    if min>=60:
        min=0
        hr+=1
    
    
    return sec,min,hr

def stopwatch():

    sec_i=0
    min_i=0
    hr_i=0

    user_start=input("Deseja começar a Estudar: ")

    if user_start.lower()!='sim':
        return None
    else:

        print("\nCronômetro iniciado! Pressione Ctrl+C para parar.\n")
    
        try:
            while True:
                

                sec_i,min_i,hr_i=time_logic(
                    sec_i,min_i,hr_i
                )
                print(f"Tempo de estudo: {hr_i:02d}:{min_i:02d}:{sec_i:02d}", end="\r")

        except KeyboardInterrupt:
            print(f"\n\nSessão finalizada")

            print(f"Total de Estudo: {hr_i:02d}:{min_i:02d}:{sec_i:02d}", end="\r")

            return sec_i, min_i, hr_i
        





