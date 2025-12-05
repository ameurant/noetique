import subprocess
import tempfile
from datetime import datetime

from bs4 import BeautifulSoup
from plone import api
from Products.Five import BrowserView


class VolumePdfView(BrowserView):
    """Vue pour générer un PDF d'un volume de posts."""

    def __call__(self):
        if not self.request.get("begin") or not self.request.get("end"):
            raise ValueError("begin et end sont requis")
        begin = datetime.strptime(self.request["begin"], "%Y-%m-%d").date()
        end = datetime.strptime(self.request["end"], "%Y-%m-%d").date()
        brains = api.content.find(
            portal_type="noetique.Post",
            sort_on="effective",
            sort_order="ascending",
            effective={"query": (begin, end), "range": "min:max"},
        )
        styles = """
          <style>
            body { font-size: 13pt;}
            .text-center { text-align: center; }
          </style>
        """
        cover_page = (
            "<div style='text-align: center;'>"
            "<h2>Journal d'une recherche</h2>"
            "<h1>De l'Être au Devenir ...</h1>"
            f"<p><strong>{begin.strftime('%d/%m/%Y')} - {end.strftime('%d/%m/%Y')}</strong></p>"
            "<p><strong>Marc Halévy</strong></p>"
            "</div>"
        )
        html_parts = [
            f"<!DOCTYPE html><html><head><meta charset='utf-8'>{styles}</head><body>",
            cover_page,
        ]
        for b in brains:
            post = b.getObject()
            html_parts.append(f"<h2>{post.title}</h2>")
            if post.text:
                soup = BeautifulSoup(post.text.raw, "html.parser")
                # Supprimer des tags indésirables
                for tag in soup.find_all(["style", "script"]):
                    tag.decompose()
                # Supprimer les attributs indésirables
                for tag in soup.find_all(True):
                    for attr in ["style", "lang"]:
                        if tag.has_attr(attr):
                            del tag[attr]
                    if tag.has_attr("class") and "MsoNormal" in tag.get("class", []):
                        tag["class"] = [c for c in tag["class"] if c != "MsoNormal"]
                        if not tag["class"]:
                            del tag["class"]
                # Supprimer les span sans attribut class (en gardant leur contenu)
                for span in soup.find_all("span"):
                    if not span.get("class"):
                        span.unwrap()
                html_parts.append(str(soup))
        html_parts.append("</body></html>")
        html = "".join(html_parts)

        # Créer les fichiers temporaires
        html_file = tempfile.NamedTemporaryFile(suffix=".html")
        pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf")
        html_file.write(html.encode("utf-8"))
        html_file.flush()

        # Générer le PDF avec wkhtmltopdf
        result = subprocess.run(
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
        if result.returncode != 0:
            raise RuntimeError(f"wkhtmltopdf failed: {result.stderr.decode('utf-8', errors='ignore')}")

        pdf_content = pdf_file.read()
        filename = "de-l-etre-au-devenir.pdf"
        self.request.response.setHeader("Content-Type", "application/pdf")
        self.request.response.setHeader("Content-Disposition", f"inline; filename={filename}")
        self.request.response.setHeader("Content-Length", str(len(pdf_content)))

        return pdf_content
