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
    root01.geometry('500x600')
    root01.config(bg=bg_col)
    root01.iconphoto(False, icon)
    frame1 = Frame(root01, bg=bg_col)
    frame1.pack(fill=BOTH, expand=TRUE)
    # main_root.update()
    # main_root.protocol("WM_DELETE_WINDOW", main_root.deiconify)
    color_stored = ''

    def second_page():
        frame2 = Frame(root01, bg=bg_col)
        frame2.pack(fill=BOTH, expand=TRUE)
        lbl5 = Label(frame2, text='Select Widgets : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                     font=(font_sty, 30))
        lbl5.pack(pady=10)

        def add_label_wdt():
            create_log('Entered Label Creation Stage')
            root3 = Toplevel(root01)
            root3.title('New label Configuration')
            root3.geometry('350x350')
            root3.config(bg=bg_col)
            lbl20 = Label(root3, text='Enter Label Text : ', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=0,
                          font=(font_sty, 15))
            lbl20.pack(pady=5)
            ent20 = Entry(root3, bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                          font=(font_sty, 15))
            ent20.pack(pady=5)
            lbl21 = Label(root3, text='Enter Label Color ( HEX Only ) : ', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=0,
                          font=(font_sty, 15))
            lbl21.pack(pady=5)

            def check_all():

                def check_text():
                    entered20 = ent20.get()

                    if entered20 == '':
                        messagebox.showerror('Oops', 'The Text Field Cannot be Empty!')
                    else:
                        pass

                def check_hex():
                    entered_text = ent21.get()
                    if len(entered_text) > 7:
                        messagebox.showerror('Wrong Info Entered', 'Max. HEX Color Length = 8')
                    elif '#' not in str(entered_text):
                        messagebox.showerror('Error!', 'Not a Valid Hex Color')
                    else:
                        pass
                    '''except:
                        messagebox.showerror('Error', 'ErrorCode-"SP()>SP()>ALW()>CA()>CH()>Exp_Block" \n Contact Dev')'''

                def check_font_len():
                    entered_text = ent22.get()
                    try:
                        if int(entered_text) > 30:
                            messagebox.showerror('Error!', 'Max Font Size = 30')
                        elif int(entered_text) < 5:
                            messagebox.showerror('Error!', 'Min Font Size = 5')
                        else:
                            pass
                    except Exception as e:
                        messagebox.showerror('Error',
                                             'ErrorCode-"SP()>SP()>ALW()>CA()>CFL()>Except_Block", Contact Dev')
                        print(e)

                check_text()
                check_hex()
                check_font_len()

            ent21 = Entry(root3, bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                          font=(font_sty, 15))
            ent21.pack(pady=5)

            lbl22 = Label(root3, text='Enter label Size ( 5 - 30 ) : ', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=0,
                          font=(font_sty, 15))
            lbl22.pack(pady=5)

            ent22 = Entry(root3, bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                          font=(font_sty, 15))
            ent22.pack(pady=5)

            btn20 = Button(root3, text='Save', bg=bg_col, fg='#ff8c00', relief=SUNKEN, bd=1,
                           font=(font_sty, 15), command=check_all)
            btn20.pack(pady=5, side=BOTTOM)

        btn5 = Button(frame2, text='Add New Label / Text', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                      font=(font_sty, 17), command=add_label_wdt)
        btn5.pack(pady=10)
        btn6 = Button(frame2, text='Add Button', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                      font=(font_sty, 17))
        btn6.pack(pady=10)
        btn7 = Button(frame2, text='Add Entry Box', bg=bg_col, fg='#4dffff', relief=SUNKEN, bd=1,
                      font=(font_sty, 17))
        btn7.pack(pady=10)
        lstbx1 = Listbox(frame2, bg=bg_col, fg='#ff3333', relief=SUNKEN, bd=1,
                         font=(font_sty, 17), width=400, height=300)
        lstbx1.pack(pady=10, side=BOTTOM)
        lstbx1.insert(0, 'Selected Items :')

    def color_choose():
        my_color = colorchooser.askcolor()[1]
        if not my_color:
            messagebox.showerror('Error!', 'Please Choose a Color to Continue')
        else:
            my_dict = {
                'background_color': my_color
            }
            jsn = json.dumps(my_dict)
            with open('color.json', 'w') as file:
                file.write(jsn)
            create_log('Saving JSON, Checkpoint 1')

    def icon_file():
        file_dir = filedialog.askopenfilename(filetypes=(('PNG Only', '*.png'),))

        def check_file():
            if not file_dir:
                messagebox.showerror('Error!', 'Please Choose a File to Continue')
            else:
                my_dict2 = {
                    'file_path': file_dir
                }
                jsn = json.dumps(my_dict2)
                with open('icon.json', 'w') as file:
                    file.write(jsn)
                create_log('Saving JSON, Checkpoint 2')

        check_file()

    def save():
        software_name = entb01.get()
        if not software_name:
            messagebox.showerror('Error!', 'The Software Name Field Cannot be Empty')
        else:

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
            frame1.pack_forget()
            second_page()

    lbl1 = Label(frame1, text='New Software Name : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15))
    lbl1.pack(pady=10)

    entb01 = Entry(frame1, fg='white', bg=bg_col, font=(font_sty, 20))
    entb01.pack(pady=10)

    lbl2 = Label(frame1, text='Choose a Icon ( only .png accepted ) : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15))
    lbl2.pack(pady=10)

    btn2 = Button(frame1, text='Click to Choose File', bg=bg_col, fg='#adff2f', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=icon_file)
    btn2.pack(pady=10)

    lbl3 = Label(frame1, text='Pick a Background Color : ', bg=bg_col, fg='white', relief=SUNKEN, bd=0,
                 font=(font_sty, 15)).pack(pady=10)

    btn3 = Button(frame1, text='Color Chooser', bg=bg_col, fg='#adff2f', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=color_choose).pack(pady=10)

    btn4 = Button(frame1, text='Save & Continue', bg=bg_col, fg='orange', relief=SUNKEN, bd=1,
                  font=(font_sty, 15), command=save).pack(side=BOTTOM, pady=10)

    main_root.withdraw()
    root01.focus_force()

    def closing():
        create_log('Entered closing()')
        main_root.update()
        main_root.deiconify()
        root01.destroy()
        messagebox.showwarning('Sed!', 'You Left Without Saving')

    root01.protocol("WM_DELETE_WINDOW", closing)


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

""", bg=bg_col, fg='white', relief=SUNKEN, bd=0,
         font=(font_sty, 15)"""

btn1 = Button(main_root, text='Create Software', font=(font_sty, 30), bg=bg_col, fg='white', relief=SUNKEN, bd=0,
              activeforeground='orange', activebackground=bg_col, command=start_page)
btn1.pack(pady=20)
main_root.mainloop()

quit()
