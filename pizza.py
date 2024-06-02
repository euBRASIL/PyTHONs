import matplotlib.pyplot as plt

# Dados de exemplo
labels = ['13Lp17NfhXsc2SkQaWpQQe5jXVDNeyL5sZ', '13Aqi2ss6X9PUx7dwZ4PmG4ugBN49svRw7', '13EP8nZXgcs12wQnNGnF2GFuicyWQdu3s1']
sizes = [29.41, 26.47, 29.41]
colors = ['#ff9999','#66b3ff','#99ff99']
 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.title('Distribuição de Endereços Bitcoin')
plt.show()
