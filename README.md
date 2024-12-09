# Projet ASCII - Dockerisé 🐳

Ce projet affiche des images en ASCII art, et grâce à Docker, il est désormais facile à utiliser sans avoir à configurer l'environnement manuellement.

---

## 🚀 Fonctionnalités

- Conversion d'images en ASCII art.
- Environnement entièrement encapsulé avec Docker.
- Aucune configuration manuelle requise (sauf si tu n’as pas Docker 😏).

---

## 🛠️ Prérequis

1. **Docker** : Installe Docker en suivant les instructions officielles [ici](https://www.docker.com/products/docker-desktop).  
2. **Docker Desktop** : Active-le après l'installation.  

Vérifie que Docker est opérationnel :  
```bash
docker --version
```
## ⚙️ Installation et utilisation

**Construis l'image Docker et lance la**
```bash
docker build -t ascii-project .
docker run --rm -it ascii-project
```
