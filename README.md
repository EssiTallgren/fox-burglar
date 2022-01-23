FOX BURGLAR

Fox Burglar on tasohyppelypeli jossa tavoitteena on varastaa aarre. Matkan varrella on vihollisia,
ansoja ja pudotuksia, jotka vaikeuttavat peliä. Varo poliisia!


TIEDOSTO JA KANSIORAKENNE

doc - doc kansiosta löytyy projektin yleissuunnitelma, tekninen suunnitelma ja dokumentti
src - src kansiosta löytyy kooditiedostot sekä kuva-, musiikki- ja karttatiedostot alakansioista:
    - graphics - hahmojen, ansojen, aarteen ja taustojen kuvat
    - maps - tasojen karttatiedostot sekä virheelliset karttatiedostot joita käytetään testauksessa
    - sound - taustamusiikin mp3 tiedosto
.gitignore - tiedosto jossa ilmaistaan tiedostot joita Gitin ei kuulu huomioida


ASENNUSOHJE

Tämän ohjelman suorittamiseen vaaditaan PyQt5 sekä pygame kirjastot. Kirjastojen asentamiseksi mene
komentoriville ja kirjoita 'pip install PyQt5' ja sen jälkeen 'pip install pygame'.


KÄYTTÖOHJE

Ohjelmaa ajetaan y2-project---fox-burglar tiedostan juuresta. Kirjoita komentoriville
'python src/main.py' tai jos koneellasi on useampi python versio kirjoita 'python3 src/main.py'.
Jos haluat ajaa testi ohjelman kirjoita komentoriville 'python src/test.py' tai python3 kuten aiemmin
on mainittu.
