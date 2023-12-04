from fpdf import FPDF

def generate_certificate(name):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page("P", (210, 297))

    # Set font
    pdf.set_font('helvetica')

    # Title
    pdf.set_text_color(0, 0, 0)  # Black color
    pdf.set_xy(0, 15)
    pdf.multi_cell(210, 10, "CS50 Shirtificate", 0, 'C')

    # Shirt Image
    pdf.image('shirtificate.png', x=50, y=60, w=110)

    # User's name on the shirt
    pdf.set_text_color(255, 255, 255)  # White color for the name
    pdf.set_xy(50, 115)  # Adjusted y-position
    pdf.multi_cell(110, 10, name, 0, 'C')  # Adjusted width and position

    pdf.output('shirtificate.pdf')

def get_user_name():
    name = input("Please enter your name: ")
    return name

def main():
    name = get_user_name()
    generate_certificate(name)

if __name__ == "__main__":
    main()
