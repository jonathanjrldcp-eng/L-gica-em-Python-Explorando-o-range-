# Exercícios de Lógica em Python: Explorando o `range()`

Este pequeno script em Python foi criado para demonstrar a versatilidade da função `range()` combinada com laços de repetição `for`. O código é dividido em três blocos interativos que mostram diferentes formas de iterar sobre sequências numéricas.

## Conceitos Abordados

*   **Laços `for`:** Utilizados para repetir um bloco de código um número predeterminado de vezes.
*   **A função `range(start, stop, step)`:**
    *   **Contagem Regressiva:** Demonstra como usar um passo (`step`) negativo para contar de trás para frente.
    *   **Sequência Padrão:** Uso do `range()` com passo implícito de 1.
    *   **Passo Customizado:** Uso de um passo (`step`) de 2 para pegar apenas números pares.
*   **Controle de Fluxo e Interface:** Uso da biblioteca `time` (`sleep()`) para criar pausas dramáticas e da biblioteca `os` para limpar o terminal entre cada exercício, mantendo a tela organizada.

## O que o código faz?

O script executa três rotinas em sequência:

1.  **Contagem Regressiva:** Conta de 10 até 1 (`range(10, 0, -1)`). Útil para entender como inverter a lógica de iteração.
2.  **Tabuada do 7:** Multiplica o número 7 pelos números de 1 a 10 (`range(1, 11)`).
3.  **Tabuada do 7 (Apenas Pares):** Multiplica o número 7 apenas pelos números pares de 0 a 10 (`range(0, 11, 2)`).

## Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Salve o código em um arquivo (ex: `loops_range.py`).
3.  Abra o terminal, navegue até a pasta do arquivo e execute:
    ```bash
    python loops_range.py
    ```
4.  Pressione `Enter` quando o programa solicitar para avançar para a próxima etapa.

*Este exercício é excelente para consolidar o entendimento básico sobre iterações matemáticas no Python!*
