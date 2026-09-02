import random

class Gene:
    def __init__(self, value=None):
        # 0 or 1 randomly if not explicitly passed
        self.value = value if value in (0, 1) else random.choice([0, 1])

    def mutate(self):
        # Flips 0 to 1, or 1 to 0
        self.value = 1 if self.value == 0 else 0

    def __repr__(self):
        return str(self.value)


class Chromosome:
    def __init__(self, genes=None):
        # A series of 10 Genes
        if genes:
            self.genes = genes
        else:
            self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        # A random number of genes can randomly flip (1/2 chance each)
        num_genes_to_mutate = random.randint(1, len(self.genes))
        genes_to_check = random.sample(self.genes, num_genes_to_mutate)
        
        for gene in genes_to_check:
            if random.random() < 0.5:  # 1/2 chance to flip
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __repr__(self):
        return "".join(str(g) for g in self.genes)


class DNA:
    def __init__(self, chromosomes=None):
        # A series of 10 Chromosomes
        if chromosomes:
            self.chromosomes = chromosomes
        else:
            self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        # Mutates a random number of chromosomes
        num_chromosomes_to_mutate = random.randint(1, len(self.chromosomes))
        chromosomes_to_check = random.sample(self.chromosomes, num_chromosomes_to_mutate)
        
        for chromosome in chromosomes_to_check:
            chromosome.mutate()

    def is_perfect(self):
        # True if all 100 genes across all chromosomes are 1s
        return all(chromo.is_all_ones() for chromo in self.chromosomes)

    def __repr__(self):
        return "-".join(str(c) for c in self.chromosomes)


class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment  # Probability of mutation (e.g., 0.8)

    def live_and_mutate(self):
        # Mutates DNA based on environmental probability
        if random.random() < self.environment:
            self.dna.mutate()


# --- Simulation Run ---

def run_evolution_simulation(population_size=5, mutation_environment=0.8):
    # Instantiate organisms
    population = [Organism(DNA(), mutation_environment) for _ in range(population_size)]
    
    generations = 0
    winner = None

    print(f"Starting simulation with {population_size} organisms (Environment mutation chance: {mutation_environment})...\n")

    while not winner:
        generations += 1
        for organism in population:
            organism.live_and_mutate()
            if organism.dna.is_perfect():
                winner = organism
                break

    print(f"=== SIMULATION COMPLETE ===")
    print(f"Generations required: {generations:,}")
    print(f"Perfect DNA Sequence: {winner.dna}")
    return generations

if __name__ == "__main__":
    run_evolution_simulation(population_size=10, mutation_environment=0.9)
# Research Notebook & Conclusion

# Observation: Because a complete DNA string requires 100 specific genes (10 chromosomes x 10 genes) to simultaneously be set to 1, pure random mutation without selective pressures takes millions of generations to reach perfection.

# Conclusion: Random mutation without natural selection is extremely inefficient for reaching a target state. In real biological evolution, natural selection acts as a filter that preserves beneficial mutations across generations rather than relying on pure chance alone.