# Matéria de Testes de Software

A matéria vai usar diferentes linguagens em cada aula, portanto o repositório vai centralizar uma variedade de projetos em uma variedade de linguagens.

Portanto a estrutura do repo será:

```markdown
- teste-de-software/
  - java/
  - js/
  - etcs..
```

# Atividade Prática com TDD

1. 🟥: Primeiro, escrevemos testes que falham, pois a funcionalidade ainda não foi implementada.
   Por exemplo, no caso do validador de senhas, escrevemos testes para verificar se senhas inválidas são corretamente rejeitadas, porém elas não serão pois não existe o validador.
2. 🟩: Em seguida, implementamos o código mínimo necessário para que os testes passem, isso pode incluir lógica inicial que ainda não cobre todos os casos, mas resolve os testes escritos.
3. 🟦: Após os testes passarem, refatoramos o código para melhorar sua qualidade, mantendo todos os testes funcionando.

### Exemplo de Teste Aceitando um Erro Inicialmente

Durante o desenvolvimento, pode ocorrer de um teste ser aceito mesmo que o código ainda não esteja completamente correto. Por exemplo:

- No validador de senhas, inicialmente, o código pode aceitar uma senha sem 8 caracteres porque a lógica para verificar isso ainda não foi implementada.
- Escrevemos o teste para este caso específico, ele falha (Red), e então ajustamos o código para que ele passe (Green).

Esse processo iterativo garante que o código seja desenvolvido de forma robusta e que todos os requisitos sejam atendidos gradualmente.
