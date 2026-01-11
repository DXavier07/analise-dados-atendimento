import os
import csv
import matplotlib.pyplot as plt # Importamos a biblioteca de gráficos

# --- CONFIGURAÇÃO ---
arquivo_csv = 'dados/chamados_99.csv'
lista_chamados = []

print(f"--- 📊 INICIANDO ANÁLISE COMPLETA ---")

try:
    # 1. Carregamento
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_chamados.append(linha)

    # 2. Processamento
    estatisticas = {}

    for chamado in lista_chamados:
        tipo = chamado['tipo_problema']
        tempo = int(chamado['tempo_resolucao_min'])
        
        if tipo not in estatisticas:
            estatisticas[tipo] = {'qtd': 0, 'tempo_total': 0}
            
        estatisticas[tipo]['qtd'] += 1
        estatisticas[tipo]['tempo_total'] += tempo

    # 3. Exibição no Terminal (Relatório de Texto)
    print("\n📋 RELATÓRIO GERAL:")
    print(f"{'TIPO':<15} | {'QTD':<5} | {'TEMPO MÉDIO':<12}")
    print("-" * 40)

    # Preparando dados para o gráfico
    tipos_grafico = []
    tempos_grafico = []

    for tipo, dados in estatisticas.items():
        media_tempo = dados['tempo_total'] / dados['qtd']
        
        # Guardando dados nas listas para o gráfico
        tipos_grafico.append(tipo)
        tempos_grafico.append(media_tempo)

        print(f"{tipo:<15} | {dados['qtd']:<5} | {media_tempo:.1f} min")

    print("-" * 40)

    # 4. GERANDO O GRÁFICO (A novidade visual)
    print("\n🎨 Gerando gráfico visual...")

    # Criando o desenho (Bar Chart)
    plt.figure(figsize=(10, 6)) # Tamanho da imagem
    plt.bar(tipos_grafico, tempos_grafico, color='orange') # Barras laranjas (cor da 99)

    # Textos do gráfico
    plt.title('Tempo Médio de Resolução por Tipo de Problema')
    plt.xlabel('Tipo de Problema')
    plt.ylabel('Tempo Médio (minutos)')
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Linhas de grade suaves

    # Salvando a imagem na pasta do projeto
    nome_imagem = 'grafico_performance.png'
    plt.savefig(nome_imagem)
    
    print(f"✅ SUCESSO! O gráfico foi salvo como '{nome_imagem}'.")
    print("Abra a pasta do projeto para ver a imagem!")

except FileNotFoundError:
    print("ERRO: Arquivo CSV não encontrado.")
except ImportError:
    print("ERRO: Biblioteca matplotlib não instalada. Rode 'pip install matplotlib' no terminal.")