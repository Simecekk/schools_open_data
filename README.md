# schools_open_data
Django applikace pro rozdělení a validování dat z https://data.msmt.cz/dataset/rejstrik-skol-a-skolskych-zarizeni-cela-cr

Pro validaci dat používám ares_util

viz: https://github.com/illagrenan/ares_util

Po naklonování a zmigrování modelu School stačí pouze zadat příkaz: 

python manage.py collect_school_data --> Uloží všechny školy do DB bez validace

python manage.py collect_school_data --validate --> Uloží všechny školy do DB s validací (trvá dlouho)

Applikace obsahuje jedno view pro zobrazení dat.

http://127.0.0.1:8000/schools/data/ --> Zobrazí prvních 10 škol

http://127.0.0.1:8000/schools/data/?number=(x) --> Zobraz prních X škol
