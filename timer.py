#Timer
import time

def timer(segundos):
    while segundos >= 0:
        minutos, segundos_restantes = divmod(segundos, 60)
        timer = "{:02d}:{:02d}".format(minutos, segundos_restantes)
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1
    print("Tempo esgotado!!")
        
def main():
    t = input("insira o tempo em segundos(s):")
   
    if not t.isdigit():
        print("Entrada Inválida!! Reinicie o programa")
        return

    timer(int(t))

if __name__ == "__main__":
    main()
    
