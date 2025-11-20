from transformers import pipeline

summerizer = pipeline("summarization")

big_text = """
Martin Scorsese is an acclaimed American film director, producer, screenwriter, and actor known for his significant contributions to the film industry.
 Born on November 17, 1942, in New York City, Scorsese has directed numerous iconic films that have left a lasting impact on cinema. Some of his most notable works include "Taxi Driver," "Raging Bull," "Goodfellas," "The Departed," and "The Irishman." His films often explore themes of identity, morality, and the human condition, frequently delving into the complexities of crime 
 and redemption. Scorsese is also recognized for his collaborations with actors like Robert De Niro and Leonardo DiCaprio, 
 as well as his distinctive visual style and storytelling techniques. Throughout his career, he has received numerous awards,
   including an Academy Award for Best Director for "The Departed." In addition to his filmmaking, Scorsese is a passionate advocate for film
     preservation and has played a crucial role in preserving classic films for future generations.
"""

result = summerizer(
    big_text,
    max_length = 35,
    min_length = 10,
    do_sample = False
)

print(f" Original: {big_text} \n Summarized: {result[0]['summary_text']}")