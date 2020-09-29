# Metody vektorizace

Jako open-source varianta se bude používat program [Inkscape](https://inkscape.org), na Windows i Linux je instalace bez problému, na Mac budete potřebovat XQuartz (viz download stránka na [](https://inkscape.org)inkscape.org), očekávejte potíže, XQuartz kupříkladu potřebuje alespoň log-out + log-in po instalaci, a po spuštění trvá věky, než se otevře nějaké okno.

Jako komerční alternativa se nabízí Illustrator od Adobe.

### Nápady

*   ilustrace
*   blueprint
*   omalovánky
*   konstrukční návod ala IKEA
*   informační schéma/poster
*   políčko komixu

## Jak vektorizovat

Cílem vektorizace je převést rastrový obraz na vektorový výstup ala ilustrace, blueprint.

**Vektorizace obtahem** je tak trochu analogie klasického obkreslování přes pauzák, kdy se obtahují hlavní kontury objektu.

**Vektorizace překryvem** je dost podobná, ale místo obrysů používám základní tvary, které lze spojovat dohromady.

**Automatická vektorizace** využívá vestavěných nástrojů pro automatickou vektorizaci, úkolem uživatele je vhodně zvolit parametry.

## Ukázka

Ukázka vektorizace obtahem, překryvem a automatické vektorizace.

![zdrojové foto](/img/vector/cica.JPG)

<div class="images">
<img src="/img/vector/obtah.svg" alt="vektorizace obtahem"> 
<img src="/img/vector/prekryv.svg" alt="vektorizace překryvem"> 
<img src="/img/vector/auto.svg" alt="automatická vektorizace">
</div>

## Tipy pro Inkscape

*   velikost obrazové plochy lze změnit v menu `File > Documen Properties`
*   panel pro změnu průhlednosti podkladového obrázku `Object > Objects`
*   Inkscape ukládá ve výchozím nastavení rovnou do svg formátu
*   Ovládání nástroje pro vektorizaci v horním panelu (módy uzlů atp.)
*   Automatická vektorizace `Path > Trace Bitmap`