# README of the Developmental AI for ROS project

This repository provides code for practicing developmental AI in the [ROS](https://www.ros.org/) environment.

world.py provides the general framework for implementing a developmental agent and testing it in rudimentary environments. 
It is a standalone file that can run in any python environment.

turtlesim_enacter.py provides the interface between a developmental agent and the [turtlesim simulator](http://wiki.ros.org/turtlesim). 
It requires a ROS installation. 

See the [wiki](https://github.com/OlivierGeorgeon/TestROS/wiki) to learn how to use it (French).

## README du TP (French)

Etudiants : 
 - ORTEGA Guillaume
 - BONNAVAUD Hedwin (https://hbonnavaud.com)
 
Enseignant : GEORGEON Olivier

### Utilisation

Pour exécuter le code lancer la commande `./world.py` (python devra être installé)

Pour paramétrer l'exécution :\
Au début du fichier world.py, vous trouverez les informations de l'exécutions :

```
hedonist_table = [[-1, 1], [-1, 1]]

# Choose an agent
use_basic_agent = 3  # we will use bored agent otherwise
# 1 : Agent
# 2 : BoredAgent
# 3 : RandomExplorerAgent

# Choose an environment
environment_id = 3      # id of the environment to use
# 1 : Environment1
# 2 : Environment2
# 3 : Environment3
```

### Informations techniques
#### Agent rudimentaire

[-> informations sur l'agent rudimentaire](https://github.com/OlivierGeorgeon/TestROS/wiki/Implementer-un-agent-rudimentaire) \
L'implémentation de cet agent se trouve dans le fichier /Agents/Agent. Il sert de classe mère aux autres agents

#### L'agent qui n'aimait pas s'ennuyer

[-> informations sur l'agent qui n'aimait pas s'ennuyer](https://github.com/OlivierGeorgeon/TestROS/wiki/Agent-1) \
L'implémentation de cet agent se trouve dans le fichier /Agents/BoredAgent

#### L'agent aléatoire

Par curiosité, nous avons décider d'implémenter un agent qui explore les positions de manière aléatoires.\
à chaque itérations, cet agent vas choisir soit d'effectuer une action connue, soit d'explorer nue nouvelle action parmis les actions qu'il n'a pas encore essayé.

#### Les environements
Les environnements /Environments/Environment1 et /Environments/Environment2 correspondent aux environnements initiaux.

Nous avons décidé d'ajouter un environnement supplémentaire, plus complexe, pour avoir une meilleur vision de l'efficatité de nos agents. Cet envirionement est implémenté dans le fichier /Environments/Environment3.