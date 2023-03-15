# Runnare lo script ogni 5 min con crontab
# crontab -e
# */5 * * * * /path/to/script.sh

#!/bin/bash

# Definisci il nome del tuo bucket
BUCKET_NAME="prog1b"

# Definisci il percorso dove vuoi salvare il file
LOCAL_DIRECTORY="/var/www/html"

# Definisci il nome del file che vuoi scaricare
FILE_NAME="index.html"

# Inizializza la variabile per il controllo del timestamp dell'ultimo download
LAST_MODIFIED_TIME=0

    # Recupera la data di ultima modifica del file
    OBJECT_LAST_MODIFIED_TIME=$(aws s3api head-object --bucket $BUCKET_NAME --key $FILE_NAME --query 'LastModified' --output text)

    # Confronta la data di ultima modifica del file con quella dell'ultimo download
    if [[ $(date -d "$OBJECT_LAST_MODIFIED_TIME" +%s) -gt $LAST_MODIFIED_TIME ]]; then
        # Scarica il file dal bucket
        aws s3 cp s3://$BUCKET_NAME/$FILE_NAME $LOCAL_DIRECTORY/$FILE_NAME

        # Aggiorna il timestamp dell'ultimo download
        LAST_MODIFIED_TIME=$(date -d "$OBJECT_LAST_MODIFIED_TIME" +%s)
    fi
