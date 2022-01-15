from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from logger import *
import json

main_root = Tk()
main_root.title('STER')
main_root.geometry('500x500')
icon = PhotoImage(file='ast/icon.png')
main_root.iconphoto(False, icon)
main_root.config(bg='#434343')
log_start()
font_sty = 'Segoe UI Semilight Italic'
bg_col = '#434343'


def start_page():
    create_log('Entered Start_Page()')
    root01 = Toplevel(main_root)
    root01.title('Create Page')
    root01.geometry('500x500')
    root01.config(bg=bg_col)
    root01.iconphoto(False, icon)
    # frame1 = Frame(root01, bg=bg_col)
    # frame1.pack(fill=BOTH, expand=TRUE)
    color_stored = ''

    def color_choose():
        my_color = colorchooser.askcolor()[1]
        my_dict = {
            'background_color': my_color
        }
        jsn = json.dumps(my_dict)
        with open('color.json', 'w') as file:
            file.write(jsn)
        create_log('Saving JSON, Checkpoint 1')

    def icon_file():
        file_dir = filedialog.askopenfilename(filetypes=(('PNG Only', '*.png'),))
        my_dict2 = {
            'file_path': file_dir
        }
        jsn = json.dumps(my_dict2)
        with open('icon.json', 'w') as file:
            file.write(jsn)
        create_log('Saving JSON, Checkpoint 2')

    def save():
        software_name = entb01.get()

        with open('color.json', 'r') as file:
            data = file.read()
            data_color = json.loads(data)

        with open('icon.json', 'r') as file:
            data2 = file.read()
            data_icon = json.loads(data2)

        my_dict = {
            'bg_col': data_color['background_color'],
            'icon-dir': data_icon['file_path'],
            'stwr-name': software_name
        }
        jsn = json.dumps(my_dict, indent=4)
        with open('builder_loader.json', 'w') as file:
            file.write(jsn)

        messagebox.showinfo('Success', 'Successfully Stored Data')
        create_log('Saving JSON, Checkpoint Final Done')

    lbl1 = Label(root01, text='New Software Name : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15))
    lbl1.pack(pady=10)

    entb01 = Entry(root01, fg='white', bg=bg_col, font=(font_sty, 20))
    entb01.pack(pady=10)

    lbl2 = Label(root01, text='Choose a Icon ( only .png accepted ) : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15))
    lbl2.pack(pady=10)

    btn2 = Button(root01, text='Click to Choose File', bg=bg_col, fg='#adff2f', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=icon_file)
    btn2.pack(pady=10)

    lbl3 = Label(root01, text='Pick a Background Color : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15)).pack(pady=10)

    btn3 = Button(root01, text='Color Chooser', bg=bg_col, fg='#adff2f', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=color_choose).pack(pady=10)

    btn4 = Button(root01, text='Save & Continue', bg=bg_col, fg='orange', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=save).pack(side=BOTTOM, pady=10)


'''    def choose_file():
        create_log('Waiting for User to Choose File')
        file_dir = filedialog.askopenfilename(filetypes=(('PNG Only', '*.png'),))

        def write_file_dir():
            my_dict = {
                'file_directory': file_dir
            }
            js = json.dumps(my_dict)
            with open('builder_loader.json', 'w') as file:
                file.write(js)
                file.close()
            create_log('Successfully Stored file_dir in JSON')
            messagebox.showinfo('Success', 'Successfully Stored')

        write_file_dir()
        create_log('User Choosed File, File stored as file_dir variable')'''

'''    def get_color_choosen():
        my_color = colorchooser.askcolor()[1]
        my_dict = {
            'background_color': my_color
        }
        jsn = json.dumps(my_dict)
        with open('builder_loader.json', 'r+') as file:
            file.read()
            my_dict['background_color'] = my_color
            file.write()
        create_log('Stored Color Choosen')
        messagebox.showinfo('Success', 'Successfully Stored Chosen Color!')'''

btn1 = Button(main_root, text='Create Software', font=(font_sty, 30), bg=bg_col, fg='white', relief=SUNKEN, bd=0,
              activeforeground='orange', activebackground=bg_col, command=start_page)
btn1.pack(pady=20)
main_root.mainloop()
