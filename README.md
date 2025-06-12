# Projeto-ICR

# 🔍 Varredura de Dados com Geração de Excel

Este projeto realiza uma varredura em um banco de dados SQL para consolidar informações de ligações telefônicas, operadores e contratos. O resultado final é exportado para uma planilha Excel organizada.

---

## 🚀 Funcionalidades

- 🔄 Consulta registros em um intervalo de datas definido pelo usuário.
- 🔎 Identifica o CPF do operador a partir dos 5 primeiros dígitos do nome do arquivo de áudio.
- 📞 Localiza o contrato mais recente (último) utilizando o telefone presente no nome do arquivo.
- ⚠️ Preenche campos com "Não encontrado" caso os dados não existam.
- 📊 Exporta os dados finais para um arquivo Excel (`resultado.xlsx`).

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- `pyodbc` – Conexão com banco de dados SQL Server
- `pandas` – Manipulação e exportação de dados
- `openpyxl` – Exportação para Excel

---

## ⚙️ Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio