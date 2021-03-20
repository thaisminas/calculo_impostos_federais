

PIS_C = float(0.65 / 100)
PIC_NC = float(1.65 / 100)
COFINS_C = float(3 / 100)
COFINS_NC = float(7.60 / 100)

adicional_irpj_limite = float(20000.00)

#Calculo PIS
def pis(regime, valor_receita, creditos_tributario):
    if regime == 'C':
        valor_pis = valor_receita * PIS_C
        return 'Valor a recolher PIS sobre Lucro Presumido R${}'.format(round(valor_pis, 2))
    else:
        valor_pis = (valor_receita * PIC_NC) + (creditos_tributario * PIC_NC)
        return 'Valor a recolher PIS sobre Lucro Real R${}'.format(round(valor_pis, 2))


#Calculo do COFINS
def cofins(regime, valor_receita, creditos_tributario):
    if regime == 'C':
        valor_cofins = valor_receita * COFINS_C
        return 'Valor a recolher COFINS sobre Lucro Presumido R${}'.format(round(valor_cofins, 2))
    else:
        valor_cofins = float((valor_receita * COFINS_NC) + (creditos_tributario * COFINS_NC))
        return 'Valor a recolher COFINS sobre Lucro Real R${}'.format(round(valor_cofins, 2))


#Calculo IRPJ - LUCRO PRESUMIDO E REAL
def calculo_irpj(regime, valor_receita,lucro_contabil):
    if regime == 'C':
        aliquota_irpj = float(input('Informe a aliquota na qual esta incluso a empresa para IRPJ: '))
        valor_irpj = valor_receita * (aliquota_irpj /100)
        return 'Valor a recolher IRPJ sobre Lucro Presumido R${}'.format(round(valor_irpj, 2))
    else:
        if lucro_contabil > adicional_irpj_limite:
            adicional = (lucro_contabil - adicional_irpj_limite) * (10/100)
            irpj_nc = ((lucro_contabil * (15/100)) + adicional)
            return 'Valor a recolher IRPJ sobre Lucro Real R${}'.format(round(irpj_nc, 2))
        else:
            irpj_nc = lucro_contabil * (15 / 100)
            return 'Valor a recolher IRPJ sobre Lucro Real R${}'.format(round(irpj_nc, 2))





#Calculo CSLL - LUCRO PRESUMIDO E REAL
def calculo_csll(regime, valor_receita, lucro_contabil):
    if regime == 'C':
        aliquota_csll = float(input('Informe a aliquota na qual esta incluso a empresa para CSLL: '))
        valor_csll = valor_receita * (aliquota_csll/ 100)
        return 'Valor a recolher CSLL sobre Lucro Presumido R${}'.format(round(valor_csll, 2))
    else:
        csll_nc = lucro_contabil * (9/100)
        return 'Valor a recolher CSLL sobre Lucro Real R${}'.format(round(csll_nc, 2))




#Consultar Tabela IRPJ e CSLL

def consulta_tabela_cs_e_ir():
    print('IRPJ TABELA:')
    print('Revenda de Combustiveis : 1.6%')
    print('Regra geral (toda empresa que não está explicitamente nas definições acima e abaixo) = 8.0%')
    print('Serviço de transporte que não seja de carga = 16%')
    print('Prestação de serviços em geral = 32%')
    print('/n')
    print('TABELA CSLL')
    print('Regra geral (toda empresa que não está na alíquota de 32%) = 12% ')
    print('Prestação de serviços em geral = 32%')


def convert_data(n):
    return str(n)
