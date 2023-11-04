
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import DND_FILES, TkinterDnD
# import tkinter as tk


from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from threading import Thread
import pathlib
import pikepdf

class PDFunpwnoannot(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=(10, 5))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.option_method_noannot = ttk.IntVar(value=100)
        self.option_method_unpw = ttk.IntVar(value=0)
        print(self.option_method_unpw, type(self.option_method_unpw))
        self.name = ttk.StringVar(value="")

        self.path_var = ttk.StringVar(value="")
        self.filename_path_var = ttk.StringVar(value="Drop file HERE")
        self.work_result_var = ttk.StringVar(value="...")

        # application variables
        _path = pathlib.Path().absolute().as_posix()
        _filename = pathlib.Path().absolute()


        # form header
        hdr_txt = "Small PDF tools" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50, font="arial 14")
        hdr.pack(fill=X, pady=10)

        # url_txt = "github_source" 
        # url_github_source = ttk.Label(master=self, text=url_txt, width=30,)
        # url_github_source.pack(side=RIGHT)

        # form entries
        self.create_form_entry("File Path", self.filename_path_var)
        self.create_buttonbox()
        # self.create_result_message()

         # two finger gestures
        option_PDF_method = ttk.Labelframe(
            master=master,
            text='Select Function',
            padding=(15, 10)
        )
        option_PDF_method.pack(
            side=TOP,
            fill=BOTH,
            expand=YES,
            pady=(10, 0)
        )
        op_noannot = ttk.Checkbutton(
            master=option_PDF_method,
            bootstyle="success-round-toggle",
            text='Delete all Annotations',
            variable=self.option_method_noannot,
            onvalue=100,
            offvalue=0,
            command=lambda: (
                        print('clicked_noannot'), 
                        self.option_method_unpw.set(0),
                    ),
        )
        op_noannot.pack(fill=X, pady=5)
        op_unpw = ttk.Checkbutton(
            master=option_PDF_method,
            bootstyle="success-round-toggle",
            text='Unprotect PDF for edit',
            variable=self.option_method_unpw,
            onvalue=10,
            offvalue=0,
            command=lambda: (
                        print('clicked_unpw'), 
                        self.option_method_noannot.set(0),
                    ),
        )
        op_unpw.pack(fill=X, pady=5)


    def toggle_checkbutton(event, checkbutton_name):
        """Toggle the state of a checkbutton"""
        print(checkbutton_name, type(checkbutton_name))
        # checkbutton_name.toggle()


    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        ent.drop_target_register(DND_FILES)
        ent.dnd_bind('<<Drop>>', self.drop_inside_box_find_filepath )
    
    
    def create_result_message(self):
        container2 = ttk.Frame(self)
        container2.pack(fill=X, expand=YES, pady=5)
        container2.children.clear()
        lbl_result = ttk.Label(master=container2, text=self.work_result_var.get())
        lbl_result.pack(side=LEFT, padx=5)
        
        

    def drop_inside_box_find_filepath(self, event):
        print(type(event.data), event.data)
        filepaths = event.data.split(' ')
        for each in filepaths:
            if each.split('/')[-1].endswith(".pdf"):
                print(each)
                self.filename_path_var.set(each)    

    
    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=SECONDARY,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=DANGER,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        # sub_btn.focus_set()



        btn_open_folder = ttk.Button(
            master=container, 
            text="Pick File",
            # image='opened-folder', 
            # bootstyle=(LINK, SECONDARY),
            bootstyle=(PRIMARY),
            command=self.on_browse_file
        )
        btn_open_folder.pack(side=RIGHT, padx=5)
        btn_open_folder.focus_set()


    def get_directory(self):
        """Open dialogue to get directory and update variable"""
        self.update_idletasks()
        d = askdirectory()
        if d:
            self.setvar('folder-path', d)

    def on_browse_folder(self):
        """Callback for directory browse"""
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)

    def on_browse_file(self):
        """Callback for A file browse"""
        path = askopenfilename(title="Browse PDF file",
                            filetypes =(("PDF files","*.pdf"),
                                    #   ("all files","*.*"),
                                      )
                            )
        print(path)
        if path:
            self.filename_path_var.set(path)

    def on_submit(self):
        """Print the contents to console and return the values."""
        print("folder name:", self.path_var.get())
        print("file name:", self.filename_path_var.get())
        filename = pathlib.Path(self.filename_path_var.get())
        print("unpw/noannot :", self.option_method_unpw.get(), self.option_method_noannot.get())
        if self.option_method_noannot.get() == 100:
            Thread(target=self.remove_annotation_from_pdf,
                   args=[filename] 
                   ).start()
        elif self.option_method_unpw.get() == 10:
            Thread(target=self.remove_password_from_pdf, 
                   args=[filename] 
                   ).start()
        result_message = str(filename) + " DONE"
        print(result_message)
        self.work_result_var.set(result_message)
        self.create_result_message()


    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()

        
    def remove_password_from_pdf(self, filename, password=None):
        # with pikepdf.open(filename) as pdf:
        #     pdf.save(f"{filename}_unpw.pdf")
        pdf = pikepdf.open(filename)
        # pdf.save(f"{filename}_unpw.pdf")
        pdf.save(f"{filename.parent}/{filename.stem}_unpw{filename.suffix}")
        
        
    def remove_annotation_from_pdf(self, filename, password=None):
        with pikepdf.open(filename) as pdf:
            for page in pdf.pages:
                print(page.Annots)
                if page.Annots:
                    page.Annots = []
            # pdf.save(f"{filename}_noAnnot.pdf")
            pdf.save(f"{filename.parent}/{filename.stem}_noAnnot{filename.suffix}")
            



if __name__ == "__main__":
    app = TkinterDnD.Tk()
    # app.iconphoto(False, tk.PhotoImage(file="icon.ico"))
    # app.iconbitmap(pathlib.Path("icon.ico"))
    app.title("PDF Tools-noAnnot_unpw v0.9.4")
    # app = ttk.Window("PDF Tools-noAnnot_unpw v0.9.4", "flatly", resizable=(False, False))
    app.geometry("500x350")
    PDFunpwnoannot(app)
    app.mainloop()
