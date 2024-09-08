
from datetime import date
import json

def lendo_documento_():
        #caminho do arquivo json com os dados
        caminho = "bancoDados.json"
        try:
            #carregar lista com dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return {
                    "receitas": [],
                    "despesas": []
            }


def adicionando_itens_no_arquivo(tipo,novo_item,baseDados):    

    baseDados[tipo].append(novo_item)   
    with open("bancoDados.json","w", encoding= "utf-8") as arquivo:
        json.dump(baseDados, arquivo, ensure_ascii=False, indent=4) 
        
def excluir_lista(tipo,tipo1, baseDados):      
    baseDados[tipo].clear()    
    baseDados[tipo1].clear()    
    with open("bancoDados.json","w", encoding= "utf-8") as arquivo:
        json.dump(baseDados, arquivo, ensure_ascii=False, indent=4) 


def criando_arquivo(nome_lista):      
    with open("bancoDados.json","w", encoding= "utf-8") as arquivo:
        json.dump(nome_lista, arquivo, ensure_ascii=False, indent=4)

bancoDados = lendo_documento_()


while True:

    print('''
            (1) - ADICIONAR RECEITAS
            (2) - ADICIONAR DESPESAS
            (3) - VER SALDO
            (4) - EXCLIR HISTÓRICO 
            (0) - SAIR
    ''')
    try:

        menu = int(input("Escolha opção:"))

    except:

        print("Informe opção válida!")

    else:

        match menu:

            case 1:
                nomeReceita = input("Informe nome da receita: ")
                valor = int(input("Informe valor (R$): "))

                receita = {
                    "nome": nomeReceita,
                    "valor": valor,
                    "data":date.today().strftime("%d/%m/%Y")
                }

                adicionando_itens_no_arquivo("receitas", receita,bancoDados)

            case 2:
                #DESPESAS
                nomeDespesa = input("Informe nome despesa: ")
                valor = float(input("Informe valor despesa: "))
                
                despesa = {
                    "nome": nomeDespesa,
                    "valor": valor,
                    "data":date.today().strftime("%d/%m/%Y")
                }

                

                adicionando_itens_no_arquivo("despesas",despesa,bancoDados)

            case 3:
                receita = 0
                despesa = 0

                for tipo, itens in bancoDados.items():
                    for item in itens:
                        if tipo == "receitas":
                            receita += item['valor']
                        else:
                            despesa += item['valor']



                print(f"\nSaldo: R${receita - despesa:.2f}")

            case 4:
                #apagar histórico
                
                excluir_lista("despesas","receitas", bancoDados)
                
            case 0:
                #SAIR
                break
            
