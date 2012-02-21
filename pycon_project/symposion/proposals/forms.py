from django import forms
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from markitup.widgets import MarkItUpWidget

from symposion.conference.models import PresentationKind, PresentationCategory
from symposion.proposals.models import Proposal


class ProposalForm(forms.ModelForm):
    
    class Meta:
        model = Proposal
        fields = [
            "title",
            "kind",
            "category",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
        ]
        widgets = {
            "description": forms.Textarea(attrs={'class': 'input-xxlarge'}),
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        self.fields["category"] = forms.ModelChoiceField(
            label = _('Category'),
            queryset = PresentationCategory.objects.order_by("name")
        )
    
    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class ProposalSubmitForm(ProposalForm):

    def __init__(self, *args, **kwargs):
        super(ProposalSubmitForm, self).__init__(*args, **kwargs)
        self.fields["kind"] = forms.ModelChoiceField(
            label = _("Kind"),
            queryset = PresentationKind.available(),
            widget = forms.RadioSelect(),
            empty_label = None
        )


class ProposalEditForm(ProposalForm):
    
    class Meta:
        model = Proposal
        fields = [
            "title",
            "category",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
        ]
        widgets = {
            "description": forms.Textarea(attrs={'class': 'input-xxlarge'}),
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class AddSpeakerForm(forms.Form):
    
    email = forms.EmailField(
        label = "Email address of new speaker (use their email address, not yours)"
    )
    
    def __init__(self, *args, **kwargs):
        self.proposal = kwargs.pop("proposal")
        super(AddSpeakerForm, self).__init__(*args, **kwargs)
    
    def clean_email(self):
        value = self.cleaned_data["email"]
        exists = self.proposal.additional_speakers.filter(
            Q(user=None, invite_email=value) |
            Q(user__email=value)
        ).exists()
        if exists:
            raise forms.ValidationError(
                "This email address has already been added to your talk proposal"
            )
        return value
