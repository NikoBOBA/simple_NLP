from transformers import pipeline

classifier = pipline("sentiment-analysis")

text1 = "I love learning about AI!"
result_1= classifier(text1)

text2 = "I hate pineapple on pizza"
result_2 = classifier(text2)

print(f"Text 1: {text1} => Sentiment: {result_1}")

print(f"Text 2: {text2} => Sentiment: {result_2}")