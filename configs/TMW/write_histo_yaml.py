import os
from collections import OrderedDict

channelNames = ['ee', 'emu', 'mumu', 'sameflavor', 'combined']
histNames = [
#            'NEvents',
#            'nJets', 'nBJets',
#            'bJet1Pt',
#            'dileptonPt','dileptonMass',
#            'metPt',
#            'mlb_min', 'mlb_minimax',
             'mlb_minimax',
#            'lept1Pt','lept2Pt','lept1Eta','lept2Eta',
#            'ht',
#            'jet1Pt','jet1Eta',
#            'jet2Pt','jet2Eta',
#            'jet3Pt','jet3Eta',
            ]
btagNames = {'ZeroBTag': '= 0',
             'InclusiveBTag': '#geq 0',
             'OneBTag': '= 1',
             'GreaterOneBTag': '#geq 2',
             'TwoBTag': '= 2'}
njetNames = {'TwoJet': '= 2',
             'InclusiveNJet': '#geq 0',
             'GreaterOneJet': '#geq 2'}

log_hists = ['mlb_minimax']
sort_hists = []

hist_items = OrderedDict()

for hname in histNames:
    for njet, njet_label in njetNames.items():
        for btag, btag_label in btagNames.items():
            for ch in channelNames:
                hout = ch + '_' + btag + '_' + njet + '_' + hname

                options_list = []

                if hname in log_hists:
                    options_list.append('  log-y: true\n')
                if hname in sort_hists:
                    options_list.append('  sort-by-yields: true\n')

                options_list.append("  labels:\n    - {text: '#splitline{N_{b jet} " + btag_label + "}{N_{jet} " + njet_label + "}', position: [0.77, .55]}\n")

                options_list.append("  save-extensions: ['pdf', 'png']\n\n")
                hist_items[hout] = options_list

with open('histos_control.yml', 'w') as f:
    for histo, options in hist_items.items():
        f.write("'" + histo + "':\n")
        for option in options:
            f.write(option)

