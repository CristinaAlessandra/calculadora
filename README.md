# 📱 Calculadora em Python
### Disciplina: DevOps - Semestre 2 
A calculadora foi construída utilizando Python para realizar operações matemáticas simples como soma, subtração, multiplicação e divisão. O projeto também inclui um módulo de automação de testes utilizando a biblioteca pytest, que valida a funcionalidade das operações matemáticas.

## 🚀 Como Rodar o Projeto
### 1. Rodar a Calculadora:
A calculadora pode ser executada diretamente no terminal ou em um ambiente Python.

Para rodar a calculadora interativamente, você pode executar o arquivo calculadora.py com o Python:

`python calculadora.py`

A calculadora permitirá que você escolha uma operação e forneça os números para realizar o cálculo.

## 🧪 Testes Automáticos
A fim de garantir a precisão das operações, foram implementados testes automatizados utilizando a biblioteca pytest.

### 2. Rodar os Testes Automáticos
Para rodar todos os testes do módulo de testes (test_calculadora.py), execute o seguinte comando:

`pytest test_calculadora.py`

Isso executará todos os testes definidos no arquivo test_calculadora.py e apresentará os resultados no terminal.

### 3. Ver Detalhes dos Testes
Se você deseja ver mais detalhes sobre a execução de cada teste (como a descrição de erros e falhas), use a opção -v (verbose):

`pytest -v test_calculadora.py`

### 4. Rodar um Teste Específico
Caso queira rodar apenas um teste específico, você pode usar a opção -k seguida do nome do teste. Por exemplo, para rodar o teste que valida a operação de soma, execute:

`pytest -k "test_soma"`

## ⚙️ Tecnologias Utilizadas
**Python:** Linguagem utilizada para implementar a calculadora e os testes. <br>
**pytest:** Framework utilizado para escrever e executar os testes automatizados.

## 📌 Notas Adicionais
Certifique-se de ter o pytest instalado em seu ambiente de desenvolvimento. Você pode instalar o pytest com o seguinte comando:

`pip install pytest`

Os testes são feitos para garantir que cada operação (soma, subtração, multiplicação, divisão) está funcionando corretamente. Mais testes podem ser adicionados para validações mais complexas, como exceções para divisão por zero.
