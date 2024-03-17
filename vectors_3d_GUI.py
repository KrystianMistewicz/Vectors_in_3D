import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from vectors_3d import Vector, VectorProduct, AddVectors


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font1 = ('Arial', 28, 'bold')
        self.font2 = ('Arial', 24, 'bold')
        self.a_vector_img = ctk.CTkImage(light_image=Image.open('a_vector.png'), size=(20, 30))
        self.b_vector_img = ctk.CTkImage(light_image=Image.open('b_vector.png'), size=(20, 30))
        self.vector_sum_img = ctk.CTkImage(light_image=Image.open('sum.png'), size=(60, 30))
        self.vector_product_img = ctk.CTkImage(light_image=Image.open('vector_product.png'), size=(60, 30))

    def read_values(self):
        try:
            self.ax = float(self.entry_ax.get())
            self.ay = float(self.entry_ay.get())
            self.az = float(self.entry_az.get())
            self.bx = float(self.entry_bx.get())
            self.by = float(self.entry_by.get())
            self.bz = float(self.entry_bz.get())
            return True
        except ValueError:
            CTkMessagebox(title='Error', message='You inserted wrong data. Please try again.', icon='warning')
            return False

    def insert_result_vector(self, calculation):
        for widget in self.frame3.winfo_children():
            widget.destroy()
        if calculation == 'vector sum':
            image = self.vector_sum_img
        elif calculation == 'vector product':
            image = self.vector_product_img
        self.empty_label5 = ctk.CTkLabel(master=self.frame3, text='\n', font=self.font1, fg_color='transparent', justify='center')
        self.empty_label5.grid(row=0, column=0, sticky="nsew")
        self.label11 = ctk.CTkLabel(master=self.frame3, image=image, text='', font=self.font1, fg_color='transparent', justify='center')
        self.label11.grid(row=1, column=0, sticky="nsew")
        # Calculation of the vector sum or vector product
        self.a_vector = Vector(self.ax, self.ay, self.az)
        self.b_vector = Vector(self.bx, self.by, self.bz)
        if calculation == 'vector sum':
            self.v = AddVectors(self.a_vector, self.b_vector)
        elif calculation == 'vector product':
            self.v = VectorProduct(self.a_vector, self.b_vector)
        self.c_vector = self.v.calculate()
        text = ' = [%5.1f, %5.1f, %5.1f]' % (self.c_vector.x, self.c_vector.y, self.c_vector.z)
        self.label12 = ctk.CTkLabel(master=self.frame3, text=text, font=self.font1, fg_color='transparent', justify='center')
        self.label12.grid(row=1, column=1, sticky="nsew")
        # Plotting the 3D graph of the vector sum or vector product
        self.v.show_3D_plot()

    def button_action(self, calculation):
        if self.read_values():
            self.insert_result_vector(calculation)

    def create_window(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.title(' ---> 3D vectors by Krystian Mistewicz')
        self.after(0, lambda: self.state('zoomed'))
        self.w_height = self.winfo_screenheight() # screen height
        self.w_width = self.winfo_screenwidth() # screen width
        self.ew = 50 # width of every entry
        self.eh = 30 # height of every entry
        self.frame1 = ctk.CTkFrame(self, fg_color='transparent', height=50)
        self.frame1.pack()
        self.frame2 = ctk.CTkFrame(self, fg_color='transparent')
        self.frame2.pack()
        self.frame3 = ctk.CTkFrame(self, fg_color='transparent')
        self.frame3.pack()
        self.empty_label1 = ctk.CTkLabel(master=self.frame1, text='', font=self.font1, fg_color='transparent', justify='center')
        self.empty_label1.grid(row=0, column=0, sticky="nsew")
        self.sum_button = ctk.CTkButton(self.frame1, width=120, height=20, text='Vector\nSum', font=self.font2, command=lambda: self.button_action('vector sum'))
        self.sum_button.grid(row=1, column=0, sticky="nsew")
        self.empty_label2 = ctk.CTkLabel(master=self.frame1, text=' '*5, font=self.font1, fg_color='transparent', justify='center')
        self.empty_label2.grid(row=1, column=1, sticky="nsew")
        self.vect_prod_button = ctk.CTkButton(self.frame1, width=120, height=20, text='Vector\nProduct', font=self.font2, command=lambda: self.button_action('vector product'))
        self.vect_prod_button.grid(row=1, column=2, sticky="nsew")
        self.empty_label3 = ctk.CTkLabel(master=self.frame1, text='\n', font=self.font1, fg_color='transparent', justify='center')
        self.empty_label3.grid(row=2, column=0, sticky="nsew")
        self.label01 = ctk.CTkLabel(master=self.frame2, image=self.a_vector_img, text='', font=self.font1, fg_color='transparent', justify='center')
        self.label01.grid(row=0, column=0, sticky="nsew")
        self.label02 = ctk.CTkLabel(master=self.frame2, text=' = [ ', font=self.font1, fg_color='transparent', justify='center')
        self.label02.grid(row=0, column=1, sticky="nsew")
        self.entry_ax = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_ax.grid(row=0, column=2, sticky="nsew")
        self.label03 = ctk.CTkLabel(master=self.frame2, text=' , ', font=self.font1, fg_color='transparent', justify='center')
        self.label03.grid(row=0, column=3, sticky="nsew")
        self.entry_ay = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_ay.grid(row=0, column=4, sticky="nsew")
        self.label04 = ctk.CTkLabel(master=self.frame2, text=' , ', font=self.font1, fg_color='transparent', justify='center')
        self.label04.grid(row=0, column=5, sticky="nsew")
        self.entry_az = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_az.grid(row=0, column=6, sticky="nsew")
        self.label05 = ctk.CTkLabel(master=self.frame2, text=' ]', font=self.font1, fg_color='transparent', justify='center')
        self.label05.grid(row=0, column=7, sticky="nsew")
        self.empty_label4 = ctk.CTkLabel(master=self.frame2, text='', font=self.font1, fg_color='transparent', justify='center')
        self.empty_label4.grid(row=1, column=0, sticky="nsew")
        self.label06 = ctk.CTkLabel(master=self.frame2, image=self.b_vector_img, text='', font=self.font1, fg_color='transparent', justify='center')
        self.label06.grid(row=2, column=0, sticky="nsew")
        self.label07 = ctk.CTkLabel(master=self.frame2, text=' = [ ', font=self.font1, fg_color='transparent', justify='center')
        self.label07.grid(row=2, column=1, sticky="nsew")
        self.entry_bx = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_bx.grid(row=2, column=2, sticky="nsew")
        self.label08 = ctk.CTkLabel(master=self.frame2, text=' , ', font=self.font1, fg_color='transparent', justify='center')
        self.label08.grid(row=2, column=3, sticky="nsew")
        self.entry_by = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_by.grid(row=2, column=4, sticky="nsew")
        self.label09 = ctk.CTkLabel(master=self.frame2, text=' , ', font=self.font1, fg_color='transparent', justify='center')
        self.label09.grid(row=2, column=5, sticky="nsew")
        self.entry_bz = ctk.CTkEntry(self.frame2, width=self.ew, height=self.eh, font=self.font2, justify=ctk.CENTER)
        self.entry_bz.grid(row=2, column=6, sticky="nsew")
        self.label10 = ctk.CTkLabel(master=self.frame2, text=' ]', font=self.font1, fg_color='transparent', justify='center')
        self.label10.grid(row=2, column=7, sticky="nsew")
        self.mainloop()


if __name__ == '__main__':
    app = Application()
    app.create_window()