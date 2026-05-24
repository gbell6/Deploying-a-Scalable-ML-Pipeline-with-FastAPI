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
Feature Glossary:
	Acceptable values:
		- work-class: 	[Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked]
		- education: [Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.]
		- marital-status: [Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse]
		- occupation: [Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces]
		- relationship: [Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried]
		- race: [White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black]
		- sex: [Male, Female]
		- native-country: [United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands]