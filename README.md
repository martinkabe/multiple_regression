# Dokumentace

## Lokalni spusteni aplikace

Nasledujici prikazy doporucuji spustit napriklad v [Git Bash](https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/Git-2.34.1-64-bit.exe).

* cd Cesta/do/lokalniho/adresare
* git clone https://github.com/martinkabe/multiple_regression.git
* source .venv/Scripts/activate    -> Abychom se vyhnuli jakymkoli problemum s nekompatibilitou balicku
* code .    -> Aplikaci otevre v VS Code

Pokud v IDE neuvidite (.venv) nad cestou k projektu, doporucuji jeste jednou z VS Code terminalu spustit prikaz [source .venv/Scripts/activate].

![image](https://user-images.githubusercontent.com/7679763/146746264-0606e1ca-e421-4a5d-a589-ae0996f7e592.png)

* flask run    -> Spusti aplikaci lokalne na portu 5000 [Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)], takze uz staci jen ctrl+click na link.

## Popis programu

Tento program slouzi k vypoctu odhadu koeficientu regresni primky/roviny/nadroviny, jejich smerodatnych chyb, testovych kriterii a p hodnot.

Uzivatel nejprve nahraje *.csv soubor, stiskem tlacitka 'Odesli' bude presmerovan na stranku s regresni diagnostikou.

Povolen je pouze *.csv soubor, kde v prvnim sloupci bude zavisle promenna, ostatni sloupce jsou zastoupeny nezavisle promennyma. V prvnim radku je samozrejme hlavicka s nazvy sloupcu. 

<ins>Vzorove soubory</ins> jsou v **/Scripts/test/** adresari, soubory jsou pojmenovany jako **test1.csv** a **test2.csv**.

**Uzivatel dale bude mit moznost zadat vlastni hodnoty pro nezavisle promenne, ze kterych bude nasledne vypoctena predikce pro zavisle promennou.**

![regresni_analyza](https://user-images.githubusercontent.com/7679763/146685520-75f2f3a1-6904-4a0e-9290-9744557b9f36.gif)

## Pouzite tridy

### Trida Matice v souboru Matrix.py

Vstupni datova struktura z *.csv souboru je naparsovana do tohoto objektu, se kterym se dale pocita ve vsech maticovych operacich.

Konstruktor: data, radky: List = [], sloupce: List = []

Gettery a settery jsou pro vsechny parametry konstruktoru. Dalsi dulezity getter je potom pro property nazvanou **dimenze**, ktera zavola privatni metodu __dim(self, d: List[List]), ktera rekurzivne zjisti dimenzi napric strukturou List[List] a vrati List, kde na prvni (0) pozici je pocet radku a na druhe (1) pozici je pocet sloupcu.

### Trida NactiData v souboru DataReader.py

Soubor obsahuje tridu **NactiData**, ktera obsahuje pouze jednu classmetodu **data_do_matice**:

vstupni argumenty: cesta [datovy typ: str]

navratova hodnota: Matice [(class) Matice(data: List[List], radky: List = [], sloupce: List = [])]

Tato metoda po radcich precte *.csv soubor a vrati objekt Matice, se kterym nasledne provadi vsechny potrebne maticove pocty.

### Trida MatrixCustom v souboru MatrixCalc.py

Tato trida je ze vsech nejdulezitejsi, jelikoz je jadrem pro maticove operace, ktere jsou pouzity v regresni analyze. 

<ins>Obsahuje nasledujici tridni metody:</ins>

* vynasob(cls, mat1: Matice, mat2: Matice) -> Matice: Metoda pro nasobeni matic a macice se skalarem.

* secti(cls, mat1: Matice, mat2: Matice) -> Matice: Metoda pro scitani matic.

* odecti(cls, mat1: Matice, mat2: Matice) -> Matice: Metoda pro odecitani matic.

* transpozice(cls, mat: Matice) -> Matice: Metoda pro transpozici matice.

* shodnost_matic(cls, mat1: Matice, mat2: Matice, tol=None) -> bool: Metoda, ktera zjisti, jestli jsou matice shodne ci nikoliv. **tol** parametr v metode predstavuje 

* matice_deep_copy(cls, mat: Matice) -> Matice: Metoda, ktera vytvori novy objekt **Matice**.

* nulova_matice(cls, radky: int, sloupce: int) -> Matice: Metoda, ktera vytvori nulovou matici.

* jednotkova_matice(cls, n: int) -> Matice: Metoda, ktera vytvori jednotkovou matici.

* skalarni_soucin(cls, mat1: Matice, mat2: Matice) -> float: Metoda pro skalarni soucin dvou matic s navratovym typem float.

* determinant_rekurzivne(cls, mat: Matice, celkem: int = 0) -> float: Metoda pro vypocet determinantu rekurzi s navratovym typem float.

* singularita(cls, mat: Matice): Metoda, ktera pokud je determinant matice nulovy, tak vyhodi **ArithmeticError**.

* ctvercovost(cls, mat: Matice): Metoda, ktera overi dimenze matice a pokud se lisi, tak vyhodi **ArithmeticError**.

* inverzni_matice(cls, mat: Matice, tol=None) -> Matice: Metoda, ktera na zaklade Gauss-Jordanovi eliminace vypocte inverzni matici k matici vstupni. **tol** argument porovnava na zaklade presnosti desetinnych mist matici jednotkovou s matici po G-J emilinaci.

* extrakce_diagonaly(cls, mat: Matice) -> List: Metoda pro extrakci hlavni diagonaly ze vstupni matice.


### Trida Regrese v souboru RegresniAnalyza.py

Trida, ktera ve svych tridnich metodach pouziva vsechny tridni metody ze tridy **MatrixCustom**. V teto tride se deji veskere operace potrebne pro regresni diagnostiku.

<ins>Tato trida obsahuje nasledujici tridni metody:</ins>

* oddel_prediktory(cls, mat: Matice) -> List: Tato metoda *rozdeli* zavisle promennou a nezavisle promenne do unikatnich objektu **Matice**. Tento krok velmi usnadni dalsi vypoctove operace v regresni diagnostice.

* vypocti_odhady_koeficientu(cls, data: Matice) -> Matice: Tato medota provede vypocet odhadu koeficientu regresni primky/roviny/nadroviny, jejich smerodatnych chyb, testovych kriterii a p hodnot.

* r_squares(cls, y: Matice, X: Matice, b: Matice) -> Tuple: Tato metoda vypocte koeficient determinace jako procento vysvetlene variability danym modelem, vcetne adjustovaneho koeficientu determinace, ktery zohlednuje pocet regresoru v danem linearnim modelu.

* aritmeticky_prumer(cls, x: List) -> float: Vypocte jednoduchy aritmeticky prumet ze zadaneho vektoru dat.

Vsechny pouzite algoritmy pro regresni diagnostiku byly pouzity z **./static/md_files/LinearRegression.pdf** souboru.

<!-- Vsechny pouzite algoritmy pro regresni diagnostiku byly pouzity z [tohoto zdroje](./LinearRegression.pdf). -->
