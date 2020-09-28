# Úvod k raytracingu

Na úvod postačí jednoduchá představa: cílem je zobrazit, co vidí pozorovatel dívající se z určitého místa na scénu reprezentovanou geometrickými útvary. Zjistit, jak scéna vypadá z určitého místa, znamená zjistit jaké paprsky se k pozorovateli ze scény odrazí.

![Šíření světla scénou](/img/introgi/lights.svg)

Šíření světla scénou na cestě k pozorovateli, oranžové paprsky značí přímé a zelené nepřímé osvětlení, modré jsou odražené do směru pozorovatele a fialové jsou lomené paprsky, šedé naznačují směry šíření po odrazu
{: class="title" }


Pro jednoduchost je v této a následujících částech uvažována pouze geometrie skládající se z trojúhelníků. Zdrojem paprsků budou nejčastěji plošné a bodové světelné zdroje.

*   paprsek který docestoval k pozorovateli se na cestě ze světla potenciálně několikanásobně odrazil
*   mnoho paprsků (potenciálně většina paprsků) vycházejících ze světla po násobných odrazech pozorovatele zcela mine a tak nemá smysl se jimi zabývat
*   libovolné místo $M$ ve scéně je osvětleno paprsky, které se odrazily ze všech ostatních ploch, které jsou z místa $M$ viditelné
*   příspěvek osvětlení odraženého z ostatních ploch může být v porovnání s přímým osvětlením malý, ale přesto zaznamenatelný

Kvůli tomu, že řada paprsků s počátkem ve světle po násobných odrazech pozorovatele mine, je výhodnější se na celou situaci dívat z opačné strany: je možné sledovat paprsky vržené z místa pozorovatele (neznamená to nic jiného, než otočit šipky na obrázku). Někoho by mohlo zarazit, jak je možné, že lze směr paprsků beztrestně obrátit. Otočení je možné jen na základe několika předpokladů které souvisí se způsobem popisu vlastností povrchů - více až později v částech věnující se BRDF.
