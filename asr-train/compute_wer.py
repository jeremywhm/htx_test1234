#!/usr/bin/env python3

# Compute the WER of the pre-trained and fine-tuned models.

import jiwer


def compute_wer(ref_dict, hyp_dict):
    # Compute WER between hypothesis and reference
    wer = 0
    total_num_ref_words = 0
    for utt_name in sorted(ref_dict.keys()):
        num_ref_words = len(ref_dict[utt_name].split(" "))
        total_num_ref_words += num_ref_words
        if utt_name not in hyp_dict:
            wer += num_ref_words # All deletions
        else:
            wer += jiwer.wer(ref_dict[utt_name], hyp_dict[utt_name]) * num_ref_words
    wer /= total_num_ref_words
    return wer
    
    
def read_ref_csv(path):
    # Read a CSV file containing reference word sequences
    ref = dict()
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip().split(",")
            if ".mp3" in line[0]:
                utt_name = line[0]
                assert(utt_name not in ref)
                ref[utt_name] = line[1].upper() # wav2vec2-large-960h only supports upper case
    return ref
    
    
pretrained_csv_filename = "/home/jeremy/htx_test1234/asr/cv-valid-dev.csv"
finetuned_csv_filename = "/home/jeremy/htx_test1234/asr-train/cv-valid-dev.csv"
ref_csv_filename = "/home/jeremy/datasets/common_voice/cv-valid-dev.csv"

# Read hypothesis transcriptions
pretrained_hyp_dict = read_ref_csv(pretrained_csv_filename)
finetuned_hyp_dict = read_ref_csv(finetuned_csv_filename)

# Read reference transcriptions
ref_dict = read_ref_csv(ref_csv_filename)

# Compute WERs
pretrained_wer = compute_wer(ref_dict, pretrained_hyp_dict)
finetuned_wer = compute_wer(ref_dict, finetuned_hyp_dict)

print("pre-trained WER = {} %".format(pretrained_wer * 100))
print("fine-tuned WER = {} %".format(finetuned_wer * 100))
