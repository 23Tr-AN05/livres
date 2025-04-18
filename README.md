<html>
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet"/>
<style>
    #search-input {
      width: 300px;
      padding: 10px;
      font-size: 16px;
    }
    .search-result {
      display: none;
      margin-top: 10px;
    }
    .search-result.active {
      display: block;
    }
    .search-result p {
      font-size: 14px;
      background-color: #f9f9f9;
      padding: 5px;
      border-radius: 4px;
    }
    .no-results {
      display: none;
      margin-top: 20px;
      color: red;
      font-weight: bold;
    }
  </style><style>
   #para1 {
	   text-align: center;
	   color: red
   }
 </style>
<style>
  #para2 {
	   text-align: center;
	   color: orange
   }
 </style>
<style>
   #para3 {
	   text-align: center;
	   color: pink 
   }
 </style>
<style>
   #para4{
     text-align:center;
     color: #FF55FF
   }
 </style>
</head><body>
<div class="w3-container">
<h1 style="color:red;"><center>家的图书目录</center></h1>
<p style="size:20px">Ecrivez le titre OU auteur du livre(ou ISBN).</p>
<input class="w3-input w3-border w3-padding" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." type="text"/>
<h1 id="para1"> 法语文学 / 欧洲文学 </h1>
<table class="w3-table-all w3-margin-top" id="myTable">
<tr>
<th>Titre</th>
<th>Auteur</th>
<th>Genre</th>
<th>Édition</th>
<th> ISBN </th>
<th> Placement </th>
</tr>
<tr>
<td>Idée d'une Histoire universelle au point de vue cosmopolitique </td>
<td>Emmanuel KANT</td>
<td>Filosofia</td>
<td> Bordas </td>
<td> 2-04-018061-3 </td>
<td> C1</td>
</tr>
<tr>
<td>Cinq leçons sur la psychanalyse</td>
<td>Sigmund FREUD</td>
<td>Psychanalyse</td>
<td> Petit Bibliothéque Payot </td>
<td> 2-228-30849-8 </td>
<td> C1 </td>
</tr>
<tr>
<td>La ligne verte</td>
<td>Stephen KING</td>
<td> - </td>
<td> J'ai lu </td>
<td> 2-290-30186-8 </td>
<td> C2 </td>
</tr>
<tr>
<td>L École des femmes</td>
<td>Molière</td>
<td>Théâtre</td>
<td>Bordas</td>
<td> 2-04-016050-7 </td>
<td>C2 </td>
</tr>
<tr>
<td>Les Misérables II</td>
<td>Victor HUGO</td>
<td>Littérature FR de XIXe</td>
<td>Livre du poche</td>
<td>-</td>
<td> C2</td>
</tr>
<tr>
<td>Les Misérables III</td>
<td>Victor HUGO</td>
<td>Littératures FR de XIXe</td>
<td>Livre du poche</td>
<td> - </td>
<td> C2</td>
</tr>
<tr>
<td>Les mots immigrés</td>
<td>Eric ORSENNA</td>
<td>Patrimoine / Fiction littéraire</td>
<td>Le livre de poche</td>
<td>978-2-253-94095-1 </td>
<td>C1 -T</td>
</tr>
<tr>
<td>Le roi se meurt</td>
<td>Ionesco</td>
<td>Théâtre</td>
<td>Folio</td>
<td> -</td>
<td>C1-T</td>
</tr>
<tr>
<td>Le Parfum</td>
<td>Patrick Süskind</td>
<td>Roman</td>
<td>Le livre de poche </td>
<td>- </td>
<td>C1</td>
</tr>
<tr>
<td>Nouvelles Histoires extraordinaires</td>
<td> Edgar Poe</td>
<td>Fiction</td>
<td>Le livre de poche</td>
<td> -</td>
<td>C1</td>
</tr>
<tr>
<td>Le marquis de Villemer</td>
<td>George Sand</td>
<td>Roman</td>
<td>-</td>
<td> -</td>
<td>C1</td>
</tr>
<tr>
<td>Thérèse Desqueyroux</td>
<td>François Mauriac</td>
<td>Romn / fiction littéraire</td>
<td>Le livre de poche</td>
<td>978-2-253-00421-9 </td>
<td>C1</td>
</tr>
<tr>
<td>La ferme des animaux</td>
<td>George Orwell</td>
<td>Allégorie</td>
<td>Folio</td>
<td> 978-2-07-037516-5</td>
<td>C1</td>
</tr>
<tr>
<td>L Île du jour d avant</td>
<td>Umberto ECO</td>
<td>Roman historique</td>
<td>Le livre de poche</td>
<td> 2-253-14361-8</td>
<td>C1</td>
</tr>
<tr>
<td>Les justes</td>
<td>ALbert Camus</td>
<td>Théâtre</td>
<td>Folio</td>
<td>2-07-036477-1 </td>
<td>C1</td>
</tr>
<tr>
<td>Discours de la méthde</td>
<td>Descartes</td>
<td>Filosofia</td>
<td>GF Flammarion</td>
<td>978-2-0807-1091-8 </td>
<td>C1</td>
</tr>
<tr>
<td>En attendant Godot</td>
<td>Samuel Backett</td>
<td>Tragi-comédie / Fiction absurde</td>
<td>Les éditions de minuit</td>
<td>978-2-7073-0148-2 </td>
<td>C1</td>
</tr>
<tr>
<td>La disparition </td>
<td>Georges Perec</td>
<td>Roman / LIPOGRAMME</td>
<td>L'imaginaire - Gallimard</td>
<td>978-2-07-071523-7 </td>
<td>C1</td>
</tr>
<tr>
<td>La femme gelée</td>
<td>Annie Ernaux</td>
<td>Roman</td>
<td>Folio</td>
<td>978-2-07-037818-0 </td>
<td>C1</td>
</tr>
<tr>
<td>La honte</td>
<td>Annie Ernaux</td>
<td>Roman / récit autobiographique</td>
<td>Gallimard</td>
<td>2-07-074787-5</td>
<td>C1</td>
</tr>
<tr>
<td>La mort du roi Athur </td>
<td>-</td>
<td>Roman de Chevalerie </td>
<td>Le livre de poche <br/> Lettres gothiques</td>
<td>978-2-253-08237-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Lancelot du Lac</td>
<td>-</td>
<td>Roman de Chevalerie</td>
<td>Le livre de poche <br/> Lettres gothiques</td>
<td> 978-2-253-08237-8 </td>
<td>C1</td>
</tr>
<tr>
<td>La quête du Graal </td>
<td>-</td>
<td>Roman de Chevalerie </td>
<td>Éditions du Seuil</td>
<td>2-02-006217-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Le chevalier de la Charette</td>
<td>Chrétien de Troyes </td>
<td>Roman de chevalerie</td>
<td>Le livre dde poche <br/> Lettres gothiques</td>
<td> 2-253-05401-1</td>
<td>C1</td>
</tr>
<tr>
<td>Le Colonel Chabert</td>
<td>Honoré de Balzac</td>
<td>Fiction / roman court</td>
<td>Le livre de poche</td>
<td> 2-253-09804-3</td>
<td>C1</td>
</tr>
<tr>
<td>Le papa de Simon</td>
<td>Maupassant</td>
<td>Nouvelle / fiction</td>
<td>GF Flammarion - Etonnants classiques</td>
<td> 2-08-07004-X</td>
<td>C1</td>
</tr>
<tr>
<td>Bel-ami</td>
<td>Maupassant</td>
<td>Roman / réalisme / fiction littéraire</td>
<td>GF Flammarion</td>
<td> 2-08-071071-0</td>
<td>C1</td>
</tr>
<tr>
<td>Les faux-monnayeurs</td>
<td>André Gide</td>
<td>Roman / fiction</td>
<td>Folio</td>
<td> 2-07-036879-3</td>
<td>C1</td>
</tr>
<tr>
<td>La muraille de Chine</td>
<td>Franz Kafka</td>
<td>Nouvelle / fiction</td>
<td>Folio</td>
<td> 2-07-03654-5</td>
<td>C1</td>
</tr>
<tr>
<td>Vendredi ou la vie sauvage </td>
<td>Michel Tournier</td>
<td>Roman (pour enfant)/ fiction</td>
<td>Le livre de poche jeunesse</td>
<td> 978-2-01-00161-5</td>
<td>C1</td>
</tr>
<tr>
<td>Pinocchio</td>
<td>Carlo Collodi</td>
<td>Littérature pour les enfant <br/> Récit d'aventure</td>
<td>Le livre de poche jeunesse</td>
<td> 978-2-01-00161-5</td>
<td>C1</td>
</tr>
<tr>
<td>La vie devant soi</td>
<td>Romain Gary ( Émile Ajar)</td>
<td>Roman / Fiction</td>
<td>Folio</td>
<td>2-07-0373626-2 </td>
<td>C1</td>
</tr>
<tr>
<td>Étranger</td>
<td>Albert Camus</td>
<td>Roman / Fiction absurde - philosophique</td>
<td>Folio -plus - classique</td>
<td>978-2-07-030602-2 </td>
<td>C1</td>
</tr>
<tr>
<td>La cantatrice chauve <br/> (suive de La leçon)</td>
<td>Ionesco</td>
<td>Théâtre</td>
<td>Folio</td>
<td> 2-07-036236-1</td>
<td>C1</td>
</tr>
<tr>
<td>Le père Goriot </td>
<td>Honoré de Balzac</td>
<td>Roman / Fiction</td>
<td>Folio- Classique</td>
<td> 2-07-026784-3 </td>
<td>C1</td>
</tr>
<tr>
<td>Petits crimes conjugaux</td>
<td>Eric-Emmanuel Schmitt</td>
<td>Théâtre / Fiction psychologique</td>
<td>le Club</td>
<td>2-7028-86461-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Les femmes savantes</td>
<td>Molière</td>
<td>Théâtre</td>
<td>Librio (2€)</td>
<td> 978-2-290-23613-0</td>
<td>C1</td>
</tr>
<tr>
<td>La Parure</td>
<td>Maupassant</td>
<td>Nouvelle réaliste</td>
<td>Librio (2€)</td>
<td>978-2-290-15129-7 </td>
<td>C1</td>
</tr>
<tr>
<td>L Île des esclaves</td>
<td>Marivaux</td>
<td>Théâtre</td>
<td>Librio (2€)</td>
<td> 978-2-290-23524-9 </td>
<td>C1</td>
</tr>
<tr>
<td>Le malade imaginaire</td>
<td>Molière</td>
<td>Théâtre</td>
<td>Librio (2€)</td>
<td>978-2-290-22984-2 </td>
<td>C1</td>
</tr>
<tr>
<td>La Belle et la Bête</td>
<td>M<sub>me</sub> Leprince de Beaumont</td>
<td>Conte de fée</td>
<td>Librio (2€)</td>
<td> 978-2-290-14626-2 </td>
<td>C1</td>
</tr>
<tr>
<td><b>Perceval </b> ou le conte du Graal</td>
<td>Chrétien de Troyes</td>
<td>Roman de Chevalerie</td>
<td>Librio (2€)</td>
<td> 978-2-290-37419-1 </td>
<td>C1</td>
</tr>
<tr>
<td>Fables (Livres VII à XI)</td>
<td>Jean de La Fontaine</td>
<td>Fable</td>
<td>Folio+ (Lycée)</td>
<td>978-2-07-285893-2 </td>
<td>C1</td>
</tr>
<tr>
<td>La Mare au Diable</td>
<td>George Sand</td>
<td>Roman</td>
<td>Le livre de poche</td>
<td> 978-2-253-00709-8</td>
<td>C1</td>
</tr>
<tr>
<td>Pauline</td>
<td>George Sand</td>
<td>Roman / Fiction</td>
<td>Folio (3€)</td>
<td>978-2-07-301355-2 </td>
<td>C1</td>
</tr>
<tr>
<td>Complot à Versailles</td>
<td>Annie Jay</td>
<td>Fiction historique / Roman jeunesse</td>
<td>Le livre de poche jeunesse</td>
<td>978-2-01-000925-9 </td>
<td>C1</td>
</tr>
<tr>
<td>Au nom du roi</td>
<td>Annie Jay</td>
<td>Fiction historique / Roman jeunesse</td>
<td>Le livre de poche jeunesse </td>
<td>978-2-01-397148-5 </td>
<td>C1</td>
</tr>
<tr>
<td>La Princesse de Clèves</td>
<td>Madame de Lafayette</td>
<td>Roman</td>
<td>Folio- Classique</td>
<td>978-2-07-041443-7 </td>
<td>C1</td>
</tr>
<tr>
<td>Une vie</td>
<td>Maupassant</td>
<td>Roman / fiction</td>
<td>Flammarion - Étonnants classiques</td>
<td>978-2-0813-4786-1 </td>
<td>C1</td>
</tr>
<tr>
<td>Thérèse Raquin</td>
<td>Émile Zola</td>
<td>Roman</td>
<td>Larousse</td>
<td> 978-2-03-583925-1</td>
<td>Can-y</td>
</tr>
<tr>
<td>Les Mystres d Udolphe</td>
<td>Ann Radcliffe</td>
<td>Roman/ Horreur <br/> Fiction gothique</td>
<td>Folio classique</td>
<td>978-2-07-040377-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Les contemplations</td>
<td>Victor HUGO</td>
<td>Poésie </td>
<td>Folio</td>
<td>978-2-07-043728-3 </td>
<td>C1</td>
</tr>
<tr>
<td>Amour et amitié</td>
<td>Jane Austen</td>
<td>Roman / Nouvelle</td>
<td>Folio (2€)</td>
<td>978-2-07-286537-4 </td>
<td>C1</td>
</tr>
<tr>
<td><q> Cher Monsieur Germain,...</q></td>
<td>Albert Camus</td>
<td>Lettres et extraits</td>
<td>Folio (2€)</td>
<td> 978-2-07-295654-6</td>
<td>C1</td>
</tr>
<tr>
<td> La cefetière</td>
<td>Théophile Gautier</td>
<td>Fantasy littéraire</td>
<td>Folio(2€)</td>
<td>978-2-07-044362-8</td>
<td>C1</td>
</tr>
<tr>
<td>Lettre au père</td>
<td>Franz Kafka</td>
<td>Non-fiction</td>
<td>Folio (2€)</td>
<td> 978-2-07-042206-7</td>
<td>C1</td>
</tr>
<tr>
<td>Emma</td>
<td>Jane Austen</td>
<td>Roman</td>
<td>Milad Romance</td>
<td>978-2-8112-1475-3 </td>
<td>C1</td>
</tr>
<tr>
<td>Les Hauts de Hurle-Vent</td>
<td>Emily Brontë</td>
<td>Roman / horruer <br/> fiction gothique</td>
<td>Le livre de poche - classique</td>
<td>978-2-253-00475-2 </td>
<td>C1</td>
</tr>
<tr>
<td>Le chemin</td>
<td>Miguel Delibes</td>
<td>Littératures Esp</td>
<td>Verdier -otra memoria</td>
<td>978-2-86432-207-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Dracula et autres histoires de vampires</td>
<td>-</td>
<td>Fiction littéraire/ Nouvelles</td>
<td>Librio (2€)</td>
<td>978-2-290-17391-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Dracula</td>
<td>Bram Stoker</td>
<td>Roman / Horreur/ fiction littéraire</td>
<td>Classiques abrégés</td>
<td>978-2-211-07438-4</td>
<td>C1</td>
</tr>
<tr>
<td>Le mythe de Sisyphe</td>
<td>Albert Camus</td>
<td>Filosofia- Essai</td>
<td>Folio-essais</td>
<td>978-2-07-032288-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Lady Susan</td>
<td>Jane Austen</td>
<td>Nouvelle</td>
<td>Folio (2€)</td>
<td>978-2-07-033756-9 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Manuel D'exil <br/> comment réussir son exil en trente-cinq leçons</td>
<td>Velibor Čolić</td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-274472-3</td>
<td>C1</td>
</tr>
<tr>
<td>L'âme du monde</td>
<td>Fédéric Lenoir</td>
<td>Fiction</td>
<td>Pocket</td>
<td> 978-2-26-6240656-9</td>
<td>C1</td>
</tr>
<tr>
<td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Écrire et combattre pour l'égalité' (2021-2025)">Déclaration des droits de la femme et de la citoyenne</span></td>
<td>Olympe de Gouges </td>
<td>Littérature d'Idées</td>
<td>Hatier</td>
<td> 978-2-401-07847-5</td>
<td>Can-y</td>
</tr>
<tr>
<td>Déclaration des droits de la femme et de la citoyenne</td>
<td>Olympe de Gouges </td>
<td>Littérature d'Idées</td>
<td>Folio (2€)</td>
<td>978-2-07-145742-7 </td>
<td>Can-y</td>
</tr>
<tr>
<td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Émancipations créatrices'(2023-2027)">Cahier de Douai</span></td>
<td>Arthur Rimbaud</td>
<td>Folio + (lycée)</td>
<td>Poésie</td>
<td> 978-2-07-3000927-2</td>
<td>H-T</td>
</tr>
<tr>
<td>Les fleurs du mal</td>
<td>Charles Baudelaire</td>
<td>Poésie</td>
<td>Hatier</td>
<td>978-2-401-06360-0 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Cyrano de Bergerac</td>
<td>Edmond Rostand</td>
<td>Théâtre</td>
<td>Pocket-Clasique </td>
<td>978-2-26-629553 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Incendies<br/><sup> Le sang es promesses/2</sup></td>
<td>Wajdi Mouawad</td>
<td>Théâtre</td>
<td>Babel</td>
<td>978-2-7427-9312-9 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Le mariqge de Figaro</td>
<td>Beaumarchais</td>
<td>Théâtre</td>
<td>Flammarion-Étonnant classiques</td>
<td> 978-2-0812-9394-6</td>
<td>Can-y</td>
</tr>
<tr>
<td>Le bal des foles</td>
<td>Victoria Mas</td>
<td>Roman</td>
<td>Le livre de poche</td>
<td>978-2-253-10362-2 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Stupeur et tremblements</td>
<td>Améle Nothomb</td>
<td>Autobiographie</td>
<td>Le livre de poche</td>
<td>2-253-15071-1 </td>
<td>Can-y</td>
</tr>
<tr>
<td>Antigone</td>
<td>Jean Anouilh</td>
<td>Théâtre</td>
<td>La table ronde</td>
<td>2-7103-0025-7 </td>
<td>Can-y</td>
</tr>
<tr>
<td>La mille et deuxième nuit</td>
<td>Théophile Gautier</td>
<td>Nouvelles</td>
<td>Folio (2€)</td>
<td>978-2-07-046934-5 </td>
<td>Can-y</td>
</tr>
<tr>
<td>L'Odysée</td>
<td>Homère</td>
<td>Mythologie</td>
<td>GF Flammarion</td>
<td>- </td>
<td>C2</td>
</tr>
<tr>
<td>Les dieux s'amusent </td>
<td>Denis Lindon</td>
<td>Mythologie</td>
<td>Flammarion jeunesse</td>
<td>978-2-0814-7983-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Le temps de l'innocence </td>
<td>Wharton</td>
<td>Roman</td>
<td> GF Flammarion</td>
<td> 978-2-0804-5158-3</td>
<td> C1-T</td>
</tr>
<tr>
<td>Tragédies complètes</td>
<td>Eschyle</td>
<td>Théâtre<br/>tragédie </td>
<td>Folio-Classique</td>
<td>978-2-07-037364-2 </td>
<td> C1-T</td>
</tr>
<tr>
<td>Traité théologico-politique<br/> <sup>Préface et Chapîtres XVI à XX </sup></td>
<td>Baruch Spinoza</td>
<td>Filosofia</td>
<td>GF Flammarion</td>
<td>798-2-0804-4809-5</td>
<td> C1-T</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td colspan="6"> <h1><center> 中国文学  亚洲文学 </center></h1></td>
</tr>
<tr>
<td>Histoir de ma vie </td>
<td>Lao She<br/> 老舍</td>
<td>Fiction</td>
<td>Folio </td>
<td>978-2-07-042208-1 </td>
<td> C1</td>
</tr>
<tr>
<td>Élégies de Chu</td>
<td>Qu Yuan</td>
<td>Poésie</td>
<td>Folio </td>
<td>978-2-07-300474-1 </td>
<td>C1</td>
</tr>
<tr>
<td>La mort du soleil</td>
<td rowspan="2">Yan Lianke <br/> 阎连科</td>
<td>Roaman</td>
<td>Picquier poche / CNL</td>
<td> 978-2-8097-1602-3</td>
<td>C1</td>
</tr>
<tr>
<td>La fuite du temps</td>
<td>Roman</td>
<td>Picquier poche / CNL</td>
<td>978-2-8097-1323-7 </td>
<td>C1</td>
</tr>
<tr>
<td>Mort d une héroïne rouge</td>
<td rowspan="2">Qiu Xiaolong <br/> 裘小龙</td>
<td>Policier</td>
<td>Points / Éditions Liana Levi</td>
<td>2-02-048887-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Chine, retines ton souffle</td>
<td>Policier</td>
<td>Points / Éditions Liana Levi</td>
<td> 978-2-7578-7796-68</td>
<td>C1</td>
</tr>
<tr>
<td>Balzac et la petite tailleuse chinoise</td>
<td rowspan="2">Dai Sijie <br/> 戴思杰</td>
<td>Roman / fiction</td>
<td> Folio</td>
<td> 2-07-041680-1</td>
<td>C1</td>
</tr>
<tr>
<td>L'Évangile selon Yong Sheng </td>
<td>Fiction</td>
<td>Folio</td>
<td> 978-2-07-288241-8</td>
<td>C1</td>
</tr>
<tr>
<td>孽子</td>
<td>白先勇</td>
<td>Roman / fiction</td>
<td> Picquier poche</td>
<td>2-87730-603-8 </td>
<td>C1</td>
</tr>
<tr>
<td>Le maître de plus en plus d humour</td>
<td>Mo Yan</td>
<td>Nouvelle </td>
<td>Points </td>
<td>978-2-02-0859566-1</td>
<td>C1</td>
</tr>
<tr>
<td>Le livre de Thé</td>
<td>OKAKURA Kakuzô</td>
<td>Essai / phi</td>
<td>Picquier poche</td>
<td>978-2-87730-821-9 </td>
<td>C1</td>
</tr>
<tr>
<td>Choses qui rendent heureux</td>
<td>Sei Shônagon</td>
<td>Fiction</td>
<td>Folio - sagesse </td>
<td> 978-2-07-292490-3</td>
<td>C1</td>
</tr>
<tr>
<td>je suis un chat</td>
<td>Natsume Sosêki</td>
<td>Roman / satire / fiction-comique</td>
<td>Gallimard / UNESCO </td>
<td> 978-2-07-070634-1</td>
<td>C1</td>
</tr>
<tr>
<td>Pachinko</td>
<td>Min Jin Lee <br/> 이민진</td>
<td>Roman / Fiction historique</td>
<td>Harper Collins / Poche</td>
<td> 979-1-0339-0895-1</td>
<td>C1</td>
</tr>
<tr>
<td> Le seigneur des anneaux  </td>
<td rowspan="2">J.R.R. Tolkien</td>
<td>Fantastique</td>
<td> Pocket </td>
<td> 2-266-11561-8 </td>
<td> C1</td>
</tr>
<tr>
<td>Contes &amp; Légendes inachevés</td>
<td>Fantastique</td>
<td>Pocket</td>
<td>2-266-11800-5 </td>
<td>C1</td>
</tr>
<tr>
<td>La pyramide rouge</td>
<td rowspan="3">Rick Riordan</td>
<td>Fantastique</td>
<td>Le livre de poche jeunesse</td>
<td> 978-2-01-712596-9</td>
<td>C1</td>
</tr>
<tr>
<td>Héros de l Olympe <br/> Le héros perdu</td>
<td>Fantastique</td>
<td>Le livre de poche jeunesse </td>
<td>978-2-01-203199-9 </td>
<td>C1</td>
</tr>
<tr>
<td>Héros de l Olympe  <br/> Le fils de Neptune</td>
<td>Fantastique</td>
<td>Le livre de poche jeunesse</td>
<td>978-2-01-203175-3 </td>
<td>C1</td>
</tr>
<tr>
<td>La guerre des clans <br/> 1- Retour à l'état sauvage</td>
<td>Erin Hunter</td>
<td>Fantastique</td>
<td>Pocket jeunesse - PKJ</td>
<td>978-2-26-16865-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Le Royaume des Loups<br/> Faolan le solitaire</td>
<td rowspan="2">Kathryn Lasky</td>
<td>Fantastique</td>
<td>Pocket jeunesse - PKJ</td>
<td>978-2-26-6629389-1 </td>
<td>C1</td>
</tr>
<tr>
<td>Le Royaume des loups <br/> Dans l'ombre de la meute</td>
<td>Fantastique</td>
<td>Pocket jeunesse - PKJ </td>
<td>978-2-26-29390-7</td>
<td>C</td>
</tr>
<tr>
<td>Bjorn le Morphir </td>
<td>Thomas Lavachery</td>
<td>Fantastique</td>
<td>Médium poche<br/>L'École des loisir </td>
<td>978-2-211-23372-9</td>
<td>Can-y</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td>L énigme de clou chinois <br/> The Chinese Nail Murders</td>
<td>Robert Van Gulik</td>
<td>Détective / mystère / fiction historique</td>
<td>Éditions 10/18</td>
<td>978-2-264-00696-7 </td>
<td>C1</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td>Une Tempête</td>
<td>Aimé Césaire</td>
<td>Théâtre </td>
<td>Points</td>
<td>978-2-02-031431-2</td>
<td>CM</td></tr>
<tr>
<td>La Tempête </td>
<td>Shakespeare</td>
<td>Théâtre </td>
<td>Folio théâtre</td>
<td>978-2-07-040315-8</td>
<td>CM</td></tr>
<tr>
<td>Tristes tropiques</td>
<td>Claude Lévi-Strauss</td>
<td>-</td>
<td>Pocket</td>
<td>978-2-266-11982-5</td>
<td>S1</td></tr>
<tr>
<td>Le roman de Renart </td>
<td>-</td>
<td>-</td>
<td>Folio classique </td>
<td>2-07-037776-8</td>
<td>S1</td></tr>
<tr>
<td>Gargantua </td>
<td>François Rabelais </td>
<td>Littérature des Idées</td>
<td>Hatier scolaire</td>
<td>978-2-401-07849-9</td>
<td>S1</td></tr>
<tr>
<td>Entre les murs</td>
<td>François Bégaudeau</td>
<td>roman</td>
<td>Folio</td>
<td>978-2-07-034290-7</td>
<td>S1</td></tr>
<tr>
<td>Nouvelle hostoire de Mouchette </td>
<td>Georges Bernanos </td>
<td>-</td>
<td>Le livre de poche</td>
<td>-</td>
<td>S1</td></tr>
<tr>
<td>Le Tartuffe</td>
<td>Molière</td>
<td>Folio classique </td>
<td>Folio classique </td>
<td>978-2-07-044994-1</td>
<td>S1</td></tr>
<tr>
<td>La Dame de pique et Les Récits de feu Ivan Petrovitch Belkine </td>
<td>Pouchkine</td>
<td>-</td>
<td>Le livre de Poche </td>
<td>978-2-253-03927-3</td>
<td>S1</td></tr>
<tr>
<td>La psychologie de l'enfant </td>
<td>Jean Piaget et Bärbel Inhelder</td>
<td>-</td>
<td>Que sais-je :</td>
<td>2-13-044689-2</td>
<td>S1</td></tr>
<tr>
<td>Discours du récit </td>
<td>Gérard Genette</td>
<td>-</td>
<td>Poinnt</td>
<td>978-2-7578-0538-1</td>
<td>S1</td></tr>
<tr>
<td>Le journal d'Anne Frank</td>
<td>Anne Frank</td>
<td>autobiographie</td>
<td>Le livre de poche </td>
<td>978-2-253-07309-3</td>
<td>S1</td></tr>
<tr>
<td>Pauline </td>
<td>Dumas</td>
<td>Roman</td>
<td>Folio</td>
<td>978-2-07-041230-3</td>
<td>S1</td></tr>
<tr>
<td>La grande traversée de l'Ouest en bus</td>
<td>Jack Kerouac</td>
<td>Folio </td>
<td>Folio</td>
<td>978-2-07-288543-3</td>
<td>S1</td></tr>
<tr>
<td>Le passe-muraille </td>
<td>Marcel Aymé</td>
<td>roman</td>
<td>Folio</td>
<td>-</td>
<td>S1</td></tr>
<tr>
<td>La grammaire est une chanson douce</td>
<td>Erik Orsenna</td>
<td>-</td>
<td>Le livre de Poche </td>
<td>978-2-253-14910-1</td>
<td>S1</td></tr>
<tr>
<td>Vacances de Pâques</td>
<td>Marcel Proust</td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-286636-4</td>
<td>S1</td></tr>
<tr>
<td>Dora Bruder </td>
<td>Patrick modiano</td>
<td>Roman</td>
<td>Folio</td>
<td>2-07-040848-5</td>
<td>S1</td></tr>
<tr>
<td>Quand dire, c'est faire </td>
<td>J.L. Austin </td>
<td>-</td>
<td>points-essais </td>
<td>2-02-012569-2</td>
<td>S1</td></tr>
<tr>
<td>Phèdre </td>
<td>Racine </td>
<td>théâtre </td>
<td></td>
<td>978-2-01-169176-7</td>
<td>S1</td></tr>
<tr>
<td>Britannicus </td>
<td>Racine </td>
<td>Théâtre </td>
<td>Le livre de Poche </td>
<td>2-253-03795-8</td>
<td>S1</td></tr>
<tr>
<td>Aurélia </td>
<td>Gérard de Nerval</td>
<td>nouvelles </td>
<td>Le livre de poche </td>
<td>2-253-01066-9</td>
<td>S1</td></tr>
<tr>
<td>Les Regrets , Les Antiquités de Rome</td>
<td>Joachim Du Bellay </td>
<td>Poèsie</td>
<td>Gallimard</td>
<td>2-07-032147-9</td>
<td>S1</td></tr>
<tr>
<td>Printemps et autres saisons</td>
<td>Le Clézio</td>
<td>Roman</td>
<td>Folio</td>
<td>2-07-038377-6</td>
<td>S1</td></tr>
<tr>
<td>Nouveau dictionnaire encyclopédique des sciences du langage </td>
<td>Oswald Ducrot et Jean-Marie Schaeffer</td>
<td>Points -essais</td>
<td>Points-essais</td>
<td>2-02-038181-8</td>
<td>S1</td></tr>
<tr>
<td>Dom Juan </td>
<td>Molière</td>
<td>théâtre </td>
<td>Hatier </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Le bourgeois gentilhomme</td>
<td>Molière</td>
<td>théâtre </td>
<td>ulb</td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Contes de la Bécasse</td>
<td>Maupassant</td>
<td>contes</td>
<td>folio classique </td>
<td>978-2-07-046667-2</td>
<td>S2</td></tr>
<tr>
<td>Contes du jour et de la nuit </td>
<td>Maupassant </td>
<td>contes</td>
<td>GF-Flammarion </td>
<td>2-08-070292-0</td>
<td>S2</td></tr>
<tr>
<td>Contes libertins </td>
<td>Jean de la Fontaine </td>
<td>contes</td>
<td>succès du livre </td>
<td>2743419784</td>
<td>S2</td></tr>
<tr>
<td>Cinq semaines en ballon</td>
<td>Jules Verne</td>
<td>roman</td>
<td>Maxi-poche </td>
<td>2-7434-3161-X</td>
<td>S2</td></tr>
<tr>
<td>Germinal</td>
<td>Zola</td>
<td>Roman</td>
<td>Le livre de poche</td>
<td>978-2-253-00422-6</td>
<td>S2</td></tr>
<tr>
<td>Moderato cantabile</td>
<td>Marguerite Duras</td>
<td>roman</td>
<td>Edition de Minuit </td>
<td>2-7073-0314-3</td>
<td>S2</td></tr>
<tr>
<td>Lettres de mmon moulin </td>
<td>Alphonse Daudet</td>
<td>Roman</td>
<td>Folio</td>
<td>2-07-040889-X</td>
<td>S2</td></tr>
<tr>
<td>Lettres de la Marquise de M*** au Compte de R***</td>
<td>Claude Crébillon </td>
<td>-</td>
<td>Rivages poche</td>
<td>2-7436-0703-3</td>
<td>S2</td></tr>
<tr>
<td>Trois histoires gourmandes</td>
<td>-</td>
<td>-</td>
<td>folio</td>
<td>326-0-05-087555-4</td>
<td>S2</td></tr>
<tr>
<td>L'Utopie </td>
<td>Thomas More </td>
<td>roman </td>
<td>Folio</td>
<td>978-2-07-043975-1</td>
<td>S2</td></tr>
<tr>
<td>La Débâche </td>
<td>Zola</td>
<td>roman</td>
<td>Le livre de poche </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Supplément au Voyage de Bougainville </td>
<td>Diderot</td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-042625-6</td>
<td>S2</td></tr>
<tr>
<td>Le vieil homme et et la mer</td>
<td>Ernest Hemingway</td>
<td>-</td>
<td>Folio</td>
<td>2-07-0333229-2</td>
<td>S2</td></tr>
<tr>
<td>Zadig ou la Destinée</td>
<td>Voltaire</td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-046661-0</td>
<td>S2</td></tr>
<tr>
<td>Courrier sud</td>
<td>Antoine de Saint-Exupéry</td>
<td>roman</td>
<td>Folio</td>
<td>978-2-07-036080-2</td>
<td>S2</td></tr>
<tr>
<td>OEdipe Roi</td>
<td>Sophocle </td>
<td>Théâtre </td>
<td>Le livre de poche </td>
<td>2-253-06713-X</td>
<td>S2</td></tr>
<tr>
<td>Enfance </td>
<td>Nathalie Sarraute </td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-286480-3</td>
<td>S2</td></tr>
<tr>
<td>L'île des esclaves </td>
<td>Marivaux</td>
<td>ANALYSE</td>
<td>Atlande</td>
<td>978-2-35030-759-6</td>
<td>S2</td></tr>
<tr>
<td>Barbe Bleue</td>
<td>Amélie Nothomb</td>
<td>roman</td>
<td>Le livre de poche </td>
<td>978-2-253-19414-9</td>
<td>S2</td></tr>
<tr>
<td>Alice au pays de merveilles</td>
<td>Lewis Carroll</td>
<td>-</td>
<td>Le livre de poche </td>
<td>978-2-253-08244-6</td>
<td>S2</td></tr>
<tr>
<td>Voyage à Lilliput </td>
<td>Swift</td>
<td>-</td>
<td>Etonnants-classiques</td>
<td>978-2-0813-9577-0</td>
<td>S2</td></tr>
<tr>
<td>L'eneide </td>
<td>Virgile</td>
<td>-</td>
<td>GF- Flammarion </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Rhinocéros </td>
<td>Ionesco</td>
<td>Théâtre </td>
<td>folio</td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Le mythe de Sisyphe </td>
<td>Albert Camus </td>
<td>Essai philosophique </td>
<td>Folio - essais </td>
<td>2-07-032288-2</td>
<td>S2</td></tr>
<tr>
<td>Comment Wang-Fô fut sauvé et autres nouvelles </td>
<td>Marguerite Yourcenar </td>
<td>-</td>
<td>Folio plus </td>
<td>978-2-07-034457</td>
<td>S2</td></tr>
<tr>
<td>Désert </td>
<td>Le Clézio </td>
<td>rroman</td>
<td>folio</td>
<td>2-07-037670-2</td>
<td>S2</td></tr>
<tr>
<td>Britannicus </td>
<td>Racine </td>
<td>théâtre </td>
<td>Hatier </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Candide </td>
<td>Voltaire </td>
<td>Théâtre </td>
<td>Hatier </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Phèdre</td>
<td>Racine </td>
<td>théâtre </td>
<td>folio </td>
<td>2-07-038763-1</td>
<td>S2</td></tr>
<tr>
<td>Les fleur du  mal</td>
<td>Baudelaire</td>
<td>Poésie </td>
<td>Hatier </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>La maison Tellier </td>
<td>Maupassant </td>
<td>roman </td>
<td>Le livre de poche </td>
<td>2-253-01345-5</td>
<td>S2</td></tr>
<tr>
<td>Les Caractères</td>
<td>La Bruyère </td>
<td>Littératures des Idées</td>
<td>GF</td>
<td>978-2-0812-6078-8</td>
<td>S2</td></tr>
<tr>
<td>Ubu roi</td>
<td>Jarry </td>
<td>Théâtre </td>
<td>Folio</td>
<td>978-2-07-042354-5</td>
<td>S2</td></tr>
<tr>
<td>La guerre de Troie n'aura pas lieu </td>
<td>Jean Giraudoux</td>
<td>Théâtre</td>
<td>Le livre de poche </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Le roman de Renart</td>
<td>-</td>
<td>-</td>
<td>Folio</td>
<td>2-07-037776-8</td>
<td>S2</td></tr>
<tr>
<td>Code 612 qui a tué le Petit Prince ?</td>
<td>Michel Bussi </td>
<td>-</td>
<td>Pocket </td>
<td>978-2-266-32821-0</td>
<td>S2</td></tr>
<tr>
<td>Histoire de MMe de La Pommeraye </td>
<td>Diderot </td>
<td>-</td>
<td>Folio</td>
<td>978-2-07-283025-9</td>
<td>S2</td></tr>
<tr>
<td>Vol de nuit </td>
<td>Antoine de Saint-Exupéry </td>
<td>roman</td>
<td>Le livre de poche </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Les fleur du mal </td>
<td>Beaudelaire </td>
<td>ANALYSE</td>
<td>Nathan </td>
<td>978-209-186495-2</td>
<td>S2</td></tr>
<tr>
<td>L'An 2440</td>
<td>Louis-Sébastine Mercier </td>
<td>-</td>
<td>La découverte Poche </td>
<td>978-2-7071-3117-1</td>
<td>S2</td></tr>
<tr>
<td>Une vie </td>
<td>Maupassant</td>
<td>novelle </td>
<td>Maxi-Poche </td>
<td>2-87714-134-9</td>
<td>S2</td></tr>
<tr>
<td>Candide </td>
<td>Voltaire </td>
<td>-</td>
<td>Hachette </td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Les fausses confidences </td>
<td>Marivaux</td>
<td>théâtre </td>
<td>Belin gallimard </td>
<td>979-10-358-0717-7</td>
<td>S2</td></tr>
<tr>
<td>Candide </td>
<td>Voltaire </td>
<td>-</td>
<td>Belin Gallimard </td>
<td>978-2-7011-5970-6</td>
<td>S2</td></tr>
<tr>
<td>Contes de monstres et de fées</td>
<td>Madame d'Aulnoy</td>
<td>conte</td>
<td>Etonnants - scolaire </td>
<td>978-2-0802-7844-9</td>
<td>S2</td></tr>
<tr>
<td>Le prince marcassin </td>
<td>Mme d'Aulnoy</td>
<td>conte</td>
<td>Librio 2£</td>
<td>978-2-29015-463-2</td>
<td>S2</td></tr>
<tr>
<td>La chute de la maison Usher </td>
<td>Edgar Allan Poe</td>
<td>nouvelles</td>
<td>Librio</td>
<td>-</td>
<td>S2</td></tr>
<tr>
<td>Le Menteur </td>
<td>Corneille </td>
<td>Théâtre </td>
<td>Hachette scolaire </td>
<td>978-2-01-726142-1</td>
<td>CM</td></tr>
<tr>
<td>On ne badine pas avec l'amour</td>
<td>Alfred de Musset </td>
<td>théâtre </td>
<td>Hatier scoalire </td>
<td>978-2-401-10542-3</td>
<td>CM</td></tr>
<tr>
<td>Manon Lescaut </td>
<td>Abbé Prévost </td>
<td>roman </td>
<td>Hachette scoalire </td>
<td>978-2-01-716694-8</td>
<td>CM</td></tr>
<tr>
<td>Manon Lescaut </td>
<td>Abbé Prévost </td>
<td>roman </td>
<td>folio lycée </td>
<td>978-2-07-296477-0</td>
<td>CM</td></tr>
<tr>
<td>Les fourberies de scapin </td>
<td>Molière </td>
<td>théâtre </td>
<td>Librio</td>
<td>978-2-290-21579-1</td>
<td>CM</td></tr>
<tr>
<td>Ruy Blas </td>
<td>Victor Hugo</td>
<td>théâtre </td>
<td>Librio</td>
<td>978-2-290-37683-6</td>
<td>CM</td></tr>
<tr>
<td>Le parti pris des choses </td>
<td>Francis Ponge</td>
<td>poèsie </td>
<td>folio</td>
<td>978-2-07-038993-3</td>
<td>CM</td></tr>
<tr>
<td>Le Peau de chagrin </td>
<td>Honoré de Balzac</td>
<td>roman </td>
<td>Nathan scolaire </td>
<td>978-209-151227-3</td>
<td>CM</td></tr>
<tr>
<td>Le Barbier de Séville</td>
<td>Beaumarchais</td>
<td>Théâtre</td>
<td>GF</td>
<td>978-2-0814-2779-2</td>
<td>CM</td></tr>
<tr>
<td>Pour un oui pour un non</td>
<td>Nathalie Sarraute </td>
<td>Théâtre </td>
<td>Folio Lycée</td>
<td>978-2-07-305214-8</td>
<td>CM</td></tr>
<tr>
<td>Anatomie d'un chœur</td>
<td>Marie Nimier</td>
<td>roman</td>
<td>Folio</td>
<td>2-07-038540-X</td>
<td>CM</td></tr>
<tr>
<td>Les dieux s'amusent </td>
<td>Denis Lindon </td>
<td>jeunesse </td>
<td>Flammarion jeunesse </td>
<td>978-2-0814-7983-8</td>
<td>CM</td></tr>
<tr>
<td>L'Odyssée </td>
<td>Homère </td>
<td>epopée </td>
<td>Babel</td>
<td>978-2-7427-0579-5</td>
<td>CM</td></tr>
<tr>
<td>Ulysse</td>
<td>Joyce </td>
<td>roman</td>
<td>folio</td>
<td>978-2-07-043971-3</td>
<td>CM</td></tr>
<tr>
<td>Mademoiselle de Maupin </td>
<td>Gautier </td>
<td>roman </td>
<td>Folio</td>
<td>978-2-07-036396-4</td>
<td>CM</td></tr>
<tr>
<td>Discours de la servitude volontaire</td>
<td>La Boétie</td>
<td>Littérature des Idées</td>
<td>Librio 3E</td>
<td>978-2-290-38504-3</td>
<td>N</td></tr>
<tr>
<td>Entreteint sur la pluralité des mondes</td>
<td>Fontenille</td>
<td>Littérature des Idées</td>
<td>GF</td>
<td>978-2-0807-1024-6</td>
<td>N</td></tr>
<tr>
<td>Lettres d'une Péruvienne </td>
<td>Françoise de Graffigny</td>
<td>Littérature des Idées </td>
<td>Folio</td>
<td>Folio 978-2-07-289061-1</td>
<td>N</td></tr>
<tr>
<td>Dans la foret </td>
<td>Jean Hegland</td>
<td>Roman (nature)</td>
<td>TOTEM CNL</td>
<td>978-2-35178-644-4</td>
<td>N</td></tr>
<tr>
<td>La où chantent les écrevisses</td>
<td>Delia Owens </td>
<td>Roman (nature)</td>
<td>Points </td>
<td>978-2-7578-8997-8</td>
<td>N</td></tr>
<tr>
<td>le mur invisible </td>
<td>Marlen Haushofer </td>
<td>Roman (Nature)</td>
<td>Babel</td>
<td>978-2-8686-9832-2</td>
<td>N</td></tr>
<tr>
<td>La Peste</td>
<td>Albert Camus </td>
<td>Roman philosophique </td>
<td>Folio</td>
<td>978-2-17-034957-9</td>
<td>N</td></tr>
<tr>
<td>La famille </td>
<td>Han Jin Lee </td>
<td>prix nobel</td>
<td>Harper collins (prix nobel)</td>
<td>979-1-0339-1365-8</td>
<td>N</td></tr>
<tr>
<td>La pesanteur et la Grâce </td>
<td>Simone Weil</td>
<td>Philosophie </td>
<td>Pocket </td>
<td>978-2-26-04596-4</td>
<td>N</td></tr>
<tr>
    <td>Poésies</td>
    <td>Louise Labé</td>
    <td>Poésie</td>
    <td>Belin gallimard-lycée</td>
    <td>979-10-358-1720-6</td>
    <td>T</td></tr>
<tr>
    <td>Les Métamorphoses (17 récits)</td>
    <td>Ovide</td>
    <td>-</td>
    <td>scolaire</td>
    <td>978-2-0815-1163-7</td>
    <td>T</td></tr>
<tr>
    <td>Les douze travaux d'Hercule</td>
    <td>-</td>
    <td>Mythologie</td>
    <td>Folio Junior</td>
    <td>978-2-07-064871-9</td>
    <td>T</td></tr>
<tr>
    <td>L'Odyssée</td>
    <td>Homère</td>
    <td>épopée</td>
    <td>Librio 2euro</td>
    <td>978-2-290-21059-8</td>
    <td>T</td></tr>
<tr>
    <td>Hernani</td>
    <td>Victor HUGO</td>
    <td>théâtre</td>
    <td>Librio  2euro</td>
    <td>978-2-290-07565-4</td>
    <td>T</td></tr>
<tr>
    <td>L"épopée de Gilgamesh </td>
    <td>-</td>
    <td>épopée</td>
    <td>Folio Junior</td>
    <td>978-2-07-062761-5</td>
    <td>T</td></tr>
</table>
<hr/>
<table>
<h1> "Académique" </h1>
<tr>
<th>Titre</th>
<th>Auteur</th>
<th>Genre</th>
<th>Édition</th>
<th> ISBN </th>
<th> Placement </th>
</tr>
<tr>
<td>Les indispensables Mathématiques et Physique-Chimie </td>
<td>Alexandre MOATTI</td>
<td>SA </td>
<td> Odile Jacob science</td>
<td> 978-2-7381-1722-9 </td>
<td> C1</td>
</tr>
<tr>
<td>La symphonie des nombres premiers</td>
<td rowspan="2">Marcus du Sautoy</td>
<td>Maths</td>
<td>Points</td>
<td>978-2-7578-0429-2 </td>
<td>C1-T</td>
</tr>
<tr>
<td>Le mystère des nombres</td>
<td>Math</td>
<td>Folio-Essais</td>
<td> 978-2-07-046588-0</td>
<td>C1-T</td>
</tr>
<tr>
<td>Histoire des mathématiques</td>
<td>-</td>
<td>math-encyclopedie</td>
<td>Encyclopoche Larousse</td>
<td> 2-03-001021-9</td>
<td>C1-T</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td>L acquisition du language par l'enfant</td>
<td>Josie Bernicot <br/> Alain Bert-Erboul</td>
<td>Psychologie - développement de l enfant </td>
<td>Concept-psy</td>
<td>978-2-84835-164-3 </td>
<td>C1</td>
</tr>
<tr>
<td>Le développement du language</td>
<td>Agnès Florin</td>
<td>Psychologie- développement de l enfant </td>
<td>DUNOP</td>
<td> 978-2-10-004195-4</td>
<td>C1</td>
</tr>
</table>
<hr/>
<table>
<h1> Autres  </h1>
<tr>
<th>Titre</th>
<th>Auteur</th>
<th>Genre</th>
<th>Édition</th>
<th> ISBN </th>
<th> Placement </th>
</tr>
<tr>
<td>5 Histoires extraordinaires!<br/><sup>UPE2A- Collège Maurice Becanne- M<sub>me</sub> Alquier</sup></td>
<td>co-</td>
<td>nouvelles</td>
<td><i> <b>Réparer le language</b> je peux </i> </td>
<td>978-2-494941-00-7 </td>
<td>C1</td>
</tr>
<tr>
<td>Petit manuel pour jeter des (gentils) sorts! </td>
<td>-</td>
<td>-</td>
<td> Larousse </td>
<td> 978-2-03-600083-4</td>
<td> C1</td>
</tr>
<tr>
<td>Chattitudes</td>
<td>Sayo Koizumi</td>
<td>Sur les chats</td>
<td>Larousse</td>
<td> 978-2-03-5879330-1</td>
<td>C1</td>
</tr>
<tr>
<td>Le Japonais en 5 minutes par jour</td>
<td>Vincent Grépinet</td>
<td>Langue</td>
<td rowspan="5">First Éditions</td>
<td>978-2-412-04165-9 </td>
<td>C1</td>
</tr>
<tr>
<td>Le Chinois en 5 minutes par jour</td>
<td>Jing Li</td>
<td>Langue</td>
<td>978-2-412-041642 </td>
<td>C1</td>
</tr>
<tr>
<td>Le coréen en 5 minutes par jour</td>
<td>-</td>
<td>Langue</td>
<td> </td>
<td>给了ha ngoc</td>
</tr>
<tr>
<td>Language symbolique des fleurs</td>
<td>Didier Colin</td>
<td>Fleur</td>
<td>978-2-412-08723-7 </td>
<td>C1</td>
</tr>
<tr>
<td>Le petit livre des symboles</td>
<td>Fabrizio Vecoli</td>
<td>Symboles</td>
<td>978-2-7540-7429-2</td>
<td> C1</td>
</tr>
tr&gt;
<td>Le petit livre de l'orthographe</td>
<td>Julien Soulié</td>
<td>ortograf</td>
<td>978-2-412-10119-3</td>
<td> C1</td>
<tr>
<td>Apprendre à Apprendre </td>
<td rowspan="2">André Giordan <br/> Jérôme Saltet</td>
<td rowspan="2">-</td>
<td>Librio (3€)</td>
<td>978-2-290-17401-2 </td>
<td>C1</td>
</tr>
<tr>
<td>Apprendre à prendre des notes</td>
<td>Librio (3€)</td>
<td>978-2-290-21583-8</td>
<td>C1</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
</table>
<hr/>
<table>
<h1> 土耳其语书籍 </h1>
<tr>
<th>Kitap İsmi</th>
<th>Yazar</th>
<th>Tür</th>
<th>Yayın evi</th>
<th> ISBN </th>
<th> Yeri </th>
</tr>
<tr>
<td>Gılgamış Destanı</td>
<td>Mehmet Ali Atak</td>
<td>Tarih</td>
<td> Anonim Yayıncılık</td>
<td> 978-605-100-384-1 </td>
<td> C1</td>
</tr>
<tr>
<td>Gazi Mustafa Kemal ATATÜRK</td>
<td>İlber Ortaylı</td>
<td>Tarih</td>
<td>Kronik</td>
<td>978-975-2430-29-7 </td>
<td>C1</td>
</tr>
<tr>
<td>Zamanın kısa tarihi</td>
<td>Stephen Hawking</td>
<td>İlim</td>
<td>Alfa bilim</td>
<td>978-605-106-758-2 </td>
<td>C1</td>
</tr>
<tr>
<td>Nikola Tesla nın sıra dışı hayatı</td>
<td>Nikola Tesla</td>
<td>İlim</td>
<td>Martı</td>
<td> 978-605-186-559-1</td>
<td>C1</td>
</tr>
<tr>
<td>Savaş sanatı</td>
<td>Sun Zi</td>
<td>-</td>
<td>İş bankası- Kültür yayınları</td>
<td>978-6056-332-269-6 </td>
<td>C1</td>
</tr>
<tr>
<td>Satranç</td>
<td>Stefan Zweig</td>
<td>-</td>
<td>Can</td>
<td> 978-975-07-3141-9</td>
<td>C1</td>
</tr>
<tr>
<td>Sumerli Ludingirra / geçmişe dönük bilimkurgu</td>
<td rowspan="3">Muazzez İlmiye Çığ</td>
<td>Tarih</td>
<td>Kaynak Yayıncılık</td>
<td>978-605-68985-2-5 </td>
<td>C1</td>
</tr>
<tr>
<td>GİLGAMEŞ <br/> Tarihteki ilk kral kahraman </td>
<td>Tarih </td>
<td>Kaynak Yayıncılık</td>
<td>978-605-69217-3-5 </td>
<td></td>
</tr>
<tr>
<td>ATATÜRK DÜŞÜNÜYOR </td>
<td>Tarih </td>
<td></td>
<td>978-605-81107-8-6 </td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
</table>
<hr/>
<table>
<h1> 外文书籍  </h1>
<tr>
<th>Titre</th>
<th>Auteur</th>
<th> Langue </th>
<th>Genre</th>
<th>Édition</th>
<th> ISBN </th>
<th> Placement </th>
</tr>
<tr>
<td>Harry Potter and the Philosopher's stone</td>
<td>J.K. Rowling</td>
<td>English</td>
<td>Fantastic</td>
<td>Bloomsbury </td>
<td>978-0-7475-7447-7</td>
<td>C1</td>
</tr>
<tr>
<td>Harry Potter and the Chamber of secrets</td>
<td>J.K. Rowling</td>
<td>English </td>
<td>Fantastic</td>
<td> Bloomsbury</td>
<td> 978-0-7475-7448-4</td>
<td> C1</td>
</tr>
<tr>
<td>Harry Potter and the Prisoner of Azkaban</td>
<td>J.K. Rowling</td>
<td>English </td>
<td>Fantastic</td>
<td> Bloomsbury</td>
<td> 978-0-7475-7449-1</td>
<td> C1</td>
</tr>
<tr>
<td>The Hobbit</td>
<td>J.R.R. Tolkien</td>
<td>English</td>
<td>Fantastic</td>
<td>Tolkien</td>
<td> 978-0-261-10221-7</td>
<td>C1</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jane Eyre</td>
<td>Charlotte Brontë </td>
<td>Anglais</td>
<td>roman</td>
<td>Harrap's</td>
<td>978-2-81-870835-4</td>
<td>CM</td></tr>
<tr>
<td>Pride and prejudice</td>
<td>Jane Austen</td>
<td>Anglais</td>
<td>roman </td>
<td>Harrp's</td>
<td>978-0-141-43951-8</td>
<td>CM</td></tr>
</table>
<hr/>
<h1 id="para2"> Le Petit Prince- Antoine de SAINT-EXUPÉRY</h1>
<table>
<!--<tr>
<td colspan="5"><h1 id="para2"> Le Petit Prince- Antoine de SAINT-EXUPÉRY</h1></td>
</tr>-->
<tr>
<th>Titre</th>
<th>Langue</th>
<th>Édition</th>
<th> ISBN </th>
<th> Placement </th>
</tr>
<tr>
<td>Le Petit Prince </td>
<td>Français</td>
<td> Folio</td>
<td> 2-07-040850-7 </td>
<td> C1</td>
</tr>
<tr>
<td>小王子</td>
<td>中国</td>
<td>果麦</td>
<td>978-7-201-07764-2</td>
<td> C1</td>
</tr>
<tr>
<td>Küçük Prens</td>
<td>Türkçe<br/>turc</td>
<td></td>
<td>798-2-07</td>
<td> C1</td>
</tr>
<tr>
<td>малкият принц</td>
<td> <br/></td>
<td></td>
<td></td>
<td>C1</td>
</tr>
<tr>
<td>Il Piccolo Principe</td>
<td>Italiano</td>
<td></td>
<td></td>
<td></td></tr>
<tr>
<td>星の王子さま</td>
<td>日本語</td>
<td></td>
<td></td>
<td></td></tr>
</table>
<hr/>
<h1 id="para2"> 漫画 (Manga - Manhua) / 만화 (Manhwa)</h1>
<table>
<tr>
<th>Titre</th>
<th>Auteur</th>
<th>Tome</th>
<th>ISBN</th>
<th>Placement</th>
</tr>
<tr>
<td>Magus of the Library</td>
<td>Mitsu Izumi</td>
<td>1</td>
<td>979-10-327-0467-7</td>
<td>T</td>
</tr>
</table>
<hr/>
<table>
<tr><th>One piece</th></tr>
<tr><td>1 à 14</td></tr>
<tr><td>18</td></tr>
<tr><td>30</td></tr>
</table>
<!-- <table>
  <h1 id="para4">要购买的书籍</h1>
   <tr>
     <th> Titre </th>
     <th> Auteur </th>
     <th>Genre <br>Matière</th>
     <th> Édition <br><sup>Si précisée</sup></th>
     <th>ISBN <br><sup>Si précisé / donné </sup></th>
   </tr>
   <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'<b>Défendre</b> et <b> entretenir</b> la liberté'(2025-2026)"> Discours de la servitude volontaire </span></td>
     <td> Étienne de La Boétie </td>
     <td rowspan="3"> <em>La Littérature d'idées<br> du XVIe siècle au XVIIIe siècle</em><br> Français </td>
     <td>-</td>
     <td>-</td>
   </tr>
   <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Le goût de la science'(2025-2026)"> Entretiens sur la pluralité des mondes </span></td>
     <td> Bernard Le Bouyer de Fontenelle </td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td> <span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Un nouveau univers s'est offert à mes yeux'(2025-2026)"> Lettres d'une Péruvienne</span></td>
     <td>Françoise de Graffigny</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Mensonge et comédie'(2025-2026)">Le menteur</span></td>
     <td>Pierre Corneille</td>
     <td rowspan="3"><em>Le Théâtre <br> du XVIIe siècle au XXIe siècle </em><br>Français </td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Les jeux du cœur et de la parole'(2025-2026)">On ne badine pas avec l'amour</span></td>
     <td>Alfred de Musset</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Théâtre et dispute'(2025-2026)">Pour un oui ou pour un non</span></td>
     <td>Nathalie Sarraute</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Émancipations créatrices'(2025-2026)">Cahier de Douai</span></td>
     <td>Rimbaud</td>
     <td rowspan="3"><em>La Poésie <br> du XIXe siècle au XXIe siècle</em><br>Français </td>
     <td>买了</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Dans l'atelier du poète'(2025-2026)">La rage de l'expression</span></td>
     <td>Ponge</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'La poésie, la nature, l'intime'(2025-2026)">Mes forêts</span></td>
     <td>Hélène Dorion</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Personnages en marge, plaisirs du romanesque'(2025-2026)">Manon Lescaut</span></td>
     <td>Abbé Prévost</td>
     <td rowspan="3"><em>Le Roman et Le récit <br> Du Moyen Âge au XXIe siècle</em><br>Français </td>
     <td>买了</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'Création et destruction'(2025-2026)">La Peau de chagrin</span></td>
     <td>Balzac</td>
     <td>-</td>
     <td>-</td>
    </tr>
    <tr>
     <td><span pop-def="Œuvre au programme de BAC de Français en classe de Première dont le parcours associé est'La célébration du monde'(2025-2026)">Sido suivi de Les Vrilles de la vigne</span></td>
     <td>Colette</td>
     <td>-</td>
     <td>-</td>
    </tr>
 </table>


 <hr>


 <table>
   <h1 id="para5"> 在土耳其购买  </h1>
   <tr>
     <th>Titre<br>İsim</th>
     <th>Auteur<br>Yazar</th>
     <th>Genre<br>Tür</th>
     <th>Édition<br>Yayın evi<br><sup>s'il y a / Varsa</sup></th>
     <th> ISBN </th>
   </tr>
   <tr>
     <td> Atatürk ve Sumerliler (16) </td>
     <td rowspan="22">Muazzez <br>İlmiye <br> Çığ</td>
     <td rowspan="22">Histoire Tarih</td>
     <td rowspan="22"> Kaynak Yayınları </td>
     <td><a href="https://www.kaynakyayinlari.com/ataturk-ve-sumerliler-p362550.html"> 978-6-056-93549-7</a></td> 
   </tr>
   <tr>
      <td>11-Atatürk Düşünüyor</td>
      <td><a href="https://www.kaynakyayinlari.com/ataturk-dusunuyor-p362485.html">978-6-058-11078-6</a></td>
   </tr>
   <tr>
     <td>01- Kur'an, İncil ve Tevrat'ın Sumer'deki Kökeni</td>
     <td><a href="https://www.kaynakyayinlari.com/kuran-incil-ve-tevratin-sumerdeki-kokeni-p362156.html">978-6-058-11071-7</a></td>
   </tr>
   <tr>
      <td>03- İbrahim Peygamber (Sumer Yazılarına ve Arkeolojik Buluntulara Göre)</td>
      <td><a href="https://www.kaynakyayinlari.com/ibrahim-peygamber-p362188.html">978-6-056-89853-2</a></td>
    </tr> 
    <tr>
     <td>04- İnanna'nın Aşkı(Sumer'de İnanç ve Kutsal Evlenme)</td>
     <td><a href="https://www.kaynakyayinlari.com/inannanin-aski-p362210.html">978-6-057-70711-6</a></td>
   </tr>
   <tr>
     <td>05- Hititler ve Hattuşa (İştar'ın Kaleminden)</td>
     <td><a href="https://www.kaynakyayinlari.com/hititler-ve-hattusa-p362242.html">978-6-056-89854-9</a></td>
   </tr>
   <tr>
     <td>06- Gilgameş (Tarihte İlk Kral Kahraman)</td>
     <td><a href="https://www.kaynakyayinlari.com/gilgames-p362254.html">978-6-056-92173-5</a></td>
   </tr>
   <tr>
     <td>07- Ortadoğu Uygarlık Mirası -1</td>
     <td><a href="https://www.kaynakyayinlari.com/ortadogu-uygarlik-mirasi-1-p362311.html">978-6-057-70713-0</a></td>
   </tr>
   <tr>
     <td>08- Ortadoğu Uygarlık Mirası -2</td>
     <td><a href="https://www.kaynakyayinlari.com/ortadogu-uygarlik-mirasi-2-p362312.html"></a>978-6-058-11076-2</td>
   </tr>
   <tr>
     <td>09- Vatandaşlık Tepkilerim</td>
     <td><a href="https://www.kaynakyayinlari.com/vatandaslik-tepkilerim-p362442.html">978-6-057-70730-7</a></td>
   </tr>
   <tr>
     <td>10- Bereket Kültü ve Mabet Fahişeliği</td>
     <td><a href="https://www.kaynakyayinlari.com/bereket-kultu-ve-mabet-fahiseligi-p362444.html">978-6-056-89855-6</a></td>
   </tr>
   <tr>
     <td>12-Uygarlığın Kökeni Sümerliler-1</td>
     <td><a href="https://www.kaynakyayinlari.com/uygarligin-kokeni-sumerliler-1-p362501.html  ">978-6-058-11074-8</a></td>
   </tr>
    <tr>
     <td>13-Uygarlığın Kökeni Sümerliler-2</td>
     <td><a href="https://www.kaynakyayinlari.com/uygarligin-kokeni-sumerliler-2-p362601.html">978-6-058-11073-1</a></td>
   </tr>
    <tr>
     <td>14-Sumerlilerde Tufan Tufan'da Türkler</td>
     <td><a href="https://www.kaynakyayinlari.com/sumerlilerde-tufan-tufanda-turkler-p362526.html">978-6-058-11079-3</a></td>
   </tr>
    <tr>
     <td>16-Sumerliler Türklerin Bir Koludur</td>
     <td><a href="https://www.kaynakyayinlari.com/sumerliler-turklerin-bir-koludur-p362664.html">978-6-058-11077-9</a></td>
   </tr>
    <tr>
     <td>17-Uyanın Artık!</td>
     <td><a href="https://www.kaynakyayinlari.com/uyanin-artik-p362798.html">978-6-057-70772-7</a></td>
   </tr>
    <tr>
     <td>18-Cumhuriyete Adanan Bir Ömür / Muazzez İlmiye Çığ</td>
     <td><a href="https://www.imge.com.tr/kitap/cumhuriyet-e-adanan-bir-omur-muazzez-ilmiye-cig-9786257697156">978-6-257-69715-6</a></td>
   </tr>
    <tr>
     <td>19-Sevgili Çocuklar</td>
     <td><a href="https://www.kaynakyayinlari.com/sevgili-cocuklar-p364208.html">978-6-059-72813-3</a></td>
   </tr>
    <tr>
     <td>20-Sümer Hayvan Masalları</td>
     <td><a href="https://www.kaynakyayinlari.com/sumer-hayvan-masallari-p364277.html">978-6-058-11010-6</a></td>
   </tr>
   <tr>
     <td>21-Zaman Tüneliyle Sümere Yolculuk</td>
     <td><a href="https://www.kaynakyayinlari.com/zaman-tuneliyle-sumer-e-yolculuk-p364207.html">978-6-057-70795-6</a></td>
   </tr>
   <tr>
     <td>22-Çam Bayramı</td>
     <td><a href="https://www.kaynakyayinlari.com/cam-bayrami-p364595.html">978-6-257-69704-0</a></td>
   </tr> 
   <tr>
     <td>23-İyi ki Varsınız</td>
     <td><a href="https://www.dr.com.tr/kitap/iyi-ki-varsiniz-muazzez-ilmiye-ciga-mektuplar/edebiyat/turk-mektup/urunno=0002040934001">978-6-256-95300-0</a></td>
   </tr>
   <tr>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
   </tr>
 </table>-->
</div>
<script>
        function myFunction() {
            var input, filter, table, tr, td, i, j;
            input = document.getElementById("myInput");
            filter = input.value.toUpperCase();
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");

            // Loop through all rows in the table
            for (i = 0; i < tr.length; i++) {
                // Get all the table cells in the row
                td = tr[i].getElementsByTagName("td");
                let rowMatches = false;

                // Loop through all columns (5 columns in this case)
                for (j = 0; j < td.length; j++) {
                    if (td[j]) {
                        // Check if the text in the cell matches the filter
                        if (td[j].textContent.toUpperCase().indexOf(filter) > -1) {
                            rowMatches = true;
                        }
                    }
                }

                // If a match is found, display the row, otherwise hide it
                if (rowMatches) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    </script>
<hr/>
<!--<script>
  // Fonction de recherche interne
  function search() {
    const input = document.getElementById('search-input').value.toLowerCase();
    const results = document.getElementsByClassName('search-result');
    let found = false;

    for (let i = 0; i < results.length; i++) {
      const result = results[i];
      const text = result.textContent.toLowerCase();

      if (text.includes(input)) {
        result.classList.add('active');
        found = true;
      } else {
        result.classList.remove('active');
      }
    }

    // Afficher le message "Aucun résultat trouvé" si rien ne correspond
    document.getElementById('no-results').style.display = found ? 'none' : 'block';
  }
 </script>-->
<p>
</p><h4> Fait par Ali Can <h4>
 &lt;/p&gt;

 &lt;/html&gt;

</h4></h4></body></html>