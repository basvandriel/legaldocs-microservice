# General terms microservice
This service is designed for providing PDF documents for my freelancing general terms.

#### Goal
The goal is to host this project at https://basvandriel.nl/legal-pdf-microservice-gh-pages/.

### Findings
- When using GitHub pages, we are only allowed to use static content. Placing an `index.pdf` file in the root unforunately does not work. When we are able to move to a dedicated server, this can be possible.


#### Architecture
Currently, the application is setup that the actual documentation lives in this repository, together with the scripts to publish them. Currently, this is only being published to GitHub Pages.

```mermaid
flowchart LR
    LEGAL_MARKDOWN_FILES
    GITHUB_PAGES_SITE
    GITHUB_PAGES_REPO
    PUBLISHING_PROCESS

    LEGAL_MARKDOWN_FILES --> PUBLISHING_PROCESS

    PUBLISHING_PROCESS --> GITHUB_PAGES_REPO
    GITHUB_PAGES_REPO --> GITHUB_PAGES_SITE;
```