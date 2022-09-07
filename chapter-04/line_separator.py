import sys, fileinput, re
from nltk.tokenize import sent_tokenize

if __name__ == "__main__":
    for line in fileinput.input():
        if line.strip() != "":
            line = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', line.strip()) # \.는 마침표에 의해 나뉜다는 뜻인듯

            sentences = sent_tokenize(line.strip()) # sentence-wise tokenization; one sentence on each line

            for s in sentences:
                if s != "":
                    sys.stdout.write(s + "\n")
