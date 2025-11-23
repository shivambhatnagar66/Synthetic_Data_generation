import numpy as np
import pandas as pd

#Generate synthetic E-Mail Data
def generate_synthetic_emails(n_samples=6000, spam_ratio=0.5):
  spam_words = ['free','winner','cash','prize','click','offer','buy','discount',
                'urgent','limited','act now','guarantee','bonus','congratulations',
                'selected','claim','million','dollars','pharmacy','pills',
                'weight loss','make money','work from home','earn','income','investment',
                'credit','loan','debt','refinance','mortgage','casino','lottery']
  ham_words = ['meeting','schedule','project','report','team','please','attached','document','review',
               'feedback','thanks','regards','discussed','conference','presentation','update','status',
               'planning','budget','deadline','contract','client','vendor','invoice','payment','account',
               'department','manager','employee']

  emails, labels = [], []
  n_spam = int(n_samples * spam_ratio)
  n_ham = n_samples - n_spam

  for _ in range(n_spam):
    n_words = np.random.randint(20, 100)
    spam_content = np.random.choice(spam_words, size=int(n_words * 0.7), replace=True)
    normal_content = np.random.choice(ham_words, size=int(n_words * 0.3), replace=True)
    emails.append(' '.join(list(spam_content) + list(normal_content)))
    labels.append(1)

  for _ in range(n_ham):
    n_words = np.random.randint(30, 120)
    ham_content = np.random.choice(ham_words, size=int(n_words * 0.9), replace=True)
    mixed_content = np.random.choice(spam_words, size=int(n_words * 0.1), replace=True)
    emails.append(' '.join(list(ham_content) + list(mixed_content)))
    labels.append(0)

  indices = np.random.permutation(n_samples)
  emails = [emails[i] for i in indices]
  labels = [labels[i] for i in indices]

  return pd.DataFrame({ 'email': emails, 'label': labels })

if __name__ == "__main__":
  df_emails = generate_synthetic_emails()
  print(df_emails.head())