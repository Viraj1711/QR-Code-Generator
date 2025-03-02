import qrcode
from tkinter import *
from tkinter import messagebox

# Function to generate and display the QR code
def generate_qr():
    # Get the data from the input field
    data = entry.get()
    
    if not data:
        messagebox.showerror("Input Error", "Please enter data for the QR code.")
        return
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code image
    img.save("generated_qr_code.png")
    messagebox.showinfo("Success", "QR Code generated and saved as 'generated_qr_code.png'.")

    # Display the image in the Tkinter window
    img.show()

# Setting up the GUI using Tkinter
root = Tk()
root.title("QR Code Generator")
root.geometry("400x250")

# Add a label to explain the input
label = Label(root, text="Enter text or URL to generate QR code:")
label.pack(pady=10)

# Add an input field for the user to enter the data
entry = Entry(root, width=40)
entry.pack(pady=10)

# Add a button to generate the QR code
generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
