# Django Uploader

Aplicação de exemplo para integrar o plugin _jQuery-File-Uploader_ _procurar o
link_ em aplicações Django.

Sim, eu sei que existe já existe uma iniciativa neste sentido, a _procurar a
referência_, porém, eu gostaria de aprender do zero, e criar algo no estilo
faça do zero, ao invés de mostrar algo já pronto.

## Preparando o ambiente

### Ambiente virtual do Python

Eu sempre uso o `virtualenvwrapper`, para instalá-lo:

```shell
# pip install virtualenvwrapper
```

Com o `virtualenvwrapper` instalado, é interessante definir em qual diretório
ficarão os ambientes virtuais e os projetos:

```shell
$ export WORKON_HOME=$HOME/.venv
$ export PROJECT_HOME=$HOME/public
$ source /usr/local/bin/virtualenvwrapper.sh
```

### Dependências do sistema operacional

Para trabalhar com imagens e usar o `ImageField`, utilizaremos a biblioteca
`Pillow`. Dada esta dependência é necessário instalar algumas novas bibliotecas
no sistema operacional, para que seja possível compilá-la.

```shell
# sudo apt-get install python-dev python-setuptools
```

Com o cabeçalho de desenvolvimento do Python instalado, é possível instalar as
bibliotecas para manipulação dos diferentes formatos de imagem.

```shell
# sudo apt-get install libtiff4-dev
# sudo apt-get install libjpeg8-dev
# sudo apt-get install zlib1g-dev
# sudo apt-get install libfreetype6-dev
# sudo apt-get install liblcms1-dev
# sudo apt-get install libwebp-dev
# sudo apt-get install tcl8.5-dev tk8.5-dev
```

Para instalar todas de uma vez, use o comando a seguir:

```shell
# sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev tcl8.5-dev tk8.5-dev
```

## Instalando o projeto

Primeiramente crie o ambiente virtual:

```shell
$ mkvirtualenv django_uploader
```

Após criar o ambiente, clone o projeto:

```shell
$ git clone _não sei o endereço do repositório_
```

Com o projeto e o ambiente virtual criados, é interessante ligar ambos:

```shell
$ setvirtualenvproject $WORKON_HOME/django_uploader $PROJECT_HOME/django_uploader
```

### Instalando as dependências

As dependências podem ser instaladas usando:

```shell
$ make deps
```

### Preparando o banco de dados

O banco de dados precisa ser inicializado usando os comandos:

```shell
$ make run cmd=syncdb
$ make run cmd=migrate
```

## Iniciando a aplicação

Para servir a aplicação rode o comando:

```shell
$ make runserver
```
