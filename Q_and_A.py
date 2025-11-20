from transformers import pipeline

qa = pipeline("question_answering")

context = """
Banitsa is a small town located in the Blagoevgrad Province of 
southwestern Bulgaria.
 It is situated in the picturesque Razlog Valley,
   surrounded by the Rila, Pirin, and Rhodope Mountains. 
   The town is known for its rich history, traditional architecture, and proximity to popular ski resorts such as Bansko and Borovets. 
   Banitsa offers a charming atmosphere with its cobblestone streets, old churches, and local crafts. It is also a gateway for outdoor activities like hiking, skiing, 
   and exploring the natural beauty of the region.
 """

question = "Is Banitsa food or a place?"

result = qa(question = question, context = context)

print(f" Context: {context} \n Question: {question} => Answer: {result ['answer']}  ")