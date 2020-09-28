# Info

*   Téma semestrální práce se každoročně [nachází na courses](https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html).
*   Hodnotí se podle pravidel [zde](https://courses.fit.cvut.cz/BI-MGA/classification/index.html#_kritéria-hodnocen%C3%AD)
*   O změnách v plánu vždy informuji včas mailem.

Na posledním cvičení proběhne prezentace vytvořených prací v SAGElabu, informace ohledně prezentací (jak prezentovat, co použít za nástroje) budou uvedeny na cvičení v týdnu, kdy proběhne galerie 3. úlohy.

## FAQ & Tips

*   **úplnost** odevzdané práce se hodnotí podle dokumentace, nehodnotí se jak to vypadá
*   **kvalita** se hodnotí jen 5 (nebo 8) body ze 17 (nebo 26)
*   pokud nevíte jak napsat dokumentaci, pište ji jako pracovní postup, napište všechno, co vás napadne
*   k práci pište dokumentaci ve formátu .adoc
*   dělejte si screenshoty během práce a ty použijte v dokumentaci
*   pokud nechcete dělat screenshoty, tak pracujte tak, abyste se mohli vrátit k předchozímu stavu (průběžné verze, git lfs...)
*   **nezapomeňte na zdroje u fotografií, které jste sami nevyfotili**
*   u vlastních fotografií uveďte, že se jedná o vaše vlastní fotky a pokud můžete, prosím dopište, čím jste je fotili
*   zapisujte si časy, jak dlouho nad projekty strávíte
*   zálohujte, zálohujte a zálohujte, fail harddisku je nepříjemná věc, stejně tak některé programy mají tendenci padat v tu nejméně vhodnou chvíli
*   sežeňte si dostatek zdrojového materiálu, připravte si víc různých snímku ke stejnému tématu
*   parodie, staira a pod. se cení, nebuďte ale nevkusní
*   horní limit složitosti není
*   ulehčete si práci, když budete fotografie pořizovat, zamyslete se nad stíny, odlesky, perspektivou atd.
*   pište mail nebo se nebojte googlit, když nebudete vědět
*   co je to [blueprint?](https://en.wikipedia.org/wiki/Blueprint)
*   dokumentace s 10-20 fotkami je plně dostatečující
*   zdokumentujte obě retuše/všechny metody vektorizace
*   prosím, dělejte dokumentaci user-friendly

## GitLab
Doporučuju dodržet tuto strukturu:

### Repozitář s dokumentací

<dl class="tree dir">
    <dt class="dir gimp">bitmap
        <dl class="tree">
            <dt>zdrojové_snímky.png/jpg/... + dokumentační_obrázky.png/jpg/...</dt>
            <dd>zdrojové snímky a obrázky z dokumentace</dd>
            <dt>2 hotové retuše.png/jpg/...</dt>
        </dl>
    </dt>
    <dt class="dir inkscape">vector
        <dl class="tree">
            <dt>zdrojové_snímky.jpg/png/... + dokumentační_obrázky.jpg/png/...</dt>
            <dd>zdrojové snímky a obrázky z dokumentace</dd>
            <dt>3 hotové vektorizace.svg</dt>
        </dl>
    </dt>
    <dt class="dir d3">3D
        <dl class="tree">
            <dt>zdrojové_snímky.jpg/png/... + dokumentační_obrázky.jpg/png/...</dt>
            <dd>zdrojové snímky a obrázky z dokumentace</dd>
            <dt>alespoň 3 výstupní rendery.jpg/png/...</dt>
        </dl>
    </dt>
    <dt class="gimp">dokumentace1.adoc</dt>
    <dd class="gimp">dokumentace k oběma provedeným retuším</dd>
    <dt class="inkscape">dokumentace2.adoc</dt>
    <dd class="inkscape">dokumentace ke třem provedeným vektorizacím</dd>
    <dt class="d3">dokumentace3.adoc</dt>
    <dd class="d3">dokumentace k modelování atd.</dd>
</dl>

### Podklady pro galerii
Nedávejte prosím do rootu 4K a 8K soubory, dejte je jen do vnitřních adresářů výše (bitmap, 3D), do kořenového adresáře dejte zmenšenou verzi (okolo HD rozlišení). <strong>Dodržujte velká a malá písmena i u koncovek</strong> - obzvláště pozor na Windows, typicky ukládá jpeg jako .JPG (s velkými písmeny). Všechna uvedená jména jsou závazná.

<dl class="tree">
    <dt class="gimp">name.txt</dt>
    <dd class="gimp">"název předmětu", je tím myšlen název vašeho semestrálního projektu</dt>
    <dt class="gimp">bitmap.jpg</dt>
    <dd class="gimp">vyberte jednu z dvou retuší, které jste vytvořili, případně zmenšete</dd>
    <dt class="gimp">bitmap_src.jpg</dt>
    <dd class="gimp">vyberte jednu zdrojovou fotku, případně zmenšete</dd>
    <dt class="gimp">tn_bitmap.jpg</dt>
    <dd class="gimp">soubor bitmap.jpg zmenšete na velikost požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="gimp">tn_bitmap_src.jpg</dt>
    <dd class="gimp">soubor tn_bitmap_src.jpg zmenšete na velikost požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="gimp">info.txt</dt>
    <dd class="gimp">texťák s obsahem STRÁVENÝ_ČAS;POUŽITÝ_PROGRAM;KOMENTÁŘ pro retuš</dd>
    <dt class="inkscape">vektor.svg</dt>
    <dd class="inkscape">vyberte jednu vektorizaci, kterou jste vytvořili</dd>
    <dt class="inkscape">vektor_src.jpg</dt>
    <dd class="inkscape">vyberte jednu zdrojovou fotku, případně zmenšete</dd>
    <dt class="inkscape">tn_vektor.png</dt>
    <dd class="inkscape">soubor vektor.svg převeďte do formátu png s velikostí požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="inkscape">tn_vektor_src.jpg</dt>
    <dd class="inkscape">soubor vektor_src.jpg zmenšete na velikost požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="inkscape">info2.txt</dt>
    <dd class="inkscape">texťák s obsahem STRÁVENÝ_ČAS;POUŽITÝ_PROGRAM;KOMENTÁŘ pro vektorizaci</dd>
    <dt class="d3">3d.jpg</dt>
    <dd class="d3">jeden vámi vytvořený render o ne příliš velkém rozlišení</dd>
    <dt class="d3">3d.zip</dt>
    <dd class="d3">výsledný projekt (např. .blend soubor, textury, bitmapa prostředí)</dd>
    <dt class="d3">3d_src.jpg</dt>
    <dd class="d3">render s vloženou postavou vloženou postavou</dd>
    <dt class="d3">tn_3d.jpg</dt>
    <dd class="inkscape">soubor 3d.jpg zmenšete na velikost požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="d3">tn_3d_src.jpg</dt>
    <dd class="inkscape">soubor 3d_src.jpg zmenšete na velikost požadovanou na <a href="https://courses.fit.cvut.cz/BI-MGA/classification/zadani.html">courses</a></dd>
    <dt class="d3">info3.txt</dt>
    <dd class="inkscape">texťák s obsahem STRÁVENÝ_ČAS;POUŽITÝ_PROGRAM;KOMENTÁŘ pro modelování</dd>
</dl>
