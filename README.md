# Repository Overview

This repository was used to develop the vulnerable code file for ds2003's dissertation project. The other repository containing the majority of the project's code can be found [at this GitHub repository](https://github.com/DavidNathaniel/ds2003_dissertation_project/). This repository is connected to SonarCloud through tokens in this projects repository secrets, and all push requests to this repository trigger an Action which sends a signal to SonarCloud to scan the newly updated branch.

## Code Files

1. **[vulnerable_code.py](vulnerable_code.py)**: Contains code vulnerabilities as described in OWASP and CWE.
   
2. **[build.yml](.github/workflows/build.yml)**: The GitHub Action which triggers a scan in Sonarcloud. 
