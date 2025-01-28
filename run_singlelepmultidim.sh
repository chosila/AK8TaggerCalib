## -------------------------------------------- lepjet, no lepjet ------------------------------------------------------------
# ## EGamma + SingleMu
# combine -M MultiDimFit cards/lepjet/combined_lepjet_Xbb_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_combined_Xbb_BBQ

# combine -M MultiDimFit cards/lepjet/combined_lepjet_Xbb_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_combined_Xbb_BBQQ

# combine -M MultiDimFit cards/nolepjet/combined_nolepjet_Xbb_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_combined_Xbb_BBQ

# combine -M MultiDimFit cards/nolepjet/combined_nolepjet_Xbb_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_combined_Xbb_BBQQ

# ## EGamma
# combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_card_Xbb_0b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_EGamma_Xbb_BBQ

# combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_card_Xbb_0b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_EGamma_Xbb_BBQQ

# combine -M MultiDimFit cards/nolepjet/EGamma/tagger_calib_card_Xbb_0b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_EGamma_Xbb_BBQ

# combine -M MultiDimFit cards/nolepjet/EGamma/tagger_calib_card_Xbb_0b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_EGamma_Xbb_BBQQ

# ## SingleMuon
# combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_SingleMuon_Xbb_BBQ

# combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n lepjet_SingleMuon_Xbb_BBQQ

# combine -M MultiDimFit cards/nolepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_SingleMuon_Xbb_BBQ

# combine -M MultiDimFit cards/nolepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n nolepjet_SingleMuon_Xbb_BBQQ


# ## move all root files into the rootfile folder
# mv higgsCombine*MultiDimFit.mH120.root output_root/


# ## run the plotting
# python plot_nll.py output_root/higgsCombinelepjet_combined_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinelepjet_combined_Xbb_BBQQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinelepjet_EGamma_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinelepjet_EGamma_Xbb_BBQQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinelepjet_SingleMuon_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinelepjet_SingleMuon_Xbb_BBQQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_combined_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_combined_Xbb_BBQQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_EGamma_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_EGamma_Xbb_BBQQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_SingleMuon_Xbb_BBQ.MultiDimFit.mH120.root
# python plot_nll.py output_root/higgsCombinenolepjet_SingleMuon_Xbb_BBQQ.MultiDimFit.mH120.root
## ------------------------------------------------ lepjet, no lepjet ---------------------------------------------------------


## run the 1b+0b combines
# combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_SingleMuon_Xbb_0b+1b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SingleMuon_Xbb_0b+1b_BBQ
# combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_SingleMuon_Xbb_0b+1b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SingleMuon_Xbb_0b+1b_BBQQ
# combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_EGamma_Xbb_0b+1b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b+1b_BBQ
# combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_EGamma_Xbb_0b+1b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b+1b_BBQQ


## ----------------------------------------------- alt norms ----------------------------------------------
combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n  SingleMuon_Xbb_0b_BBQ_alt_norm
combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_card_Xbb_0b_BBQQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SingleMuon_Xbb_0b_BBQQ_alt_norm
combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_card_Xbb_0b_BBQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b_BBQ_alt_norm
combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_card_Xbb_0b_BBQQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b_BBQQ_alt_norm

combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_SingleMuon_Xbb_0b+1b_BBQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SingleMuon_Xbb_0b+1b_BBQ_alt_norm
combine -M MultiDimFit cards/lepjet/SingleMuon/tagger_calib_SingleMuon_Xbb_0b+1b_BBQQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SingleMuon_Xbb_0b+1b_BBQQ_alt_norm
combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_EGamma_Xbb_0b+1b_BBQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b+1b_BBQ_alt_norm
combine -M MultiDimFit cards/lepjet/EGamma/tagger_calib_EGamma_Xbb_0b+1b_BBQQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n EGamma_Xbb_0b+1b_BBQQ_alt_norm

combine -M MultiDimFit cards/lepjet/tagger_calib_SM+EG_Xbb_0b_BBQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SM+EG_Xbb_0b_BBQ_alt_norm
combine -M MultiDimFit cards/lepjet/tagger_calib_SM+EG_Xbb_0b_BBQQ_alt_norm.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SM+EG_Xbb_0b_BBQQ_alt_norm

combine -M MultiDimFit cards/lepjet/tagger_calib_SM+EG_Xbb_0b_BBQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SM+EG_Xbb_0b_BBQ
combine -M MultiDimFit cards/lepjet/tagger_calib_SM+EG_Xbb_0b_BBQQ.txt --setParameterRanges s2B_4bin=-1.5,2.5  --algo grid --parameters s2B_4bin --points 1001 --floatOtherPOIs yes --redefineSignalPOIs s2B_4bin -n SM+EG_Xbb_0b_BBQQ


## move all root files into the rootfile folder
mv higgsCombine*.root output_root/

## plot nll
python plot_nll.py output_root/higgsCombineEGamma_Xbb_0b+1b_BBQQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSM+EG_Xbb_0b_BBQQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSingleMuon_Xbb_0b_BBQQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineEGamma_Xbb_0b+1b_BBQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSM+EG_Xbb_0b_BBQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSingleMuon_Xbb_0b_BBQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineEGamma_Xbb_0b_BBQQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSingleMuon_Xbb_0b+1b_BBQQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineEGamma_Xbb_0b_BBQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSingleMuon_Xbb_0b+1b_BBQ_alt_norm.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSM+EG_Xbb_0b_BBQ.MultiDimFit.mH120.root
python plot_nll.py output_root/higgsCombineSM+EG_Xbb_0b_BBQQ.MultiDimFit.mH120.root
