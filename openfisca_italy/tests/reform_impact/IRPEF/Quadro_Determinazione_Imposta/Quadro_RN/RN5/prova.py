# importo reform
from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario

def init_profile(scenario):
    scenario.init_single_entity(
        period = '2017',
        parent1 = dict(
            RN4_reddito_imponibile= 10000,
        )
    )
    return scenario


# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
# scenario normale
print "Riforma per diminuzione aliquota IRPEF dal 23 al 18 per i redditi inferiori a 15000"
print "\nCreazione ed inizializzazine dello scenario di tasse e benefici normale"
simple_scenario = tax_benefit_system.new_scenario() # nuovo scenario normale
simple_scenario = init_profile(simple_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "Simulazione dello scenario di tasse e benefici normale"
simulation = simple_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print('Irpef Lorda con sistema senza riforma:')
print(simulation.calculate('RN5_irpef_lorda','2017'))
