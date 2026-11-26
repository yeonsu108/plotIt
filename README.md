plotIt
======
An utility to plot ROOT histograms.

## You should have boost and root env from either cmssw (scram tool works) or lcg ($LCIO is set)

```bash
cd plotIt/external
./build-external.sh
cd ..
make -j 4
```

## Run 3 Configuration Notes (as of 2026-11-25)

- **Active configs**: `configs/Run3_muon/` and `configs/Run3_electron/` (`config_2022.yml`, `config_2022EE.yml`, `config_2023.yml`, `config_2023BPix.yml`, `config_2024.yml`, `config_Run3.yml`, and `template_Run3.yml`).
- **Luminosity errors (`XPOG-01`)**: `config_2024.yml` uses `luminosity-error: 0.016`; combined `config_Run3.yml` / `template_Run3.yml` use `luminosity-error: 0.012`.
- **Synchronized Run 3 systematics**:
  - Lepton S&S, split SFs, and TOP-23-008 phase-space extrapolation: `muonscale`, `muonsmear`, `elescale`, `elesmear`, `*_stat`/`*_syst` variants, plus flat `muExtra: {type: const, value: 1.005}` (0.5%, muon) and `elExtra: {type: const, value: 1.01}` (1.0%, electron) in all 5 era configs and `template_Run3.yml` (legacy `muonhighscale`, `muhighpt`, and unsplit lepton SFs retired/commented).
  - Tau ID & FF: decomposed `tauidjet*` sources only (inclusive `tauidjet`, `Highpt*`, and legacy aliases commented), `tauidel`, `tauidmu`, `tes`, `tauFFstat`, `tauFFsyst`.
  - JME: sub-era JES (`jesAbsolute_<era>`, `jesBBEC1_<era>`, `jesEC2_<era>`, `jesHF_<era>`, `jesRelativeSample_<era>` for `2022`, `2022EE`, `2023`, `2023BPix`, `2024`), correlated `jesAbsolute`, `jesBBEC1`, `jesEC2`, `jesHF`, `jesRelativeBal`, 4 `jesFlavorPure*`, `jer`, `metUnclust` (`jesFlavorQCD` and `jesHEM` removed).
  - BTV & Theory: `btagSFbc_correlated`/`btagSFbc_<era>`, `btagSFlight_correlated`/`btagSFlight_<era>`, segmented xsec nuisances (`tt` 5%, `singleTop` 25%, `dy`/`wjets`/`diboson` 30%, etc.), and single-regex `mescale`/`renscale`/`facscale`/`isr`/`fsr`/`pdfalphas`/`hdamp`/`tune`.
- **Histogram & Automation Notes (2026-11-25)**:
  - `h_leptau_mass_blind_*` in `histos.yml` and `histos_FFapply.yml` sets `show-onlyoverflow: true` so `-1.0` blinded data entries in bin 0 are cleared instead of folded into bin 1 while high-mass overflow is retained.
  - When invoking `LFVAnalyzer/plot_era.py` or `plot_run3.py` with `-F` (`--ff`), all 52 `_S5` plots are auto-extracted from `histos.yml` + `histos_reco.yml` (so `histos_FFapply.yml` is kept untouched for Run 2 compatibility).
- **Git tracking note**: `plotIt/` is ignored in `NanoAODRun3/.gitignore`, so config updates here are not tracked by `NanoAODRun3` git history.
