## to run this script, need to be in cmssw 14 environment, and need to `cmsenv`
## source runimpacts.sh <path to card> <name of impact plot without .pdf>
cardloc="$1"
plotname="$2"
text2workspace.py "$cardloc" -m 125 -o "$plotname".root
## s4B_4bin
#combineTool.py -M Impacts -d "$plotname".root -m 125 --doInitialFit --robustFit 1 --redefineSignalPOIs s4B_4bin --preFitValue 0 --setParameters s4B_4bin=0
#combineTool.py -M Impacts -d "$plotname".root -m 125 --robustFit 1 --doFits --redefineSignalPOIs s4B_4bin --preFitValue 0 --setParameters s4B_4bin=0
#combineTool.py -M Impacts -d "$plotname".root -m 125 -o impacts.json --redefineSignalPOIs s4B_4bin --preFitValue 0 --setParameters s4B_4bin=0
#plotImpacts.py -i impacts.json -o "$plotname"_impact

## s2B2Q_4bin. should we make the POI a arg too?
combineTool.py -M Impacts -d "$plotname".root -m 125 --doInitialFit --robustFit 1 --redefineSignalPOIs s2B2Q_4bin --preFitValue 0 --setParameters s2B2Q_4bin=0
combineTool.py -M Impacts -d "$plotname".root -m 125 --robustFit 1 --doFits --redefineSignalPOIs s2B2Q_4bin --preFitValue 0 --setParameters s2B2Q_4bin=0
combineTool.py -M Impacts -d "$plotname".root -m 125 -o impacts.json --redefineSignalPOIs s2B2Q_4bin --preFitValue 0 --setParameters s2B2Q_4bin=0
plotImpacts.py -i impacts.json -o "$plotname"_impact

## s4B_3bin for X4b QCD where we combine the top bin bc we want info on sideband + signal region
#combineTool.py -M Impacts -d "$plotname".root -m 125 --doInitialFit --robustFit 1 --redefineSignalPOIs s4B_3bin --preFitValue 0 --setParameters s4B_3bin=0
#combineTool.py -M Impacts -d "$plotname".root -m 125 --robustFit 1 --doFits --redefineSignalPOIs s4B_3bin --preFitValue 0 --setParameters s4B_3bin=0
#combineTool.py -M Impacts -d "$plotname".root -m 125 -o impacts.json --redefineSignalPOIs s4B_3bin --preFitValue 0 --setParameters s4B_3bin=0
#plotImpacts.py -i impacts.json -o "$plotname"_impact



## s2B_4bin
# combineTool.py -M Impacts -d "$plotname".root -m 125 --doInitialFit --robustFit 1 --redefineSignalPOIs s2B_4bin --preFitValue 0 --setParameters s2B_4bin=0 --cminDefaultMinimizerStrategy 0
# combineTool.py -M Impacts -d "$plotname".root -m 125 --robustFit 1 --doFits --redefineSignalPOIs s2B_4bin --preFitValue 0 --setParameters s2B_4bin=0 --cminDefaultMinimizerStrategy 0
# combineTool.py -M Impacts -d "$plotname".root -m 125 -o impacts.json --redefineSignalPOIs s2B_4bin --preFitValue 0 --setParameters s2B_4bin=0 --cminDefaultMinimizerStrategy 0
#plotImpacts.py -i impacts.json -o "$plotname"_impact
