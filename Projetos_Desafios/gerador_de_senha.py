senha = input("Digite sua senha: ")
caracteres_especiais = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

erros = []

if len(senha) < 8:
    erros.append("⚠️ Pelo menos 8 caracteres")
if not any(c.isupper() for c in senha):
    erros.append("⚠️ Pelo menos uma letra maiúscula")
if not any(c.islower() for c in senha):
    erros.append("⚠️ Pelo menos uma letra minúscula")
if not any(c.isdigit() for c in senha):
    erros.append("⚠️ Pelo menos um número")
if not any(c in caracteres_especiais for c in senha):
    erros.append("⚠️ Pelo menos um símbolo especial (!@#$...)")

if erros:
    print("❌ Senha fraca. Veja o que faltou:")
    for erro in erros:
        print(erro)
else:
    print(" Senha forte! Tudo certo.")





