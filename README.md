# Ngrok_Serveur

## Description

**Ngrok_Server** est un projet permettant de partager des fichiers via un tunnel sécurisé créé avec Ngrok. Il offre une méthode simple pour exposer un dossier local à Internet, facilitant ainsi le partage de fichiers ou l'accès à des services locaux depuis n'importe où.

## Structure du projet

Le dépôt contient les éléments suivants :

- **Ngrok_Web** : Interface web pour interagir avec Ngrok.
- **Public** : Dossier contenant les fichiers à partager.
- **Script** : Scripts pour automatiser la création du tunnel Ngrok.

## Prérequis

- [Ngrok](https://ngrok.com/) installé sur votre machine.
- Un compte Ngrok pour obtenir un token d'authentification (facultatif mais recommandé pour des fonctionnalités avancées).

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/kibagami-nc/Ngrok_PF.git
   cd Ngrok_PF
   ```
   
2. Placez les fichiers que vous souhaitez partager dans le dossier Public.

3. Exécutez le script approprié pour lancer Ngrok :

Pour un tunnel HTTP :

  ```bash
  ./Script/start_http.sh
  ```

Pour un tunnel HTTPS :

  ```bash
  ./Script/start_https.sh
  ```

Ces scripts démarreront Ngrok et fourniront une URL publique pour accéder à vos fichiers.

## Utilisation

Une fois le tunnel Ngrok lancé, vous recevrez une URL publique (par exemple, https://abcd1234.ngrok.io). Partagez cette URL avec les personnes avec qui vous souhaitez partager vos fichiers.

## Contribuer

Les contributions sont les bienvenues ! Pour proposer des améliorations ou signaler des problèmes, veuillez ouvrir une issue ou soumettre une pull request.
