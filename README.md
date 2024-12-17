# python-car-picker
This is a full-stack website incorporating some data analytics and prediction modeling. A user will insert a list of cars and this program will provide an optimal car. The optimal car will have a high fuel-capacity, high tire-size, low cost, and will be as recently manufactured. There is an edge case however, cars can be electric as well (any Tesla for example)

For the scatter plot, the x-axis will be the year manufactured and the y-axis is a numerical measurement between 0 and 1. The number will be higher given 3 criteria:
1. the closer the cost of the current model is to the minimum cost of each car
2. the closer the fuel-capacity or battery amount is to the maximum cost of each car 

## Phase 1 (Generic Phase)
This phase is geared towards providing the best cars given a list of car brands provided by the user.

### Backend / Server-Side
* Python (primary programming language)
* Selenium (for scraping all contents of the website)
* Flask or FastAPI (Python framework for building endpoints and a RESTful API)
* MySQL (for storing all possible car brands, their models, and their generations)

### Data Analytics
* NumPy (for parsing data into arrays)
* Pandas (used for querying all MySQL database results into dataframes)
* Matplotlib (efficient for plotting data and regression analysis)
* Seaborn (to enhance color in these scatter plots)
* scikit-learn (for predicting the statistics of the next possible cars)

### Frontend / Client-Side
* Figma (for emphasizing UI/UX)
* CSS and Bootstrap (Styling and Formatting elements)
* React (front-end JS framework for adding a flexible number of cars per list)

### Cloud Computing
* AWS Lambda (API hosting)
* AWS Amplify (Frontend)
* Amazon S3 (Storage)

### Checkpoint Report
* LaTeX

### Skills Inherited
* HTTP (from Computer Networking)

# Phase 2 (Personalized Phase)
This phase is dedicated towards choosing the best cars given a prompt from the user.

**Some example prompts:**
1. The top 10 most cost effective cars
2. Five of the best electric cars overall
3. Cars with identical stats to the Acura NSX 2016

## Natural Language Processing and Deep Learning
* HuggingFace
* PyTorch
