# Usa una immagine di base
FROM python:3.7

# Copia il codice sorgente nella directory /app
COPY . /app

# Imposta la directory di lavoro come /app
WORKDIR /app

# Installa le dipendenze richieste
RUN pip install -r requirements.txt

# Espone la porta 80
EXPOSE 80

# Avvia il tuo script
CMD [ "python", "script.py" ]
