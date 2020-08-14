def matchword(sen1,sen2):
    words1=sen1.split(" ")
    words2=sen2.split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]
    query = input("Please enter the query string\n")
    scores = [matchword(query, sentence) for sentence in sentences]
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] != 0]
    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")