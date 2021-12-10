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

for p in personas:
    print(p['nombre'], 'tiene', p['edad'], 'años y su cédula es', p['cedula'])