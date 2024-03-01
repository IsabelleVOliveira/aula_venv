# main.py
import typer
import inquirer
from pydobot import Dobot
from yaspin import yaspin

dobot = Dobot(port="COM7", verbose=False)

# Cria uma instância da aplicação
app = typer.Typer()

# Cria um comando do CLI
@app.command()
def home():
    dobot.move_to(242.2, 0, 151.3, 0, wait=True)
    print(dobot.pose())

# Cria um segundo comando do CLI
@app.command()
def ligarS():
    dobot.suck(True)
    if True:
        print("Sugador ligado")

# Cria um segundo comando do CLI
@app.command()
def desligarS():
    dobot.suck(False)
    if dobot.suck(False):
        print("Sugador desligado")

@app.command()
def p_atual():
    p_atual = dobot.pose()
    print(f"Posição atual: {p_atual}")  

@app.command()
def distancia():
    eixo = str(typer.prompt("Escolha um eixo (x, y, z): "))
    n = int(typer.prompt("Digite a distância: "))
    escolha(n, eixo)
    

def escolha(n, eixo):
    (x,y,z,r,_,_,_,_) = dobot.pose()
    if eixo == "x":
        dobot.move_to(x+n, y,z,r, wait=True)
    elif eixo == "y":
        dobot.move_to(x, y+n,z,r, wait=True)
    elif eixo == "z":
        dobot.move_to(x, y,z+n,r, wait=True)
    else:
        print("Erro: Eixo inválido")

@app.command()
def close():
    dobot.close()
    print("Conexão encerrada")



# Cria um quarto comando do CLI
@app.command()
def comandos():
    # realiza lista de perguntas para o usuário
    perguntas = [
        inquirer.List("comandos", message="Qual comando deseja realizar?", choices=["home", "ligar ferramenta","desligar ferramenta","posição atual", "distância", "sair"])
    ]



    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    # chama a funcao que processa a operação e exibe uma spinner para o usuário
    spinner = yaspin(text="Processando...", color="blue")

    if respostas["comandos"] == "home":
        spinner.start()
        home()
        spinner.stop()
    elif respostas["comandos"] == "ligar ferramenta":
        spinner.start()
        ligarS()
        spinner.stop()
    elif respostas["comandos"] == "desligar ferramenta":
        spinner.start()
        desligarS()
        spinner.stop()
    elif respostas["comandos"] == "posição atual":
        spinner.start()
        p_atual()
        print(f"Posição atual: {p_atual}")
        spinner.stop()
    elif respostas["comandos"] == "distância":
        # spinner.start()
        distancia()
        # spinner.stop()

    elif respostas["comandos"] == "sair":
        spinner.start()
        print("Saindo...")
        spinner.stop()

    else:
        print("Erro: Comando inválido")

  

    


# Executa a aplicação
if __name__ == "__main__":
    app()