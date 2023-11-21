# O Projeto

Projeto desenvolvido para o seminário de Frameworks da matéria de Engenharia de Software (C214).
A atividade consiste em apresentar alguns testes de unidade feitos com uma ferramenta de testes, a qual, para nosso grupo foi a Pytest. Para isso desenvolvemos uma simples calculadora em python.

# Equipe

- Guilherme Henrique Ribeiro Martins de Oliveira
- Gustavo Ramos Lages Torres
- Leonardo Liberato Jóia Ribeiro

# Instalação

## Python

### Windows

#### Download:

Baixe o instalador MSI do <a href="https://www.python.org/downloads/" >site oficial do Python</a> e execute o instalador.

### PIP

Para instalar o Pytest é preciso ter em sua máquina o PIP, gerenciador de pacotes do Python.
Normalmente, o PIP é instalado automaticamente quando você instala a partir do site oficial.

### Verificar a instalação 

Para verificar se o Python e o PIP foi instalado corretamente abra um terminal e execute o comando:
```bash
python --version
```

```bash
pip --version
```

Você sera capaz de ver a versão de ambos instalados.

### Visual Studio Code

- Baixe e instale <a href="https://code.visualstudio.com/download">Visual Studio Code</a>
- Inicie o Visual Studio Code e vá para 'Extensions'. Procure por Python e baixe a extensão.

### Pytest

Para fazer a instalação do Pytest abra um terminal e execute o comando:
```bash
pip install -U pytest
```

### Verificar a instalação 

Para verificar se o Pytest foi instalado corretamente abra um terminal e execute o comando:
```bash
pytest --version
```

# Execução

### Instalação das depedencias

Para instalação das dependencias do projeto basta rodar
```bash
pip install -r requirements.txt
```

### Clonando o projeto

Agora é hora de baixar o projeto e poder testar um pouco dessa ferramenta de testes.

Com o terminal ainda aberto, navegue até a pasta onde deseja salvar o projeto e cole o seguinte comando:

```bash
git clone https://github.com/guilhermexd11/Seminario_Pytest_C214.git
```

### Comandos de teste

Para realização dos testes, 3 comandos podem ser feitos:
Rodar todos os arquivos de teste
```bash
pytest
```

Rodar um arquivo de teste específico
```bash
pytest nome_do_arquivo.py
```
