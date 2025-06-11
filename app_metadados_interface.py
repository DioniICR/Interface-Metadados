import customtkinter as ctk

ctk.set_appearance_mode('dark')

def abrir_configuracoes():
    def placeholder_bindings(caixa_texto, placeholder):
        def on_focus_in(event):
            if caixa_texto.get("1.0", "end-1c") == placeholder:
                caixa_texto.delete("1.0", "end")
                caixa_texto.configure(text_color="white")  # volta à cor normal

        def on_focus_out(event):
            if caixa_texto.get("1.0", "end-1c").strip() == "":
                caixa_texto.insert("1.0", placeholder)
                caixa_texto.configure(text_color="gray")  # cor do placeholder

        caixa_texto.insert("1.0", placeholder)
        caixa_texto.configure(text_color="gray")  # placeholder visível
        caixa_texto.bind("<FocusIn>", on_focus_in)
        caixa_texto.bind("<FocusOut>", on_focus_out)

    janela_config = ctk.CTkToplevel(app_interface)
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
    placeholder_bindings(caixa_texto3, "Códigos de ocorrência")



def validar_data():
    data_inicio = digitar_data_inicial.get()
    data_fim = digitar_data_final.get()

    if data_inicio == '10/10/2010' and data_fim == '11/11/2011':
        resultado_da_busca.configure(text='Buscando áudios ▶︎ •၊၊||၊|။||||။‌‌‌‌၊|• 0:30', text_color='green')
    else:
        resultado_da_busca.configure(text='Ocorreu um erro, tente novamente', text_color='red')


app_interface = ctk.CTk()
app_interface.title('Metadados')
app_interface.geometry('400x400')

# ⚙️ Botão de configuração com apenas o ícone no canto superior direito
botao_config = ctk.CTkButton(app_interface, text='⚙️', width=30, height=30, command=abrir_configuracoes)
botao_config.place(relx=1.0, x=-10, y=10, anchor='ne')  # Posiciona no canto superior direito com margem

# Restante da interface
mostrar_texto_data_inicial = ctk.CTkLabel(app_interface, text='DATA INICIAL: ')
mostrar_texto_data_inicial.pack(pady=10)

digitar_data_inicial = ctk.CTkEntry(app_interface, placeholder_text='01/01/2025')
digitar_data_inicial.pack(pady=10)

mostrar_texto_data_final = ctk.CTkLabel(app_interface, text='DATA FINAL: ')
mostrar_texto_data_final.pack(pady=10)

digitar_data_final = ctk.CTkEntry(app_interface, placeholder_text='02/01/2025')
digitar_data_final.pack(pady=10)

botao = ctk.CTkButton(app_interface, text='Buscar Áudios', command=validar_data)
botao.pack(pady=10)

resultado_da_busca = ctk.CTkLabel(app_interface, text='')
resultado_da_busca.pack(pady=10)

app_interface.mainloop()
