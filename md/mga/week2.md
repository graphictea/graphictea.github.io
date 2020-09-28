# Vrstvy a masky

Pokud jste se dosud nesetkali s žádným grafickým editorem, tak je třeba se seznámit s konceptem vrstev a masek. Na co se podívat:

*   [Layer modes in GIMP docs](https://docs.gimp.org/en/gimp-concepts-layer-modes.html)
*   [layer mask tutorial by Pat David](https://www.gimp.org/tutorials/Layer_Masks/)

## Vrstvy

Často bude cílem složit více samostatných obrázků dohromady. Za tímto účelem řada editorů pracuje s vrstvami, které jsou následně v kombinaci s maskami a poloprůhledností složeny dohromady. Operaci která bude aplikována při skládání snímků je možné zvolit.

![](/img/mask/layer.svg)

*   každá vrstva může mít **masku** či **alfa kanál**, které rozhodují o poloprůhlednosti
*   vrstvy lze skládat odpředu dozadu, či naopak, postupy se liší provedením operací

## Základní nástroje pro výběr

Základním úkolem je často izolovat objekt ze scény, aby ho bylo možné vložit do scény jiné. Jednoduchý postup pro vyjmutí objektu ze scény:

1.  použít vybraný nástroj pro výběr
    *   **laso** - vybranou oblastí je polygon
    *   **magická hůlka** - vybírá oblast dle barvy/jasu, je možné kombinovat, dobé pro kontrastní oblasti
    *   **nůžky** - umožňuje přichytávání
2.  Select > Toggle quick mask pro přechod do módu umužňující rychlou úpravu masky
3.  dodatečné úpravy vybrané oblasti pomocí štětce nebo tužky
4.  copy-paste do nové vrstvy

## Výběr pomocí masky

Copy-paste postupem dojde ke ztrátě jakékoliv původní informace a výřez je možné pouze zmenšovat, není možné se vrátit zpět. Tomu je možné předejí pomocí masky:

1.  vezmu fotografii ze které budu vyřezávat [src](https://www.pexels.com/photo/paper-boats-on-solid-surface-194094/)
    
    ![gui](/img/mask/sc1.png){: class="natural"}
    
2.  vyberu si nástroj pro výběr

    ![nástroje pro výběr](/img/mask/sc2.png){: class="natural"}

4.  nahrubo vyberu objekt
    
    ![výběr](/img/mask/sc3.png){: class="natural"}
    
5.  v menu `Select` zvolím `Toggle Quick Mask`
    
    ![toggle quick mask](/img/mask/sc4.png){: class="natural"}
    
6.  po přepnutí
    
    ![quick mask](/img/mask/sc5.png){: class="natural"}
    
7.  v režimu úpravy masky vezmu vhodný štětec/tužku/gumu...
    
    ![drawing tools](/img/mask/sc6.png){: class="natural"}
    
8.  ...a s vhodným nastavením poloměru, tvrdosti atd. opravím špatně vybrné části
    
    ![drawing tools](/img/mask/sc7.png){: class="natural"}
    
9.  když jsem s úpravou spokojený, přepnu se zpět z režimu `Quick Mask`
    
    ![toggle quick mask again](/img/mask/sc8.png){: class="natural"}
    
10.  v pravém dolním rohu vyberu ikonu masky
    
    ![create mask](/img/mask/sc9.png){: class="natural"}
    
11.  vyskočí dialog, zvolím možnost `Selection` a potvrdím `Add`
    
    ![create mask](/img/mask/sc10.png){: class="natural"}
    
12.  a dostanu izolovaný objekt
    
    ![final image](/img/mask/sc11.png){: class="natural"}