import os
from core.timer import main_timer


def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")

    
def selection_show():
    print("Selecione:\n")
    print("1-Começar Estudos")
    print("2-Relatório")
    print("3-Histórico")
    print("4-Metas")
    print("5-Configurações")
    print("6-Sair")

def selection_choice():

    try:
        index_user=int(input("\nEscolha o indice: "))

        match index_user:
            
            case 1:
                print("qualquer coisa")
            
            case 2:
                print("qualquer coisa")

            
            case 3:
                print("qualquer coisa")

            
            case 4:
                print("qualquer coisa")


            case 5:
                print("qualquer coisa")

            
            case 6:
                print("qualquer coisa")
            
            case _:
                input("Opção Inválida - Pressione qualquer Tecla")
                main()          


    
    except ValueError,:
        input("Erro: Tente Novamente - Pressione qualquer Tecla ")
        main()
        
    


def menu():

    clear()

    print("============")
    print("\nSTUDY TRACKER (CLI)\n")
    print("============\n")

    selection_show()


def main():
    menu()
    selection_choice()
    

if __name__=="__main__":
    main()