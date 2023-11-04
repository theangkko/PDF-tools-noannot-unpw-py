# PDF Tools-noannot-unpw

<br>

## 주요기능 Functions
- PDF내 주석을 일괄삭제합니다    
  Delete All annotation in PDF
- PDF수정보호(자물쇠) 상태를 해제합니다    
  Remove Lock status in PDF(Read Protected)

<br><br>

## 사용법 How to Use
- “Pick File” 버튼을 눌러, 주석제거 또는 암호해제할 pdf 파일을 선택합니다.    
  Select the PDF file with "Pick File" button
- 암호해제 기능과 주석제거 기능 중 원하는 기능을 선택합니다.    
  Select a function with Button selection
- “Submit” 버튼을 눌러 작업을 실행합니다    
  Run progress with "Submit" button

   
<br><br>

![image](https://github.com/theangkko/PDFtools-py/assets/75212211/071c232c-052d-4275-b9ba-214e203cfa4a)



<br><br><br>

***




### install library
poetry install 

### activating venv 
poetry shell

### for running
poetry run python PDFtools-tk.py


### to build exe file
```
auto-py-to-exe
```

```
pyinstaller -F --noconfirm --onefile --windowed --icon "D:/repo/PDF-tools-noannot-unpw-py/icon.ico" --name "PDFtools_noAnnot" --additional-hooks-dir=. "D:/repo/PDF-tools-noannot-unpw-py/PDFtools-tk.py"
```


<br><br><br><br>


### REFERENCE
to use pyinstaller with tkinterdnd2
need addtional hook file(hook-tkinterdnd2.py) at root folder 
https://github.com/Eliav2/tkinterdnd2