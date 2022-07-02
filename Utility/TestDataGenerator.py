from Objects import Supplier, Design, Process


def generateBusinesses():
    manufacturer_1 = Supplier('Business 1', ['EDM-Machining', '3-Axis-Machining', 'SLM-Additive'])
    manufacturer_2 = Supplier('Business 2', ['Buffing', '5-Axis-Machining', 'SLM-Subtractive', 'Shot-Peening'])
    manufacturer_3 = Supplier('Business 3', ['FDM-Additive', '3-Axis-Machining', 'Shot-Peening'])
    return manufacturer_1, manufacturer_2, manufacturer_3


def generateProcesses():
    process_1 = Process('Process 1', 'bracket', 'titanium', 3.14, 1234.567, 123.4, 77,
                        ['3-Axis-Machining', 'Shot-Peening'],
                        ['3-Axis-machining-1', '3-Axis-refixture-1', '3-Axis-machining-2', 'Bracket-polishing'])
    process_2 = Process('Process 1', 'bracket', 'titanium', 3.14, 1234.567, 123.4, 77,
                        ['5-Axis-Machining', 'Shot-Peening'],
                        ['5-Axis-machining-1', '5-Axis-refixture-1', '5-Axis-machining-2', 'Bracket-polishing'])
    return process_1, process_2


def generateDesigns():
    bracket1 = Design('Bracket 1', '/design_pics/bracket1.jpg', generateProcesses())
    bracket2 = Design('Bracket 2', '/design_pics/bracket2.jpg', generateProcesses())
    bracket3 = Design('Bracket 3', '/design_pics/bracket3.jpg', generateProcesses())
    return bracket1, bracket2, bracket3

