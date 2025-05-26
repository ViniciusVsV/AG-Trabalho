Métodos utilizados durante o funcionamento da aplicação para o processamento de dados e geração de respostas ao usuário.

A solução desenvolvida para o problema foi pensada em etapas e os méttodos organizados como tal. O raciocínio para o funcionamento da aplicação é:
    Passo 0 -> Montar, manualmente, os datasets utilizadas pela aplicação de acordo com os PPDs dos cursos de computação (CCO, SIN, ECO). A modelagem do dataset deverá incluir diversas informações pertinentes sobre cada matéria, estas sendo:
        >Sigla;
        >Nome;
        >Curso;
        >Categoria (Obrigatória, Optativa, Equivalente);
        >Nome;
        >Período;
        >Horários;
        >Carga Horária;
        >Pré-Requisitos.

    1° Passo -> Receber como input do usuário o seu histórico em forma de um arquivo pdf, pelo qual obter-se-á as matérias já concluídas e o curso do usuário. Deverá requisitar, também, um form com as preferências do usuário quanto às matérias optativas e aos horários do dia preferidos.

    2° Passo -> Instanciar um grafo dirigido com as informações do dataset pertinente ao curso do usuário obtido no primeiro passo. As arestas desse grafo irão representar as relações de dependência (pré-requisitos) entre as disciplinas. As arestas também serão instanciadas de forma inversa, isto é, uma matéria que atua como pré-requisito ira apontar às matérias que a requerem.
    
    3° Passo -> Calcular os pesos de cada vértice (matéria) fazendo-se o uso de uma BFS inversa, ou seja, do maior nó (ou mais à direita, levando em conta a visualização do grafo como o diagrama de matérias do PPD) ao menor (mais à esquerda). Durante esse percurso, cada vértice acumulará os pesos dos vértices antecessores na sequência - dessa forma as matérias que travam mais matérias e estão mais ao início do curso possuem prioridade. Alguns outros fatores também irão influenciar o resultado final do peso, como a Categoria e Anualidade.

    4° Passo -> Filtrar o dataset utilizado, removendo dele todas as matérias obsoletas para o caso de uso. A ordem de remoção é:
        1°>Matérias que não estão sendo ofertadas;
        2°>Matérias já concluídas pelo usuário;
        3°>Matérias cujos pré requisitos não foram atendidos.

    5° Passo -> Montar um novo grafo simples a partir das matérias restantes do dataset. As arestas desse novo grafo irão representar matérias que possuem conflitos de horários entre si.

    6° Passo -> Calcular os Conjuntos Independentes Máximos do grafo simples. Também ter como base parâmetros passados pelo usuário, como limite de carga semestral e horários preferidos. Retornar, então, os conjuntos máximos encontrados, como no máximo 5.

LeHistorico.py -> InstanciaGrafoDirigido.py -> CalculaPesos.py -> FiltaDataframe.py -> matrizAdjSimples.py -> CalculaCIM.py