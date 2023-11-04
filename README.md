# PDFtools-py

poetry install 

## activating venv 
poetry shell

## for running
poetry run python PDFtools-tk.py


## to build exe file
auto-py-to-exe

pyinstaller -F --noconfirm --onefile --windowed --icon "D:/repo/PDF-tools-noannot-unpw-py/icon.ico" --name "PDFtools_noAnnot" --additional-hooks-dir=. "D:/repo/PDF-tools-noannot-unpw-py/PDFtools-tk.py"


<br><br><br><br>


## REFERENCE
to use pyinstaller with tkinterdnd2
need addtional hook file(hook-tkinterdnd2.py) at root folder 
https://github.com/Eliav2/tkinterdnd2