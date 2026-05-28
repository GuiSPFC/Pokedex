# 👾 Pokedex em CLI (Interface de Linha de Comando)

Este é um programa interativo em Python executado diretamente no terminal para gerenciar uma Pokedex pessoal e o histórico de capturas de Pokémon. O projeto foca em lógica de programação pura, manipulação de estruturas de dados nativas e controle de fluxo.

## 🚀 Conceitos de Python Aplicados

*   **Dicionários (`dict`):** Utilizados para armazenar os Pokémon como chaves únicas, garantindo busca rápida O(1) e o vínculo com sub-dicionários contendo as propriedades `Tipo` e `Nivel`.
*   **Listas de Dicionários (`list[dict]`):** Aplicação de listas para estruturar e acumular de forma cronológica o histórico de capturas.
*   **Modularização (Funções):** Código totalmente dividido em funções específicas (`def`) para cada responsabilidade do sistema, seguindo boas práticas de organização.
*   **Controle de Fluxo e Loops:** Uso de estruturas condicionais (`if/elif/else`) e um loop infinito (`while True`) com interrupção controlada (`break`) para o menu dinâmico.
*   **Tratamento de Ordenação:** Uso da função nativa `sorted()` para exibir os registros da Pokedex em ordem alfabética.

## 🎮 Funcionalidades do Sistema

1. **Adicionar Pokémon:** Registra um novo monstrinho validando se ele já existe na base e aplicando uma regra de negócio que impede níveis superiores a 100.
2. **Listar Pokedex:** Exibe todos os Pokémon cadastrados organizados em ordem alfabética pelo nome.
3. **Remover Pokémon:** Exclui um registro da Pokedex com base no nome inserido.
4. **Registrar Captura:** Permite salvar um evento de captura associando o contador de vezes que aquele Pokémon específico foi pego.
5. **Histórico de Capturas:** Mostra uma listagem em ordem cronológica de todos os registros de capturas efetuados.
6. **Atualizar Nível:** Altera dinamicamente o nível de um Pokémon já existente no banco de dados em memória.

## 🔧 Como Executar o Projeto

### Pré-requisitos
*   Apenas o Python instalado (versão 3.x recomendada). Não é necessária a instalação de nenhuma biblioteca externa.

### Passo a Passo

1. **Clone ou baixe o arquivo do código:**
   ```bash
   git clone https://github.com
   cd NOME_DO_REPOSITORIO_POKEDEX
   ```

2. **Execute o script pelo terminal:**
   ```bash
   python nome_do_arquivo.py
   ```

3. **Utilize o menu interativo** digitando os números de 1 a 7 para navegar pelas funções do sistema.
