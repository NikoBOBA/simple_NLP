from transformers import pipeline
ner = pipeline("ner", grouped_entities=True)

text = " Nikola was born in Bulgaria, in 2005."
results = ner(text)

print(f"Text: {text} => Entities: {results}")