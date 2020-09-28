# Rasterizace a raytracing

V následujících částech se budeme věnovat práci s 3D grafikou v Blenderu. Na úvod je zde krátký přehled termínů, se kterými se lze často setkat. Popis v této části by měl v krátkosti usnadnit pochopení, jak věci fungují, když se budeme bavit o generování obrazu.

Následující část silně zjednodušuje celou problematiku za účelem umožnění jednoduššího pochopení.

Chci vygenerovat obraz realistické scény. Jak na to? Budeme se bavit o prostoru, tedy **scéně**, která bude obsahovat **objekty**, které mají nějaký tvar - **geometrii**. Pro popis geometrie bude fajn zvolit takový způsob, který se bude dobře strojově reprezentovat.

Je třeba nějakým obecným způsobem popsat **materiály** a **textury** jednotlivých objektů a na závěr bude třeba doplnit **světelné zdroje**.

Nakonec přijde to hlavní - je třeba se zabývat způsobem generování obrazu. V zásadě máme na výběr ze dvou možných postupů:

*   budeme se snažit o aproximaci simulace šíření světla scénou, prakticky budeme pracovat s paprsky světla, které se budou scénou šířit, těmto metodám se říká globální osvětlovací metody a mezi ně se řadí **ray tracing**, potažmo se pravděpodobně setkáte s metodou jménem **path tracing**
*   na druhou stranu je možné využít **rasterizaci**, metodu, která byla dlouho mainstreamovou metodou zobrazování 3D grafiky, pomohla modelovat podobu prvních GPU; proces rasterizace se snaží na obrazovce zobrazit jednotlivá geometrická primitiva a používá řadu triků, aby se přiblížila kvalitě obrazu vytvořeného pomocí raytracingu

Pro zájemce doporučuji projít [Raytracing vs Rasterization](http://www.scarydevil.com/~peter/io/raytracing-vs-rasterization.html) - Professer Philipp Slusallek of the University of Saarbruecken and chief scientist David Kirk of nVidia at GameStar.de - nejedná se o nikterak hluboký rozhovor, je možné si na jeho základě udělat určitou představu o porovnání těchto dvou zobrazovacích metod.

V souvislosti se způsobem generování obrazu není možné minout termín **rendering engine**, což je ta část progamu, která je za vykreslení zodpovědná - v Blenderu jich najdeme několik, budeme se bavit zejména o enginu Cycles (path tracer) a možná občas narazíme na Eevee (rasterizace).

V předchozím popisu jsem záměrně vynechal věci jako jsou částicové systémy, enviromentální mapy, atp. Konceptuálně se jedná o věci spadající do některé z kategorií uvedených výše a blíže se k nim dostaneme v dalších částech.

Konec terminologického okénka.

TODO 