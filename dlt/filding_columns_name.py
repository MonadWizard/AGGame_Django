import itertools

column_names = [
    "Square_Deep_Forward",
    "MidWicket_DeepSweeper",
    "MidWicket_DeepForward",
    "LongOn_Wide",
    "Long_On",
    "LongOn_Straight",
    "StraightHit",
    "LongOff_Straight",
    "LongOff",
    "LongOff_Wide",
    "DeepExtraCover",
    "DeepCover",
    "DeepCoverPoint",
    "DeepPoint",
    "DeepBackwardPoint",
    "Thirdman_Deep",
    "Thirdman_Fine",
    "LongStop",
    "FineLeg_Long",
    "FineLeg_Deep",
    "SquareLeg_DeepBackward",
    "SquareLeg_Deep",
    "MidWicket",
    "MidOn_Deep",
    "MidOff_Deep",
    "ExtraCover",
    "Cover",
    "Coverpoint",
    "ForwardPoint",
    "Point",
    "BackwardPoint",
    "SquareLeg_Backward",
    "SquareLeg",
    "SquareLeg_Forward",
    "Thirdman_Short",
    "Fineleg_Short",
    "Square",
    "ThirdMan",
    "Fineleg_Straight",
    "FineLeg",
    "FineLeg_Square",
    "Mid_On",
    "Mid_off",
    "WicketKeeper",
    "Gully",
    "FlySlip",
    "Slip",
    "LegSlip",
    "Backward_ShortLeg",
    "LegGully",
    "MidWicket_Short",
    "MidOn_Short",
    "MidOff_Short",
    "Cover_Short",
    "SillyMidOn",
    "SillyMidOff",
    "ShortLeg",
    "SillyPoint",
    "Slip1",
    "Slip2",
    "Slip3",
    "Slip4",
    "Slip5"
]

# words = ["__catches", "__directthrough", "__runout", "__runssaved", "__Spectaqulorfilding"]
words = ["__catches",__directthrough]

combinations = list(itertools.product(column_names, repeat=len(words)))

joined_names = []

for combination in combinations:
    joined_name = "_".join([f"{word}_{column_name}" for word, column_name in zip(combination,words)])
    joined_names.append(joined_name)

print(joined_names)
