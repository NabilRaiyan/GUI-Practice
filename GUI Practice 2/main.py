import customtkinter
import tkinter


# Function
def message_send():
    text_box.configure(state="normal")
    message = message_box.get("0.0", "end")
    text_box.insert("end", message)
    text_box.configure(state="disabled")

    message_box.delete("0.0", "end")


# Main UI
window = customtkinter.CTk()

window.title("GUI Practice Using CTKFrame")
window.geometry("500x500")

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

FONT = ("Serif", 13, "bold")

left_frame = customtkinter.CTkFrame(master=window, fg_color="#2B2B2B", height=500, width=150)
left_frame.grid(row=0, column=0, padx=10, pady=20, sticky="news")

right_frame = customtkinter.CTkFrame(master=window, fg_color="#2B2B2B", height=500, width=300)
right_frame.grid(row=0, column=1, padx=10, pady=20, sticky="news")

contact_label = customtkinter.CTkButton(master=left_frame, text="Contact", text_font=FONT,
                                        text_color="white", fg_color="black", hover_color="black", border_color="white",
                                        corner_radius=8, border_width=2)
contact_label.grid(row=0, column=0, pady=10, padx=5)

my_name = customtkinter.CTkButton(master=left_frame, text="Raiyan", text_font=FONT, text_color="white",
                                  fg_color="#2B2B2B", hover_color="black", border_color="black", corner_radius=8,
                                  border_width=2)
my_name.grid(row=1, column=0, pady=10, padx=5)

father = customtkinter.CTkButton(master=left_frame, text="Father", text_font=FONT, text_color="white",
                                 fg_color="#2B2B2B", hover_color="black", border_color="black", corner_radius=8,
                                 border_width=2)
father.grid(row=2, column=0, pady=10, padx=5)

mother = customtkinter.CTkButton(master=left_frame, text="Mother", text_font=FONT, text_color="white",
                                 fg_color="#2B2B2B", hover_color="black", border_color="black", corner_radius=8,
                                 border_width=2)
mother.grid(row=3, column=0, pady=10, padx=5)

text_label = customtkinter.CTkLabel(master=right_frame, text_font=FONT, text_color="white", text="Message")
text_label.grid(column=2, row=0, padx=10, pady=3)

text_box = customtkinter.CTkTextbox(master=right_frame, width=270, height=250, text_font=("Serif", 10, "bold"))
text_box.grid(row=1, column=2, padx=20, pady=10)

text_area_label = customtkinter.CTkLabel(master=right_frame, text="Text", text_font=FONT, text_color="white")
text_area_label.grid(column=2, row=2)

message_box = tkinter.Text(master=right_frame, width=33, height=4)
message_box.grid(row=3, column=2, padx=20, pady=10)

send_button = customtkinter.CTkButton(master=right_frame, text="Send", text_color="white",
                                      text_font=("Serif", 12, "bold"),
                                      fg_color="#2B2B2B", hover_color="black", border_color="black", corner_radius=8,
                                      border_width=2, width=10, command=message_send)

send_button.grid(column=2, row=4, padx=10, pady=2)

window.mainloop()
