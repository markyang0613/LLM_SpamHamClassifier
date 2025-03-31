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


Install Dependencies: Make sure you have Python 3 installed, then run:

bash
Copy
pip install openai scikit-learn pandas
Set Up Your OpenAI API Key: Export your API key as an environment variable:

bash
Copy
export OPENAI_API_KEY='your-api-key'
Alternatively, you can add it directly in your code (not recommended for production).

Usage
Run the Classification Script: The main script iterates through a set of SMS messages, sends them to the ChatGPT-3.5 Turbo model for classification, and computes evaluation metrics:

bash
Copy
python classifier_script.py
The script outputs the confusion matrix and a classification report.

Interpreting the Results:

Confusion Matrix: Shows the number of true positives, true negatives, false positives, and false negatives.

Classification Report: Displays precision, recall, f1-score, and overall accuracy for both classes (spam and ham).

Sample Results
An example of a high-performing model output is as follows:

Confusion Matrix:

lua
Copy
[[88  0]
 [ 1 11]]
Classification Report:

markdown
Copy
              precision    recall  f1-score   support
         ham       0.99      1.00      0.99        88
        spam       1.00      0.92      0.96        12

    accuracy                           0.99       100
   macro avg       0.99      0.96      0.98       100
weighted avg       0.99      0.99      0.99       100
These results are particularly surprising given that the base ChatGPT-3.5 Turbo model was used without any task-specific fine-tuning.

Future Enhancements
Fine-Tuning: Even better performance may be achieved by fine-tuning the model on a dedicated spam detection dataset.

Deployment: Integrate the classifier into a FastAPI application to serve predictions in real-time.

Expanded Evaluation: Test on a larger dataset and perform error analysis to further understand misclassifications.

Acknowledgments
Thanks to OpenAI for the ChatGPT-3.5 Turbo model.

Dataset providers for the SMS messages used in this project.

The open-source community for the tools and libraries that made this project possible.

License
This project is licensed under the MIT License.

yaml
Copy

---

Feel free to modify this README to suit your specific project details and repository structure!
