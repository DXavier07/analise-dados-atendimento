import os
import csv

# --- CONFIGURAÇÃO ---
arquivo_csv = 'dados/chamados_99.csv'
lista_chamados = []

print(f"--- 📊 INICIANDO ANÁLISE DE DADOS DA 99 ---")

try:
    # 1. Carregamento dos Dados
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_chamados.append(linha)

    # 2. Processamento (Agrupando os dados)
    estatisticas = {} # Vai guardar: {'Pagamento': {'qtd': 10, 'tempo_total': 200, 'nota_total': 30}}

    for chamado in lista_chamados:
        tipo = chamado['tipo_problema']
        tempo = int(chamado['tempo_resolucao_min'])
        nota = int(chamado['nota_usuario'])
        
        if tipo not in estatisticas:
            estatisticas[tipo] = {'qtd': 0, 'tempo_total': 0, 'nota_total': 0}
            
        estatisticas[tipo]['qtd'] += 1
        estatisticas[tipo]['tempo_total'] += tempo
        estatisticas[tipo]['nota_total'] += nota

    # 3. Exibição da Tabela
    print("\n📋 RELATÓRIO GERAL:")
    print(f"{'TIPO':<15} | {'QTD':<5} | {'TEMPO MÉDIO':<12} | {'NOTA MÉDIA'}")
    print("-" * 55)

    pior_tempo = 0
    problema_mais_lento = ""

    for tipo, dados in estatisticas.items():
        media_tempo = dados['tempo_total'] / dados['qtd']
        media_nota = dados['nota_total'] / dados['qtd']
        
        # Lógica para descobrir o gargalo automaticamente
        if media_tempo > pior_tempo:
            pior_tempo = media_tempo
            problema_mais_lento = tipo

        print(f"{tipo:<15} | {dados['qtd']:<5} | {media_tempo:.1f} min      | {media_nota:.1f} / 5.0")

    print("-" * 55)

    # 4. Insight Automático (A mágica acontece aqui)
    print("\n💡 INSIGHT DO SISTEMA:")
    print(f"O gargalo operacional é: >> {problema_mais_lento.upper()} <<")
    print(f"Este problema leva em média {pior_tempo:.1f} minutos para ser resolvido.")
    
    if pior_tempo > 30:
        print("⚠️ ALERTA: Tempo de resolução acima do ideal (30 min). Sugere-se revisão do processo.")
    else:
        print("✅ Operação dentro dos parâmetros normais.")

except FileNotFoundError:
    print("ERRO: O arquivo CSV não foi encontrado.")