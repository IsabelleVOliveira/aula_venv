# Ponderada Construção de Interface por Linha de Comando (CLI) para Controle do Robô

&emsp;Desenvolvido por Isabelle Beatriz Vasquez Oliveira

## Descrição

&emsp;Para o desenvolvimento dessa ponderada, utilizei as seguintes bibliotecas: typer, inquirer, pydobot e yaspin. Além disso, criei uma função para cada um dos comandos executados e uma única função para selecionar o comando que deve ser executado.

&emsp;As funções são:

- `def home`: voltar para aposição inicial predefinida chamada "Home".
- `def ligarS`: ligar a ferramenta de sucção do robô.
- `def desligarS`: desligar a ferramenta de sucção do robô.
- `def p_atual`: fornecer a posição atual do robô.
- `def distancia`: inserir o eixo e a distância a ser movida.
- `def escolha`: mover o robô para a distância e eixo escolhidos.
- `def close`: encerrar a conexão com o robô.
- `def comandos`: executar a lista de perguntas para o usuário.

&emsp;Os comandos disponíveis para o usuário são:

- `home`
- `ligar ferramenta`
- `desligar ferramenta`
- `posição atual`
- `distância`
- `sair`

&emsp; Para o bom fncionamento do código, o usuário deve utilizar o terminal do Visual Studio Code e insirir o seguinte comando: `python .\main.py comandos`, então selecionar o comando de sua preferência.
Além disso, o usuario deve verificar se a porta de conecção do robô está de acordo com `COM7`, caso contrario, o mesmo deve ajustar a porta na linha 7 do código `main.py`. 
