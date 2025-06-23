import epitran

epi = epitran.Epitran('eng-Latn')
text = "example"

phonemes = epi.transliterate(text)

input = "/home/u6/kathleencosta/independentstudy/metadata.csv"            
output = "/home/u6/kathleencosta/independentstudy/phonememetadata.csv"               

with open(input, "r", encoding="utf-8") as fin, \
     open(output, "w", encoding="utf-8") as fout:
    
    for line in fin:
        if "|" not in line:
            continue  
        wav, text = line.strip().split("|", maxsplit=1)
        text = text.strip().lower()
        phonemes = epi.transliterate(text)
        phonemes = phonemes.replace(" ", "")  
        fout.write(f"{wav}|{phonemes}\n")  

