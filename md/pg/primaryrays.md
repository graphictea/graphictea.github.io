# Vrhání paprsků

Bude potřeba vyřešit následující problémy:

*   jak reprezentovat paprsek
*   a jak počítat průsečík paprsku a trojúhelníku.

Druhému problému se věnuje příští část textu, v této části je popsáno generování primárních paprsků. Paprsek lze reprezentovat řadou způsobů. Důležité je následující:

*   paprsek je polopřímka, kterou lze v prostoru reprezentovat pomocí dvou vektorů - počátku a směru,
*   paprsek lze zapsat jako $\\mathbf{o} + t\\mathbf{s}$ (parametrická forma),
*   běžně se bude hledat nejbližší nebo první průsečík paprsku a trojúhelníku (test průsečíku),
*   a je dobré na přístupném místě uschovat výsledek testu a uschovat také odkaz na protnutý trojúhelník.
*   testu se běžně říká **incidenční operace**

Paprsek je nejvhodnější reprezentovat pomocí dvou vektorů dle parametrického zápisu, alternativní používaná reprezentace využívá polární souřadnice.

## Primární paprsky

V této části je uveden způsob, jakým je možné získat směry paprsků vržených do scény z místa pozorovatele. Tím, že paprsky směřují z místa pozorovatele, jsou eliminovány výpočety paprsků, které nepřispívají do výsledného obrazu. Je vhodné uvést, že:

*   paprsky vržené z místa pozorovatele se nazývají **primární**,
*   primární paprsky určují barvu korespondujícího pixelu ve výsledném obraze
*   v nejjednodušší variantě určuje rozlišení mřížky počet primárních paprsků, uvažujeme jeden paprsek na pixel (paprsek prochází středem pixelu)

V následující části jsou krátce popsány dva způsoby jak získat vektory primárních paprsků.

## Přímý výpočet ze vstupních parametrů

Cílem je najít střed každého pixelu ze vstupních parametrů. Vstupy pro získání primárních paprsků jsou:

*   rozlišení průmětny $w$ a $h$
*   pozice pozorovatele $\\mathbf{o}$
*   up vector aneb kterým směrem je nahoru $\\mathbf{u}$
*   směr pohledu pozorovatele $\\mathbf{d}$
*   field of view aneb velikost zorného pole, běžně se udává jako úhel $\\theta$

![Primární paprsky](/img/introgi/view.svg)

Ilustrace generování souřadnic směrových vektorů pro jednotlivé pixely
{: class="title" }

Všechny vstupní směrové vektory jsou normalizované. $$\\mathbf{b} = \\mathbf{d} \\times \\mathbf{u} $$ Dále je nutné spočítat velikost průmětny (jen pro ujasnění - jedná se o opravdové rozměry, nikoliv rozlišení) \\begin{align} g\_w &= 2t\\tan{\\frac{\\theta}{2}}, \\\\ g\_h &= g\_w \\frac{h}{w}. \\end{align} Z výše připravených hodnot je možné spočítat posuny $\\mathbf{q}\_w$ a $\\mathbf{q}\_h$ mezi pixely v jednotlivých osách \\begin{align} \\mathbf{q}\_w &= \\frac{g\_w}{w - 1} \\mathbf{b},\\\\ \\mathbf{q}\_h &= \\frac{g\_h}{h - 1} \\mathbf{u}\\\\ \\end{align} a souřadnice směru k počátečnímu pixelu \\begin{align} \\mathbf{p}\_{00} &= t \\mathbf{d} - \\frac{g\_w}{2} \\mathbf{b} + \\frac{g\_h}{2} \\mathbf{u}. \\end{align} Normalizovaný směrový vektor $\\mathbf{r}\_{xy}$ směřující k pixelu $(x, y)$ je pak možné získat pomocí \\begin{align} \\mathbf{p}\_{xy} &= \\mathbf{p}\_{00} + x\\mathbf{q}\_w - y\\mathbf{q}\_h,\\\\ \\mathbf{r}\_{xy} &= \\frac{\\mathbf{p}\_{xy}}{|\\mathbf{p}\_{xy}|}. \\end{align} Bez úhony na obecnosti je možné zvolit $t = 1$.

## Výpočet z transformačních matic

Je možné si vzpomenout na transformační matice ve spojitosti se zobrazovacím řetězcem. Vstupem jsou:

*   viewport matice $\\mathbf{V}$,
*   projekční matice $\\mathbf{P}$,
*   a pohledová matice $\\mathbf{C}$.

Modelovou matici $\\mathbf{M}$ můžeme zanedbat, jelikož budeme pracovat ve světovém souřadném systému. Původní řetězec transformaci \\begin{equation} \\mathbf{p}\_t = \\mathbf{V} \\mathbf{P} \\mathbf{C} \\mathbf{p} \\end{equation} je nutno invertovat. Pozici kamery $\\mathbf{o}$ ve světových souřadnicích je možné získat jako \\begin{equation} \\mathbf{o} = \\mathbf{C}^{-1} \\left\[0, 0, 0, 1\\right\]^T \\end{equation} a souřadnici pixelu $\\mathbf{s}\_{xy}$ ve světových souřadnicích kde $x$ a $y$ jsou indexy daného pixelu \\begin{equation} \\mathbf{s}\_{xy} = \\mathbf{C}^{-1} \\mathbf{P}^{-1} \\mathbf{V}^{-1}\\left\[x, y, 0, 1\\right\]^T. \\end{equation} Směrový vektor je nakonec možné jednoduše spočítat \\begin{align} \\mathbf{p}\_{xy} &= \\mathbf{s}\_{xy} - \\mathbf{o},\\\\ \\mathbf{r}\_{xy} &= \\frac{\\mathbf{p}\_{xy}}{|\\mathbf{p}\_{xy}|}. \\end{align} Je možné postupovat libovolným způsobem, výsledkem je mechanismus, který umožní generovat primární paprsky dané dvěma vektory - pozicí kamery $\\mathbf{o}$ a normalizovaným směrem paprsku $\\mathbf{r}\_{xy}$