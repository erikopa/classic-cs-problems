class CompressedGene:
    def __init__(self, gene:str) -> None:
        self._compress(gene)
    
    def _compress(self, gene:str) -> None:
        self.bit_string: int = 1 # inicializa sentinela
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # desloca dois bits para esquerda
            if nucleotide == "A": # muda os dois últimos bits para 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # muda os dois últimos bits para 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # muda os dois últimos bits para 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # muda os dois últimos bits para 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f'Invalid Nucleotide: {nucleotide}')
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2): # -1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11 # obtém apenas os 2 bits relevantes
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T"
            else:
                raise ValueError(f'Invalid bits: {bits}')
        return gene[::-1] # [::-1] inverte a string usando fatiamento com inversão

    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print(f'original is {getsizeof(original)} bytes')
    compressed: CompressedGene = CompressedGene(original) # compacta
    print(f'compressed is {getsizeof(compressed.bit_string)} bytes')
    print(compressed) # descompacta
    print(f'original and decompressed are the same: {original == compressed.decompress()}')
