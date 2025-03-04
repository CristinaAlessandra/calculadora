import argparse
import calculadora

parser = argparse.ArgumentParser(description="Calculadora")
parser.add_argument("operacao", choices=["soma", "subtrai", "multiplica", "divide"], help="Operação matemática")
parser.add_argument("num1", type=float, help="Primeiro número")
parser.add_argument("num2", type=float, help="Segundo número")

args = parser.parse_args()

if args.operacao == "soma":
    resultado = calculadora.somar(args.num1, args.num2)
elif args.operacao == "subtrai":
    resultado = calculadora.subtrair(args.num1, args.num2)
elif args.operacao == "multiplica":
    resultado = calculadora.multiplicar(args.num1, args.num2)
elif args.operacao == "divide":
    resultado = calculadora.dividir(args.num1, args.num2)

print(f"Resultado: {resultado}")
