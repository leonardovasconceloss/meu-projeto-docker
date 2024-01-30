# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app-flaskpy

# Copiar o arquivo de dependências para o diretório atual
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o conteúdo local para o diretório de trabalho no contêiner
COPY . .

# Definir a variável de ambiente para executar a aplicação em modo de produção
ENV FLASK_ENV=production

# Comando para executar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

