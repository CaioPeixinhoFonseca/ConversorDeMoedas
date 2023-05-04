nome = str(input('Digite o seu nome: '))
real = float(input('Quanto dinheiro você tem? R$'))
escolhas = ('dolar', 'euro', 'libra esterlina', 'iene', 'dolar australiano')
print('''suas opções:
(0) dolar
(1) euro
(2) libra
(3) iene
(4) dolar australiano''')
conversao = int(input(f'{nome}, qual moeda você deseja converter? '))
dolar = real / 4.99
euro = real / 5.50
libra = real / 6.28
iene = real / 0.037
dolarAUD = real / 3.35

if conversao == 0:
    print(f'Com R${real} você consegue comprar U${dolar:.2f}')
elif conversao == 1:
    print(f'Com R${real} você consegue comprar EUR{euro:.2f}')
elif conversao == 2:
    print(f'Com R${real} você consegue comprar GBP{libra:.2f}')
elif conversao == 3:
    print(f'Com R${real} você consegue comprar JPY{iene:.2f}')
else:
    print(f'Com R${real} você consegue comprar AUD{dolarAUD:.2f}')
