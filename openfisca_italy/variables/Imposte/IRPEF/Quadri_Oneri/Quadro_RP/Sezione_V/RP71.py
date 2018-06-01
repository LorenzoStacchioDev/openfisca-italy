# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import common
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_V_common import *

class RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale(Variable):
    value_type = Enum
    possible_values = RP71_TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipale
    default_value = RP71_TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipale.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "Tipologia di detrazione inserita Rigo RP71 col.1"

class RP71_numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Giorni dell’anno in cui l’immobile è stato adibito ad abitazione principale"

class RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Percentuale di spettanza relativa a inquilini di alloggi adibiti ad abitazione principale che va dallo 0 al 100%"
