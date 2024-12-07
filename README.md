# legaldocs-microservice
This service was designed to automate the process of creating and publishing my legal documents. Previously, this was done in some text editor and exported to PDF. The goal of this project is to create and style a PDF from Markdown files and publish those directly.

### Findings
- When using GitHub pages, we are only allowed to use static content. Placing an `index.pdf` file in the root unforunately does not work. When we are able to move to a dedicated server, this can be possible.


### Architecture
The legal documentation lives in this repository, together with the scripts to publish them. Currently, this is only being published to GitHub Pages.

```mermaid
flowchart LR
    LEGAL_MARKDOWN_FILES
    GITHUB_PAGES_SITE
    PUBLISHING_PROCESS

    LEGAL_MARKDOWN_FILES --> PUBLISHING_PROCESS
    PUBLISHING_PROCESS --> GITHUB_PAGES_SITE;
```