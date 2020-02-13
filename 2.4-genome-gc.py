genome = input()

print(((genome.lower().count('g') + genome.lower().count('c')) / len(genome)) * 100)