


class Player:
    def __init__(self, namn):
        self._namn = namn
    def getNamn(self)->str:
        return self._namn

def listaPlayers(playersList : list[Player]):
    for player in playersList:
        print(player.getNamn())



def test( namn : str, tallista:list[int],  tal:int)->str:
    parts = namn.split(":")
    tal = tal + 12
    return "123"

x = [12,13,14,234423]

lista : list[Player] =  []
#lista = []
p = Player("Mats")
lista.append(p)
#listaPlayers(lista)
for player in lista:
    print(player.getNamn())

