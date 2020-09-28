
# Barva
V této části je krátce popsán kolorimetrický experiment a jsou zde uvedeny nejznámější barevné prostory.

## Kolorimetrický experiment

Výchozím bodem kolorimetrie je kolorimetrický experiment z roku 1928 provedený Williamem Davidem Wrightem \[1\] na základě testování s 10 účastníky a Johnem Guildem z roku 1932 \[2\] se 7 účastníky. Experiment měl následující průběh - před účastníkem experimentu jsou dvě pole:

*   **referenční pole**, do kterého svítí monochromatické světlo; monochromatické světlo má ve svém spektru má pouze jednu vlnovou délku
*   na druhé straně je **testovací pole**, do kterého svítí 3 světla a účastník experimentu mění intezitu těchto 3 světel tak, aby výsledná barva kterou vidí odpovídala barvě monochromatického světla v referenční oblasti

Výsledkem tohoto kolorimetrického experimentu jsou tzv. srovnávací funkce, které pro každou vlnovou délku referenčního světla udávají intezity světel v testovací oblasti (jak je nastavit aby vznikla barva referenčního světla).

![srovnávací funkce](/img/color/CIE1931_RGBCMF.svg)

Srovnávací funkce, jaké intenzity barev jsou nutné pro vytvoření dané vlnové délky, záporné hodnoty u funkce r (red) vysvětleny níže
{: class="title" }

Na základě těchto srovnávacích křivek je postaven barevný model CIE RGB. V určité části jsou srovnávací funkce záporné, světlo by tedy mělo mít zápornou intenzitu, což je ale fyzicky nemožné. Záporné hodnoty jsou důsledkem faktu, že ne pro všechna monochromatická světla je možné nastavit 3 světla tak, aby odpovídala referenční barvě. To je vyřešeno tak, že do referenční části experimentu se přidají 3 světla totožná se světly v testovací oblasti a pomocí nich je možné upravovat referenční barvu. Nakonec je potřeba přidanou intenzitu odečíst od intenzit světel v testovací oblasti, ovšem tím se křivky dostávají do záporných hodnot.

The transferred primary appears with a negative coefficient in the result. As the spectrum locus lies completely outside the colour triangle for any set of real primaries, this procedure of adding one of the primaries to the colour under test and matching the combination by means of the others is necessary in all measurements on the spectrum. \[2\]

### CIE XYZ

Jelikož jsou záporné hodnoty problematické, byl originální model CIE RGB transformován tak, aby byly všechny srovnávací funkce kladné a hodnota funkce $y$ je identická s luminositou monochromatických světel (jas). Takto vznikl nový model nazvaný CIE XYZ. Světla XYZ jsou ovšem pouze teoretickým experimentem, fyzicky je nelze vyrobit.

![CIE XYZ](/img/color/CIEXYZ.svg)

Transformované křivky pro CIE XYZ
{: class="title" }

Aby bylo možné s barevným prostorem CIE XYZ lépe pracovat, lze souřadnice XYZ normalizovat a zavést prostor CIE xyY. Platí tedy $x + y + z = 1$ a pro identifikaci barvy je třeba znát pouze 2 souřadnice, třetí je možné dopočítat. Zároveň je třeba znát pouze jednu hodnotu z původních nenormalizovaných XYZ pro transformaci z xyY zpět do XYZ - k tomu se nejčastěji využívá souřadnice Y (jas).

![Model CIE XYZ](/img/color/xyz.png){: class="natural" }

CIE XYZ ve 3D, [[img src](https://sudonull.com/post/126584-About-color-spaces)]
{: class="title" }

### CIE xyY

Za předpokladu konstatního jasu, je možné zobrazit barevný prostor CIE xyY (resp. jeho řez) do roviny (proto se často místo CIE xyY mluví o CIE xy). Takto vznikne chromatický diagram. Na křivce, která se táhne po obvodu diagramu se nachází monochromatická světla viditelného spektra. Uvnitř diagramu jsou všechny barvy viditelné lidským okem a zároveň to jsou barvy, které lze získat kombinací monochromatických světel na obvodu.

![CIE xy](/img/color/CIExy.svg)

Chromatický diagram
{: class="title" }

Lze vybrat dva body v chromatickém diagramu a jim odpovíající monochromatická světla. Posunem po přímce mezi těmito body je možné získat všechny kombinace barev těchto dvou světel. Přidáním třetího světla lze získat všechny barvy uvnitř takto ohraničeného trojúhelníku. Tento trojúhelník se nazývá barevný gamut. Zásadním faktem je, že není možné pokrýt celý chromatický diagram pomocí 3 světel, proto se vyskytovaly v originálních srovnávacích křivkách záporné hodnoty - bylo vyžadováno posunutí barev "dovnitř" barevného gamutu.

![Bervný gamut](/img/color/gammut.svg)

CIE xy a 3 světly ohraničený barevný gamut
{: class="title" }

### CIE LAB a HCL

CIE xyY (CIE XYZ) není perceptuálně uniformní barevný prostor, ovšem nelineární transformací lze získat CIE LAB, který již perceptuálně uniformní je.

CIE LAB je takový barevný prostor, kde osa $L$ reprezentuje jas barvy, osa $a$ jde od zelené do červené, osa $b$ jde od modré do žluté. Tento barevný model neumožňuje dekomponovat barvu na jas/saturaci/barevný odstín, ovšem za použití polárních souřadnic ve stejném prostoru dostaneme model HCL (hue, chroma, luminance) - L zůstává a $a$ a $b$ jsou nahrazeny saturací a odstínem. **Pozor, HCL, HSL a HSV jsou jiné barevné prostory.**

### RGB a CMYK

Barevný prostor RGB v kontextu předchozích barevných prostorů je analogií trojúhelníku v chromatickém diagramu, jedná se o barevný prostor namapovaný na krychli a existuje jeho standardní podoba s názvem sRGB. Jedná se o aditivní barevný model, přirozeným doplňkem tohoto barevného modelu je subtraktiní model CMY. Teoreticky je přecházení mezi RGB a CMY jednoduché, pro praktický tisk/zobrazení na display je převod mezi těmito prostory komplikovanější, neboť CMYK používaný pro tisk (s přidanou černou K) stejně tak RGB musí brát v potaz zobrazovací vlastnosti tiskárny či obrazovky pro korektní zobrazení barev.

## Jiné aplikace nad barevnými prostory

TODO

---

## Literatura

1.  Wright, W.D., 1929. A re-determination of the trichromatic coefficients of the spectral colours. Transactions of the Optical Society, 30(4), p.141.
2.  Guild, J., 1931. The colorimetric properties of the spectrum. Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character, 230(681-693), pp.149-187. [doi:10.1098/rsta.1932.0005](https://royalsocietypublishing.org/doi/10.1098/rsta.1932.0005)

Obrázky pochází z [CIE 1931 color space na Wikipedii](https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_RGB_color_space)
