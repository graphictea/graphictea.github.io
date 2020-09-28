# Editace a transfromace obrazu

Tato část je věnována editaci obrazu na úrovni jasových hodnot jednotlivých pixelů v rastru.

## Histogram a monadické operace

Jednoduše, histogram zaznamenává počet pixelů o dané jasové hodnotě v obraze. Znalost jejich distribuce může pomoci nalézt vhodné paramtery pro další editaci. Hodí se tedy vědět, jak jednotlivé operace ovlivňují podobu histogramu.

Původní obraz je zde označen jako $f(x, y)$, obraz po transformaci jako $f'(x, y)$.

<div class="images">
    <img src="/img/monadic/duck.png">
    <img src="/img/monadic/histoduck.png">
</div>

original
$$f'(x, y) = f(x, y)$$
{: class="title" }



<div class="images">
    <img src="/img/monadic/negateduck.png">
    <img src="/img/monadic/histonegateduck.png">
</div>

negace
$$f'(x, y) = 1 - f(x, y)$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/threshduck.png">
    <img src="/img/monadic/histothreshduck.png">
</div>

prahování
$$l = 0.5,\, f'(x, y) = \begin{cases}0\text{ iff }f(x, y) \leq l\\\\1\text{ iff } f(x, y) > l\end{cases}$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/brightnessduck.png">
    <img src="/img/monadic/histobrightnessduck.png">
</div>

jas
$$l = 0.2,\, f'(x, y) = f(x, y) + l$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/contrastduck.png">
    <img src="/img/monadic/histocontrastduck.png">
</div>

kontrast
$$l = 1.25,\, f'(x, y) = f(x, y) \cdot l$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/gammaduck.png">
    <img src="/img/monadic/histogammaduck.png">
</div>

gamma
$$\gamma = 1.75,\, f'(x, y) = f(x, y)^{\gamma}$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/nonlincontrastduck.png">
    <img src="/img/monadic/histononlinearduck.png">
</div>

nelineární kontrast
$$f'(x, y) = \begin{cases}\frac{1}{2}(2f(x, y))^{\gamma}\text{ iff }f(x, y) \leq \frac{1}{2}\\\\1 - \frac{1}{2}(2 - 2f(x, y))^{\gamma} \text{ iff } f(x, y) > \frac{1}{2} \end{cases}\;\gamma = \frac{1}{1 - l},\;l = 0.5$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/logscaleduck.png">
    <img src="/img/monadic/histologduck.png">
</div>

logaritmizace
$$f'(x, y) = \frac{\log(1 + f(x, y) \cdot l)}{\log(1 + l)},\; l = 8$$
{: class="title" }


<div class="images">
    <img src="/img/monadic/quantizeduck.png">
    <img src="/img/monadic/histoquantizeduck.png">
</div>

kvantizace
$$l = 5,\, f'(x, y) = \lfloor f(x, y) \cdot l\rfloor$$
{: class="title" }

<div class="images">
    <img src="/img/monadic/equalizedduck.png">
    <img src="/img/monadic/histoequalizedduck.png">
</div>

ekvalizace
viz níže
{: class="title" }

### Ekvalizace histogramu a histogram matching

Ilustrace ekvalizace histogramu - mapování kumulativní distribuční funkce (cdf) příslušející vstupnímu obrazu na lineární cdf a poté zpětnou transformaci jasových hodnot, celou proceduru ilustruje následující obrázek.

![ekvalizace histogramu](/img/monadic/equalization.png)

Operace histogram matching je analogická ekvalizaci výše, pouze je lineární kumulativní distribuční funkce (linear cdf) nahrazena cdf příslušející obrazu, jehož rozložení intenzit se snažíme namapovat na originální obraz. V případě barevných obrázků je možné postupovat po složkách nezávisle, viz ukázka níže.

<div class="images">
    <img src="/img/monadic/city.jpeg">
    <img src="/img/monadic/jungle.jpeg">
    <img src="/img/monadic/city_mapped.jpeg">
</div>

histogram prvního snímku byl namapován na histogram druhého snímku, třetí snímek je výstup
{: class="title" }

## Prostorové transformace

Pod pojmem transformace se neskrývá nic nečekaného, jedná se transformaci obrazu v prostoru, např:

*   otočení (rotation)
*   změna velikosti (scale)
*   zkosení (shear)
*   posun (translation)
*   perspektivní transformace

Jednotlivé transformační operace lze reprezentovat pomocí matic a lze je roztřídit do několika kategorií dle vlastností, které v obraze zachovávají.

TODO

### Liquid scale

Má smysl se zabývat i transformacemi, které nespadají do kategorií výše, na ukázku je zde uvedeno video z kurzu [Introduction to Computational Thinking - MIT 18.S191](https://computationalthinking.mit.edu/Fall20/) které přibližuje metodu škálování obrazu podobnou [Liquid rescale](http://www.faculty.idc.ac.il/arik/SCWeb/imret/imret.pdf) ([youtube](https://www.youtube.com/watch?v=6NcIJXTlugc)).

<div class="video-box">
    <div class="video">
        <iframe width="420" height="315" src="https://www.youtube.com/embed/rpB6zQNsbQU">
        </iframe>
    </div>
</div>

## Editace v gradientní oblasti

Jako zajímavost lze uvést, že existují automatické metody pro bezešvé sešívání obrazu založené na [editaci v gradientní oblasti](https://en.wikipedia.org/wiki/Gradient-domain_image_processing).




<div class="images">
<img src="/img/edit/bonsai_combined.jpeg">
<img src="/img/edit/bonsai_border_left.png">
</div>

vlevo original, vpravo po editaci
{: class="title" }

<div class="images">
<img src="/img/edit/desk_left.jpeg">
<img src="/img/edit/desk_right.jpeg">
<img src="/img/edit/desk.png">
</div>

první a druhý snímek byly sloučeny do třetího, šev je sice stále znatelný, je zde ale demonstrována schopnost automatické kompenzace různých expozic vstupních obrazů
{: class="title" }

TODO demo