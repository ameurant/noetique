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
    # introduction = schema.Text(
    #     title="Introduction du volume",
    #     required=False,
    # )
    begin = schema.Date(
        title="Date de début",
    )
    end = schema.Date(
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

        # Rediriger vers la vue qui génère le PDF
        portal = api.portal.get()
        url = f"{portal.absolute_url()}/@@volume-pdf"
        url += f"?begin={data['begin'].isoformat()}"
        url += f"&end={data['end'].isoformat()}"

        return self.request.response.redirect(url)
