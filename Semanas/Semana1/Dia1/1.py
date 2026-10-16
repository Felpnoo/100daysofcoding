import time
import random



if __name__ == '__main__':
    start_time = time.time()
    ops = ['+', '-', '*', '/']


    respostas = []
    acertos = 0
    total = 0
    
    
    while time.time() - start_time <= 60:
        
        a = random.randint(0,99)
        b = random.randint(0,99)
        op = random.choice(ops)

        if op == '/':
            b = random.randint(1,99)
            a = b * random.randint(0,99)
        else:
            pass

        if op == '+':
            resposta = a + b
        elif op == '-':
            resposta = a - b 
        elif op == '*':
            resposta = a * b 
        elif op == '/':
            resposta = a // b 


        print('{}{}{} = ?'.format(a,op,b))
        try:
            resposta_user = int(input())
        except ValueError:
            resposta_user = None
        
        if time.time() - start_time <= 60: 
            if resposta == resposta_user:
                print("Correto, {}{}{} = {}, você tem {} segundos".format(a,op,b,resposta_user, int(60 - (time.time() - start_time))))
                acertos = acertos + 1
                total = total + 1
                respostas.append("{}{}{} = {}, Correta!".format(a,op,b,resposta_user))
            elif resposta_user != resposta:
                print("Incorreto, {}{}{} = {}, você tem {} segundos".format(a,op,b,resposta, int(60 - (time.time() - start_time))))
                total = total + 1
                respostas.append("{}{}{} = {}, Incorreta!".format(a,op,b,resposta_user))

#        print("tempo = {}".format(int(60 - (time.time() - start_time))))


    if total == 0:
        print("Você não respondeu nada bocó")
    else:
        taxa = (acertos/total) * 100
        mensagem = "Parabéns!!!" if taxa>=70 else "Seu Burro" 
        print("Sua taxa de acertos é de {:.0f}%, {}".format(taxa, mensagem))
        print('\n'.join(respostas))
