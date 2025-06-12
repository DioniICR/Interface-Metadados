import customtkinter as ctk
from consulta_banco_de_dados import consulta_dados_banco
from main import main
from datetime import datetime
import threading

ctk.set_appearance_mode('dark')

def abrir_configuracoes():
    def placeholder_bindings(caixa_texto, placeholder):
        def on_focus_in(event):
            if caixa_texto.get("1.0", "end-1c") == placeholder:
                caixa_texto.delete("1.0", "end")
                caixa_texto.configure(text_color="white")  

        def on_focus_out(event):
            if caixa_texto.get("1.0", "end-1c").strip() == "":
                caixa_texto.insert("1.0", placeholder)
                caixa_texto.configure(text_color="gray")  

        caixa_texto.insert("1.0", placeholder)
        caixa_texto.configure(text_color="gray")  
        caixa_texto.bind("<FocusIn>", on_focus_in)
        caixa_texto.bind("<FocusOut>", on_focus_out)

    '''janela_config = ctk.CTkToplevel(app_interface)
    janela_config.title("Metadados")
    janela_config.geometry("400x400")

    label_config = ctk.CTkLabel(janela_config, text="Configure a busca mudando os parâmetros da pesquisa:")
    label_config.pack(pady=20)

    # Query 1
    label_query1 = ctk.CTkLabel(janela_config, text="Query 1:")
    label_query1.pack(anchor="w", padx=10)
    caixa_texto1 = ctk.CTkTextbox(janela_config, width=250, height=25)
    caixa_texto1.pack(pady=10)
    placeholder_bindings(caixa_texto1, "Códigos de ocorrência")

    # Query 2
    label_query2 = ctk.CTkLabel(janela_config, text="Query 2:")
    label_query2.pack(anchor="w", padx=10)
    caixa_texto2 = ctk.CTkTextbox(janela_config, width=250, height=25)
    caixa_texto2.pack(pady=10)
    placeholder_bindings(caixa_texto2, "Códigos de ocorrência")

    # Query 3
    label_query3 = ctk.CTkLabel(janela_config, text="Query 3:")
    label_query3.pack(anchor="w", padx=10)
    caixa_texto3 = ctk.CTkTextbox(janela_config, width=250, height=25)
    caixa_texto3.pack(pady=10)
    placeholder_bindings(caixa_texto3, "Códigos de ocorrência")'''

def validar_data(data_inicial: str, data_final: str):
    try:
        if not data_inicial or not data_final:
            resultado_da_busca.configure(text='Preencha as datas corretamente.', text_color='red')
            return

        # Tenta buscar os dados do banco com as datas fornecidas
        dados = consulta_dados_banco(data_inicial, data_final)

        if dados:  # Se houver resultados
            resultado_da_busca.configure(text='Buscando áudios ▶︎ •၊၊||၊|။||||။‌‌‌‌၊|• 0:30', text_color='green')
        else:  
            resultado_da_busca.configure(text='Nenhum dado encontrado para o período.', text_color='orange')
    except Exception as e:
        print(f"Erro: {e}")
        resultado_da_busca.configure(text='Ocorreu um erro, tente novamente.', text_color='red')





def buscar_dados(resposta_botao):
    def executar_tarefa():
        data_inicial_str = digitar_data_inicial.get()
        data_final_str = digitar_data_final.get()

        try:
            data_inicial = datetime.strptime(data_inicial_str, '%d/%m/%Y')
            data_final = datetime.strptime(data_final_str, '%d/%m/%Y')
            resultado_da_busca.configure(text='Download dos áudios, aguarde...', text_color='yellow')
            
            main(data_inicial, data_final, resposta_botao)
            resultado_da_busca.configure(text='Busca concluída com sucesso!', text_color='green')
        except Exception as e:
            resultado_da_busca.configure(text='Erro ao processar datas ou buscar dados.', text_color='red')
            print(f"Erro: {e}")

    threading.Thread(target=executar_tarefa).start()

app_interface = ctk.CTk()
app_interface.title('Metadados')
app_interface.geometry('400x400')

botao_config = ctk.CTkButton(app_interface, text='⚙️', width=30, height=30, command=abrir_configuracoes)
botao_config.place(relx=1.0, x=-10, y=10, anchor='ne')


mostrar_texto_data_inicial = ctk.CTkLabel(app_interface, text='DATA INICIAL: ')
mostrar_texto_data_inicial.pack(pady=10)

digitar_data_inicial = ctk.CTkEntry(app_interface, placeholder_text='01/01/2025')
digitar_data_inicial.pack(pady=10)

mostrar_texto_data_final = ctk.CTkLabel(app_interface, text='DATA FINAL: ')
mostrar_texto_data_final.pack(pady=10)

digitar_data_final = ctk.CTkEntry(app_interface, placeholder_text='02/01/2025')
digitar_data_final.pack(pady=10)


botao1 = ctk.CTkButton(app_interface, text='Botão 1 > Iniciar Busca ', command=lambda: buscar_dados(1))
botao1.pack(pady=10)

botao2 = ctk.CTkButton(app_interface, text='Botão 2 > Iniciar Busca ', command=lambda: buscar_dados(2))
botao2.pack(pady=10)

botao3 = ctk.CTkButton(app_interface, text='Botão 3 > Iniciar Busca ', command=lambda: buscar_dados(3))
botao3.pack(pady=10)


resultado_da_busca = ctk.CTkLabel(app_interface, text='')
resultado_da_busca.pack(pady=10)

app_interface.mainloop()
