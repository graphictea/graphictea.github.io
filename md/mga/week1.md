# Editace obrazu

Tento týden je věnován editaci obrazu na úrovni jasových hodnot jednotlivých pixelů v rastru. Je doporučeno si projít část [věnovanou monadickým operacím a transformacím obrazu](../pg/monadic.html), **není potřeba si pamatovat vzorce, ani přesné metody implementace**, je vhodné si udělat představu o tom co jde a je možné. A případně se něčemu přiučit.

Pár poznámek:

*   z telefonů atp. se pod úpravou kontrastu typicky skrývá nelineární varianta této operace
*   nástroje pro úpravy barevného podání se nachází v menu `Color > *` (přebarvení `Colors > Map > Rotate Colors`)
*   pár odkazů na dokumentaci - [jas a kontrast](https://docs.gimp.org/2.10/en/gimp-tool-brightness-contrast.html), použít [thresholding](https://docs.gimp.org/2.10/en/gimp-tool-threshold.html), [curves](https://docs.gimp.org/2.10/en/gimp-tool-curves.html) (jedná se o alternativu "obyčené" gamma korekce) a [levels](https://docs.gimp.org/2.10/en/gimp-tool-levels.html) (slouží mimo jiné k vyvážení stínů a jasnějších částí)
*   při skládání více obrazů dohromady je často užitečné použít techniku [histogram matching](http://www.silent9.com/blog/archives/162-Gimp-Script-Histogram-Match.html), kdy se jedná v podstatě o zobecněnou metodu ekvalizace histogramu

## Filtrace

Filtry se nachází v menu Filtry, jsou rozděleny podle funkcionalit do podtříd. Mezi základní filtry je možné zařadit:

*   rozostření (`Filters > Blur > \*`)
*   doostření (`Filters > Enhance > Sharpen`)
*   detekce hran
*   eliminace defektů v obraze (např. nejjednodušeji vyhlazením...)

Pod pojmem filtr se toho skrývá hodně, lze rozlišovat lineární a nelineární filtry, pro orientaci v nabídce GIMPu je lepší ale chápat pojem filtr, jako něco, co mění obraz určitým očekáváným způsobem, nebo např. přidává nějaký nový element (např. šum).

Alternativně existuje řada pluginů, které přidávají další filtry.

Jak bylo uvedeno, filtrovat se obecně dá více způsoby, dost často se jedná o lineární filtraci obrazu s použitím [konvoluce](https://en.wikipedia.org/wiki/Convolution), s jejím použitím lze implementovat 4 příklady filtrace uvedené v seznamu výše.

Prakticky je užitečné, že filtry v GIMPu lze aplikovat také jen na části obrazu:

1.  vybrat část obrazu jakýmkoliv nástrojem pro výběr
2.  aplikovat filtr z menu

## Prostorové transformace

Při spojení si informací z kurzu BI-LIN ([lehké připomenutí z wiki](https://cs.wikipedia.org/wiki/Grafické_transformace)), není na škodu si uvědomit, že se jedná o lineární, potažmo afinní transformace a je možné je nějak maticově reprezentovat (hlouběji v BI-PGR).

Prakticky je velice užitečná perspektivní transformace - `Tools > Transform Tools > Perspective`. V GIMPu se nachází nástroj umožňující 4 bodovou transformaci obrazu, pravděpodobně nejpřímočařeji se tento nástroj dá použít pro

*   extrakci kusu obrazu ze zdrojového snímku (budeme chtít extrahovat ze zdrojových obrázků textury)
*   trasformaci výřezu do cílového obrazu, tak aby odpovídal cílové perspektivě (např. umístění nápisu na zeď)

## Manuální sešívání snímků

Při sešívání se pro korekci nekonzistentních švů hodí funkcionality jako [klonování](https://docs.gimp.org/2.10/en/gimp-tool-clone.html) (a [perspektivní klonování](https://docs.gimp.org/2.10/en/gimp-tool-perspective-clone.html)). Bohužel je nutné se potýkat také s jinými nedostatky:

*   nedostatky jsou velmi často v **odrazech** - některé techniky k odhalování retuší se soustředí právě na hledání těchto nedostatků
*   problematické je také postupné navyšování rozlišení (ve 4K se nedostatky hledají lépe)

Pro manuální korekci je vhodné využít kombinaci několika metod, níže je pár nápadů:

*   velmi hrubě - vezmu pipetu, naberu barvu z okolí, pak štětcem místo odrazu překreslím
*   lepší - vezmu razítko z okolí - naberu vzorek ctrl + mouse click a pak ho aplikuji na vybrané místo, hodí se klonovat do nové vrstvy
*   zkusím rozmazání, mám na výběr z více metod rozmazání (klasický, gaussian...)
*   zkusím defekt zamaskovat pomocí airbrushe (naberu barvu pomocí pipety, aplikuju lokálně)