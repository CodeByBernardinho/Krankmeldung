#Krankmeldungschreiber 
import sys

from func_kmeldung import abfrage_kmeldung
from func_kmeldung import text_kmeldung

print("Willkommen bei ihrer Krankmeldungautomatisierung!")
abfrage_kmeldung()

fh = "krankmeldung_neu.txt"
sys.stdout = open(fh, "w")
text_kmeldung()






