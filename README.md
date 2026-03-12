# README – test.ipynb

## Description
Ce notebook est un fichier de **test et d’expérimentation** avec l’API OpenAI et la bibliothèque **LangChain**.  
Le but est de comprendre comment utiliser un modèle d’IA pour travailler avec du **texte, des images et des tokens**.

## Ce que nous avons fait dans ce notebook

### 1. Gestion de la clé API
On charge la clé API avec **dotenv** depuis les variables d’environnement pour pouvoir utiliser l’API OpenAI dans le code.

### 2. Travail avec les tokens
On utilise la bibliothèque **tiktoken** pour comprendre comment un texte est découpé en tokens.

Dans cette partie on :
- écrit un prompt (texte)
- transforme ce texte en **tokens**
- affiche la liste des tokens
- affiche chaque morceau de texte correspondant à un token
- crée une fonction `tokens_count()` pour **compter le nombre de tokens d’un texte**

Le but est de comprendre comment les modèles lisent un texte et pourquoi le nombre de tokens est important.

### 3. Utilisation d’un modèle LLM
On utilise **LangChain** pour appeler un modèle et lui envoyer un prompt.  
Le modèle génère ensuite une réponse qui est affichée dans le notebook.

### 4. Génération d’image
On utilise un modèle avec un **outil de génération d’image**.  
On lui demande par exemple de générer une image (ex : un chat qui code).  
L’image est retournée en **base64**, puis décodée pour l’afficher dans le notebook.

### 5. Lecture d’une image avec l’IA
On prend une image locale (`test.jpg`) et on l’envoie au modèle.

Le modèle analyse l’image et **explique ce qu’il voit dedans**.

### 6. Analyse d’un texte en JSON
On demande au modèle de répondre dans un **format JSON** (comme un assistant RH qui analyse un candidat).  
Ensuite :
- on récupère la réponse
- on la convertit en **objet JSON**
- on affiche certaines informations (nom du candidat, poste, points forts)

## Objectif
Ce notebook sert principalement à :
- apprendre comment fonctionnent les **tokens**
- tester **l’appel aux modèles LLM**
- tester la **génération d’images**
- tester la **compréhension d’images**
- manipuler des **réponses JSON générées par l’IA**

## Remarque
Ce fichier est surtout un **notebook de test pour apprendre à utiliser les modèles d’IA avant de les intégrer dans un projet plus grand.**
=======
# IA-agentic
repo avec les tp de ia agentic
