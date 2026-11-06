# Orchestrateur ou integration continue ? (TP06)

| Critere | Prefect (orchestrateur) | GitHub Actions (CI) |
|---|---|---|
| Ce qui declenche l'execution | Une planification cron, un lancement depuis l'interface ou un appel Python | Un push ou un lancement manuel avec workflow_dispatch |
| Ou s'execute le traitement | Sur la machine du serveur/worker Prefect, ici le poste local | Sur une machine Linux temporaire de GitHub |
| Qui surveille, et ou | Prefect Server, dans son interface web avec l'etat et les journaux des taches | GitHub Actions, dans l'onglet Actions avec les journaux de chaque etape |
| Ce qui se passe en cas d'echec | La tache et le flow passent en echec; le seuil de qualite bloque la notification | Le job devient rouge et les etapes suivantes sont arretees |
| Type de tache adapte | Traitements recurrents et pipelines de donnees/ML en exploitation | Verification du code et de la qualite a chaque changement |
| Ce qui est versionne dans Git | Le code du flow et les fichiers de deploiement/configuration versionnes | Le fichier YAML du workflow CI, les scripts et les dependances |

## Conclusion (5 lignes)

La chaine d'integration continue valide le code a chaque modification.
L'orchestrateur planifie, lance et surveille les traitements recurrents.
Prefect expose l'etat de chaque tache et applique le seuil de qualite avant notification.
GitHub Actions verifie que le pipeline reste reproductible dans un environnement propre.
Les deux approches sont complementaires et repondent a des besoins differents.

## Reponses aux questions

1. Un orchestrateur gere l'execution des traitements en production (ordre, planification, reprises et suivi); la CI verifie automatiquement les changements de code avant leur integration.
2. Le tableau Prefect montre l'execution en echec, la tache fautive et ses journaux. Pour prevenir activement l'equipe, il faut ajouter une notification (courriel, Slack ou autre integration); la tache `notifier` actuelle ne fait qu'ecrire dans les journaux et ne s'execute pas si la validation echoue.
3. Les reprises de `rejouer_pipeline` peuvent absorber une panne transitoire d'outil ou d'infrastructure. Une validation sous le seuil est un resultat deterministe: la relancer sans changer le modele ne l'ameliorerait pas.
4. Une interface graphique facilite le demarrage et l'observation pour les profils non techniques. Une configuration faite uniquement dans l'interface est moins facile a relire, auditer et reproduire; un fichier versionne rend les changements visibles et partageables.
5. L'arrivee d'un volume de nouvelles transactions ou une derive des donnees pourrait declencher le reentrainement. Un service de surveillance detecterait le seuil de volume ou de derive et appellerait l'API Prefect pour lancer le flow.
6. Le stockage DVC local du poste n'est pas accessible aux runners GitHub. La CI regenere donc les donnees deterministes. En equipe, il faudrait un stockage distant DVC securise et accessible au runner, configure avec des identifiants stockes dans les secrets GitHub.

## Captures a completer apres execution

Les captures Prefect (1 a 4) et GitHub Actions (5) doivent etre ajoutees apres les executions reelles et la publication du depot. Elles ne peuvent pas etre reconstituees a partir des fichiers seuls.
