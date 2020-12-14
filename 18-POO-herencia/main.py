import clases
persona = clases.Persona()
persona.setNombre("Nicolas")
persona.setApellidos("Sepulveda")
persona.setAltura("185cm")
persona.setEdad("26 años")

print("La persona es: {} {} ".format(persona.getNombre(),persona.getApellidos()))
print(persona.hablar())


informatico = clases.Informatico()
informatico.setNombre("Don Nico")
informatico.setApellidos("Martinez")

print("El  Informatico es: {} {} {} ".format(informatico.getNombre(),informatico.getApellidos(),informatico.experiencia))
print(informatico.getLenguajes())

print("-----")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Francisco")
print(tecnico.auditarRedes, tecnico.getLenguajes())