from fpdf import FPDF


class PDF(FPDF):

    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'News in pdf format', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def print_article_list_to_pdf(list_articles, file_name):
    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 10)

    for item in list_articles:
        pdf.cell(0, 10, "Title: %s"%item.title, 0, 1)
        pdf.cell(0, 10, "Date: %s" % item.date, 0, 1)
        pdf.cell(0, 10, "Link: %s" % item.link, 0, 1)
        pdf.multi_cell(0, 5, "%s" % item.article, 0, 1)
        for idx, link in enumerate(item.links):
            pdf.multi_cell(0, 10, "[%d]:%s" % (idx, link), 0, 1)
        pdf.cell(0, 10, "", 0, 1)
    pdf.output(file_name, 'F')