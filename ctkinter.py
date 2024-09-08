from datetime import date
import json
import customtkinter as ctk
from tkinter import messagebox, simpledialog, scrolledtext

# Funções para manipulação de dados
def lendo_documento_():
    caminho = "bancoDados.json"
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return {"receitas": [], "despesas": []}

def adicionando_itens_no_arquivo(tipo, novo_item, baseDados):
    baseDados[tipo].append(novo_item)
    with open("bancoDados.json", "w", encoding="utf-8") as arquivo:
        json.dump(baseDados, arquivo, ensure_ascii=False, indent=4)

def excluir_lista(tipo, tipo1, baseDados):
    baseDados[tipo].clear()
    baseDados[tipo1].clear()
    with open("bancoDados.json", "w", encoding="utf-8") as arquivo:
        json.dump(baseDados, arquivo, ensure_ascii=False, indent=4)

# Função para atualizar a interface gráfica
def atualizar_historico():
    receitas_text = "RECEITAS:\n"
    despesas_text = "DESPESAS:\n"
    
    for item in bancoDados["receitas"]:
        receitas_text += f"  tipo: {item['tipo']} | valor: R${item['valor']:.2f} | data: {item['data']}\n"
        
    for item in bancoDados["despesas"]:
        despesas_text += f"  tipo: {item['tipo']} | valor: R${item['valor']:.2f} | data: {item['data']}\n"
    
    historico_text.delete(1.0, ctk.END)
    historico_text.insert(ctk.END, receitas_text + "\n" + despesas_text)

def adicionar_receita():
    tipo = simpledialog.askstring("Entrada", "Informe o tipo da receita:")
    valor = simpledialog.askfloat("Entrada", "Informe o valor (R$):")
    
    if tipo and valor is not None:
        receita = {
            "tipo": tipo,
            "valor": valor,
            "data": date.today().strftime("%d/%m/%Y")
        }
        adicionando_itens_no_arquivo("receitas", receita, bancoDados)
        atualizar_historico()

def adicionar_despesa():
    
    tipo = simpledialog.askstring("Entrada", "Informe o tipo da despesa:")
    valor = simpledialog.askfloat("Entrada", "Informe o valor (R$):")
    
    if tipo and valor is not None:
        despesa = {
            "tipo": tipo,
            "valor": valor,
            "data": date.today().strftime("%d/%m/%Y")
        }
        adicionando_itens_no_arquivo("despesas", despesa, bancoDados)
        atualizar_historico()

def excluir_historico():
    excluir_lista("despesas", "receitas", bancoDados)
    atualizar_historico()
    messagebox.showinfo("Info", "Histórico apagado!")

def mostrar_saldo():
    receita = sum(item['valor'] for item in bancoDados["receitas"])
    despesa = sum(item['valor'] for item in bancoDados["despesas"])
    saldo = receita - despesa
    messagebox.showinfo("Saldo", f"Saldo: R${saldo:.2f}")

# Configuração da interface gráfica
bancoDados = lendo_documento_()

# Inicializar CustomTkinter
ctk.set_appearance_mode("light")  # "light" ou "dark"
ctk.set_default_color_theme("blue")  # Tema padrão

root = ctk.CTk()
root.title("Finance Personal")

# Criação de frames
frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Adicionar widgets
adicionar_receita_btn = ctk.CTkButton(frame, text="Adicionar Receita", command=adicionar_receita)
adicionar_receita_btn.pack(fill="x", pady=5)

adicionar_despesa_btn = ctk.CTkButton(frame, text="Adicionar Despesa", command=adicionar_despesa)
adicionar_despesa_btn.pack(fill="x", pady=5)

excluir_historico_btn = ctk.CTkButton(frame, text="Excluir Histórico", command=excluir_historico)
excluir_historico_btn.pack(fill="x", pady=5)

mostrar_saldo_btn = ctk.CTkButton(frame, text="Mostrar Saldo", command=mostrar_saldo)
mostrar_saldo_btn.pack(fill="x", pady=5)

historico_text = ctk.CTkTextbox(frame, width=500, height=300)
historico_text.pack(padx=10, pady=10)

atualizar_historico()

root.mainloop()
