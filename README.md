# LLM_SpamHamClassifier
## Overview
This project demonstrates how to utilize the ChatGPT-3.5 Turbo model from OpenAI to create a spam/ham classifier for SMS messages. By leveraging the model’s robust language understanding, the classifier can differentiate between spam and legitimate (ham) messages without any additional fine-tuning.

## Project Description
The goal of this project is to build a classifier that:
- Takes an SMS message as input.
- Uses a prompt engineered for ChatGPT-3.5 Turbo to classify the message as either **spam** or **ham**.
- Returns the classification result along with the probability of the message being spam.

Even though ChatGPT-3.5 Turbo is a general-purpose language model, it demonstrates surprisingly high accuracy on this task, showcasing the potential of large-scale pre-trained models for specialized applications.

## How It Works
1. **Data Preparation**  
   A dataset containing SMS messages and their true labels (spam or ham) is used. Each message is extracted along with its actual category.

2. **Prompt Engineering**  
   For each message, a prompt is generated that instructs the model to classify the message. For example:
   > “Classify the following sms message as ham or spam. Also return the probability of it being spam.  
   Message: 'Your message text here.'  
   The output should only contain two words: ham or spam, and the probability with two decimal points.”

3. **API Call and Prediction**  
   The ChatGPT-3.5 Turbo model is invoked via the OpenAI API using the generated prompt. The model’s response is parsed to extract the predicted label and probability.

4. **Evaluation**  
   The predicted labels are compared with the true labels from the dataset. A confusion matrix and classification report (using scikit-learn) are generated to evaluate the model's performance.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/spam-ham-classifier.git
   cd spam-ham-classifier
