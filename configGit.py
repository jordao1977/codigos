'Git Cloud

Git Desktop

Download do aplicativo Git (http://git-scm.com/downloads)
Para baixar o Git Desktop

Despois de baixar
Obs: na instalação selecionar a terceira opção no Adjusting your Path, com isso teremos  o comandos do Unix habilitados, para fazer no CMD.

Depois disto criar um para no seu computador para linkcar com git cloud.

Depois de criar o Repositório Git Cloud .

No repositório que desejamos subir os arquivos temos que pegar o link lá na pasta

A estrutura o link 

Exemplo: https://github.com/Ls2m/DataSciense.git
https://github.com/ ----- link do site Git
Ls2m/ ---- Usuário do Git
/DataSciense.git – Repositório do Git

Para linkar meus arquivos do meu computador com a Repositório tem que copiar o link completo. 

https://github.com/Ls2m/DataSciense.git


CMD GIt
Acessar o git Bash

Raiz https://github.com/jordao1977/” nameNewRepositorio”

Para linkar o novo repositório.
Acessar o git Bash
git config --global user.name ”jordao1977”
git config --global user.email “jordaomarcio62@gmail.com”
git clone https://github.com/jordao1977/codigos.git

Depois para apontar a pastar para monitoramento.

Temos que acessar a pasta cd “nome da pasta” exemplo cd codigos


git add Git_Cloud.docx  ---- para enviar o arquivo 
git commit -m “20210820 novo” Git_Cloud.docx   -- para commitar
git push –u origin main 

'