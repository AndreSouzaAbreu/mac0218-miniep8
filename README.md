# MINI EP 8

O objetivo deste projeto é utilizar o TDD (Test-Driven Development) no  processo
de desenvolvimento de software; neste caso, alguma aplicação simples.

O que eu desenvolvi foi uma aplicação simples que  contém  um  módulo  utilizado
para calcular a raiz quadrada de  um  número  utilizando  o  método  de  Newton.
Primeiramente, adicionei os testes, depois implementei o  código,  e  finalmente
rodei os testes (felizmente, o código passou nos testes).

O código fonte, junto com os testes, está no  diretório  [src/](./src).  Como  o
projeto é pequeno e visa o aprendizado, resolvi deixar os arquivos  de  teste  e
implementação junto. Se o projeto fosse um pouco mais complexo, eu  deixaria  os
testes em um diretório `tests/` em vez de `src/`. Por este mesmo motivo  escolhi
a linguagem Python, por ser  fácil  e  de  rápido  desenvolvimento;  mas  em  um
projeto maior eu escolheria outra linguagem, tal como Java.

Por fim, para rodar os testes basta rodar o comando:

```python
python src/test_sqroot.py
```
