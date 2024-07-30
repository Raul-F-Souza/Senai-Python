# Salvar informaçôes dos proprietarios dos veiculos

# Casdatramento
def informacoes ():
    pessoas = {
        'OTM 2022':['MARLON', 'NEW CIVIC', 2022],
        'AAA-5551':['ENZO', 'GOLF', 2021],
        'UTS-0000':['RAUL', 'ECLIPSE', 2023],
        'IRS-1836':['JONATHAN', 'LANCER', 2022],
        'FBI-5551':['GUSTAVO', 'NEW BEATLE', 2023]
    }
    return pessoas

# Exibir todos os dados do dicionário
# for placa, cadastro in pessoas.items():
#     print(f'Placa: {placa}   Proprietário: {cadastro[0]}   Modelo: {cadastro[1]}   Ano veículo: {cadastro[2]}')

# Exibir todas as placas de veiculos (somente as placas)
# for placa, cadastro in pessoas.items():
#     print(placa)

#Exibir todos os propriertários de veículos (somente proprietarios)
# for placa, cadastro in pessoas.items():
#     print(f'{cadastro[0]}') #Indice 0 = proprietario, 1 = modelo, 2 = ano veiculo