animals = ['овца', 'овца', 'волк', 'овца', 'овца']
wolf_pos = animals.index('волк')
dangerous = [wolf_pos] * (wolf_pos > 0) + [wolf_pos + 2] * (wolf_pos < len(animals) - 1)
print(" и ".join(map(str, dangerous)))