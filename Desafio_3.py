nmr_1=int(input("Digite um numero: "))
nmr_2=int(input("Digite outro numero: "))

opcao=input("Digite a operacao matematica que deseja realizar (soma, mult, sub, div): ")

if opcao == "soma":
    print(nmr_1 + nmr_2)
elif opcao == "sub":
    print(nmr_1 - nmr_2)
elif opcao == "div":
    print(nmr_1 / nmr_2)
elif opcao == "mult":
    print(nmr_1 * nmr_2)
else:
    print("opcao invalida")
