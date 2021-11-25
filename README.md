# InnoPro
Innovation project in MTELSYS

Norwegian project description:
Vi gir publikum på NRKs live innspillinger en ny måte å interagere med programmet, som ikke går negativt utover selve innspillingen.
I velkomstmailen får publikum en lenke til en spørreundersøkelse, hvor de kan stille spørsmål til eller utfordre programledere og gjester.
Godkjente spørsmål blir så presentert for publikum i en arkademaskin, hvor de kan stemme frem de beste.
De mest populære blir med i studio, men ikke nødvendigvis sendingen. Programleder har selvsagt siste ordet. 

Målet med vårt prosjekt er å gi publikum en ny mulighet til å delta aktivt og få en mer eksklusiv opplevelse, samtidig som den tomme foajeen blir litt mer livlig og innholdsrik.

Technical info:
This is a Django-server, you must install django and python for it to run.
In order for the server to function you must change the absolute path to static in the python file "webkurs/elsysapp/questions.py" to fit your system.
You must also edit the secret key in  "webkurs/webkurs/settings.py" and preferably turn off debug in the same file.
Due to creator inexperience, you will have to follow some instructions for cookies to work properly, these instructions will be shown where necessary.
