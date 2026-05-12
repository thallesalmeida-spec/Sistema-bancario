# Comparativo Técnico: C++ vs. Python (Sistema Bancário)

Este documento descreve as principais diferenças de implementação e abstração entre o código original em C++ e a nova versão em Python, focando em como os conceitos de um foram traduzidos para o outro.

## 1. Gerenciamento de Memória e Estruturas de Dados

### C++ (Vetores Dinâmicos Manuais)
No código C++, o gerenciamento de contas no `banco.cpp` era feito manualmente usando ponteiros e alocação dinâmica:
- **Uso de `new` e `delete[]`**: Para adicionar ou remover uma conta, era necessário criar um novo array, copiar os dados do antigo e deletar a memória anterior.
- **Risco**: Exige cuidado extremo com *memory leaks* (resolvido com o destruidor `~Banco()`).

### Python (Listas Dinâmicas)
Em Python, a classe `list` é inerentemente dinâmica e otimizada:
- **Uso de `.append()` e `.remove()`**: O Python gerencia o redimensionamento do array e a limpeza da memória (Garbage Collection) automaticamente.
- **Abstração**: O desenvolvedor foca na lógica de negócio em vez da manipulação de endereços de memória.

---

## 2. Encapsulamento e Visibilidade

### C++ (Modificadores de Acesso)
- **`private` / `public`**: A linguagem impõe restrições rígidas. Atributos privados não podem ser acessados fora da classe, exigindo métodos `get` e `set`.
- **Headers (`.h`)**: Separação clara entre a interface (assinaturas) e a implementação (`.cpp`).

### Python (Convenções de Nomenclatura)
- **`_atributo` (Underscore)**: Em Python, não existe "privado" real por imposição da linguagem. Usa-se o prefixo `_` para indicar que um atributo é de uso interno (convenção).
- **Módulos**: A separação ocorre por arquivos `.py`, que funcionam como namespaces. Não há necessidade de arquivos de cabeçalho.

---

## 3. Tipagem e Segurança

### C++ (Tipagem Estática)
- Todas as variáveis devem ter tipos declarados (`int`, `double`, `std::string`).
- Erros de tipo são capturados em tempo de compilação.
- O uso de `status.h` com `#define` cria constantes globais de pré-processamento.

### Python (Tipagem Dinâmica)
- Variáveis são referências a objetos e não precisam de tipo declarado.
- Erros de tipo ocorrem em tempo de execução.
- As constantes em `status.py` são variáveis de módulo, mantendo a semântica mas com tipagem flexível.

---

## 4. Entrada/Saída e Tratamento de Erros

### C++ (`std::cin` / `std::cout`)
- O `cin` pode entrar em estado de erro se receber um tipo inesperado (ex: string em um `int`), exigindo `cin.clear()` e `cin.ignore()`.
- O código original não tratava exaustivamente entradas inválidas.

### Python (`input()` / `try-except`)
- O Python lê tudo como string, exigindo conversão explícita (`int()`, `float()`).
- **Robustez**: Na versão Python, foi implementado o bloco `try-except ValueError` para garantir que o programa não aborte caso o usuário digite caracteres inválidos nos menus.

---

## 5. Estrutura de Classes (Boilerplate)

### C++
- Necessita de construtores, destruidores (especialmente para limpeza de ponteiros) e muitas vezes o "Big Three" (construtor de cópia, atribuição, destruidor).

### Python
- O método `__init__` funciona como construtor.
- O parâmetro `self` deve ser explicitamente declarado em todos os métodos de instância, ao contrário do `this->` implícito/opcional do C++.

---

## Conclusão
Enquanto o **C++** oferece controle total sobre a máquina e eficiência de memória (ideal para sistemas de baixa latência), o **Python** prioriza a velocidade de desenvolvimento e legibilidade do código, abstraindo a complexidade da infraestrutura. O nível de abstração no Python é mais alto, permitindo que a mesma lógica do sistema bancário seja expressa de forma mais concisa.

