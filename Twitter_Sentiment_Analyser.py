from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__)

def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict['compound'] >= 0.05:
        return "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        return "Negative"

    else:
        return "Neutral"


@app.route('/')
def Tweet_Input():
    return render_template('Tweet_Input.html')

@app.route('/Analysis', methods = ['POST'])
def Analysis():
    sentence = request.form.get('sentence')
    Sentiment = sentiment_scores(sentence)
    return render_template('Analysed_Sentiment.html', sentence= sentence, Sentiment = Sentiment)



if __name__ == '__main__':
    app.run(debug=True)

