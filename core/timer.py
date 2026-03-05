"""
O objetivo do timer.py é ser o cronometro da aplicação
"""

import time
from storage.json_manager import open_create,save

session_study=open_create("time_data") #link com .json


def time_count(time_sec,time_min,time_hours): #isolamento do tempo + get valores

    time.sleep(1)
    time_sec+=1

    if time_sec==60:
        time_sec=0
        time_min+=1
                    
    if time_min==60:
        time_min=0
        time_hours+=1

    return time_sec,time_min,time_hours

    
def study_main(): #função principal
    time_sec=0
    time_min=0
    time_hours=0

    start_time=input("Deseja estudar: ").lower()

    if start_time == "sim":

        
        subject_study=int(input("\nAssunto: ")) #indice

        print("\nCronômetro iniciado! Pressione Ctrl+C para parar.\n")

        try:
            while True:
                    
                time_sec,time_min,time_hours=time_count(
                    time_sec,time_min,time_hours
                )

                print(f"Tempo de estudo: {time_hours:02d}:{time_min:02d}:{time_sec:02d}", end="\r")

        except KeyboardInterrupt: #ctrl+c
            print(f"\n\nSessão finalizada")

            session={
                "hours":time_hours,
                "minutes":time_min,
                "seconds":time_sec,
            }


            session_study.append(session)
            save("time_data",session_study)

            print(f"Total estudado: {session['hours']}h {session['minutes']}min {session['seconds']}s")
        
    else:
        input("Erro - tente novamente")
        main_timer()


def main_timer():
    study_main()


