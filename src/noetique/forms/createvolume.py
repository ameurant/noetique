import subprocess
import tempfile

from lxml.html.clean import Cleaner
from plone import api
from plone import schema
from plone.autoform.form import AutoExtensibleForm
from plone.supermodel import model
from z3c.form import button
from z3c.form import form


class ICreateVolume(model.Schema):
    # introduction = RichText(
    #     title="Introduction du volume",
    #     required=False,
    # )
    introduction = schema.Text(
        title="Introduction du volume",
        required=False,
    )
    begin_date = schema.Date(
        title="Date de début",
    )
    end_date = schema.Date(
        title="Date de fin",
    )


class CreateVolume(AutoExtensibleForm, form.Form):
    schema = ICreateVolume
    ignoreContext = True

    label = "Créer un nouveau volume"
    description = "Utiliser ce formulaire pour créer un nouveau volume de messages journalier."

    @button.buttonAndHandler("Créer le volume")
    def handleChange(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        brains = api.content.find(
            portal_type="noetique.Post",
            sort_on="effective",
            sort_order="ascending",
            effective={"query": (data["begin_date"], data["end_date"]), "range": "min:max"},
        )

        cleaner = Cleaner(
            scripts=True,
            javascript=True,
            comments=True,
            style=True,
            inline_style=True,
            links=False,
            meta=True,
            page_structure=False,
            processing_instructions=True,
            embedded=True,
            frames=True,
            forms=True,
            annoying_tags=True,
            remove_tags=None,
            kill_tags=["o:p"],  # Balises spécifiques Word
            remove_unknown_tags=False,
            safe_attrs_only=False,
        )
        introduction = f"<p>{data['introduction'].replace('\n', '</p><p>')}</p>" if data["introduction"] else ""
        # "<div style='page-break-after: always; text-align: center;'>"

        cover_page = (
            "<div style='text-align: center;'>"
            "<h2>Journal d'une recherche</h2>"
            "<h1>De l'Être au Devenir ...</h1>"
            f"<p><strong>{data['begin_date'].strftime('%d/%m/%Y')} - {data['end_date'].strftime('%d/%m/%Y')}</strong></p>"
            "<p><strong>Marc Halévy</strong></p>"
            "</div>"
            f"{introduction}"
        )
        html_parts = [
            "<!DOCTYPE html><html><head><meta charset='utf-8'><style>body { font-size: 14pt; }</style></head><body>",
            cover_page,
        ]
        for b in brains:
            post = b.getObject()
            html_parts.append(f"<h2>{post.title}</h2>")
            if post.text:
                cleaner.clean_html(post.text.raw)
                html_parts.append(cleaner.clean_html(post.text.raw))
        html_parts.append("</body></html>")
        html = "".join(html_parts)
        html_file = tempfile.NamedTemporaryFile(suffix=".html")
        html_file.write(html.encode("utf-8"))
        html_file.flush()
        pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf")
        subprocess.call(
            [
                "wkhtmltopdf",
                "--quiet",
                "--print-media-type",
                "--page-size",
                "A4",
                "--margin-top",
                "25mm",
                "--margin-bottom",
                "25mm",
                "--margin-left",
                "25mm",
                "--margin-right",
                "25mm",
                "--footer-spacing",
                "10",
                "--footer-center",
                "[page]",
                html_file.name,
                pdf_file.name,
            ]
        )

        filename = "de-l-etre-au-devenir.pdf"
        pdf_content = pdf_file.read()
        pdf_file.close()
        html_file.close()

        self.request.response.setHeader("Content-Type", "application/pdf")
        self.request.response.setHeader("Content-Disposition", "attachment; filename={}".format(filename))
        self.request.response.write(pdf_content)
