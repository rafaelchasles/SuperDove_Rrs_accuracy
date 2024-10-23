# -*- coding: utf-8 -*-
"""dsf_psr_graph_stats.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XeGBoyBgLAsvJoxgtA8EV-ZAYxTa1FYF
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lendo os dados do arquivo CSV
df = pd.read_csv('/content/drive/MyDrive/mestrado/dissertacao/dados/tabelas/resultados/dsf_psr_graph_stats.csv', sep=';')

# Definindo os valores de x
valores_x = df.iloc[:, 0]

# Criando os gráficos para cada métrica
plt.figure(figsize=(10, 12))

# Plotando e_DSF com e_PSR
plt.subplot(2, 2, 1)
plt.plot(valores_x, df['e_DSF'], label='DSF', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.plot(valores_x, df['e_PSR'], label='PSR', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.xlabel('Comprimento de onda (nm)', fontsize=8)
plt.ylabel('ε (%)', fontsize=8)
plt.title('ε (%)', fontsize=10)
plt.ylim(0, 100)  # Limitando o eixo y para 0 a 100
plt.legend(fontsize=8)
plt.grid(True)

# Plotando b_DSF com b_PSR
plt.subplot(2, 2, 2)
plt.plot(valores_x, df['b_DSF'], label='DSF', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.plot(valores_x, df['b_PSR'], label='PSR', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.xlabel('Comprimento de onda (nm)', fontsize=8)
plt.ylabel('β (%)', fontsize=8)
plt.title('β (%)', fontsize=10)
plt.ylim(0, 100)  # Limitando o eixo y para 0 a 100
plt.legend(fontsize=8)
plt.grid(True)

# Plotando mape_DSF com mape_PSR
plt.subplot(2, 2, 3)
plt.plot(valores_x, df['mape_DSF'], label='DSF', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.plot(valores_x, df['mape_PSR'], label='PSR', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.xlabel('Comprimento de onda (nm)', fontsize=8)
plt.ylabel('MAPE', fontsize=8)
plt.title('MAPE', fontsize=10)
plt.ylim(0, 500)  # Limitando o eixo y para 0 a 100
plt.legend(fontsize=8)
plt.grid(True)



# Plotando s_DSF com s_PSR
plt.subplot(2, 2, 4)
plt.plot(valores_x, df['s_DSF'], label='DSF', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.plot(valores_x, df['s_PSR'], label='PSR', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.xlabel('Comprimento de onda (nm)', fontsize=8)
plt.ylabel('S', fontsize=8)
plt.title('Slope', fontsize=10)
plt.ylim(-0.5, 0.5)  # Limitando o eixo y para 0 a 100
plt.legend(fontsize=8)
plt.grid(True)

plt.tight_layout()
plt.show()

# Plotando rmlse_DSF com rmlse_PSR
plt.subplot(3, 2, 4)
plt.plot(valores_x, df['rmlse_DSF'], label='DSF', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.plot(valores_x, df['rmlse_PSR'], label='PSR', marker='o', linestyle='--',markersize=3, linewidth=1)
plt.xlabel('Comprimento de onda (nm)', fontsize=8)
plt.ylabel('RMLSE', fontsize=8)
plt.title('RMLSE', fontsize=10)
plt.ylim(0, 0.03)  # Limitando o eixo y para 0 a 100
plt.legend(fontsize=8)
plt.grid(True)