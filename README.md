# TD XP : Coffre à Trésor  
### TDD • Pair Programming • Équipes de 4 • Design simple

Votre objectif : développer un **moteur de Coffre à Trésor** en appliquant les pratiques XP (eXtreme Programming).

Vous travaillerez en :
- **Pair Programming** (Driver/Navigator, rotation régulières)
- **Équipe de 4** (2 binômes en parallèle)
- **TDD strict** (Red → Green → Refactor)
- **Itérations courtes** avec synchronisations régulières

Le code appartient **à l’équipe entière**.

---

## Objectifs du TD
- Concevoir un système simple guidé par les tests  
- Pratiquer le Pair Programming de manière fluide  
- Coordonner deux binômes dans une mini‑équipe XP  
- Construire un backlog fonctionnel minimal  
- Maintenir un design propre malgré les rotations

Durée estimée : **4 heures**

---

## User Stories

### MVP
1. **Ajouter un objet**  
   En tant qu’aventurier, je veux ajouter un objet (nom, poids, valeur) dans mon coffre.

2. **Retirer un objet**  
   En tant qu’aventurier, je veux retirer un objet par son nom.

3. **Lister les objets**  
   En tant qu’aventurier, je veux afficher la liste des objets présents.

4. **Poids total**  
   En tant qu’aventurier, je veux connaître le poids total du coffre.

5. **Valeur totale**  
   En tant qu’aventurier, je veux connaître la valeur totale du coffre.

---

### Fonctionnalités utiles
6. **Empêcher les doublons**  
7. **Capacité maximale configurable**  
8. **Objets rares (valeur ×2)**  
9. **Trier les objets** (nom, poids, valeur)  
10. **Rechercher un objet par son nom**

---

### Bonus
11. **Verrouiller le coffre** (aucune modification possible)  
12. **Historique des actions**  
13. **Transférer un objet entre deux coffres**

---

## Organisation de l’équipe

### Binômes  
- Travail en parallèle par 2 paires.  
- Driver = code • Navigator = réflexion.  
- **Rotation Driver/Navigator toutes les 4 minutes.**

### Synchronisations (toutes les ~25–30 min)
Durée : 5 minutes max  
Objectifs :
- partager l’avancement (tests + code)  
- aligner le design  
- ajuster le backlog  
- **changer les binômes**  
- décider des prochaines micro‑US  

---

## Règles TDD
1. **Écrire un test qui échoue**  
2. **Faire passer le test avec le code le plus simple**  
3. **Refactoriser** en gardant tous les tests au vert  
4. Recommencer

**Interdiction d’écrire du code sans test préalable.**

---

## Livrables attendus
- moteur de coffre minimal fonctionnel  
- tests unitaires écrits en TDD  
- board de stories (photo ou fichier)  
- mini rétrospective (5–10 lignes)  
- code propre, lisible, cohérent entre binômes

---

## Pour démarrer
1. Choisissez un langage commun dans l’équipe  
2. Créez la structure minimale du projet  
3. Commencez par **US1**  
4. Avancez en micro‑pas et synchronisez régulièrement

---

## Conseils
- Visez la simplicité (KISS).  
- Préférez plusieurs petits tests à un gros.  
- N’ayez pas peur de refactoriser souvent.  
- Le design doit **émerger**, pas être planifié d’avance.

---

Bon courage, et… testez d’abord !

