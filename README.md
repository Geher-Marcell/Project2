# 2022-2023-as tanév 2. projectmunka

### Csapattagok:

- [Gehér Marcell](https://github.com/Geher-Marcell)
- [Gerencsér Olivér](https://github.com/GerencserOliver)
- [Borsodi Koppány](https://github.com/borsodi-koppany)

---

### Projekt bemutató:
A tamagotchi egy hordozható kisállat-szimulátor, amelyet Akihiro Yokoi és Aki Maita készítettek. Japánban 1996. november 23-án, a világ többi részén pedig 1997. május 1-jén jelent meg. A tamagoccsi a kilencvenes/kétezres évek egyik legnagyobb trendjének számított. Világszerte több mint 83 millió példányban kelt el.

Ez a projekt a fentit átalakítja egy nyílt forráskódú számítógépes játékká.

---

### Játék tartalma:
Letöltés után batch fájl és egy mappa fogad minket.
- start.bat -> Játék elindítása
- update.bat -> A játékhoz szükséges python könyvárak letöltése **Szükséges python verzió >3.9**
- deleteSave.bat -> A már meglévő mentés kitörlésére szolgál
- Game/ -> A játék forráskódját és képeket tartalmazó mappa

---

### Játék menete:
Megnyitáskor egy karakter készítő fogad. Egy nevet kötelezően meg kell adni a karakterünknek. Amennyiben ezt sikeresen megtettük választanunk kell egyet a látható állatkák közül.
A fő cél: az állatunk életbentartása. Ehhez 3 dolgot kell tennünk:
- Megsimogatni
- Játszani vele
- Megetetni
Ezeket a felcimkézett gombokkal tudjuk megtenni. Amennyiben valamelyiket elhanyagoljuk és az értéke nulla lesz, az állatunk meghal. Mivel ez digitális környezet ezért a program újraindításával lehetőségünk lesz új mentést kezdeni.

Az **idő telése** miatt at állatunk statjai csökkenek ezért fontos, hogy rendszeresen ránézzünk és foglalkozzunk vele.

---

### Továbbiak:
Amennyiben saját képet akarunk az állatoknak a következőt kell tennünk:
1. Kell egy kép aminek **.png** a formátuma
2. Ezt a képet másoljuk át a `Game/images/tamagotchies` mappába
3. Töröljük a meglévő mentést, ha van
4. Indítsunk egy új játékot
