# Solicita uma string do usuário
inverte = input('Seu texto será invertido: ')


invertida = ''


for i in range(len(inverte) - 1, -1, -1):
  invertida += inverte[i]


print(f'O texto invertido é: {invertida}')
