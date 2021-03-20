from funcoes import pis, cofins, calculo_irpj, calculo_csll, convert_data


# Calculo de Impostos Federais
regime = input('Informe seu regime tributário: C para Cumulativo e NC para Nao cumulativo: ')
valor_receita = float(input('Informe o valor da receita bruta: '))
creditos_tributario = float(input('Informe o valor dos créditos tributários orindus dos custos, despesas e encargos: '))
lucro_contabil = float(input('Informe o valor do Lucro contabil do periodo: '))

pis = pis(regime, valor_receita, creditos_tributario)
cofins = cofins(regime, valor_receita, creditos_tributario)
irpj = calculo_irpj(regime, valor_receita, lucro_contabil)
csll = calculo_csll(regime, valor_receita, lucro_contabil)

title = "CALCULO DE IMPOSTOS FEDERAIS \n \n"
text = [title, pis, cofins, irpj, csll]
text = map(convert_data, text)

arquivo = open('arquivo.txt','w')
arquivo.write("\n".join(text))
arquivo.close()



