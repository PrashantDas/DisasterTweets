import re


# designed by me, does not remove stopwords
def excess_remover(para):
    """makes the following changes:
        replace newline with space
        replace email ids
        replace hypertext
        replace special characters
        hypertext
        extraspaces
        longwords over 14 chrs
        the stop-words remover part requires import nltk, nltk.download('stopwords')"""
    email_removed = re.sub(pattern='[^\s]+@[^\s]+ ', repl='', string=para)
    newline_removed = re.sub(pattern='\n', repl=' ', string=email_removed)
    spe_chr_removed = re.sub(pattern='[^a-zA-Z0-9\s]', repl='', string=newline_removed)
    hyper_removed = re.sub(pattern='htt\S+', repl='', string=spe_chr_removed)
    extra_spc_removed = re.sub(pattern='\s+', repl=' ', string=hyper_removed)
    long_wd_removed = re.sub(pattern='\S{14,}\s', repl='', string=extra_spc_removed)
    individual_words = long_wd_removed.lower().split()
    meaningful_words = [w for w in individual_words]

    return ' '.join(meaningful_words)