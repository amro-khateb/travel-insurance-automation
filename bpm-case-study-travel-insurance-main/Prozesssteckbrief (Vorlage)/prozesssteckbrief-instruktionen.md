# Hinweise
> Zweck des Prozesssteckbriefs ist es, in strukturierter Form alle relevanten Informationen über einen Prozess zu sammeln. Er dient explizit nicht als komplette Beschreibung aller Prozessschritte, Entscheidungen etc. - diese Funktion nimmt das Prozessmodell wahr.
> Daher wird der Prozess hier zu einem gewissen Teil als Black Box betrachtet - wir beschreiben vor allem die Eingaben und Ausgaben sowie den organisatorischen Kontext, aber das Innere des Prozesses nur soweit es wirklich benötigt wird.

> Der Steckbrief muss nicht dogmatisch befolgt werden, sondern ist lediglich als Hilfe zu verstehen. Nicht benötigte Überschriften können entfernt werden, neue hinzugefügt. Die genauen Inhalte und Darstellungsformen (z.B. Tabelle) innerhalb einzelner Abschnitte können variiert werden.

# [Name des Prozesses]

*Jeder Prozess soll letzten Endes als BPMN-Diagramm modelliert und in seinen Steckbrief integriert werden. Das Modell entsteht spätestens zu dem Zeitpunkt der Implementierung und entwickelt sich i.d.R. iterativ weiter.*

![](prozessdiagramm.png)

## Kurzbeschreibung

*Hier soll der Prozess kurz in natürlichsprachlicher Form beschrieben werden. Dabei ist ein Detaillierungsgrad zu wählen, der der Komplexität des Prozesses angemessen wird. Auf technische Details soll hier nicht eingegangen werden, sondern lediglich auf die Fachlichkeit, die der Prozess abbildet bzw. abbilden soll.*

*Die Beschreibung kann mehrere Absätze lang sein und neben dem Normalfall auch wichtige Ausnahme- bzw. Fehlerfälle beschreiben, die bei der Prozessausführung entstehen können. Darüber hinaus kann bei der Beschreibung auf alle anderen wichtigen Aspekte eines Prozesses eingegangen werden, die hervorgehoben werden sollen - selbst wenn diese in späteren Abschnitten des Steckbriefs noch einmal separat aufgeführt werden.*

*Insgesamt sollte jedoch versucht werden, die Kurzbeschreibung so sparsam wie möglich zu halten und nur so viel vorweg zu nehmen, wie unbedingt nötig.

## Technischer Name

*Hier soll die ID der Prozessdefinition, so wie sie im Camunda Modeler spezifiziert wurde, angegeben werden. Durch diese kann der Prozess in Camunda eindeutig identifiziert werden.*

Der eindeutige Bezeichner des Prozesses lautet wie folgt:

`id_der_prozessdefinition_wie_im_camunda_modeler_angegeben`

## Organisatorischer Kontext

### Prozessziele

*Hier sollen in fachlicher Sprache die Ziele dieses Prozesses aufgeführt werden. Hierzu kann bspw. als strukturierendes Element eine Bullet-Point-Liste genutzt werden.*

### Stakeholder

*Bei Prozessstakeholdern handelt es sich um unterschiedliche Personengruppen, die ein Interesse an einem bestimmten Prozess haben oder an dessen Ausführung beteiligt sind. In der nachfolgenden Tabelle sollen drei Arten von Stakeholdern beschrieben werden:*

| Stakeholder         | Details                                                      |
| ------------------- | ------------------------------------------------------------ |
| Prozesseigner:innen | *Prozesseigner:innen sind verantwortlich für die zielorientierte, strategische Steuerung eines Prozesses und dessen Zielausrichtung mit anderen Prozessen. Hierzu gehört auch die Auswahl nachhaltiger Kennzahlen für die Erfolgsmessung des Prozesses und die Koordination von Ressourcen für die Prozesssteuerung und -ausführung.* |
| Prozessbeteiligte   | *Prozessbeteiligte spielen bei der Ausführung eines Prozesses eine aktive Rolle. Dies können bspw. Personen sein, die Formulare ausfüllen, Personen, die Genehmigungen erteilen. Diese sollen hier aufgeführt werden.* |
| Kund:innen          | *Kund:innen müssen nicht notwendigerweise bei der Ausführung des Prozesses beteiligt sein. Sie müssen aber vom Ergebnis der Prozessausführung profitieren. Hier soll aufgeführt, welche Person oder Personen vom Ergebnis des Prozesses profitieren und welcher Mehrwert diesen aus dem Prozess entsteht*. |

### Anwendungssysteme

*Hier sollen Anwendungssysteme genannt werden, die für die Ausführung des Prozesses eine aktive Rolle spielen. Dies können bspw. Systeme sein, aus denen gelesen wird, oder Systeme, in die geschrieben wird, oder Services, die über eine Schnittstelle konsumiert werden.*

| System                     | Details                                                      |
| -------------------------- | ------------------------------------------------------------ |
| Name des Anwendungssystems | Hier soll kurz beschrieben werden, in welcher Form das Anwendungssystem für die Prozessausführung benötigt wird, bspw. als Quelle zum Lesen bestimmter Daten oder als Ziel für Schreibeoperationen |
| Name des Anwendungssystems | Kurzbeschreibung                                             |
| Name des Anwendungssystems | Kurzbeschreibung                                             |

## Prozessbeginn

### Start / Auslöser

*Hier soll beschrieben werden, auf welche Art und Weise eine neue Instanz dieses Prozesses gestartet werden kann. Dies korrespondiert direkt mit den verschiedenen Arten von Start Events, die BPMN kennt. Mögliche Optionen sind hierbei unter anderem:*

* *Eingabeformular: Der Prozess wird manuell durch eine Nutzerin über ein Formular gestartet.*
* *Zeitbasiert: Der Prozess wird automatisch nach einer zeitbasierten Regel gestartet.*
* *Ferngesteuert: Der Prozess wird ferngesteuert durch einen Trigger gestartet, bspw. durch Aufruf aus einem anderen System, Empfang einer Email in einem bestimmten Postfach, o.Ä.*

| Startbedingung          | Details                                                      |
| ----------------------- | ------------------------------------------------------------ |
| Name der Startbedingung | Kurzbeschreibung der Startbedingung, z.B. Regel für zeitbasierten Start |
| Name der Startbedingung | Kurzbeschreibung der Startbedingung, z.B. Regel für zeitbasierten Start |
| Name der Startbedingung | Kurzbeschreibung der Startbedingung, z.B. Regel für zeitbasierten Start |

### Input

*Hier soll beschrieben werden, welche Informationen zum Starten einer Instanz dieses Prozesses benötigt sind. Wird der Prozess durch ein Formular gestartet, so handelt es sich hierbei bspw. um die Eingabefelder des Formulars. Eventuell gibt es auch gar keinen benötigten Input, bspw. bei zeitbasiert gestarteten Prozessen.*

*Die Beschreibung sollte hier aus fachlicher Perspektive erfolgen, d.h. technische Details wie z.B. Datentypen oder Variablennamen sind hier nicht nötig. Diese werden später im Abschnitt zum Prozesskontext genauer aufgeführt.*

| Eingabe          | Details                               |
| ---------------- | ------------------------------------- |
| Name der Eingabe | Zusätzliche Informationen zur Eingabe |
| Name der Eingabe | Zusätzliche Informationen zur Eingabe |
| Name der Eingabe | Zusätzliche Informationen zur Eingabe |

## Prozessschritte

*Hier sollen weitere wichtige Schritte während der Prozessausführung beschrieben werden, die zwischen Prozessbeginn und Prozessende liegen. Hierbei handelt es sich im Wesentlichen um die unterschiedlichen Arten von Tasks, die im Prozessmodell abgebildet sind.*

*Allgemeine Informationen, die je Prozessschritt angegeben werden können, umfassen bspw. Name des Tasks, Beschreibung, Ergebnis des Prozessschritts, mögliche Entscheidungen nach Prozesschritt durch Gateways, mögliche Ereignisse (boundary Events), mögliche Fehler und Verhalten im Fehlerfall, etc.*

*Je nach Typ des Tasks sind für die Beschreibung unterschiedliche Informationen relevant; hier sollt ihr euch euer eigenes Schema überlegen. Für Service Tasks relevante Informationen könnten bspw. Name, Task Type, Retry-Verhalten und Eingabe- und Ausgabevariablen sein. Für User Tasks relevante Informationen könnten bspw. Name und Art des Formulars, Formularfelder und Validierungsregeln sein. Für Konnektoren relevante Informationen hängen vom spezifischen Konnektor ab.*

### Prozessschritt 1

*Beschreibung des ersten Prozessschritts*

### Prozessschritt 2

*Beschreibung des zweiten Prozessschritts*

## Prozessende

### Ende

*Hier soll aufgeführt werden, auf welche Arten ein Prozess zu Ende gehen kann. Neben dem "Gutfall", d.h. dem regulären Prozessende mit gewünschtem Ergebnis, sind hierbei insbesondere auch Fehlerfälle aufzuführen, soweit sie bekannt sind.*

| Endbedingung               | Details                                                      |
| -------------------------- | ------------------------------------------------------------ |
| :heavy_check_mark: Gutfall | Kurzbeschreibung des Prozessendes im Gutfall                 |
| :x: Fehlerfall 1           | Kurzbeschreibung der Bedingungen bei Eintreten von Fehlerfall 1 |
| :x: Fehlerfall 2           | Kurzbeschreibung der Bedingungen bei Eintreten von Fehlerfall 2 |

### Ergebnis / Output

*Hier soll aufgeführt werden, mit welchem Ergebnis ein Prozess beendet wird und welche Ausgabe er ggf. erzeugt. Ausgabe sind dabei Geschäftsobjekte, die sowohl in Form von Daten (in ein Zielsystem geschriebene Datensätze als auch in physischer Form (eine ausgedruckte Rechnung) vorliegen können. Betrachtet wird hierbei das reguläre Prozessende. Soll für bestimmte Fehlerfälle ein anderer Output produziert werden, kann dieser gesondert unterhalb der Tabelle aufgeführt werden.*

| Geschäftsobjekt                                  | Zielsystem                 | Verantwortlich                     |
| ------------------------------------------------ | -------------------------- | ---------------------------------- |
| Grobe Beschreibung der Datenstruktur des Objekts | Name des Anwendungssystems | Personengruppe / Abteilung / Rolle |
| Grobe Beschreibung der Datenstruktur des Objekts | Name des Anwendungssystems | Personengruppe / Abteilung / Rolle |
| ...                                              | ...                        | ...                                |

## Prozesskontext

*Hier sollen alle Variablen beschrieben, die während der Prozessausführung in den Prozess hineingehen, in diesem generiert werden oder aus diesem wieder hinausgehen.*

*Je nach Funktion einer Variable innerhalb des Prozesses, können unteschiedliche Typen unterschieden werden: 1) Externe Variablen, die von außen in den Prozess hineingegeben werden (bspw. bei Prozessstart), oder aus diesem nach außen gegeben werden. 2) Interne Variablen, die während der Prozessausführung erzeugt werden. 3) Technische Variablen, die nur für die Steuerung des Kontrollflusses genutzt werden, aber keine fachliche Bedeutung haben. Es sollten zumindest externe und interne Variablen unterschieden werden, weitere Typen sind optional.*

*Für die Namensgebung von Variablen bietet es sich an, je nach Typ mit Präfixen zu arbeiten, bspw. `ext_`  für externe Variablen, `int_` für interne Variablen und `tec_` für technische Variablen.*

Folgende Variablen werden während der Ausführung im Prozesskontext abgelegt:

| Variablenname       | Typ                 | Datentyp                       | Details                                                  |
| ------------------- | ------------------- | ------------------------------ | -------------------------------------------------------- |
| `name_der_variable` | Extern, Intern, ... | String, Zahl, Datum, Json, ... | Relevante Details, z.B. Validierungsregeln, Wertebereich |
| `name_der_variable` | Extern, Intern, ... | String, Zahl, Datum, Json, ... | Relevante Details, z.B. Validierungsregeln, Wertebereich |
| `name_der_variable` | Extern, Intern, ... | String, Zahl, Datum, Json, ... | Relevante Details, z.B. Validierungsregeln, Wertebereich |
