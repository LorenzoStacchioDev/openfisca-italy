# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_conigue_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per coniuge a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

class detrazioni_per_figli_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per figli a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class detrazioni_per_altri_famigliari_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per altri famigliari a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source    

class detrazioni_per_carichi_famigliari(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per carichi di famiglia "
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula (person,period,parameter):
        detrazioni_per_conigue_a_carico = person('detrazioni_per_conigue_a_carico',period)
        detrazioni_per_carichi_famigliari = person('detrazioni_per_carichi_famigliari',period)
        detrazioni_per_altri_famigliari_a_carico = person('detrazioni_per_altri_famigliari_a_carico',period)
        return detrazioni_per_conigue_a_carico + detrazioni_per_carichi_famigliari + detrazioni_per_altri_famigliari_a_carico

class detrazioni_per_lavoro_dipendente(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni per lavoro dipendente"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class detrazioni_per_pensionati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni per i pensionati"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class per_assegni_percepiti_ex_coniuge(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni per i pensionati"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

