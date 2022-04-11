#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        #Prediction based on expected number of mistakes
        careless = request.form.get("careless")
        conceptual = request.form.get("conceptual")
        presentation = request.form.get("presentation")
        print(careless, conceptual, presentation)
        model = joblib.load("Mistake")
        pred = model.predict([[int(careless), int(conceptual), int(presentation)]])
        print(pred)
       
        #Prediction based on confidence of topics
        topic_1 = request.form.get("topic_1")
        topic_2 = request.form.get("topic_2")
        topic_3 = request.form.get("topic_3")
        topic_5 = request.form.get("topic_5")
        topic_6 = request.form.get("topic_6")
        topic_7 = request.form.get("topic_7")
        topic_8 = request.form.get("topic_8")
        topic_9 = request.form.get("topic_9")
        topic_10 = request.form.get("topic_10")
        print(topic_1,topic_2,topic_3,topic_5,topic_6,topic_7,topic_8,topic_9,topic_10)
        model2 = joblib.load("Topic")
        pred2 = model2.predict([[int(topic_1)*10, int(topic_2)*10, int(topic_3)*10, int(topic_5)*10, int(topic_6)*10, int(topic_7)*10,
                                int(topic_8)*10, int(topic_9)*10, int(topic_10)*10]])
        print(pred2)
        
        if pred > pred2:
            s = "The predicted student's score is : " + str(pred2) + "-" + str(pred)
        else:
            s = "The predicted student's score is : " + str(pred) + "-" + str(pred2)
        
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




