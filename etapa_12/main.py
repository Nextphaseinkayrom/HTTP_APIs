import requests

# Principais usados >
link = f"https://jsonplaceholder.typicode.com/posts/"


# Menu com ações
try:
  menu  = int(input("""--- M ---
1 - Consultar
2 - Cadastrar
Tecla/AL - Sair"""))
except ValueError:
  print("Ponha o valor exato")
else:
 if menu == 1:
   try:
    puxada = int(input("Digite o id existente de algum produto"))
   except ValueError:
    print("Põe um valor")
   else:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{puxada}")
    
    if response.status_code == 404:
        print("Sem Cadastros de produtos com este id")
    else:
        dados = response.json()
        print(f""" 
        ID > {dados["id"]}
        Titulo > {dados["title"]}
        Descrição > {dados["body"]}""")    
 elif menu == 2:
   print("Área de cadastro(Área de ADM/FNC)")
   try:
    produto = input("Nome do produto novo:")
    valor = float(input("Preço: "))
    quantidade = int(input("Quantidade disponiveis: "))
   except ValueError:
    print("Ponha valores apenas com [.] Ou valores inteiros")
   else: 
    dados = {
    "Produto": produto,
    "Preço": valor,
    "Quantidade": quantidade,
    "Id_user": "1"
}
    resultado = requests.post(link, json=dados)
    print(resultado.status_code)
    print(resultado.json())

 else:
  print("Finalizando o programa")