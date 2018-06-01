# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class RP71_TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipale(Enum):
    nessun_codice = u"Il rigo non è stato compilato"
    codice_uno = u"Detrazione per gli inquilini di alloggi adibiti ad abitazione principale"
    codice_due = u"Detrazione per gli inquilini di alloggi adibiti ad abitazione principale con contratti a regime convenzionale"
    codice_tre = u"Detrazione per canoni di locazione relativi a contratti di locazione per abitazione principale per i giovani di età compresa tra i 20 ed i 30 anni, con reddito complessivo non superiore ad euro 15.493,71"
