def count_keys_freq(d):
    from collections import Counter
    return dict(Counter(d.keys()))

def unique_keys(d):
    return list(set(d.keys()))

inventory = {'apple': 5, 'banana': 3, 'apple': 2, 'orange': 4}
# Eslatma: Python lug‘atida bir xil kalit bo‘lmaydi, oxirgisi saqlanadi
inventory = {'apple': 5, 'banana': 3, 'orange': 4}
print(count_keys_freq(inventory))   # {'apple': 1, 'banana': 1, 'orange': 1}
print(unique_keys(inventory))       # ['apple', 'banana', 'orange']
