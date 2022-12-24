# Arkkitehtuurikuvaus

## Pakkausrakenne:

Pakkausrakenne on rippuvuuksiltaan hyvin yksinkertainen.

![Pakkausrakenne](./kuvat/pakkauskaavio.png)

## Käyttöliittymä
Sovelluksen käynnistämisen yhteydessä avautuu graafinen käyttöliittymä. Käyttöliitymää navigoidaan painamalla nappeja. Käyttöliittymä vaihtaa tiloja nappien avulla, esimerkiksi jos painaaa nappia "Deal Cards", näkymä piilottaa napin ja ikkunaan ilmestyy kaksi uutta nappia: "Hit" ja "Stand". 

## Sovelluslogiikka
Sovelluslogiikasta vastaa pääosin luokka "HandChecker", mutta myös osittain sen graafinen käyttöliittymä "BlackjackGUI". Sovelluksessa on kaksi listaa mitkä kuvaavat pelaajan ja jakajan käsiä. HandChecker pystyy tarkistamaan näiden käsien summia ja muuttamaan niiden arvoja tarvittaessa. Käyttöliittymä taas saa näitä syötteinä ja tekee muutoksia pelitilaan niiden perusteella.

## Päätoiminnallisuudet

### Deal Cards
Kun käyttäjä painaa nappia "Deal Cards", sovellus luo uuden "Deck" olion ja jakaa pelaajalle ja jakajalle 2 korttia. Tässä vaiheessa korteille generoidaan kuvat "resize_cards" funktion avulla. Ensimmäinen jakajan korteista pysyy piilotettuna erän loppuun asti. Funktio myös tarkistaa lopuksi että saiko pelaaja blackjackin, ja jos sai, niin siirtyy pelitila tarkistamaan myös jakajan käden.

### Hit
"Hit" nappia painaessa pelaaja saa uuden kortin. Kortin saamisen yhteydessä "HandChecker" tarkistaa käden arvon ja tarvitaessa muuttaa ässät arvoltaan yhdeksi. Jos 21 ylittyy niin peli päättyy.

### Stand
"Stand" nappi siirtää vuoron jakajalle, missä käyttöliittymä menee funktioon "dealer_hit", missä jakaja lyö siihen asti kunnes saa 17 tai enemmän.

## Ohjelman rakenteen heikkoudet

### Käyttöliittymä
Käyttöliittymässä olisi voinut käyttää controlleria, mikä olisi tehnyt käyttöliittymästä vähän selkeämmän ja erottanut sovelluslogiikkaa käyttöliittymästä.


