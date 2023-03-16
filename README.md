# Data recovery from .csv files and analysis


Questo progetto è stato creato per raccogliere e analizzare dati relativi all'e-commerce. La repository contiene gli script necessari per configurare un'infrastruttura di analisi dati su AWS utilizzando servizi come EC2, S3 e Redshift.

## Struttura della repository
La repository è organizzata come segue:

conf/: contiene i file di configurazione per l'infrastruttura (e.g. file di configurazione Docker).
data/: contiene i dati di esempio che verranno caricati su S3 e successivamente elaborati su Redshift.
scripts/: contiene gli script di configurazione dell'infrastruttura e gli script di analisi dei dati.

## Requisiti
Per utilizzare questo progetto è necessario disporre dei seguenti requisiti:

Un account AWS con le autorizzazioni necessarie per configurare l'infrastruttura descritta nella repository.
Python 3.6 o superiore con le librerie boto3 e psycopg2 installate per eseguire gli script di configurazione e di analisi dei dati.
Utilizzo
Per utilizzare questo progetto, seguire i seguenti passaggi:

Clonare la repository.
Configurare l'infrastruttura su AWS eseguendo gli script di configurazione nella directory scripts/. Per eseguire gli script, assicurarsi di avere configurato le credenziali di accesso ad AWS e le variabili d'ambiente necessarie.
Caricare i dati di esempio nella directory data/ su S3.
Eseguire gli script di analisi dei dati nella directory scripts/ per elaborare i dati su Redshift e produrre report statistici.

## Crediti
Il progetto è stato creato da M. Gandelli, M. Genovese, S. Ciafartini, A. Luvoni e P. Laganà come parte di un'attività di formazione per DevOps su AWS.
