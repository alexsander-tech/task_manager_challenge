# Gerenciador de Lista de Tarefas

Após concluir um curso de Python Básico pela fundação Bradesco, decidi colocar os conhecimentos adquiridos à prática, para assim fixá-los melhor em minha memória, para isso me aliei a uma **IA** 😱. Pedi ao Gemini que me desafiasse para testar tudo aquilo que recém havia aprendido, mas mal sabia eu que minha criatividade me levaria à ambientes, até então, desconhecidos por minha pessoa, durante o processo surgiam ideias que todo aquele conteúdo que eu havia absorvido jamais seriam capaz de tornar realidade, abaixo irei detalhar melhor todo esse processo!

## O Desafio

Este foi o segundo desafio proposto pelo Gemini, criar uma simples lista de tarefas interativa.

Abaixo o desafio:

Gemini: 

*"Excelente! Vamos subir o nível. Trabalhar com listas e funções vai te dar superpoderes, pois você deixará de escrever códigos que "morrem" quando terminam e passará a criar ferramentas que manipulam dados.*

*📝 O Desafio: Gerenciador de Tarefas (To-Do List)*

*Seu objetivo é criar um programa que permita ao usuário gerenciar uma lista de afazeres. O diferencial aqui é que o código deve ser modular (usando funções).*

*Estrutura do Desafio:*

*Crie uma lista vazia chamada tarefas.*

*Crie três funções principais:*

*adicionar_tarefa(nome): Recebe o nome de uma tarefa e a coloca na lista.*

*listar_tarefas(): Exibe todas as tarefas numeradas (ex: 1. Lavar louça). Se a lista estiver vazia, avise ao usuário.*

*remover_tarefa(indice): Remove a tarefa da lista baseada no número dela.*

*Crie um menu interativo (usando while True) que permita ao usuário escolher qual dessas ações quer realizar ou se deseja sair do programa."*

## O Processo
### Etapa 1 (Preparar o ambiente)

A partir deste momento, comecei de fato o desafio preparando a estrutura do meu código, criando a lista e as funções que até então permaneciam vazias, em seguida dei inicio a criação do "Menu interativo". Foi nesse momento que utilizei do "if", "elif" e "else" para criar uma forma de chamar minhas funções (ainda vazias), utilizando uma variavel que recebia inputs de números inteiros e logo em seguida comparando a resposta da variavel com os números que deveriam chamar a função correspondente (1. Adicionar | 2. Remover | 3. Listar | 4. Sair ).

### Etapa 2 (Lista e Funções Funcionais?)

Foi nessa etapa onde eu percebi que o buraco seria mais baixo.
De primeira instância tentei fazer a função que adcionaria itens na lista, funcionar, porém durante este processo percebi que eu não tinha entendido tão bem quanto acreditava, como colocar em prática tudo aquilo que aprendi sobre a manipulação de listas. Por mais simples que a keyword "append" fosse, a parte dos parâmetros e de chamar a função acabou me deixando bem confuso e eu simplesmente não conseguia fazer funcionar da forma como eu queria, toda hora que rodava meu script parecia que meu terminal havia sido atacado era sangue para todo lado (erros em vermelho), então naquele instante percebi que não adiantava eu ficar batendo minha cabeça contra parede, e decidi dar uma pausa, não para descansar, e sim para estudar e pesquisar como fazer aquilo funcionar, e depois de um breve intervalo, voltei, dessa vez mais confiante, sentindo que de fato sabia o que eu ia fazer, e dessa vez, pasmem, o terminal não sangrou, então parecia que tudo havia dado certo, porém, não conseguia obter uma confirmação, pois a função que listaria os itens adcionados ainda não estava funcional, e foi ai que decidi qual era o próximo passo, conseguir exibir a minha lista, nesse momento minha criatividade e perfeccionismo despertaram, eu até sabia uma forma de listar mas ela não era bem o que eu queria, então mais uma vez parei para pesquisar e explorar as possibilidades que o Python me proporcionava e foi ai que o remédio para minhas dores de cabeça aparecereu, a keyword "enumerate", que me permitia exibir minha lista já numerada de maneira automática. Nesse ponto, 66% do desafio original já estava pronto e funcional e só faltava colocar a opção para remover itens da lista de tarefas, o que de novo, acabou sendo mais dificel do que eu esperava, mas no fim cheguei em um resultado satisfatório, certo? **ERRADO!!**, havia chegado ao fim do desafio, mas ainda não estava satisfeito, sentia que meu script era extremamente limitado e tinha uma péssima UX, e foi nesse momento que avancei para a próxima etapa.

### Etapa 3 (Aprimorar o código e mais desafios?!)

Nesse momento percebi que meu código não era útil no dia a dia, pois a partir do momento que eu desligasse meu terminal, tudo aquilo que havia sido listado, se perderia no vazio computacional, além disso ainda havia muita margem para erros, junto com uma péssima experiência para o usuário (eu tinha que adicionar uma tarefa por vez, retornando ao menu inicial toda vez que uma tarefa era adicionada, o mesmo acontecia com a função de remover). Decidi começar a resolver a parte "*Fácil*", que seria diminuir a margem de erro, e de qual erro estou falando? Claro que era o problema clássico de USB (Usuario Super Burro), no meu código havia muitos momentos onde para nevagar entre as interfaces era necessário responder a inputs que solicitavam números inteiros, mas não estava preparado para o caso onde um usuário iria utilizar do seu livre arbítrio para escrever algo como "Adicionar", para tentar acessar o menu de "Adicionar", e foi então que após muita pesquisa acabei conhecendo algumas keywords que resolveriam os problemas do meu programa, sendo elas: try, except, continue, ValueError, IndexError, lower e strip. A partir disso consegui resolver os problemas, mas ainda me restava uma questão, "Meu programa é inútil", precisava descobrir uma forma de salvar esses dados para não perde-los, e após um tempinho pensando, me lembrei que no curso teve um momento onde vimos como criar, editar e ler arquivos .txt utilizando o Python, seguindo desse ponto consegui chegar em uma quarta função no meu código, a função "Imprimir", que gera ou edita um arquivo txt com a nossa lista de tarefas.

### Etapa 4 (Fim?????)

Finalmente me dei por satisfeito, mas isso é só um começo e estou bem longe do fim, posso até estar satisfeito com o resultado alcançado com os meus conhecimentos atuais, mas pretendo no futuro voltar aqui e melhorar esse "Gerenciador de Lista de Tarefas". Nesse projeto eu aprendi muito mais do que eu esperava, acredito que até mais do que em um projeto pré-criado e guiado de algum curso online qualquer, estou muito feliz por ter chego até aqui, em um primeiro momento até fiquei com vergonha de upar isso no GitHub por conta da "simplicidade" do projeto, e sinceramente nem acho que alguém vá ler até aqui, mas sinto que eu precisava registrar minha curva de aprendizado por aqui, se não para os outros, por mim mesmo!

Agradeço você, que chegou até aqui!