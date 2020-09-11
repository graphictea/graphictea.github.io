# Monadické operace

Samotné implementace operací se nachází v třídě Editor - [monadic.cpp](../src/monadic.cpp), [Editor.hpp](../src/editor.hpp). Všechny operace jsou demonstrovány na obrázku `cica.png`. Následující operace jsou naimplementovány:

## Negativ
```
open cica.png
negate
save png negate
histogram histonegate
```
<img src="../cica.png" width="200">
<img src="negate.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histonegate.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="negateduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histonegateduck.png" width="200">

## Prahování
```
open cica.png
threshold 0.5
save png threshold
histogram histothres
```
<img src="../cica.png" width="200">
<img src="threshold.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histothres.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="threshduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histothreshduck.png" width="200">


## Jas
```
open cica.png
brightness 0.1
save png brightness
histogram histobrightness
```
<img src="../cica.png" width="200">
<img src="brightness.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histobrightness.png" width="200">

```
brightness 0.2
```

<img src="duck.png" width="200">
<img src="brightnessduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histobrightnessduck.png" width="200">


Hodnoty v histogramu v pravo jsou mrňavé dole v porovnáním s hodnotami vpravo...

## Kontrast
```
open cica.png
contrast 0.5
save png contrast
histogram histocontrast
```
<img src="../cica.png" width="200">
<img src="contrast.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histocontrast.png" width="200">

```
brightness 1.25
```

<img src="duck.png" width="200">
<img src="contrastduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histocontrastduck.png" width="200">

## Gamma
```
open cica.png
gamma 2
save png gamma
histogram histogamma
```
<img src="../cica.png" width="200">
<img src="gamma.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histogamma.png" width="200">

```
gamma 1.75
```

<img src="duck.png" width="200">
<img src="gammaduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histogammaduck.png" width="200">

## Nelineární kontrast
```
open cica.png
nonlincontrast 0.5
save png nonlincontrast
histogram histononlinear
```
<img src="../cica.png" width="200">
<img src="nonlincontrast.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histononlinear.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="nonlincontrastduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histononlinearduck.png" width="200">

## Logaritmická škála
```
open cica.png
logscale 8
save png logscale
histogram histolog
```
<img src="../cica.png" width="200">
<img src="logscale.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histolog.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="logscaleduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histologduck.png" width="200">

## Kvantizace
```
open cica.png
quantize 5
save png quantize
histogram histoquantize
```
<img src="../cica.png" width="200">
<img src="quantize.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histoquantize.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="quantizeduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histoquantizeduck.png" width="200">

## Ekvalizace
```
open cica.png
equalize
save png equlized
histogram histoequlized
```
<img src="../cica.png" width="200">
<img src="equalized.png" width="200">
<br>
<img src="histogram.png" width="200">
<img src="histoequlized.png" width="200">
<br>
<img src="duck.png" width="200">
<img src="equalizedduck.png" width="200">
<br>
<img src="histoduck.png" width="200">
<img src="histoequalizedduck.png" width="200">

## Něco navíc...
Umí to kreslit histogram do terminálu! Implementace v [Editor.cpp](../src/editor.cpp) bude chtít trochu refaktorizace.

<img src="screen.png" width="300">
