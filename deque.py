from collections import deque
import time

#insercion de codigo sin usar deque (Tarda muchisio y es ineficiente)
# lista_normal = [0] * 1000000
# start_time = time.time()
# for _ in range(1000000):
#     lista_normal.insert(0,1)
# end_time = time.time()
# print("Tiempo transcurrido: "\
#        f"{end_time - start_time}")

#usando deque

lista_normal = [0] * 1000000
start_time = time.time()
for _ in range(1000000):
    lista_normal.append(0)
end_time = time.time()
print("Tiempo transcurrido: "\
      f"{end_time - start_time}")