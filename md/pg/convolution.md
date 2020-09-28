# Filtrace obrazu

Pojem filtr je poněkud obecný a může se pod ním skrývat celá řada operací. Mezi filtry lze například zařadit:

*   rozostření či doostření
*   detekci hran
*   eliminace defektů v obraze

Filtrovat obraz lze obecně více způsoby, dost často se jedná o lineární filtraci obrazu s použitím [konvoluce](https://en.wikipedia.org/wiki/Convolution), s jejím použitím lze implementovat 4 příklady filtrace uvedené v seznamu výše. Jiné typy filtrace mohou zahrnovat např. filtraci ve frkvenční oblasti (viz Fourierova transformace) nebo nelineární filtraci (viz bilatelární filtr níže).

## Konvoluce

$$(f \* g)(s, t) = \\int\_{-\\infty}^{\\infty} \\int\_{-\\infty}^{\\infty} f(x, y) \\cdot g(s−x,t−y) dxdy$$ nebo také diskrétně $$(f \* g)(s, t) = \\sum\_{x}\\sum\_{y} f\[x, y\] \\cdot g\[s − x, t − y\]$$ jsou předpisy pro konvoluci. K čemu? Za $f$ je možné dosadit upravovaný snímek jako dvourozměrnou funkci, za $g$ libovolné konvoluční jádro a jednoduše lze obrázek filtrovat řadou způsobů prostou výměnou jádra za jiné. Pokud za $g$ dosadíme např gaussian, jednoduše lze na snímek aplikovat rozmazání:

<div class="images">
    <img src="/img/gaussian/duck.png" alt="">
    <img src="/img/gaussian/duck10.png" alt="">
    <img src="/img/gaussian/duck20.png" alt="">
    <img src="/img/gaussian/duck30.png" alt="">
    <img src="/img/gaussian/duck40.png" alt="">
</div>

aplikace gaussianu s rozptylem 10, 20, 30 a 40px
{: class="title" }

Pro lepší pochopení konvoluce lze vřele doporučit video vytvořené ke kurzu [Introduction to Computational Thinking - MIT 18.S191](https://computationalthinking.mit.edu/Fall20/).

<div class="video-box">
    <div class="video">
        <iframe width="420" height="315"
        src="https://www.youtube.com/embed/8rrHTtUzyZA">
        </iframe>
    </div>
</div>

TODO praktické aplikace konvoluce

TODO metody akcelerace výpočtu kovoluce

## Bilaterální filtr

Pokud pracujeme se zašuměnými snímky, hodí se lehké rozmazání pro odšumění. Problémem ovšem je, že touto operací ze snímku odstraňujem detaily a ostré hrany. Z toho důvodu se hodí použít [Bilaterální filtr](https://en.wikipedia.org/wiki/Bilateral_filter), jehož předpis může nápaditě připomínat konvoluci výše $$f\_{filtered}(s, t) = \\frac{1}{W\_p}\\sum\_{x}\\sum\_{y} f\[x, y\] \\cdot g\[s - x, t - y\] \\cdot h\[\\left|f\[x, y\] - f\[s, t\]\\right|\],$$ kde $$W\_p = \\sum\_{x}\\sum\_{y} g\[s - x, t - y\] \\cdot h\[\\left|f\[x, y\] - f\[s, t\]\\right|\].$$ Objevil se člen $h$, který reprezentuje jednodimenzioální gaussian a váží originální konvoluční jádro $g$. K čemu to? Prakticky jsme pomocí tohoto vylepšeného filtru schopni zachovat ostré přechody a zároveň se zbavit šumu.


<div class="images">
    <img src="/img/gaussian/facet.png" alt="">
    <img src="/img/gaussian/f4.png" alt="">
    <img src="/img/gaussian/archi.png" alt="">
    <img src="/img/gaussian/archi10_60.png" alt="">
</div>

vlevo originál, vpravo snímek s potlačeným šumem
{: class="title" }
