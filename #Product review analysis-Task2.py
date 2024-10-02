#Product review analysis - Task 2:Sentiment Tally

reviews = ["This product is really good. I'm impressed with its quality.", 
    "The performance of this product is excellent. Highly recommended!", 
    "I had a bad experience with this product. It didnt meet my expectation.",
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it."]


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews:
    for positive in positive_words:
            if positive in review:
                print(len(positive.split()))

    for negative in negative_words:
         if negative in review:
              print(len(negative.split()))



#Task 3:Review Summary
for review in reviews:
    if review.startswith("This product"):
        summary = review[:32] + "...,'"
        print(summary)

    if review.startswith("The performance"):
        summary_2 = review[:31] + "...,'"
        print(summary_2)

    if review.startswith("I had"):
        summary_3 = review[:32] + "...,'"
        print(summary_3)

    if review.startswith("Poor quality"):
        summary_4 = review[:30] + "...,'"
        print(summary_4)

    if review.startswith("The product"):
        summary_5 = review[:32] + "...,'"
        print(summary_5)