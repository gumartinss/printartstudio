
import tkinter as tk
from tkinter import messagebox


def calcular_custo():
    try:
        # Obtendo os valores dos campos de entrada
        custo_kg_filamento = float(entry_custo_filamento.get().replace(',', '.'))
        quantidade_material_usado = float(entry_quantidade_material.get().replace(',', '.'))
        duracao_impressao = float(entry_duracao_impressao.get().replace(',', '.'))
        taxa_energia = float(entry_taxa_energia.get().replace(',', '.'))
        consumo_impressora = float(entry_consumo_impressora.get().replace(',', '.'))
        margem_lucro = float(entry_margem_lucro.get().replace(',', '.'))

        # Cálculo do custo do filamento
        quantidade_material_usado_kg = quantidade_material_usado / 1000
        resultado_custo_filamento = custo_kg_filamento * quantidade_material_usado_kg

        # Cálculo do custo da energia
        consumo_impressora_kw = consumo_impressora / 1000
        duracao_impressao_horas = duracao_impressao / 60
        resultado_energia = consumo_impressora_kw * duracao_impressao_horas * taxa_energia / 60

        # Cálculo do custo total com margem de lucro
        custo_total_sem_lucro = resultado_custo_filamento + resultado_energia
        custo_total_com_lucro = custo_total_sem_lucro * (1 + margem_lucro / 100)

        # Exibindo resultado em uma janela de mensagem
        messagebox.showinfo("Resultado", f'Custo total com margem de lucro: R$ {custo_total_com_lucro:.2f}')

    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de preencher todos os campos com valores numéricos.")

def on_entry_change(*args):
    # Função para substituir vírgulas por pontos
    s = entry_custo_filamento.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_custo_filamento.delete(0, tk.END)
        entry_custo_filamento.insert(0, s)

    s = entry_quantidade_material.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_quantidade_material.delete(0, tk.END)
        entry_quantidade_material.insert(0, s)

    s = entry_duracao_impressao.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_duracao_impressao.delete(0, tk.END)
        entry_duracao_impressao.insert(0, s)

    s = entry_taxa_energia.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_taxa_energia.delete(0, tk.END)
        entry_taxa_energia.insert(0, s)

    s = entry_consumo_impressora.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_consumo_impressora.delete(0, tk.END)
        entry_consumo_impressora.insert(0, s)

    s = entry_margem_lucro.get()
    if ',' in s:
        s = s.replace(',', '.')
        entry_margem_lucro.delete(0, tk.END)
        entry_margem_lucro.insert(0, s)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Custo de Impressão 3D")

# Criando os widgets (campos de entrada e rótulos)
label_custo_filamento = tk.Label(root, text="Preço do quilo do filamento (em R$):")
label_custo_filamento.grid(row=0, column=0, padx=10, pady=10)
entry_custo_filamento = tk.Entry(root)
entry_custo_filamento.grid(row=0, column=1, padx=10, pady=10)
entry_custo_filamento.bind('<KeyRelease>', on_entry_change)

label_quantidade_material = tk.Label(root, text="Quantidade de material usado (em gramas):")
label_quantidade_material.grid(row=1, column=0, padx=10, pady=10)
entry_quantidade_material = tk.Entry(root)
entry_quantidade_material.grid(row=1, column=1, padx=10, pady=10)
entry_quantidade_material.bind('<KeyRelease>', on_entry_change)

label_duracao_impressao = tk.Label(root, text="Duração da impressão (em minutos):")
label_duracao_impressao.grid(row=2, column=0, padx=10, pady=10)
entry_duracao_impressao = tk.Entry(root)
entry_duracao_impressao.grid(row=2, column=1, padx=10, pady=10)
entry_duracao_impressao.bind('<KeyRelease>', on_entry_change)

label_taxa_energia = tk.Label(root, text="Taxa de energia da distribuidora (em R$/kWh):")
label_taxa_energia.grid(row=3, column=0, padx=10, pady=10)
entry_taxa_energia = tk.Entry(root)
entry_taxa_energia.grid(row=3, column=1, padx=10, pady=10)
entry_taxa_energia.bind('<KeyRelease>', on_entry_change)

label_consumo_impressora = tk.Label(root, text="Consumo médio da impressora 3D (em watts):")
label_consumo_impressora.grid(row=4, column=0, padx=10, pady=10)
entry_consumo_impressora = tk.Entry(root)
entry_consumo_impressora.grid(row=4, column=1, padx=10, pady=10)
entry_consumo_impressora.bind('<KeyRelease>', on_entry_change)

label_margem_lucro = tk.Label(root, text="Margem de lucro (em %):")
label_margem_lucro.grid(row=5, column=0, padx=10, pady=10)
entry_margem_lucro = tk.Entry(root)
entry_margem_lucro.grid(row=5, column=1, padx=10, pady=10)
entry_margem_lucro.bind('<KeyRelease>', on_entry_change)

# Botão para calcular o custo
btn_calcular = tk.Button(root, text="Calcular Custo", command=calcular_custo)
btn_calcular.grid(row=6, columnspan=2, padx=10, pady=10)

# Rodando o loop principal da interface gráfica
root.mainloop()
