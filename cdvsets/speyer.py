# coding: utf-8

"""
http://codingdavinci.de/daten/#stadtarchiv-speyer

Fotografien aus dem Ersten und vor allem Zweiten Weltkrieg, hauptsächlich von
der Ostfront und Italien. Alltag und Kriegsgeschehen werden gleichermaßen
abgebildet.

Der Fotonachlass von Karl Lutz umfasst ca. 5.000 Fotografien auf
unterschiedlichem Trägermaterial. Die enthaltenen Negative, Dias, Glasplatten
und Abzüge sind weitestgehend digitalisiert. Dabei wurden auch
Rückseitenvermerke und Notizen aufgenommen. Die Fotosammlung bietet Motive
unterschiedlichster Art. Neben zahlreichen Aufnahmen, die den Alltag der
Menschen in den Kriegsgebieten darstellen und typischen Motiven aus dieser
Zeit, wie Panzer und Schützengräben, findet man Porträt­, Gruppen­ und
Landschaftsaufnahmen. Bemerkenswert an diesem Bestand ist die Sichtweise eines
Fotografen, der von Beruf Archivar ist. So hatte Karl Lutz kein Interesse
daran, Bilder zu Propagandazwecken aufzunehmen, sondern fotografierte aus der
Sicht des aufmerksamen Beobachters. Davon zeugen auch spezielle Bildmotive,
wie zum Beispiel eine Serie von Straßen­ und Hinweisschildern. Auch die
professionelle Beschriftung der Bilder ist eher ungewöhnlich. Die Bilder sind
datiert, weitere Informationen konnten teilweise durch Vermerke und Recherchen
der Bearbeiter erschlossen werden. Der gesamte Bestand samt Metadaten wird für
Coding Da Vinci zur Verfügung gestellt. Lediglich einige private
Familienfotografien wurden herausgenommen.

"""

from cdvsets.task import DefaultTask
from gluish.parameter import ClosestDateParameter
from gluish.utils import shellout
import datetime
import luigi

class SpeyerTask(DefaultTask):
    TAG = 'speyer'

    def closest(self):
        return datetime.date(2015, 4, 1)

class SpeyerDump(SpeyerTask):

    date = ClosestDateParameter(default=datetime.date.today())

    def run(self):
        url = "https://offenedaten.de/storage/f/2015-04-09T13%3A17%3A11.125Z/speyer-192-20-hackathon.xml"
        output = shellout("""curl "{url}" > {output}""", url=url)
        luigi.File(output).move(self.output().path)

    def output(self):
        return luigi.LocalTarget(path=self.path())

