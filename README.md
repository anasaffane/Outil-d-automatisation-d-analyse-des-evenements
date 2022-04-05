# SOC_Analysis_Tool
Outil d'analyste SOC pour automatiser l'investigation et la validation d'éventuels indicateurs de compromission (IOC) et effectuer diverses tâches, notamment l'analyse des e-mails de phishing et la surveillance de la marque pour accélérer la réponse aux incidents.

L'objectif principal de l'utilisation de cet outil est d'automatiser autant de points de validation que possible effectués par l'équipe des opérations de sécurité d'entreprise tout en travaillant sur tout incident de sécurité, y compris la surveillance de la marque et une éventuelle attaque de phishing.

L'outil implémente également le cryptage (symétrique) afin que toutes vos clés API soient secrètes et sûres et ne puissent pas être manipulées tant que la clé de cryptage secrète n'est pas utilisée. Vous pouvez cependant modifier à tout moment vos clés API si vous avez accès à la clé de chiffrement.

## CARACTÉRISTIQUES

Cet outil peut actuellement effectuer les tâches ci-dessous :
Vérification de la réputation des adresses IP, des domaines, des URL et des hachages de fichiers:
- [Virustotal](https://www.virustotal.com/gui/home/upload)
- [Abuse IP DB](https://www.abuseipdb.com/)
- [Alienvault OTXv2](https://otx.alienvault.com/)
- [Spyse](https://spyse.com/)
- [Phishtank](https://phishtank.org/)
- [URL Scan](https://urlscan.io/)

Analyse de la sécurité des e-mails ( Phishing Email Analysis ) :

- Analyser une URL de phishing
- Sandbox une pièce jointe malveillante présente dans un e-mail
- Analyse de l'en-tête des e-mails
- Directives pour effectuer une analyse des e-mails de phishing afin d'identifier les menaces .

Effectuer des recherches DNS, DNS inversé, WHOIS, ISP Lookups .
Décodage des URL Office365 Safelink, des URL encodées UTF-8 ou Base64 .
Exécution de File Sandboxing pour le fichier et sa réputation de hachage de fichier associée .
Effectuer une analyse de surveillance .
## COMMENT L'UTILISER
Le script est simple à comprendre et à utiliser. Il peut être utilisé dans toutes ses fonctionnalités sans ouvrir le code source d'édition
1. Lors de l'exécution du script principal pour la première fois, il vous dirigera automatiquement vers le menu de configuration, où il vous sera demandé d'entrer les clés API des plates-formes utilisées dans l'outil .
2. Toutes les clés API sont gérées séparément dans le fichier de clés API. Les clés API sont également cryptées avec un cryptage à clé symétrique .
