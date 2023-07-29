Eine schöne Sammlung aller Test für das Endprojekt, die uns einfallen können!

P.S.: Ihr könnte mehrere Sachen in einer Datei testen, indem ihr mehrere Prints macht! Eure .golden kann dann eine Linie von Werten haben! (Wichtig: Die prints in den Tests machen nicht automatisch Newline, also könnte ich nicht über mehrere Zeilen!)

# Regeln

- Vergesst nicht auch mit großen Zahlen zu testen! ($2^{63}-1$ ist die größte Zahl und $- 2^{63}$ die kleinste Zahl.)

- Achtet auf die Lineendings in eueren Dateien! Wir wollen nur den Linuxstandard, LN, sonst gibt es Probleme mit den Tests!

- Teilt die Tests in Ordnern auf, so dass wir einen schönen Überblick haben. Z.b.: Tests für Aufgabe 2, Tests für Division, Tests für Aufgabe 2 Regression, etc..

- Die Datei "Intentionen für Tests.md" ist dafür da, eine zentrale Sammlung für die Absichten hinter den einzelnen Tests zu sein. (Wollen die in der Dokumentation ja.)
  Fügt also für jede Testdatei einen Eintrag hinzu. (Nur einer nötig pro .py, .in und .golden.)

- Vergesst nicht, eure Namen auch mit rein zu schreiben! Der Thiemann verlangt den  Namen des Authors für Tests!

- Der genaue Aufbau von "Intentionen für Tests.md" ist eine Überschrift pro Ordner, gefolgt von einer Liste von Einträgen der Art "Authorname - Dateiname: Für was ist es gut, bzw., was testet es von der Implementierung."
