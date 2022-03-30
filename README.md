# Classiﬁcation of Textual Data

## Background
In this project, we implemented naive Bayes and K-fold cross-validation from scratch, while using logistic regression from scikit-learn package – and compare these two algorithms on two distinct textual datasets. The goal is to gain experience implementing these algorithms from scratch and to get hands-on experience comparing performance of different models.


## Data Set
We will use two datasets in this project, outlined below.

• 20 news group dataset:https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html. Use the default train subset (subset=‘train’, and remove=([‘headers’, ‘footers’, ‘quotes’]) in sklearn.datasets) to train the models and report the ﬁnal performance on the test subset. 
Note: need to start with the text data and convert text to feature vectors.  

• IMDB Reviews: http://ai.stanford.edu/˜amaas/data/sentiment/ Here, need to use only reviews in the train folder for training and report the performance from the test folder. Need to work with the text documents to build our own features and ignore the pre-formatted feature ﬁles.


## Experiments
The goal of this project is to explore linear classiﬁcation and compare different features and models. Use 5-fold cross validation to estimate performance in all of the experiments. Evaluate the performance using accuracy. You are welcome to perform any experiments and analyses you see ﬁt (e.g., to compare different features), but at a minimum you must complete the following experiments in the order stated below:

1. Conduct multiclass classiﬁcation on the 20 news group dataset, and binary classiﬁcation on the IMDb Reviews.

2. In a single table, compare and report the performance of the performance of naive Bayes and logistic regression on each of the two datasets (with their best hyperparameters), and highlight the winner for each dataset and overall. 

3. Further, with a plot, compare the accuracy of the two models as a function of the size of dataset (by controlling the training size). For example, you can randomly select 20%, 40%, 60% and 80% of the available training data and train your model on this subset. Now, compare the performance of corresponding models and highlight the best.

Note: The above experiments are the minimum requirements; For this part, you might implement logistic regression from scratch (and try different learning rates, investigate different stopping criteria for the gradient descent), try linear regression for predicting ratings in the IMDB data, try different text embedding methods as alternatives to bag of words.















