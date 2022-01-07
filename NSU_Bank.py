from tkinter import *
import tkinter.messagebox


class Bank:
    """class of bank terminal"""

    def __init__(self, root):
        self.root = root
        blank_space = ' '
        self.root.title(100 * blank_space + 'NSU BANK')
        self.root.geometry('760x700+290+60')
        self.root.configure(bg='grey')
        self.root.iconbitmap('root_icon.ico')

        self.cash = 1000
        self.state = ''
        self.statement = []

        # ====================================Frames=======================================================
        MainFrame = Frame(self.root, bd=20, width=760, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=3)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=3)

        TopFrame2Left = Frame(TopFrame2, bd=4, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)

        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

        # =============================Functions==================================================
        def resizeImage(img, newWidth, newHeight):
            """Resizing any images if necessary"""
            oldWidth = img.width()
            oldHeight = img.height()
            newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
            for x in range(newWidth):
                for y in range(newHeight):
                    xOld = int(x * oldWidth / newWidth)
                    yOld = int(y * oldHeight / newHeight)
                    rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                    newPhotoImage.put(rgb, (x, y))
            return newPhotoImage

        def credit_card_whole_movement():
            """for animation of credit card"""
            self.img_card = PhotoImage(file='creditka.png')
            self.img_card = resizeImage(self.img_card, 100, 80)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.label_card.grid(row=5, column=4)
            root.after(750, move_credit_card1)
            root.after(1300, move_credit_card2)
            root.after(2000, destroy_credit_card)

        def move_credit_card1():
            """a part of animation"""
            self.img_card = resizeImage(self.img_card, 85, 75)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.label_card.grid(row=4, column=4)

        def move_credit_card2():
            """a part of animation"""
            self.img_card = resizeImage(self.img_card, 65, 75)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.card_hole = Button(TopFrame1, width=25, heigh=1, state=DISABLED, bg='LightSteelBlue4')
            self.card_hole.grid(row=3, column=4)
            self.label_card.grid(row=3, column=4)

        def destroy_credit_card():
            """the end of animation - destroying the credit card"""
            self.img_card = resizeImage(self.img_card, 65, 75)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.label_card.destroy()

        def initial_state_card():
            """a part of animation"""
            self.img_card = resizeImage(self.img_card, 90, 80)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.label_card.grid(row=5, column=4)

        def credit_card_back():
            """animation of getting back credit card"""
            self.img_card = PhotoImage(file='creditka.png')
            self.img_card = resizeImage(self.img_card, 65, 75)
            self.label_card = Label(TopFrame1, image=self.img_card)
            self.label_card.grid(row=3, column=4)
            root.after(750, move_credit_card1)
            root.after(1300, initial_state_card)
            root.after(1900, destroy_credit_card)
            self.card_hole = Button(TopFrame1, width=25, heigh=1, state=DISABLED, bg='LightSteelBlue4')
            self.card_hole.grid(row=3, column=4)

        def enter_Pin():
            pinNum = self.txtReceipt.get('1.0', 'end-1c')
            if self.state == '':
                if pinNum == '2022':
                    self.state = 'entered'
                    self.txtReceipt.delete('1.0', END)

                    self.txtReceipt.insert(END, "\t\t         ATM \n\n")
                    self.txtReceipt.insert(END, "Withdraw Cash\t\t\t\t            Loan   \n\n\n")
                    self.txtReceipt.insert(END, "Cash With Receipt\t\t\t\t       Deposit \n\n\n\n")
                    self.txtReceipt.insert(END, "Balance\t\t\t         Request New Pin \n\n\n\n\n")
                    self.txtReceipt.insert(END, "Mini Statement\t\t\t           Print Statement \n\n\n")

                    credit_card_whole_movement()

                    self.btnArrowL1.config(state=NORMAL)

                    self.btnArrowL1 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowL1.grid(row=0, column=0, padx=2, pady=5)

                    self.btnArrowL2 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowL2.grid(row=1, column=0, padx=2, pady=5)

                    self.btnArrowL3 = Button(TopFrame2Left, width=160, heigh=50, command=balance, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowL3.grid(row=2, column=0, padx=2, pady=5)

                    self.btnArrowL4 = Button(TopFrame2Left, width=160, heigh=50, command=statement, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowL4.grid(row=3, column=0, padx=2, pady=5)

                    self.btnArrowR1 = Button(TopFrame2Right, width=160, heigh=50, command=loan, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowR1.grid(row=0, column=0, padx=2, pady=5)

                    self.btnArrowR2 = Button(TopFrame2Right, width=160, heigh=50, command=deposit, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowR2.grid(row=1, column=0, padx=2, pady=5)

                    self.btnArrowR3 = Button(TopFrame2Right, width=160, heigh=50, command=request_new_pin, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowR3.grid(row=2, column=0, padx=2, pady=5)

                    self.btnArrowR4 = Button(TopFrame2Right, width=160, heigh=50, command=print_statement, state=NORMAL,
                                             image=self.img_arrow_Left)
                    self.btnArrowR4.grid(row=3, column=0, padx=2, pady=5)
                else:
                    self.txtReceipt.delete('1.0', END)
                    self.txtReceipt.insert(END, 'Invalid Pin Number' + '\n')
            elif self.state == 'withdraw':
                self.withdraw = float(self.txtReceipt.get("1.11", END))
                self.cash -= self.withdraw
                self.statement.append('withdrawal ' + str(self.withdraw))
                if self.cash < 0:
                    self.txtReceipt.insert(END, '\nATTENTION Your balance is less than 0\n')
                    self.txtReceipt.insert(END, 'Please top up Your balance\n\n')
                self.txtReceipt.insert(END, '\nThank You for using NSU Bank\n')
            elif self.state == 'loan':
                self.loan = float(self.txtReceipt.get("1.6", END))
                self.cash += self.loan
                self.statement.append('loan ' + str(self.loan))
                self.txtReceipt.insert(END, '\nYou have just got a loan of ' + str(self.loan) + '\n')
                self.txtReceipt.insert(END, '\n\nThank You for using NSU Bank\n')
            elif self.state == 'deposit':
                self.deposit = float(self.txtReceipt.get("1.9", END))
                self.cash -= self.deposit
                self.statement.append('deposit ' + str(self.deposit))
                if self.cash < 0:
                    self.txtReceipt.insert(END, '\nATTENTION Your balance is less than 0\n')
                    self.txtReceipt.insert(END, 'Please top up Your balance\n\n')
                self.txtReceipt.insert(END, '\nYou have just gave a money for deposit of ' + str(self.deposit) + '\n')
                self.txtReceipt.insert(END, '\nThank You for using NSU Bank\n')

        def clear():
            self.txtReceipt.delete('1.0', END)
            if self.state != '':
                credit_card_back()
            self.state = ''
            self.btnArrowL1 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowL1.grid(row=0, column=0, padx=2, pady=5)

            self.btnArrowL2 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowL2.grid(row=1, column=0, padx=2, pady=5)

            self.btnArrowL3 = Button(TopFrame2Left, width=160, heigh=50, command=balance, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowL3.grid(row=2, column=0, padx=2, pady=5)

            self.btnArrowL4 = Button(TopFrame2Left, width=160, heigh=50, command=statement, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowL4.grid(row=3, column=0, padx=2, pady=5)

            self.btnArrowR1 = Button(TopFrame2Right, width=160, heigh=50, command=loan, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowR1.grid(row=0, column=0, padx=2, pady=5)

            self.btnArrowR2 = Button(TopFrame2Right, width=160, heigh=50, command=deposit, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowR2.grid(row=1, column=0, padx=2, pady=5)

            self.btnArrowR3 = Button(TopFrame2Right, width=160, heigh=50, command=request_new_pin, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowR3.grid(row=2, column=0, padx=2, pady=5)

            self.btnArrowR4 = Button(TopFrame2Right, width=160, heigh=50, command=print_statement, state=DISABLED,
                                     image=self.img_arrow_Left)
            self.btnArrowR4.grid(row=3, column=0, padx=2, pady=5)

        def insert0():
            value0 = 0
            self.txtReceipt.insert(END, value0)

        def insert1():
            value1 = 1
            self.txtReceipt.insert(END, value1)

        def insert2():
            value2 = 2
            self.txtReceipt.insert(END, value2)

        def insert3():
            value3 = 3
            self.txtReceipt.insert(END, value3)

        def insert4():
            value4 = 4
            self.txtReceipt.insert(END, value4)

        def insert5():
            value5 = 5
            self.txtReceipt.insert(END, value5)

        def insert6():
            value6 = 6
            self.txtReceipt.insert(END, value6)

        def insert7():
            value7 = 7
            self.txtReceipt.insert(END, value7)

        def insert8():
            value8 = 8
            self.txtReceipt.insert(END, value8)

        def insert9():
            value9 = 9
            self.txtReceipt.insert(END, value9)

        def cancel():
            Cancel = tkinter.messagebox.askyesno("NSU BANK", "Do you really want to cancel?")
            if Cancel > 0:
                self.root.destroy()
                return

        def withdrawcash():
            self.state = 'withdraw'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, 'Withdraw ₽ ')
            enter_Pin()

        def loan():
            self.state = 'loan'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, 'Loan ₽ ')
            enter_Pin()

        def deposit():
            self.state = 'deposit'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, 'Deposit ₽ ')
            enter_Pin()

        def request_new_pin():
            self.state = 'request'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, '\t   Welcome to NSU Bank\n')
            self.txtReceipt.insert(END, '\nYour New Pin Number will be send to your NSU mail address\n')
            self.txtReceipt.insert(END, '\n\nThank You for using NSU Bank\n')

        def balance():
            self.state = 'balance'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, '\t   Welcome to NSU Bank\n')
            self.txtReceipt.insert(END, '\nYour balance: ' + str(self.cash) + ' ₽\n')
            if self.cash < 0:
                self.txtReceipt.insert(END, '\nATTENTION Your balance is less than 0\n')
                self.txtReceipt.insert(END, 'Please top up Your balance\n\n')
            self.txtReceipt.insert(END, '\nThank You for using NSU Bank\n')

        def statement():
            self.state = 'statement'
            self.txtReceipt.delete('1.0', END)
            for i in self.statement:
                self.txtReceipt.insert(END, i)
                self.txtReceipt.insert(END, '\n')
            self.txtReceipt.insert(END, '\n\nThank You for using NSU Bank\n')

        def print_statement():
            self.state = 'statement'
            self.txtReceipt.delete('1.0', END)
            self.txtReceipt.insert(END, '\nPrinting Your Statement')
            self.txtReceipt.insert(END, '\nFinished, please take Your Statement')
            self.txtReceipt.insert(END, '\n\nThank You for using NSU Bank\n')

        # =========================Widget===========================================
        self.txtReceipt = Text(TopFrame2Mid, heigh=17, width=42, bd=12, font=('arial', 9, 'bold'), bg='LightBlue1')
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_Left = PhotoImage(file='empty.png')
        self.img_arrow_Left = resizeImage(self.img_arrow_Left, 160, 50)

        self.btnArrowL1 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowL1.grid(row=0, column=0, padx=2, pady=5)

        self.btnArrowL2 = Button(TopFrame2Left, width=160, heigh=50, command=withdrawcash, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowL2.grid(row=1, column=0, padx=2, pady=5)

        self.btnArrowL3 = Button(TopFrame2Left, width=160, heigh=50, command=balance, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowL3.grid(row=2, column=0, padx=2, pady=5)

        self.btnArrowL4 = Button(TopFrame2Left, width=160, heigh=50, command=statement, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowL4.grid(row=3, column=0, padx=2, pady=5)

        # ====================================================================================================
        self.img_arrow_Right = PhotoImage(file='empty.png')

        self.btnArrowR1 = Button(TopFrame2Right, width=160, heigh=50, command=loan, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowR1.grid(row=0, column=0, padx=2, pady=5)

        self.btnArrowR2 = Button(TopFrame2Right, width=160, heigh=50, command=deposit, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowR2.grid(row=1, column=0, padx=2, pady=5)

        self.btnArrowR3 = Button(TopFrame2Right, width=160, heigh=50, command=request_new_pin, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowR3.grid(row=2, column=0, padx=2, pady=5)

        self.btnArrowR4 = Button(TopFrame2Right, width=160, heigh=50, command=print_statement, state=DISABLED,
                                 image=self.img_arrow_Left)
        self.btnArrowR4.grid(row=3, column=0, padx=2, pady=5)

        # ================================KeyBoardButtons===============================================
        self.imgEmpty = PhotoImage(file='empty.png')
        self.imgEmpty = resizeImage(self.imgEmpty, 90, 70)
        self.img0 = PhotoImage(file='zero.png')
        self.img0 = resizeImage(self.img0, 90, 70)
        self.img1 = PhotoImage(file='one.png')
        self.img1 = resizeImage(self.img1, 90, 70)
        self.img2 = PhotoImage(file='two.png')
        self.img2 = resizeImage(self.img2, 90, 70)
        self.img3 = PhotoImage(file='three.png')
        self.img3 = resizeImage(self.img3, 90, 70)
        self.img4 = PhotoImage(file='four.png')
        self.img4 = resizeImage(self.img4, 90, 70)
        self.img5 = PhotoImage(file='five.png')
        self.img5 = resizeImage(self.img5, 90, 70)
        self.img6 = PhotoImage(file='six.png')
        self.img6 = resizeImage(self.img6, 90, 70)
        self.img7 = PhotoImage(file='seven.png')
        self.img7 = resizeImage(self.img7, 90, 70)
        self.img8 = PhotoImage(file='eight.png')
        self.img8 = resizeImage(self.img8, 90, 70)
        self.img9 = PhotoImage(file='nine.png')
        self.img9 = resizeImage(self.img9, 90, 70)

        self.card_hole = Button(TopFrame1, width=25, heigh=1, state=DISABLED, bg='LightSteelBlue4')
        self.card_hole.grid(row=3, column=4)

        self.imgCE = PhotoImage(file='cancel.png')
        self.imgCE = resizeImage(self.imgCE, 90, 70)

        self.imgClear = PhotoImage(file='clear.png')
        self.imgClear = resizeImage(self.imgClear, 90, 70)

        self.imgEnter = PhotoImage(file='enter.png')
        self.imgEnter = resizeImage(self.imgEnter, 90, 70)

        self.imgLeftArrow = PhotoImage(file='lArrow.png')
        self.imgLeftArrow = resizeImage(self.imgLeftArrow, 90, 70)
        self.imgRightArrow = PhotoImage(file='rArrow.png')
        self.imgRightArrow = resizeImage(self.imgRightArrow, 90, 70)

        self.btn1 = Button(TopFrame1, width=90, heigh=70, command=insert1, image=self.img1)
        self.btn1.grid(row=2, column=0, padx=6, pady=4, sticky=N)

        self.btn2 = Button(TopFrame1, width=90, heigh=70, command=insert2, image=self.img2)
        self.btn2.grid(row=2, column=1, padx=6, pady=4, sticky=N)

        self.btn3 = Button(TopFrame1, width=90, heigh=70, command=insert3, image=self.img3)
        self.btn3.grid(row=2, column=2, padx=6, pady=4, sticky=N)

        self.btnCE = Button(TopFrame1, width=90, heigh=70, command=cancel, image=self.imgCE)
        self.btnCE.grid(row=2, column=3, padx=6, pady=4, sticky=N)

        self.btn4 = Button(TopFrame1, width=90, heigh=70, command=insert4, image=self.img4)
        self.btn4.grid(row=3, column=0, padx=6, pady=4, sticky=N)

        self.btn5 = Button(TopFrame1, width=90, heigh=70, command=insert5, image=self.img5)
        self.btn5.grid(row=3, column=1, padx=6, pady=4, sticky=N)

        self.btn6 = Button(TopFrame1, width=90, heigh=70, command=insert6, image=self.img6)
        self.btn6.grid(row=3, column=2, padx=6, pady=4, sticky=N)

        self.btnClear = Button(TopFrame1, width=90, heigh=70, command=clear, image=self.imgClear)
        self.btnClear.grid(row=3, column=3, padx=6, pady=4, sticky=N)

        self.btn7 = Button(TopFrame1, width=90, heigh=70, command=insert7, image=self.img7)
        self.btn7.grid(row=4, column=0, padx=6, pady=4, sticky=N)

        self.btn8 = Button(TopFrame1, width=90, heigh=70, command=insert8, image=self.img8)
        self.btn8.grid(row=4, column=1, padx=6, pady=4, sticky=N)

        self.btn9 = Button(TopFrame1, width=90, heigh=70, command=insert9, image=self.img9)
        self.btn9.grid(row=4, column=2, padx=6, pady=4, sticky=N)

        self.btnEnter = Button(TopFrame1, width=90, heigh=70, command=enter_Pin, image=self.imgEnter)
        self.btnEnter.grid(row=4, column=3, padx=6, pady=4, sticky=N)

        self.btnEmpty1 = Button(TopFrame1, width=90, heigh=70, image=self.imgEmpty)
        self.btnEmpty1.grid(row=5, column=0, padx=6, pady=4, sticky=N)

        self.btn0 = Button(TopFrame1, width=90, heigh=70, command=insert0, image=self.img0)
        self.btn0.grid(row=5, column=1, padx=6, pady=4, sticky=N)

        self.btnEmpty2 = Button(TopFrame1, width=90, heigh=70, image=self.imgEmpty)
        self.btnEmpty2.grid(row=5, column=2, padx=6, pady=4, sticky=N)

        self.btnEmpty3 = Button(TopFrame1, width=90, heigh=70, image=self.imgEmpty)
        self.btnEmpty3.grid(row=5, column=3, padx=6, pady=4, sticky=N)


if __name__ == '__main__':
    root = Tk()
    application = Bank(root)
    root.mainloop()
