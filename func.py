persona_1 = {
  'nombre': 'Sara',
  'edad': 27,
  'cedula': '115820287'
}
persona_2 = {
  'nombre': 'Oscar',
  'edad': 35,
  'cedula': '112310501'
}
persona_3 = {
  'nombre': 'Mario',
  'edad': 40,
  'cedula': '111020253'
}

personas = [persona_1, persona_2, persona_3]

def info(p):
    return p['nombre'] + ' tiene ' + str(p['edad']) + ' años y su cédula es ' + p['cedula']

for persona in personas:
    print(info(persona))