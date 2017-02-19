"""
Casus 'ICT in de zorg'
Blok 2

Tawwab Djalielie

ICT-1
ZUYD Hogeschool
27-01-2016
"""


import time, csv, random


def main():
    
    """ Hoofdfunctie van het programma.

        De variabele terminate wordt gebruikt om te zien of de gebruiker het programma wilt afsluiten.
        Als dit zo is, wordt er een melding geprint dat het programma is afgesloten.
    """
    
    terminate = False
    while not terminate:
        kies_patient()
        terminate = keuzemenu(terminate)
        schrijven_domotica()
    print('Het programma is nu afgesloten.')


def kies_patient():
    
    """ Hier wordt het BSN-nummer van de patiënt uitgelezen.

        Dit nummer wordt gebruikt als naam van het CSV-bestand.
    """

    global lijst_patienten, patientnummer, bsn_nummer
    lijst_patienten = lezen_patienten()
    patientnummer = 2
    bsn_nummer = lijst_patienten[int(patientnummer)-1][4]
    

def keuzemenu(terminate):
    
    """ Dit is het menu waar de arts/patiënt een programmaonderdeel kan kiezen.

        Het nummer dat de gebruiker intypt wordt doorgegeven aan de opgeroepen functie. Dit nummer functioneert later als categorie in het CSV-bestand.
        Indien de gebruiker voor 'Q' kiest, wordt de waarde van terminate False. Deze waarde wordt doorgegeven aan main() en er verschijnt een melding
        dat het programma is afgesloten.
    """
    
    print('\nWelkom bij eHealthSysT!\n')
    print('Kies een cijfer of letter van het programmaonderdeel.')
    print('1. Bloedstollingswaardes\n2. Medicijnen\n3. Gemoedstoestand\n4. Voeding\n5. Domotica\n6. Diagnose\n7. Persoonlijke gegevens\nQ. Quit')

    correcte_invoer = False
    while not correcte_invoer:
        menu_keuze = input('\nKeuze: ')
        correcte_invoer = True
        if menu_keuze == '1':
            bloed(menu_keuze)
        elif menu_keuze == '2':
            medicijnen(menu_keuze)
        elif menu_keuze == '3':
            gemoedstoestand(menu_keuze)
        elif menu_keuze == '4':
            voeding(menu_keuze)
        elif menu_keuze == '5':
            domotica(menu_keuze)
        elif menu_keuze == '6':
            menu_keuze = '0'
            diagnose(menu_keuze)
        elif menu_keuze == '7':
            tonen_gegevens()
        elif menu_keuze == 'Q' or menu_keuze == 'q':
            terminate = True
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')
            correcte_invoer = False
    return terminate


def bloed(categorie):
    
    """ Hier kan de gebruiker de bloedstollingswaarde doorgeven.

        Een bloedstollingswaarde wordt uitgedrukt in INR. INR moet tussen 1.0 en 4.0 liggen.
        Bron: http://www.trombosestichting.nl/trombose/behandeling/inr.html
    """

    lijst_csv = lezen_csv(categorie)
    tonen_csv(lijst_csv)
    
    correcte_invoer = False
    while not correcte_invoer:
        bloedstollingswaarde = input('\nGeef een nieuwe bloedstollingswaarde in INR in. \nLaat het veld leeg en druk op enter om de invoer te annuleren. ')
        if bloedstollingswaarde.replace('.', '', 1).isdecimal() and (float(bloedstollingswaarde) >= 1.0 and float(bloedstollingswaarde) <= 4.0):
            print('Weet je zeker dat je bovenstaande bloedstollingswaarde wilt ingeven?')
            bevestiging = input('Typ J om je keuze te bevestigen. Typ iets anders om te annuleren. ') 
            if bevestiging == 'J' or bevestiging == 'j':
                correcte_invoer = True
                bloedstollingswaarde = round(float(bloedstollingswaarde), 2)
                regel = format_regel(bloedstollingswaarde, categorie)
                schrijven_csv(regel)
                print('De bloedstollingswaarde is toegevoegd.')
        elif bloedstollingswaarde == '':
            correcte_invoer = True
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')


def gemoedstoestand(categorie):

    """ Hier kan de gebruiker de gemoedstoestand doorgeven.

        De gemoedstoestand moet minimaal 10 tekens en maximaal 300 tekens zijn. 
    """

    lijst_csv = lezen_csv(categorie)
    tonen_csv_tekst(lijst_csv)
    
    correcte_invoer = False
    while not correcte_invoer:
        gemoedstoestand = input('\nBeschrijf je gemoedstoestand. \nLaat het veld leeg en druk op enter om de invoer te annuleren.\n')
        if gemoedstoestand == '':
            correcte_invoer = True
        elif len(gemoedstoestand) > 300:
            print('Je beschrijving is te lang, gebruik maximaal 300 tekens!')
        elif len(gemoedstoestand) < 10:
            print('Je beschrijving is te kort, gebruik minimaal 10 tekens!')
        else:
            print('Weet je zeker dat je bovenstaande gemoedstoestand wilt ingeven?')
            bevestiging = input('Typ J om je keuze te bevestigen. Typ iets anders om te annuleren. ') 
            if bevestiging == 'J' or bevestiging == 'j':
                correcte_invoer = True
                regel = format_regel(gemoedstoestand, categorie)   
                schrijven_csv(regel)
                print('De gemoedstoestand is toegevoegd.')


def voeding(categorie):
    
    """ Hier kan de gebruiker de voeding doorgeven.

        De voeding moet minimaal 10 tekens en maximaal 300 tekens zijn.
    """
    lijst_csv = lezen_csv(categorie)
    tonen_csv_tekst(lijst_csv)
    
    correcte_invoer = False
    while not correcte_invoer:
        voeding = input('\nBeschrijf je voeding. \nLaat het veld leeg en druk op enter om de invoer te annuleren.\n')
        if voeding == '':
            correcte_invoer = True
        elif len(voeding) > 300:
            print('Je beschrijving is te lang, gebruik maximaal 300 tekens!')
        elif len(voeding) < 10:
            print('Je beschrijving is te kort, gebruik minimaal 10 tekens!')
        else:
            print('Weet je zeker dat je bovenstaande voeding wilt ingeven?')
            bevestiging = input('Typ J om je keuze te bevestigen. Typ iets anders om te annuleren. ') 
            if bevestiging == 'J' or bevestiging == 'j':
                correcte_invoer = True
                regel = format_regel(voeding, categorie)
                schrijven_csv(regel)
                print('De voeding is toegevoegd.')


def diagnose(categorie):
    
    """ Hier wordt de diagnose van de patiënt getoond. """
    
    lijst_csv = lezen_csv(categorie)
    tonen_csv_diagnose(lijst_csv)
    input('\nDruk op enter om terug te keren naar het menu. ')
                

def medicijnen(categorie):

    """ Hier kan de gebruiker medicijnen doorgeven.

        De gebruiker voert de eerste letters van het medicijn in, deze worden doorgegeven aan zoeken_medicijnen
    """

    lijst_csv = lezen_csv(categorie)
    tonen_csv(lijst_csv)
    
    invoer_correct = False
    while not invoer_correct:
        invoer = input("\nGeef de eerste letter(s) van het medicijn in. \nLaat het veld leeg en druk op enter om de invoer te annuleren. ")
        if invoer == '':
            invoer_correct = True
        elif invoer.isalpha() and len(invoer) == 1:
            invoer = invoer.upper()
            invoer_correct = True
        elif invoer.isalpha() and len(invoer) > 1:
            invoer = invoer[0].upper() + invoer[1:len(invoer)].lower()
            invoer_correct = True
        else:
            print('\nOngeldige zoekopdracht. Probeer het nog eens.')

    if invoer != '':
        zoeken_medicijnen(categorie, invoer)


def zoeken_medicijnen(categorie, invoer):

    """ Hier wordt de invoer van de gebruiker gezocht in het bestand lijstmedicijnen.txt

        Zodra er 15 resultaten zijn gevonden of indien de zoekopdracht minder dan 15 resultaten heeft, worden deze geprint en doorgegeven aan
        selecteer_medicijnen. Als er geen resultaten zijn gevonden, wordt registreer_medicijnen aangeroepen
    """
    
    lees = open('lijstmedicijnen.txt')
    
    aantal_gevonden = 1
    lees.seek(0)
    regel = lees.readline()
    zoekresultaten = []

    gevonden = False
    while regel != '' and not gevonden:
        
        regel = lees.readline()
        if invoer == regel[:len(invoer)]:
            zoekresultaten.append(regel)
            print(aantal_gevonden, regel, end='')
            aantal_gevonden += 1
        if len(zoekresultaten) != 0 and (len(zoekresultaten) % 15 == 0 or regel[:len(invoer)] != invoer):
            gevonden = selecteer_medicijn(categorie, gevonden, aantal_gevonden, zoekresultaten)
    lees.close()
    if not gevonden:
        registreer_medicijnen(categorie)


def selecteer_medicijn(categorie, gevonden, aantal_gevonden, zoekresultaten):

    """ Hier kan de gebruiker een medicijn uit de zoekopdrachten selecteren.

        Het nummer wordt gekoppeld aan het juiste zoekresultaat. Dit zoekresultaat wordt omgezet naar CSV-regel in format_regel en vervolgens doorgegeven
        aan schrijven_csv.
    """
    
    invoer_correct = False
    while not invoer_correct:
        print("\nWelk cijfer staat voor het medicijn? Typ N om naar de volgende pagina te gaan.")
        medicijnnummer = input('Laat het veld leeg en druk op enter om de invoer te annuleren. ')
        if medicijnnummer == '':
            invoer_correct = True
            gevonden = True
        elif medicijnnummer.isdecimal() and int(medicijnnummer) in range(1,aantal_gevonden):
            bevestiging = input('Typ J om je keuze te bevestigen. Typ iets anders om te annuleren. ') 
            if bevestiging == 'J' or bevestiging == 'j':
                gevonden = True
                invoer_correct = True
                medicijn = zoekresultaten[int(medicijnnummer)-1]
                regel = format_regel(medicijn, categorie)
                schrijven_csv(regel)
                print('Het medicijn is toegevoegd.')
        elif medicijnnummer == 'n' or medicijnnummer == 'N':
            invoer_correct = True
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')
    return gevonden


def registreer_medicijnen(categorie):

    """ Hier kan de gebruiker kiezen om een nieuw medicijn toe te voegen indien het niet in de lijst staat.

        Als de gebruiker een nieuw medicijn toevoegt, wordt medicijn_toevoegen aangeroepen.
    """
    
    invoer_correct = False
    while not invoer_correct:
        print('\nHet medicijn is niet gevonden. Druk op M om een medicijn toe te voegen.')
        keuze = input('Laat het veld leeg en druk op enter om de invoer te annuleren. ')
        if keuze == '':
            invoer_correct = True
        elif keuze == 'M' or keuze == 'm':
            medicijn_toevoegen(categorie)
            invoer_correct = True
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')
            

def medicijn_toevoegen(categorie):

    """ Hier kan de gebruiker een nieuw medicijn toevoegen indien het niet in de lijst staat.

        De naam van het nieuwe medicijn moet minimaal 4 karakters zijn.
        Het nieuwe medicijn wordt omgezet naar CSV-regel in format_regel en vervolgens doorgegeven aan schrijven_csv.
    """
    
    invoer_correct = False
    while not invoer_correct:
        print('\nWat is de naam van het medicijn?')
        keuze = input('Laat het veld leeg en druk op enter om de invoer te annuleren.\n')
        if keuze == '':
            invoer_correct = True
        elif len(keuze) > 3:
            invoer_correct = True
            keuze = keuze[0].upper() + keuze[1:].lower()
            regel = format_regel(keuze, categorie)
            schrijven_csv(regel)
            print('Het medicijn is toegevoegd.')
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')

            
def domotica(categorie):

    """ Hier kan de gebruiker zijn domoticagegevens bekijken.

        De gebruiker kiest het soort domotica, vervolgens worden de relevante gegevens getoond.
    """
    
    print('Kies een cijfer van het programmaonderdeel. Laat het veld leeg en druk op enter om de invoer te annuleren.\n')
    print('1. Aantal bewegingen\n2. Temperatuur\n3. Luchtvochtigheid')

    correcte_invoer = False
    while not correcte_invoer:
        menu_keuze = input('\nKeuze: ')
        if menu_keuze == '':
            correcte_invoer = True
        elif menu_keuze.isdecimal() and int(menu_keuze) in range(1,4):
            categorie = 4 + int(menu_keuze)
            correcte_invoer = True
            lijst_csv = lezen_csv(str(categorie))
            tonen_csv(lijst_csv)
            input('\nDruk op enter om terug te keren naar het menu. ')
        else:
            print('Incorrecte invoer! Probeer het nog een keer.')


def format_regel(invoer, categorie):

    """ Zorgt ervoor dat de invoer wordt omgezet naar een regel die aan het CSV-bestand toegevoegd kan worden. De regel wordt geretourneerd. """
    
    regel = [categorie,time.strftime("%d-%m-%Y"), time.strftime("%H:%M"), invoer]
    return regel


def schrijven_csv(regel):

    """ Hier wordt een regel aan het CSV-bestand van de patiënt toegevoegd. """
    
    with open(bsn_nummer + '.csv', 'a', newline='') as f:
        gelezen = csv.writer(f, delimiter=';')
        gelezen.writerow(regel)
        f.close()


def lezen_csv(categoriecode):

    """ Hier wordt het CSV-bestand gelezen en gefilterd op de categorie die de gebruiker in het hoofdmenu koos.

        Deze resultaten worden in lijst_csv opgeslagen, deze lijst wordt geretourneerd.
    """
    
    fo = open(bsn_nummer + ".csv")
    lijst_csv = []
    for l in fo:
        if l[0] == categoriecode:
            lijst = l.replace("\n", "")
            lijst = lijst.replace('\"', "")
            lijst_csv.append(lijst.split(";")[1:])
    fo.close()
    return lijst_csv


def lezen_patienten():

    """ Hier wordt het CSV-bestand met patiënten gelezen en opgeslagen in een lijst.

        De lijst wordt geretourneerd.
    """
    
    fo = open("lijstpatienten.csv")
    lijst_patienten = []
    for l in fo:
        lijst = l.replace("\n", "")
        lijst_patienten.append(lijst.split(";"))
    fo.close()
    return lijst_patienten


def tonen_gegevens():

    """ Hier worden de persoonlijke patiëntgegevens getoond.

        Zodra de gebruiker iets intypt, keert hij terug naar het hoofdmenu.
    """
    
    kolomnamen = ["\nVoorletters:", "Achternaam:", "\nGeboortedatum:", "Geslacht:", "BSN-nummer:",
                  "\nAdres:", "Woonplaats:", "\nHuisarts:", "Zorgverzekeraar:"]

    for g in range(len(kolomnamen)):
        print(kolomnamen[g], lijst_patienten[int(patientnummer)-1][g])
    input('\nDruk op enter om terug te keren naar het menu. ')
    

def tonen_csv(lijst_csv):

    """ Hier worden de relevante gegevens uit het CSV-bestand getoond.

        Dit gebeurt met de eerder samengestelde variabele lijst_csv. Datum, tijd en waarde staan op één regel.
    """
    
    print('\nDatum', format(' ', '8'), 'Tijd', format(' ', '4'), 'Waarde')
    for each in range(len(lijst_csv)):
        for g in range(len(lijst_csv[0])):
            print(lijst_csv[each][g], format(' ', '4'), end='')
            if g != 0 and g % 2 ==0:
                print()


def tonen_csv_diagnose(lijst_csv):

    """ Hier wordt de diagnose uit het CSV-bestand getoond.

        Dit gebeurt met de eerder samengestelde variabele lijst_csv.
    """
    
    print('\nOnderstaande tekst was ingevoerd op', lijst_csv[-1][0], 'om', lijst_csv[-1][1], 'uur:')
    print(lijst_csv[-1][2])

    
def tonen_csv_tekst(lijst_csv):

    """ Hier worden de relevante gegevens uit het CSV-bestand getoond.

        Dit gebeurt met de eerder samengestelde variabele lijst_csv. Datum en tijd staan op een andere regel dan de waarde.
    """
    
    for each in range(len(lijst_csv)):
        print('\nOnderstaande tekst was ingevoerd op', lijst_csv[each][0], 'om', lijst_csv[each][1], 'uur:')
        print(lijst_csv[each][2])
    

def schrijven_domotica():

    """ Hier worden de domoticagegevens gegenereerd, omgezet naar een CSV-regel in format_regel en vervolgens doorgegeven aan schrijven_csv. """
    
    if int(time.strftime("%M")) % 30 == 0:
        domotica = []
        
        # aantal bewegingen
        domotica.append(random.randint(5, 40))

        # temperatuur
        domotica.append(random.randint(170, 220) / 10)

        # luchtvochtigheid
        domotica.append(random.randint(35, 65))
        
        for h in range(len(domotica)):
            regel = format_regel(domotica[h], 5 + h)
            schrijven_csv(regel)

            
main()
