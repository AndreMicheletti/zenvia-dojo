# Zenvia Test

#### Problema escolhido

[Conversão de números romanos](http://codingdojo.org/kata/RomanNumerals/)

### Descrição da solução

Para chegar a essa solução, eu decidi usar o método TDD
 de escrever testes antes do código.
 
Eu comecei tentando resolver na ordem: `I`, `III`, `III`,
e meu código começou assim:

```python
return "I" * arabic
```

E para resolver o `IV` eu tive que levar em conta a 
subtração.

Porém foi olhando para o maior dos paramêtros do teste que
eu havia montado que eu percebi uma coisa:

```python
(5423, "MMMMMCDXXIII")
```

Eu poderia separar dessa maneira

```python
(5423, "MMMMM CD XX III")
```

Ou seja, para dizer `5` quando estamos na cada dos 
milhares, usamos 5 vezes o `M`

Para dizer `4` na casa das centenas, precisamos usar
a lógica de subtração, assim `CD`. Assim como fazemos 
quando representamos `4` usando `IV`

Portanto, cada __casa__ do nosso sistema numérico seguia
a mesma lógica que a lógica de `1` a `9` romano, apenas mudando
os símbolos.

### Instruções

Segue instruções para executar os testes do `pytest`

#### Executar ambiente local

Requisitos:
 - `Python` >= 3.6
 - `pip`
 - (opcional) `virtualenv`

Passos:

Clone o repositório, navegue para o diretório do projeto 
`cd zenvia_dojo/`

Crie um novo ambiente virtual python (opcional), e instale as dependências `pip install -r requirements.txt`

E execute os testes usando o comando:
 
`pytest -x`


#### Executar usando docker

Requisitos:

 - Docker
 
Para executar, basta montar a imagem:

`docker build -t zenvia_test .`

E depois rodar a imagem:

`docker run -it zenvia_test`

Obs:
Caso não funcione, é possível tirar o argumento `-it`.
Ele serve somente para manter as cores do terminal
