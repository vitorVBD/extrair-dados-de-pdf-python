import pdfplumber
import pandas as pd
import re

extracted_data = []
pdf_path = "assets/nota_fiscal_teste.pdf"

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                notas = re.findall(r'Nota Fiscal: (\d+)', text)
                datas_emissao = re.findall(r'Data: (\d{2}/\d{2}/\d{4})', text)
                cnpjs = re.findall(r'CNPJ: (\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})', text)
                valores = re.findall(r'Valor Total: R\$ (\d+\.\d+,\d{2})', text)

                if len(notas) == len(datas_emissao) == len(cnpjs) == len(valores):
                    for i in range(len(notas)):
                        extracted_data.append({
                            "Nota": notas[i],
                            "data_emissao": datas_emissao[i],
                            "cnpj": cnpjs[i],
                            "valor": valores[i]
                        })
                else:
                    print("Aviso: Número de ocorrências inconsistente em uma página.")


extract_text_from_pdf(pdf_path)

df = pd.DataFrame(extracted_data)
df.to_excel("relatorio_notas.xlsx", index=False)

print(f"Relatório gerado com sucesso! {len(extracted_data)} notas extraídas.")