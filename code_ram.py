import random

def generar_id_persona(department):
  if department == "Sales":
    codigo = random.randint(1000,1499)
  elif department == "Human Relations":
    codigo = random.randint(1500,1999)
  elif department == "Design":
    codigo = random.randint(2000, 2999)
  elif department == "Accounting":
    codigo = random.randint(3000,3499)
  elif department == "Finance":
    codigo = random.randint(3500,3999)
  elif department == "Management":
    codigo = random.randint(4000,4100)
  else:
    codigo = 0
  return codigo
