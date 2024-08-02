import re
import os
import json

# Input text
text = '''(1) Všechno, čeho si přeješ dosáhnout postupem času, můžeš mít
už nyní, nebudeš-li to sám sobě odpírat. A to bude, jestliže všechnu
minulost pustíš z mysli, budoucnost svěříš prozřetelnosti a jenom
svůj přítomný život zařídíš ve smyslu zbožnosti a spravedlnosti:
zbožnosti, abys ochotně přijímal svůj úděl, neboť tobě ho přidělila
příroda a tebe zase jemu; ve smyslu pak spravedlnosti, abys
svobodně a bez okolků mluvil pravdu a jednal podle zákona a
přiměřeně ceně věcí; a v tom si nedávej bránit ani špatností ani
míněním a řečí jiných, ani pocity své tělesné schránky, neboť ty se
týkají její trpící části.
Jestliže aspoň teď, kdy už jsi konečně na odchodu, budeš mít v
úctě toliko svůj rozum a to, co je v tobě božského, a všechno ostatní
pustíš z mysli, a jestliže se nebudeš děsit toho, že se tvůj život
jednou skončí, nýbrž toho, že jsi ještě nezačal žít ve shodě s
přírodou, pak se staneš člověkem hodným vesmíru, který tě zplodil,
a přestaneš být cizincem ve své vlasti, přestaneš se divit věcem,
které se dějí každým dnem, jako něčemu nenadálému a přestaneš
lpět na tom a onom.
(2) Bůh vidí všechny duše v jejich nahotě – bez jejich hmotných
nádob, obalů a roušek, neboť svým čirým rozumem je ve styku s tím
čirým, co se z něho samého do nich vyronilo a přelilo. Jestliže si také
ty zvykneš jednat podobně, zhostíš se mnohého nepokoje. Neboť
kdo dovede nevidět tu trochu masa, kterou je obklopen, zdalipak se
bude obírat uvažováním o oděvu, obydlí, slávě a jiných takových
cestách a lidských okázalostech?
(3) Jsou tři věci, ze kterých se skládáš: tělo, živočišná duše a
rozum. První dvě z nich jsou potud tvoje, že se musíš o ně starat;
teprve třetí část je v pravém slova smyslu tvá. Jestliže tedy odloučíš
od sebe, tj. od svého myšlení, všechno to, co činí nebo říkají jiní
nebo co jsi kdy sám učinil nebo řekl a co tě v budoucnosti
zneklidňuje, a všechno, co na tobě ulpívá z tvého těla, v němž vězíš,
nebo z tvé živočišné duše, která je s ním sloučena, a co je tedy
mimo tvou vůli, a všechno, co ti hrne do cesty vír dění kolem tebe,
tak aby tvá myslící síla, vymaněna z moci osudu, žila sama sobě
čistá a volná, aby uskutečňovala spravedlnost, byla spokojena s tím,
co se přihází, a mluvila pravdu – jestliže odloučíš, pravím, od této
své vůdčí části všechno, co na ní ulpělo z náruživých sklonů a co je
dosud v lůně času nebo již v minulosti, a sebe připodobníš oné
Empedokleově kouli, krásně zaokrouhlené a šťastné svou
uzavřeností, a dokonale se naučíš prožívat jenom ten čas, který
doopravdy žiješ, to je přítomnost, teprve potom budeš moci alespoň
zbytek svého života až do smrti trávit bez nepokoje a v dobré vůli a
smíru se svým daimónem.1
1. Empedoklés z Akragantu (na Sicílii), řecký básník, filozof, lékař a fyzik v 5. stol. př. n. l.
(4) Mnohokrát jsem se podivil tomu, že každý má sice sebe sama
raději než všechny ostatní, ale že si svého mínění o sobě váží méně
než mínění ostatních lidí. Kdyby přistoupil k někomu z nás bůh nebo
rozumný učitel a nařídil mu, aby sám u sebe nepřemýšlel a
neuvažoval o ničem, co by nebyl ochoten vyslovit zároveň i nahlas,
jistě by to nevydržel ani jeden den. O tolik více dbáme svých
bližních, co si asi budou o nás myslet, než svého vlastního soudu.
(5) Jak jen mohli bohové, kteří všechno dokonale a lidumilně
zařídili, jednu věc přehlédnout, totiž tu, že někteří lidé, a to zvláště
dobří, kteří jsou, abych tak řekl, v nejvroucnějším vztahu k božstvu a
zbožnými skutky a posvátnou službou božstvu se stali co nejvíce
jeho důvěrníky – že i ti, jakmile jednou zemřou, nikdy se sem už
nevracejí a nadobro zanikají? – Buď jist, jestli je tomu opravdu tak,
že kdyby to mělo být jinak, byli by to jistě učinili! Neboť kdyby to bylo
spravedlivé, bylo by to i možné, a kdyby to bylo ve shodě s přírodou,
byla by to příroda tak zařídila. Z toho tedy, že tomu tak není (není-li
tomu přece tak), čerpej přesvědčení, že se tak nemělo stát. Vždyť i
sám vidíš, že se takovým mudrováním jen hádáš s bohem; takto
bychom přece s bohy mluvit neměli, ani kdyby nebyli nejlepší a
nejspravedlivější. Jsou-li však takoví, jistěže při pořádání světa
nedopustili nic, co by bylo zanedbáním spravedlnosti a rozumu.
(6) Zvykej si konat i to, nač si netroufáš! Vždyť i levice, k ostatním
výkonům nedostatkem zvyku neobratná, otěží vládne rázněji než
pravice. Přivykla tomu.
(7) Měj na mysli, v jakém stavu má být tvé tělo i duše, až tě
zastihne smrt; a krátkost života, bezednou propast času za sebou i
před sebou a vetchost veškeré hmoty!
(8) Pozoruj činné síly věcí bez jejich hmotných obalů a cíle lidských
činů; uvažuj, co je bolest a rozkoš, smrt a sláva; kdo je vinen svým
vlastním nepokojem; a že všechno je jen představa.2
2. „že všechno je jen představa“: Srov. aforismus 22 této knihy.
(9) Pohotovým užíváním svých zásad máš se podobat pěstnímu
zápasníkovi, nikoli šermíři. Neboť odloží-li šermíř meč, který užívá, je
zničen; naproti tomu zápasník má ruku pohotově vždycky a
nepotřebuje nic jiného než ji sevřít v pěst.
(10) Hledej pravou jakost věcí tím, že je rozbíráš v hmotu, činnou
sílu a účel.
(11) Člověk má možnost nečinit nic jiného než to, co bůh mu
schválí, a ochotně přijímat všechno, co bůh mu uděluje.
(12) To, co se děje podle přírodního řádu, nelze vytýkat ani bohům,
neboť nechybují v ničem ani úmyslně, ani neúmyslně, ale ani lidem,
neboť chybují toliko neúmyslně. Proto nelze činit výtky nikomu.
(13) Jak směšným cizincem je ve světě ten, kdo se diví kterékoli
události v životě!
(14) Buďto je nutnost osudu a nezměnitelný řád, nebo shovívavá
prozřetelnost, anebo náhodný a bezhlavý zmatek. Je-li tedy
nezměnitelná nutnost, proč se jí vzpíráš? Je-li prozřetelnost
náchylná k shovívavosti, učiň sebe hodným pomoci boží. A je-li
zmatek nikým neovládaný, buď rád, že máš v takovém příboji sám v
sobě vůdce – rozum! A i když tě příboj bude strhávat, jen ať si
strhává tvé chabé tělo, tvou živočišnou duši a ostatní; neboť tvůj
rozum nestrhne!
(15) Světlo září, dokud lampa nezhasne, a dříve svou zář neztratí; a
v tobě by měla pravda, spravedlnost a rozvaha vyhasnout
předčasně?
(16) Vnukne-li ti někdo představu, že chybil, ptej se v duchu:
„Jakpak vím, zdali je to chyba?“ – Ale i když opravdu chybil, tu si
pomysli: „Sám se odsoudil,“ a potom: „Podobá se tomu, kdo sám
sobě drásá tvář!“
Kdo nechce, aby špatný chyboval, podobá se tomu, kdo nechce,
aby fíkovník měl ve svých plodech šťávu, aby nemluvňata vrněla,
aby kůň řehtal a aby se nestalo i tolik jiných přirozených nutností.
Neboť co si má počít ten, kdo má takové sklony? Máš-li k tomu
odvahu, vyleč ho z nich.
(17) Není-li to příkaz povinnosti, nečiň to; není-li to pravda, neříkej
to! Neboť tvá vůle má být zcela ve tvé moci.
(18) Vždycky přihlížej k celku každé věci: co je právě ona věc, která
ti vnuká představu, a pak si ji objasni rozborem v její činnou sílu, v
její hmotu, účel a čas, ve kterém bude muset zaniknout.
(19) Konečně už pochop, že máš v sobě cosi ušlechtilejšího a více
božského, než jsou ony věci, které budí tvé náruživosti a cloumají
tebou jako loutkou. A rozjímej: Jaképak je právě teď mé smýšlení?
Není to strach? Není to podezření? Nejsou to chtíče nebo něco
jiného podobného?
(20) Zaprvé: nic nečiň nazdařbůh a neúčelně! Zadruhé: svou
činností nesměřuj k žádnému jinému cíli než k obecnému
prospěchu!
(21) Pamatuj, že zanedlouho nebude z tebe nikde nic, ani ze žádné
z těch věcí, které nyní vidíš, ani ze žádného z těch lidí, kteří nyní žijí.
Neboť všechny věci jsou přírodou určeny k přeměně a k přetvoření a
k zániku, aby je jiné mohly střídat.
(22) Všechno záleží na tvé představě, a ta je ve tvé moci. Zbav se
tedy, jestli chceš, své představy a jako plavci, který objel předhoří,
objeví se ti smavá hladina, všechno klidné a nezvlněný záliv.
(23) Jedna každá činnost, ať kterákoli, jež se ukončí včas, nic zlého
neutrpí tím, že se skončila; a ani ten, kdo tuto činnost provedl, nic
zlého netrpí právě tím, že se skončila. Podobně tedy i souhrn všech
činností, to je život, kdykoli se ukončí včas, nic zlého netrpí tím, že
se skončil; a ani ten, kdo tuto řadu včas ukončil, tím nezakusí nic
zlého. A onen pravý čas a konečnou mez určuje příroda, leckdy také
lidská přirozenost, jak tomu bývá v stáří, ale pokaždé vesmírná
příroda; neboť právě tím, že se její části přeměňují, vesmírný celek
si uchovává květ nehynoucího mládí. Ale krásné a včasné je
vždycky jen to, co prospívá celku; tedy ukončení života není
jednotlivci zlem a není ani hanbou, protože se děje nezávisle na naší
vůli, a není na újmu obecného dobra, ba spíše je dobrem, poněvadž
je celku včasné, prospěšné a příhodné. Neboť ten, kdo spěje stejnou
cestou jako bůh i svým smýšlením ke stejnému cíli, takto spěje ruku
v ruce se samým bohem.3
3. Slovní hříčku závěru nelze plně vystihnout.
(24) Toto trojí si máš oživovat v paměti: pokud se týká toho, co činíš
sám – zdali to nečiníš ani nazdařbůh ani jinak, než jak by to sama
Spravedlnost provedla; pokud se pak týká toho, co se ti přihází
zvenčí – že se to děje buď čirou náhodou, nebo řízením
prozřetelnosti; ale nesmíš ani na náhodu naříkat, ani prozřetelnost
obviňovat. Zadruhé: jaká je každá bytost od svého početí do svého
oživnutí a od svého oživnutí až do návratu duše k bohu, z jakých
součástí je složena a v jaké látky se rozloučí. Zatřetí: kdyby ses
náhle vznesl vysoko do ovzduší a odtamtud popatřil na lidské věci a
jejich rozmanitost, a až bys zároveň přehlédl i všechno tvorstvo,
které kolem dokola bydlí ve vzduchu i v éteru, že bys pocítil nechuť,
a ať by ses tam povznesl kolikrátkoli, uviděl bys znova a znova totéž:
stejnotvářnost, dočasnost. A k tomu: všechno jen pouhý dým!
(25) Vyhosti domněnku, a jsi zachráněn! Kdo ti brání se jí zbavit?
(26) Kdykoli býváš něčím roztrpčen, pak jsi zapomněl, že se
všechno děje podle vesmírné přírody, že provinění jiného se netýká
tebe, a posléze i na to, že všechno, co se děje, vždycky se takto
dálo a bude dít a už nyní se všude děje. Zapomněl jsi, jak blízké je
příbuzenství člověka s veškerým lidským pokolením, nikoli snad
společným podílem v krvi nebo rodu, nýbrž rozumu! Zapomněls také
na to, že rozum jednoho každého z nás je bůh a že náš rozum je
»výron« z něho; i na to, že nikomu vůbec nic nenáleží, nýbrž že se
každému i jeho dítěte, i jeho těla, ba i jeho živočišné duše dostalo
»odtamtud«; a konečně že všechno je jen domněnka a že každý z
nás jen přítomný čas prožívá a jen toho pozbývá.
(27) Neustále si připomínej lidi, kteří se něčím přespříliš rozčilovali
nebo kteří byli nad jiné proslulí slávou, neštěstím, nepřátelstvím
nebo jakýmikoli osudy. A potom si pomysli: Kde je nyní to všechno?
Dým a popel a pohádka, anebo už ani pohádka! A zároveň si
vybavuj všechno podobné, jako například jak si vedl Fabius
Catullinus na svém statku nebo Lucius Lupus ve svých sadech nebo
Stertinius v Bajích nebo Tiberius na Caprejích a Velius Rufus – a
vůbec jakékoli lidské zájmy, které se zakládají na klamu. A uvažuj,
jak nicotné je všechno to, po čem tolik bažili, a oč má blíže k filozofii
osvědčování spravedlnosti, rozvahy a neokázalé poslušnosti bohům
při každé příležitosti! Neboť pýcha, která se pyšní pokorou, je pýcha
nejodpornější ze všech.4
4. Ke konci: „pýcha, která se pyšní pokorou“: Epifonéma s aliterací, která se dobře hodí
na císaře Tiheria, jak ho líčí Tacitus.
(28) Těm, kteří se tě ptají: „Kdepak jsi viděl bohy anebo z čeho jsi
poznal, že skutečně jsou, že je máš v takové úctě?“ odpověz:
Zaprvé jsou také zrakem viditelní, a zadruhé ani svou duši jsem
neviděl, a přece ji ctím. Tedy podobně je tomu i s bohy: z projevů
jejich moci, o které se znova a znova přesvědčuji, bezpečně
poznávám, že jsou, a mám je v úctě.5
5. „jsou také zrakem viditelní“: Viz pozn. k VIII 19.
– „z projevů jejich moci... poznávám, že (bohové) jsou“: Takové soudy z účinků na
původce byly ve starověku oblíbené (Sókratův důkaz boží jsoucnosti v Xenofóntových
Vzpomínkách na Sókrata IV 3) a přežily starověk i středověk, až Immanuel Kant
dokázal, že problémy, jako je jsoucnost boží, nesmrtelnost duše nebo svoboda vůle, se
logickému důkazu vymykají, neboť náležejí – jako požadavky našeho mravního vědomí
– sféře jiné, vyšší.
(29) Přihlížet k tomu, co je každá věc sama o sobě jako celek, co je
její hmotná podstata a co její činná síla, a z celé duše činit, co je
spravedlivé, a mluvit pravdu – v tom je spása života. A jestliže řadíš
dobrý čin k dobrému, takže mezi nimi není ani nejmenší mezery, co
jiného z toho vyplyne než radost ze života?
(30) Je jediné sluneční světlo, i když se tříští myriádami stěn a hor a
jiných věcí; je jediná společná pralátka, i když se tříští v myriády těl
vlastní podstaty; je jediná duše, i když je roztříštěna v myriády
bytostí svým způsobem ohraničených; a jediná rozumná duše, i když
se zdá rozdělená. Ostatní součásti řečených věcí, jako například
jejich živočišné duše a jejich tělesné podklady, jsou sice neschopné
citu a vzájemné příchylnosti, a přesto i je udržuje pohromadě
jednotící a soudržná síla. Ale myslící duše svým zvláštním
způsobem tíhne ke všemu sourodému a s ním se spojuje; a tento
společenský pud se roztříštit nedá.
(31) Co by sis přál? Být ustavičně živ? Chceš tedy mít pocity a
pudy, chceš růst a opět přestávat růst, chceš užívat svého hlasu,
chceš přemýšlet? Kterápak z těchto činností se ti zdá žádoucí? Je-li
každá z nich bezcenná, uchyl se k poslednímu: poslouchej rozum a
boha! Ale s tím je v rozporu, jestliže si někdo tyto věci cení a rmoutí
se proto, že jich smrtí pozbude.
(32) Jak skrovný dílek bezmezného a bezedného času je každému
z nás přidělen! Okamžik, a zmizí ve věčnosti. A jak skrovný díl
vesmírné pralátky! Jak skrovný zlomek vesmírné duše! Na jakém
kousíčku zemského celku se to plazíš! Toto všechno měj na paměti
a nic nepokládej za důležité, leč jediné: jednat, jak tě k tomu vede
tvá přirozenost, a přijímat, cokoli ti přináší vesmírná příroda.
(33) Jak užívá rozum sebe sama? Neboť na tom záleží nejvíc!
Všechno ostatní, ať už závisí na tvé vůli nebo nezávisí, je mrtvý a
prázdný dým.
(34) K tomu, aby se na životě nelpělo, může být nejúčinnější
pobídkou, že ti, kteří pokládali rozkoš za dobro a bolest za zlo,
přesto také na životě nelpěli.6
6. Marcus má na mysli Epikúra a jeho školu.
(35) Komu je dobrem jenom to, co se přihází ve svůj čas, a komu je
lhostejné, zdali vykoná více či méně skutků podle správného
rozumu, a komu nezáleží na tom, zdali pozoruje vesmír po delší či
kratší dobu, tomu ani smrt není hrozná.
(36) Člověče, žils jako občan v tomto velkém státě: co ti na tom
záleží, zdali pět či sto let? Neboť zákony měří každému stejně. Co je
tedy na tom hrozného, jestliže tě ze státu odesílá nikoli tyran ani
nespravedlivý soudce, nýbrž příroda, která tě do něho uvedla?
Stejně jako když herce propouští z divadla praetor, který ho přijal do
svých služeb. „Ale ještě jsem neodehrál svých pět dějství, nýbrž jen
tři.“ – Máš pravdu; ale v životě jsou tři dějství celé drama! Neboť kdy
je konec, to určuje onen, kdo byl kdysi původcem tvého stvoření,
jako je nyní tvé rozloučení. Ani tím, ani oním nejsi vinen ty. Odejdi
tedy v dobré vůli! Neboť také ten, kdo tě propouští, je dobré vůle.7
7. – „praetor“: Vypravení her bylo od doby Augustovy úkolem praetorů.
– „je dobrá vůle“: Poslední slova úvah Marka Aurelia připomínají začáteční slova
Kantovy Etiky: Není vůbec nic ve světě, co by se mohlo bez omezení pokládat za
dobré, než jedině dobrá vůle.

'''

# Regular expression to match paragraphs starting with a number in brackets
paragraphs = re.split(r'\(\d+\)', text)

# Directory to save the JSON files
output_dir = "12"
os.makedirs(output_dir, exist_ok=True)

# Pattern to identify notes starting with a number followed by a period
note_pattern = re.compile(r'(\d+\.\s.*)', re.DOTALL)

# Processing and saving each paragraph into a JSON file
for i, paragraph in enumerate(paragraphs[1:], 1):
    cleaned_paragraph = paragraph.strip()
    if cleaned_paragraph:
        # Remove all new line characters
        cleaned_paragraph = cleaned_paragraph.replace('\n', ' ').replace('\r', '')

        # Find the first occurrence of a note and split the paragraph
        match = note_pattern.search(cleaned_paragraph)
        if match:
            main_text = cleaned_paragraph[:match.start()].strip()
            note = cleaned_paragraph[match.start():].strip()
        else:
            main_text, note = cleaned_paragraph, ""

        # Remove the last two letters from the main text
        if len(main_text) > 2:
            main_text = main_text[:-2]

        # Remove the first three letters from the note
        if len(note) > 3:
            note = note[3:]

        # Prepare data for JSON
        paragraph_data = {
            "text": main_text,
            "note": note
        }

        # Save data to JSON file
        json_filename = os.path.join(output_dir, f"paragraph_{i}.json")
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(paragraph_data, json_file, ensure_ascii=False, indent=4)
        print(f"Saved Paragraph {i} to {json_filename}")
