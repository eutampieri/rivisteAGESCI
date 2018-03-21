# Tool per lo scaricamento delle riviste AGESCI

Questo strumento serve a scaricare le riviste pubblicate dall'[AGESCI](https://agesci.it) (Associazione Guide E Scout Cattolici Italiani).

Le riviste supportate sono:

* Scout Giochiamo, attraverso il programma `giochiamo.py`
* Scout Avventura, attraverso il programma `avventura.py`
* Scout Camminiamo Insieme, attraverso il programma `insieme.py`

## Utilizzo

Ogni programma, quando avviato, chiede da quale anno a quale anno si vuole scaricare e fa partire lo scaricamento, che avviene nella directory in cui si trova il codice sorgente.

## Prerequisiti

* [Requests](http://docs.python-requests.org/en/master/)
* [lxml](http://lxml.de)
