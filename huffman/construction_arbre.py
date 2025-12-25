import heapq

class Noeud:
    def __init__(self, char, freq, gauche=None, droite=None):
        self.char = char
        self.freq = freq
        self.gauche = gauche
        self.droite = droite

    def __lt__(self, autre):
        return self.freq < autre.freq

def construire_arbre(frequences):
    heap = [Noeud(char, freq) for char, freq in frequences.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        gauche = heapq.heappop(heap)
        droite = heapq.heappop(heap)
        parent = Noeud(None, gauche.freq + droite.freq, gauche, droite)
        heapq.heappush(heap, parent)

    return heap[0]
