from django.contrib import admin

from symposion.proposals.actions import export_as_csv_action
from symposion.proposals.models import Proposal, ProposalFile

class ProposalFileAdmin(admin.ModelAdmin):
    list_display = ('proposal', 'file', 'proposal_speaker')
    ordering = ('proposal',)

    def proposal_speaker(self, obj):
        return obj.proposal.speaker.name
admin.site.register(ProposalFile, ProposalFileAdmin)


admin.site.register(Proposal,
    list_display = [
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
        "audience_level",
        "cancelled",
    ],
    list_filter = [
        "kind__name",
        #"result__accepted",
    ],
    actions = [export_as_csv_action("CSV Export", fields=[
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
    ])]
)
