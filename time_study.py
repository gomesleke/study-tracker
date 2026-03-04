import time
import os
from manager import open_create,save
#variaveis globais
time_sec=0
time_min=0
time_hours=0


session_study=open_create()

start_time=input("Deseja estudar: ").lower()
subject_study=input("Assunto: ")

if start_time == "sim":
    print("\nCronômetro iniciado! Pressione Ctrl+C para parar.\n")

    try:
        while True:
            
            time.sleep(1)
            time_sec+=1

            if time_sec==60:
                time_sec=0
                time_min+=1
            
            if time_min==60:
                time_min=0
                time_hours+=1


            print(f"Tempo de estudo: {time_hours:02d}:{time_min:02d}:{time_sec:02d}", end="\r")

    except KeyboardInterrupt: #ctrl+c
        print(f"\n\nSessão finalizada")

        session={
            "hours":time_hours,
            "minutes":time_min,
            "seconds":time_sec,
            "subject":subject_study
        }

        session_study.append(session)
        save(session_study)

print(f"Total estudado de '{session['subject']}': {session['hours']}h {session['minutes']}min {session['seconds']}s")

