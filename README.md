# Código de exemplo para estudo de caso de IoT + Bigdata
# Leia útimo aviso!


## Links úteis

- [Documentação PyCom](https://docs.pycom.io)
- [Repositório com libs pycom](https://github.com/pycom/pycom-libraries)
- [Tutorial básico GIT](https://rogerdudler.github.io/git-guide/index.pt_BR.html)
- [VS Code](https://code.visualstudio.com)
- [Google Colab](https://colab.research.google.com)
- [Anaconda](https://www.anaconda.com/distribution/)
- [MQTTBox](http://workswithweb.com/mqttbox.html)
- [Robot 3T](https://robomongo.org/download)

## Comandos

- Comandos basicos:

`
cd --> acessa a pasta
cd .. --> voltar para a pasta anterior
ls --> lista as pastas


- Para subir os containers `sudo docker-compose up -d`
- Criar o ambiente virtual: 
``
cd in242/
virtualenv -p python3.7 env
``
- Para habilitar o venv: `source env/bin/activate`
- Para iiiiinstalar as libs: `(env) pip install -r requirements.txt`
- Para sair do env: `deactivate`
- Para rodar o producer: `(env) python producer/producer.py`
- Para rodar o consumer: `(env) python consumer/consumer.py`
- Para rodar o jupyter: `(env) jupyter notebook`

## Projeto da disciplina

1. Instalar o MQTT e Mongo usando AWS e deixar disponivel publicamente.
2. Usar o producer e consumer para gerar a cada segundo 1h de dado de temperatura (15~30o) enviando para o MQTT e armazenando no Mongo.
3. Consumir o resultado do Mongo e salvar em CSV/XLS.
4. Fazer a analise dos dados do CSV em um notebook (media, minuto com a maior media, dv)
5. Subir o codigo, arquivos do docker, notebook e csv no github.
6. Enviar o link para lucio.oliveira@inatel.br ate o dia 5/11


ATENÇÃO:
Professor, existe uma instância do jupiter radando em meu aws, peço acessa-la pelo seguinte link:

https://ec2-18-228-116-164.sa-east-1.compute.amazonaws.com:8888/tree/notebooks

Desde já, agradeço!

.
