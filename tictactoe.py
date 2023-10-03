"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
# Se alguem jogar em uma casa preenchida, a casa será marcada novamente com um dos símbolos. Se voçê marca o X em uma casa e depois marca o O na mesma, os dois símbolos ficaram nas mesmas posições, dentro da casa.
3. How would you detect when someone has won?
# Para detectar se alguém venceu no jogo da velha, eu verificaria todas as possíveis combinações vencedoras de três símbolos em uma linha. Ou seja, é verificar todas as linhas, colunas e diagonais possíveis. Para isso, criaria um tabuleiro de jogo 'board' para verificar as combinações de vitória. Após isso, chamaria algum metódo para checar de nessas linhas, colunas e diagonais possíveis a uma combinação de três símbolos, por exemplo: check_win(). Logo após isso, imprimia uma menssagem indicando qual jogadpr seria o vencedor.
4. How could you create a computer player?
# Poderíamos criar um jogador computador adicionando uma função, que é chamada após cada jogada do jogador humano. Criariamos então a função com random_move() que é chamada após cada jogada do jogador humano. Ela gera posições aleatórias no tabuleiro usando a função random.randint(), e então faz uma jogada para o jogador computador utilizando a mesma lógica do desenho das letras "X" e "O".
Com essa adição, o jogador computador fará jogadas aleatórias após cada jogada do jogador humano.
  
"""

from turtle import *

from freegames import line

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    color("green") #alteração para cor verde
    width(3)
    line(x, y, x + 135, y + 135)
    line(x, y + 123, x + 123, y)

def drawo(x, y):
    """Draw O player."""
    color("red") #alteração para cor vermelha
    width(3)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()