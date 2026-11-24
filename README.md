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

## Run 3 Configuration Notes (as of 2026-11-12)

- **Active configs**: `configs/Run3_muon/` and `configs/Run3_electron/` (`config_2022.yml`, `config_2022EE.yml`, `config_2023.yml`, `config_2023BPix.yml`, `config_2024.yml`, `config_Run3.yml`, and `template_Run3.yml`).
- **Luminosity errors (`XPOG-01`)**: `config_2024.yml` uses `luminosity-error: 0.016`; combined `config_Run3.yml` / `template_Run3.yml` use `luminosity-error: 0.012`.
- **Synchronized Run 3 systematics**:
  - Lepton S&S and split SFs: `muonscale`, `muonsmear`, `elescale`, `elesmear`, and `*_stat`/`*_syst` variants (legacy `muonhighscale`, `muhighpt`, and unsplit lepton SFs retired/commented).
  - Tau ID & FF: decomposed `tauidjet*` sources only (inclusive `tauidjet`, `Highpt*`, and legacy aliases commented), `tauidel`, `tauidmu`, `tes`, `tauFFstat`, `tauFFsyst`.
  - JME: sub-era JES (`jesAbsolute_<era>`, `jesBBEC1_<era>`, `jesEC2_<era>`, `jesHF_<era>`, `jesRelativeSample_<era>` for `2022`, `2022EE`, `2023`, `2023BPix`, `2024`), correlated `jesAbsolute`, `jesBBEC1`, `jesEC2`, `jesHF`, `jesRelativeBal`, 4 `jesFlavorPure*`, `jer`, `metUnclust` (`jesFlavorQCD` and `jesHEM` removed).
  - BTV & Theory: `btagSFbc_correlated`/`btagSFbc_<era>`, `btagSFlight_correlated`/`btagSFlight_<era>`, segmented xsec nuisances (`tt` 5%, `singleTop` 25%, `dy`/`wjets`/`diboson` 30%, etc.), and single-regex `mescale`/`renscale`/`facscale`/`isr`/`fsr`/`pdfalphas`/`hdamp`/`tune`.
- **Git tracking note**: `plotIt/` is ignored in `NanoAODRun3/.gitignore`, so config updates here are not tracked by `NanoAODRun3` git history.
