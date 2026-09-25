# Vocab Orbit: Mission New York

Interaktives Vokabelspiel mit 86 Haupteinträgen aus den bereitgestellten Vokabelseiten 184–189 (Topic 1). Die Übungssätze wurden für dieses Spiel neu formuliert. Die zusätzlichen Präpositions- und Wortfamilienübungen gehören nicht zum Wortpool.

## Spielen

https://danizahnweh-oss.github.io/vocab-orbit-new-york/

Alternativ `index.html` herunterladen und im Browser öffnen. Keine Installation, keine Anmeldung und kein Internet erforderlich. Es werden keine personenbezogenen Daten erfasst. Der Spielstand bleibt nur während der geöffneten Sitzung erhalten.

1. Themenbereich, Aufgabentyp und Aufgabenzahl wählen.
2. Mission starten und die richtige Antwort anklicken oder antippen.
3. Mit den Pfeiltasten zielen und mit der Leertaste schießen. Die Tasten 1–4 schießen direkt auf eine Antwort.
4. Nach jeder Antwort die Rückmeldung lesen und auf „Weiter“ klicken.
5. Am Ende lassen sich falsch beantwortete Vokabeln gezielt wiederholen.

Ohne Zeitlimit. Je richtige Antwort 100 Punkte plus Serienbonus (20 pro weiterem Treffer, bis maximal 100 Bonuspunkte). Ein Fehler setzt nur die Serie zurück. Keine Leben und kein Ausscheiden.

## Bearbeiten

`vocabulary.tsv` enthält Themen, Übersetzungen und Übungssätze. `index.template.html` enthält das Spiel. Nach Änderungen `python3 build.py` ausführen. GitHub Pages veröffentlicht den Hauptzweig.

## Geprüft

Alle 86 Fragen in allen vier Modi, Tastatursteuerung, vorzeitiges Beenden, Fehlerwiederholung, Themenauswahl sowie Bildschirmbreiten von 390, 768 und 1440 Pixeln mit automatisierten Chromium-Browsertests. Zusätzlich visuelle Kontrolle der Start-, Spiel- und Mobilansicht. Reduzierte Bewegung wird respektiert.
