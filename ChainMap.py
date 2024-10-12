from collections import ChainMap

customers1 = {'Alice': 25, 'Bob': 30}
customers2 = {'Charlie': 40, 'David': 45}

# Opción 1
customers_direct = {}
customers_direct.update(customers1)
customers_direct.update(customers2)
print("Resultado Opción 1:", customers_direct)

# Opción 2
customers_direct_chainmap = ChainMap(customers1, customers2)
print("Resultado Opción 2:", dict(customers_direct_chainmap))
