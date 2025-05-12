Métodos utilizados durante o funcionamento da aplicação para o processamento de dados e geração de respostas ao usuário.

A solução desenvolvida para o problema foi pensada em etapas e os méttodos organizados como tal. O raciocínio para o funcionamento da aplicação é:
    Passo 0 -> Montar, manualmente, os datasets utilizadas pela aplicação de acordo com os PPDs dos cursos de computação (CCO, SIN, ECO). A modelagem do dataset deverá incluir diversas informações pertinentes sobre cada matéria, estas sendo:
        >Período pretendido para realização;
        >Anual;
        >Sigla;
        >Categoria (Obrigatória, Optativa, Equivalente);
        >Carga Horária;
        >Nome;
        >Pré Requisitos;
        >Horários;
        >Equivalentes;
        >Curso.

    1° Passo -> Receber como input do usuário o seu histórico em forma de um arquivo pdf, pelo qual obter-se-á as matérias já concluídas e o curso do usuário. Deverá requisitar, também, um form com as preferências do usuário quanto às matérias optativas.

    2° Passo -> Instanciar um grafo simples com as informações do dataset pertinente ao curso do usuário obtido no primeiro passo. Em seguida, serão calculados os pesos de cada vértice (matéria) fazendo-se o uso de uma BFS inversa, ou seja, do maior nó (ou mais à direita, levando em conta a visualização do grafo como o diagrama de matérias do PPD) ao menor (mais à esquerda). Durante esse percurso, cada vértice acumulará os pesos dos vértices antecessores na sequência - dessa forma as matérias que travam mais matérias e estão mais ao início do curso possuem prioridade. Alguns outros fatores também irão influenciar o resultado final do peso, como a Categoria e Anualidade.

    3° Passo -> Filtrar o dataset utilizado, removendo dele todas as matérias obsoletas para o caso de uso. A ordem de remoção é:
        1°>Matérias que não estão sendo ofertadas;
        2°>Matérias já concluídas pelo usuário;
        3°>Matérias cujos pré requisitos não foram atendidos.
    Enfim, criar um novo grafo dirigido apenas com as matérias restantes.

    4° Passo -> Colorir os vértices do grafo instanciado no terceiro passo com base nos horários da matérias. Para cada matéria, poder-se-á atribuir múltiplas cores caso apresente horários variados para cada dia da semana. Será atribuída uma cor a cada horário presente no grafo.

    5° Passo -> Adicionar arestas dirigidas entres os vértices, seguindo a ordem do maior peso ao menor, criando-se um trajeto que representa uma possível recomendação de matérias ao usuário. Para poder recomendar múltiplas soluções, deve-se calcular os conflitos de horário de cada matéria e remover um dos vértices com maior conflito, um por um, de forma descendente, gerando um novo trajeto para cada remoção. Calcular até 4 soluções. Para cada trajeto produzido, um grafo dirigido, será necessário criar uma lista de adjacência, e as arestas do grafo removidas para o cálculo da próxima solução.

    6° Passo -> A partir das listas de adjacência geradas no quinto passo, utilizar de uma DFS para percorrer os trajetos e retornar as recomendações ao usuário.

    Passo Opcional -> Caso a carga horária de uma solução esteja abaixo de um valor definido arbitráriamente, realizar o processamento para as optativas e recomendar matérias optativas até o limite da carga horária recomendada. Este processamento é idêntico ao realizado para obrigatórias, porém o cálculo dos pesos também levará em conta as preferências do usuário obtidas no primeiro passo.

    