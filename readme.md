<p align="center"> <img src="./assets/img/python_logo.png" alt="Nota Fiscal" width="150" /> <br /> <b>Extrair Dados de PDF</b> <br /> <sub><sup><b>(AUTOMATIZAR-PROCESSOS-EM-PYTHON)</b></sup></sub> <br /> </p> <p align="center"> Este projeto é uma aplicação Python para extrair dados de notas fiscais em formato PDF e gerar um relatório em Excel. Utiliza bibliotecas como pdfplumber, pandas e re para realizar a extração e manipulação dos dados. 💡<br /> </p>

## Estrutura do Projeto

### Arquivos Principais
- `main.py`: Script principal que realiza a extração dos dados do PDF e gera o relatório em Excel.
- `nota_fiscal_teste.pdf`: PDF que criei simulando várias notas fiscais para testar o código.
- `readme.md`: Documentação do projeto (este arquivo).

### Estrutura de Pastas

extrair_dados_de_pdf_python/
├── assets/
│ └── nota_fiscal_teste.pdf
├── main.py
└── readme.md


## Funcionalidades
- **Extração de Dados**: Extrai informações como número da nota fiscal, data de emissão, CNPJ e valor total das notas fiscais presentes no PDF.
- **Geração de Relatório**: Gera um relatório em formato Excel (`relatorio_notas.xlsx`) com os dados extraídos.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolver o script.
- **pdfplumber**: Biblioteca para manipulação e extração de texto de arquivos PDF.
- **pandas**: Biblioteca para manipulação e análise de dados.
- **re**: Biblioteca para operações com expressões regulares.

## Instruções para Uso
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias utilizando o comando:
    ```sh
    pip install pdfplumber pandas
    ```
3. Coloque o arquivo PDF da nota fiscal na pasta `assets` (certifique que seja um texto e não uma imagem).
4. Execute o script `main.py`:
    ```sh
    python main.py
    ```
5. O relatório será gerado na raiz do projeto (logo abaixo de `main.py`) com o nome `relatorio_notas.xlsx`.

## Licença
Este software é licenciado sob os termos da MIT License.

## Desenvolvedor

<div align="center">

⌨️ Desenvolvido por [Vitor Bittencourt](https://github.com/vitorVBD) ☕

</div>