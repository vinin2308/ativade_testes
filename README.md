### Criar VirtualEnv

1. Você já deve ter o python instalado;
2. As variáveis de ambiente do python já devem ser criadas;
3. Onde geralmente o python fica instaldo?

~~~shell
C:\Users\{seuusuario}\AppData\Local\Programs\Python\Python38-32 C:\Users\{seuusuario}\AppData\Local\Programs\Python\Python38-32\Scripts
~~~

4. Você deve instalar o pacote virtualenv na instalação global do python:

~~~shell 
pip install virtualenv
~~~

5. Executar o comando para criação da virtualenc:

~~~shell 
python -m venv c:\virtualenv\sfc-station
~~~ 

6 - Ativar virtualenv:

~~~shell 
c:\virtualenv\sfc-station\Scripts\activate.bat
~~~

### Instalar pytest

~~~shell
pip install -r requirements.txt
~~~
