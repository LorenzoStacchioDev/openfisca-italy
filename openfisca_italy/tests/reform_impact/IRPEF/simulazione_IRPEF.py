from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario


def init_profile(scenario):
    scenario.init_single_entity(
        period = '2018',
        parent1 = dict(
            RN1_reddito_complessivo = 25000,
            RN2_deduzione_abitazione_principale = 2000,
            RN3_oneri_deducibili_totali = 1500,
            RN22_totale_detrazioni_imposta = 2000,
            RN25_totale_altre_detrazioni_crediti_imposta = 1000
        )
    )
    return scenario

# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
# scenario normale
print "Simulazione IRPEF"
print "\nCreazione ed inizializzazine dello scenario di tasse e benefici normale"
simple_scenario = tax_benefit_system.new_scenario() # nuovo scenario normale
simple_scenario = init_profile(simple_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "Simulazione dello scenario di tasse e benefici normale"
simulation = simple_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print 'reddito imponibile', simulation.calculate('RN4_reddito_imponibile','2018')
print 'irpef lorda', simulation.calculate('RN5_irpef_lorda','2018')
print 'irpef netta', simulation.calculate('RN26_irpef_netta','2018')
