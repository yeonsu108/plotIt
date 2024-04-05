import os
from collections import OrderedDict

channelNames = {'ee': 'ee', 'emu': 'e#mu', 'mumu': '#mu#mu',
                'sameflavor': 'ee+#mu#mu', 'combined': 'ee+e#mu+#mu#mu'}
histNames = [
            #'NEvents',
            #'nVtx', 'rho',
            'nJets', 'nBJets',
            #'bJet1Pt',
            'dileptonPt','dileptonMass',
            'metPt',
            #'mlb_min',
            'mlb_minimax',
            'lept1Pt','lept2Pt',
            'lept1Eta','lept2Eta',
            'jet1Pt','jet1Eta',
            'jet2Pt','jet2Eta',
            'mbb',
            ]

#Not drawing all histos! {hname: [[btag], [njet]]}
allowed_dict = {
                 'mlb_minimax': [[], ['GreaterOneBTag', 'TwoBTag'], ['TwoJet', 'GreaterOneJet']],
                 'mlb_min': [[], [], ['TwoJet', 'GreaterOneJet']],
                 'mbb': [[], ['GreaterOneBTag', 'TwoBTag'], ['TwoJet', 'GreaterOneJet']],
                 'nJets': [['combined'], [], ['InclusiveNJet', 'GreaterOneJet']],
                 'nBJets': [['combined'], ['InclusiveBTag', 'GreaterOneBTag'], []],
                 'jet1Pt': [['combined'], [],['GreaterOneJet', 'TwoJet']],
                 'jet1Eta': [['combined'], [],['GreaterOneJet', 'TwoJet']],
                 'jet2Pt': [['combined'], [],['GreaterOneJet', 'TwoJet']],
                 'jet2Eta': [['combined'], [],['GreaterOneJet', 'TwoJet']],
                 'bJet1Pt': [['combined'], ['InclusiveBTag', 'GreaterOneBTag', 'TwoBTag'],[]],
               }
btagNames = {#'ZeroBTag': '= 0',
             'InclusiveBTag': '#geq 0',
             'GreaterOneBTag': '#geq 2',
             'TwoBTag': '= 2'}
njetNames = {'TwoJet': '= 2',
             'InclusiveNJet': '#geq 0',
             'GreaterOneJet': '#geq 2'}

#Draw stat. unc. overlayed in the ratio pad
stat_hists = ['mlb_minimax']
log_hists = ['mlb_minimax', 'mlb_min', ]
non_equ_binning = ['mlb_minimax']
sort_hists = []

hist_items = OrderedDict()

for hname in histNames:
    for njet, njet_label in njetNames.items():
        for btag, btag_label in btagNames.items():
            for ch, ch_label in channelNames.items():

                if hname in allowed_dict:
                    if (len(allowed_dict[hname][0]) > 0 and ch not in allowed_dict[hname][0])\
                       or (len(allowed_dict[hname][1]) > 0 and btag not in allowed_dict[hname][1])\
                       or (len(allowed_dict[hname][2]) > 0 and njet not in allowed_dict[hname][2]): continue

                hout = ch + '_' + btag + '_' + njet + '_' + hname

                options_list = []

                if hname in log_hists:
                    options_list.append('  log-y: true\n')
                    options_list.append('  sort-by-yields: true\n')
                if hname in sort_hists:
                    options_list.append('  sort-by-yields: true\n')
                #if hname in stat_hists:
                #    options_list.append('  ratio-draw-mcstat-error: true\n')
                if hname in non_equ_binning:
                    options_list.append('  y-axis-format: "%1% / Bin\n')
                if ch == 'combined':
                    options_list.append("  rename:\n    - {from: '" + hout + "', to: '" + hout.replace(ch, 'll') + "'}\n")

                options_list.append("  labels:\n    - {text: '" + ch_label + "', position: [0.77, .725], font: 44, size: 14}\n")
                options_list.append("    - {text: '#splitline{N_{b jet} " + btag_label + "}{N_{jet} " + njet_label + "}', position: [0.77, .65], font: 44, size: 14}\n")
                #options_list.append("  ratio-y-axis-range: [0.95, 1.05]\n")

                options_list.append("  save-extensions: ['pdf', 'png']\n\n")
                hist_items[hout] = options_list

with open('histos_control.yml', 'w') as f:
#with open('histos_control_bb4l.yml', 'w') as f:
    for histo, options in hist_items.items():
        f.write("'" + histo + "':\n")
        for option in options:
            f.write(option)

