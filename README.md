# masters_experiment_analysis
Data analysis for my Master Experiment Data

Renderizando

install.packages("rmarkdown")
install.packages("tinytex")

library(rmarkdown)
library(tinytex)
tinytex::install_tinytex()

render("main.Rmd")
render("main.Rmd", output_format = "word_document")

Possíveis tipos

html_notebook ? - Interactive R Notebooks
html_document ? - HTML document w/ Bootstrap CSS
pdf_document ? - PDF document (via LaTeX template)
word_document ? - Microsoft Word document (docx)
odt_document ? - OpenDocument Text document
rtf_document ? - Rich Text Format document
md_document ? - Markdown document (various flavors

ioslides_presentation ? - HTML presentation with ioslides
revealjs::revealjs_presentation ? - HTML presentation with reveal.js
slidy_presentation ? - HTML presentation with W3C Slidy
beamer_presentation ? - PDF presentation with LaTeX Beamer
powerpoint_presentation ?: PowerPoint presentation