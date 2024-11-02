import json

persona = {
    "nombre": "Salva",
    "apellido": "Ri",
    "edad": 24
}
objecto_json = json.dumps(persona, indent=2)
with open("persona.json", "w") as archiv_json:
    archiv_json.write(objecto_json)

# sin indentacion
with open("persona_no_ident.json", "w") as archiv_json:
    json.dump(persona, archiv_json)