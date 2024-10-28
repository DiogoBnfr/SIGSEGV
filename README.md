# SIGSEGV
Repositório oficial do blog da SIGSEGV

# Ambiente completo
Nesse tópico será passado um passo a passo da preparação de ambiente para executar a aplicação do nosso blog

## Clonar repositório
Um simples git clone irá automáticamente clonar os repositórios do front e backend do blog em duas pastas diferentes mas no mesmo diretório

```
git clone https://github.com/DiogoBnfr/sigsegv.git
```

## Configuração da API
Nesse tópico será descrita a configuração completa para o backend

Pressupomos que já tenha as sequintes dependências:
1. python3.8+

Depois de garantir as dependências instaladas:

### 1. Crie um virtual enriroment com o python:
isso irá criar uma pasta com o ambiente virtual

```
cd sigsegv/
python3 -m venv venv
```

em seguida você deve ativar esse ambiente usando:

```
source venv/bin/activate
```

isso fará com que o interpretador usado seja o do virtual enriroment. Dentro dele use o:

```
pip install -r require.txt
```

isso baixará os pacotes python necessários apenas dentro do ambiente virtual

### 2. Pronto!
Seu ambiente já está pronto para execução, apenas rode o comando:

```
fastapi dev main
```
