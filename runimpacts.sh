text2workspace.py <card> -m 125 -o <name.root>
combineTool.py -M Impacts -d <name.root> -m 125 --doInitialFit --robustFit 1 --redefineSignalPOIs s2B_4bin
combineTool.py -M Impacts -d <name.root> -m 125 --robustFit 1 --doFits --redefineSignalPOIs s2B_4bin
combineTool.py -M Impacts -d <name.root> -m 125 -o impacts.json --redefineSignalPOIs s2B_4bin
plotImpacts.py -i impacts.json -o <name>
