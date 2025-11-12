# Dicionário  (estoque)
estoque = {
    1: {"nome": "cereja",     "quantidade": 25, "valor": 40, "kilo": 5},
    2: {"nome": "goiaba",     "quantidade": 30, "valor": 12, "kilo": 18},
    3: {"nome": "figo",       "quantidade": 10, "valor": 35, "kilo": 4},
    4: {"nome": "caqui",      "quantidade": 15, "valor": 14, "kilo": 9},
    5: {"nome": "nectarina",  "quantidade": 20, "valor": 16, "kilo": 12},
    6: {"nome": "jabuticaba", "quantidade": 50, "valor": 25, "kilo": 7},
    7: {"nome": "tamarindo",  "quantidade": 18, "valor": 30, "kilo": 6},
    8: {"nome": "pitanga",    "quantidade": 40, "valor": 22, "kilo": 8},
    9: {"nome": "carambola",  "quantidade": 28, "valor": 19, "kilo": 10},
    10: {"nome": "framboesa", "quantidade": 12, "valor": 45, "kilo": 3},
}

# Lista onde vamos guardar as vendas realizadas
vendas = []

# Usuário e senha fixos
usuario_correto = "admin"
senha_correta = "1234"

# ============================
# LOGIN
# ============================
print("==== BEM VINDO AO SISTEMA ====")

while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso autorizado!")
        break
    else:
        print("Acesso negado, tente novamente.")

# ============================
# MENU PRINCIPAL
# ============================
while True:
    print("\n==== MENU ====")
    print("1 - Ver estoque")
    print("2 - Entrada de itens")
    print("3 - Saída de itens")
    print("4 - Vender item")
    print("5 - Ver relatório de vendas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # --------------------------
    # Opção 1 - Mostrar Estoque
    # --------------------------
    if opcao == "1":
        print("\n--- Estoque Atual ---")
        for codigo, produto in estoque.items():
            print(f"{codigo} - {produto['nome']} | "
                  f"Unidades: {produto['quantidade']} | "
                  f"Kg: {produto['kilo']}kg | "
                  f"R$ {produto['valor']}/kg")

    # --------------------------
    # Opção 2 - Entrada de Itens
    # --------------------------
    elif opcao == "2":
        print("\n--- Entrada de Itens ---")
        codigo = int(input("Código do produto: "))

        if codigo in estoque:
            add_qtd = int(input("Quantidade a adicionar: "))
            add_kg = float(input("Kg a adicionar: "))

            estoque[codigo]["quantidade"] += add_qtd
            estoque[codigo]["kilo"] += add_kg

            print("Entrada registrada com sucesso!")
        else:
            print("Código inválido.")

    # --------------------------
    # Opção 3 - Saída de Itens
    # --------------------------
    elif opcao == "3":
        print("\n--- Saída de Itens ---")
        codigo = int(input("Código do produto: "))

        if codigo in estoque:
            remove_qtd = int(input("Quantidade a remover: "))
            remove_kg = float(input("Kg a remover: "))

            if remove_qtd <= estoque[codigo]["quantidade"] and remove_kg <= estoque[codigo]["kilo"]:
                estoque[codigo]["quantidade"] -= remove_qtd
                estoque[codigo]["kilo"] -= remove_kg
                print("Saída registrada com sucesso!")
            else:
                print("Erro: quantidade ou kg insuficiente no estoque.")
        else:
            print("Código inválido.")

    # --------------------------
    # Opção 4 - Vender Item
    # --------------------------
    elif opcao == "4":
        print("\n--- Venda de Itens ---")
        codigo = int(input("Código do produto: "))

        if codigo in estoque:
            qtd_venda = int(input("Quantidade a vender: "))
            kg_venda = float(input("Kg a vender: "))

            if qtd_venda <= estoque[codigo]["quantidade"] and kg_venda <= estoque[codigo]["kilo"]:
                # Atualiza estoque
                estoque[codigo]["quantidade"] -= qtd_venda
                estoque[codigo]["kilo"] -= kg_venda

                # Calcula valor da venda
                valor_total = estoque[codigo]["valor"] * kg_venda

                # Registra a venda
                vendas.append({
                    "produto": estoque[codigo]["nome"],
                    "quantidade": qtd_venda,
                    "kg": kg_venda,
                    "valor_total": valor_total
                })

                print(f"Venda realizada: {estoque[codigo]['nome']} | "
                      f"{kg_venda}kg | R$ {valor_total:.2f}")
            else:
                print("Erro: estoque insuficiente.")
        else:
            print("Código inválido.")

    # --------------------------
    # Opção 5 - Relatório de Vendas
    # --------------------------
    elif opcao == "5":
        print("\n--- Relatório de Vendas ---")

        if vendas:
            total = 0
            for i, venda in enumerate(vendas, start=1):
                print(f"{i} - {venda['produto']} | "
                      f"Unidades: {venda['quantidade']} | "
                      f"{venda['kg']}kg | "
                      f"R$ {venda['valor_total']:.2f}")
                total += venda["valor_total"]

            print(f"\nTotal geral de vendas: R$ {total:.2f}")
        else:
            print("Nenhuma venda registrada até agora.")

    # --------------------------
    # Opção 6 - Sair
    # --------------------------
    elif opcao == "6":
        print("Saindo do sistema...")
        break

    # --------------------------
    # Opção Inválida
    # --------------------------
    else:
        print("Opção inválida. Tente novamente.")