# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a random forest classifier that predicts whether an individual's salary is more or less than $50k based on other details about them such as age, sex, occupation, etc.
## Intended Use
This model may be used in the absence of concrete salary data when it is needed and other relevant data is available. the API's inference endpoint expects a combination of the below details:
	- age: str
	- workclass: str
	- fnlgt: int
	- education: str
	- education_num: int
	- marital_status: str
	- occupation: str
	- relationship: str
	- race: str
	- sex: str
	- capital-gain: int
	- capital-loss: int
	- hours-per-week: int
	- native-country: str
## Training Data
The training data was sliced from the 'census.csv' dataset, and contains 80% of the total records in the set.
## Evaluation Data
The evaluation data was also sliced from the 'census.csv' dataset, and contains the remaining 20% of the records in the set.
## Metrics
Metrics were calculated for a variety of hyperparameter combinations during training using RandomSearchCV. The final scores for the optimal model are as follows:

| Precision | Recall |   F1   |
|  0.8023   | 0.5220 | 0.6325 |

## Ethical Considerations
This model is by no means a perfect predictor and it's outputs should not be taken as hard-truth, but rather as a statistical estimation based on previous training data. Please use it's results in accordance with this fact.
Additionally, although the model is not trained on nor capable of processing PII (Personally Identifiable Information), please refrain from feeding it data of that kind.
## Caveats and Recommendations
For the most accurate predictions, you should include all features listed above in your API request. Results listed above are not guaranteed in the event that incomplete data is provided.