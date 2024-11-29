
---

# Projeto de Pipeline ETL com Apache Airflow

Este projeto contém um pipeline de ETL (Extração, Transformação e Carga) utilizando o **Apache Airflow** para automação de tarefas. O pipeline coleta dados meteorológicos e realiza algumas transformações, armazenando as informações para posterior análise.

## Pré-requisitos

Antes de começar, é necessário ter o seguinte instalado no seu ambiente:

- **Python 3.x** (recomendado Python 3.7 ou superior)
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)
- **Apache Airflow** (para orquestrar as tarefas)

## Passos para Instalação

### 1. **Clone o repositório**

Clone o repositório do projeto para o seu ambiente local:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. **Crie um ambiente virtual (virtualenv)**

Recomenda-se usar um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando para criar e ativar o ambiente:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
```

### 3. **Instale as dependências do projeto**

Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Se estiver tendo problemas com a instalação do Apache Airflow, use o comando abaixo para instalar uma versão específica com as dependências adequadas para Python 3.7 (ou a versão que você está utilizando):

```bash
pip install apache-airflow==2.7.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.7.txt"
```

### 4. **Inicialize o banco de dados do Airflow**

O Airflow usa um banco de dados para armazenar o estado das tarefas e outros metadados. Para inicializar o banco de dados, execute o seguinte comando:

```bash
airflow db init
```

### 5. **Crie o usuário admin do Airflow**

Para acessar a interface web do Airflow, você precisa criar um usuário administrador. Execute o comando abaixo para criar um usuário com privilégios de administrador:

```bash
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --email admin@example.com \
    --role Admin \
    --password admin
```

### 6. **Inicie o servidor web do Airflow**

Agora, inicie o servidor web para acessar a interface do Airflow no navegador. O servidor será iniciado na porta `8080`:

```bash
airflow webserver --port 8080
```

Acesse a interface web através de [http://localhost:8080](http://localhost:8080).

### 7. **Inicie o Scheduler do Airflow**

Em um terminal separado, inicie o scheduler do Airflow, que é responsável por executar os DAGs (grafos acíclicos dirigidos) conforme a programação:

```bash
airflow scheduler
```

### 8. **Verifique a interface do Airflow**

Agora, abra o navegador e vá para a interface web do Airflow em [http://localhost:8080](http://localhost:8080). Você deve ser capaz de ver seus DAGs e monitorar a execução das tarefas.

---

## Executando o Pipeline ETL

### 1. **Definindo os DAGs**

Os DAGs (Directed Acyclic Graphs) são os fluxos de trabalho definidos no Airflow. Os arquivos de definição dos DAGs estão na pasta `dags/`.

### 2. **Executando manualmente um DAG**

Se quiser executar manualmente um DAG, acesse a interface web do Airflow, clique no DAG desejado e, em seguida, clique no botão "Trigger DAG".

### 3. **Verificando os logs**

O Airflow gera logs detalhados para cada tarefa executada. Se uma tarefa falhar ou você quiser revisar a execução, basta clicar no DAG e na tarefa desejada para ver o log correspondente.

---

## Testando o Sistema

Para testar o pipeline localmente, siga os passos abaixo:

1. **Execute o pipeline manualmente** clicando no botão de "Trigger" na interface web do Airflow.
2. **Verifique os logs** de execução das tarefas para garantir que a extração, transformação e carga dos dados estejam funcionando corretamente.
3. **Monitore o progresso** das tarefas através da interface web.

---

## Estrutura do Projeto

```
weather_etl_project/
│
├── dags/
│   └── weather_etl_dag.py        # Arquivo principal com o DAG do pipeline
│
├── scripts/
│   ├── extract_weather.py        # Script de extração de dados
│   ├── transform_weather.py      # Script de transformação dos dados
│   └── load_weather.py           # Script de carga dos dados
│
├── config/
│   └── settings.py               # Configurações da API e outros parâmetros
│
├── requirements.txt              # Arquivo com as dependências do projeto
│
└── README.md                    # Este arquivo
```

---

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma branch para a sua modificação (`git checkout -b feature/nome-da-sua-feature`).
3. Faça as suas mudanças e commit (`git commit -am 'Adicionando uma nova feature'`).
4. Envie para o seu fork (`git push origin feature/nome-da-sua-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
