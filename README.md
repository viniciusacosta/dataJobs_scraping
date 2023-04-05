# **Introduction:**
Knowing which technologies are most commonly used in data science job postings is essential for anyone seeking to enter the field or further specialize in a specific area. This is because data science is a rapidly evolving field that requires a broad range of technical skills and expertise.

With that in mind I performed web scraping on job postings to gain insights into the most commonly used technologies and tools in the field of data science. Web scraping allowed me to collect data on job postings, including the required qualifications, preferred skills, and other relevant information.

Having this information can enabled job seekers to tailor their resumes and cover letters to better match the requirements of job postings and increase their chances of being selected for an interview. It also could helpe to identify the areas in which a job seeker need to develop their skills and knowledge to become more competitive in the job market.

Moreover, web scraping allowed me to identify emerging trends and opportunities in the field of data, such as the increasing use of cloud computing platforms like AWS and Azure. This information is important for job seekers to stay up-to-date with the latest developments in the field and to prepare for future job opportunities.
 
# **Exploratory Data Analysis**

## **1. Jobs location:** 
_________________________________________________________________________________________________
## **1.1 Country and regions:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228260779-69fdc06c-ac2b-44ac-b480-fa255c59c499.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228287265-45dc9919-e9ca-4561-9b5c-291bee68fa2a.png" />
</p>


> -  62% of the job advertisements are from companies located in São Paulo;
> -  With 81% coming from Southeast region, and 10% from the South;
>    -  SP (1697 ≅ 62%)
>    -  RJ (359 ≅ 13%)
>    -  MG (147 ≅ 5%)
> - Outside the Southeast region;
>    -  PR (116 ≅ 4%)
>    -  RS (104 ≅ 4%)
>    - SC (66 ≅ 2,4%)


## **1.2 Cities:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228260757-df2adb8d-bdd8-4100-897d-b0f93473c3ae.png" />
</p>

> - Although the state of Rio de Janeiro is second in total job vacancies, there is not a large concentration in its cities;
>
> - Disregarding Rio de Janeiro and São Paulo, the jobs are concentrated in the capital of the states;
>   - In **Paraná (Curitiba)** and **Rio Grande do Sul (Porto Alegre)** more than 70% are situated on it's capitals
>   - While __Ceará (Fortaleza)__ and __Bahia (Salvador)__ theses numbers goes up to more than 90%

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228288328-904fb736-94dd-44b1-871b-c2363f503230.png" />
</p>

> - Upon further analysis of **Rio de Janeiro**, we realized that these lower-than-expected numbers  have to do with the advertisements themselves, which are not informing the city in which the vacancy is located; 
>
> - Same goes for **São Paulo**, even with it's whomping numbers, it has only 4 cities (**Campinas, Barueri, São Bernardo do Campo e Osasco**) in the top 15;



## **2. Jobs description overview**
_________________________________________________________________________________________________



<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228260865-326768c4-38ad-4465-a3ef-c490b5151b60.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228260880-10021c3c-43c5-4983-94f5-c6a16926cde2.png" />
</p>

> - Although there is almost no difference between Data Scientist and Data Analyst numbers, it is noticeable that in Data Engineer there is a smaller number of opportunities;
>
> - Another important take is that 62% of data engineer jobs announced are for *Jr level* professionals; 

## **2.1 Overall description:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228633982-904762df-9a69-4904-a1b5-579fc728beaa.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/228628446-b3579ea9-532c-4685-b078-4cd20708ffd7.png" />
</p>


</p>

## **2.2 Comparison between roles:**

### **2.2.1 Programming Languages:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229182790-38867cea-a6e6-4537-9ac7-8dd82a2490a3.png" />
</p>

>   - As expected Python is by far the most popular language in all areas;
>   - Apart from the Data Engineer numbers, which Java is presented at second, in general R is the  second most used;
>     - An interesting take is that although Java appears little in Data Science and Data Analyst vacancies, Data Engineer vacancies managed to raise the numbers of this language to practically the second most used next to R;
> - In order of top 5 most used languages;
>   - Python - (1303)
>   - R - (436)
>   - Java - (427)
>   - Basic - (228)
>   - Javascript - (209)



### **2.2.2 Database technologies:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229182996-6b8bb66e-2d8f-4a1c-a19a-0ad628a136b2.png" />
</p>

> Overall, **SQL** technology was the most mentioned, with a total of **1791** mentions. When comparing the different roles, it can be observed that SQL technology is equally important in all of them, being the most mentioned technology in each;
> - For the **Data Science** and **Data Analyst** roles, **Azure** and **AWS** were the next most mentioned technologies, with **Spark** and **SAP** also being relevant technologies mentioned in job advertisements for this role;
> - In the **Data Engineer** roles, **AWS** takes the place of **Azure** as the second most mentioned technology, while **Git** stays as the third most mentioned, and **SAP** leaving the top 5;

### **2.2.3 Data Packages:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229182613-46de9384-3814-4f69-bc91-a9bd044abf3f.png" />
</p>

> Despite the data career, in all of them the same Python packages are the most used and asked for, which is in line with the most used language being Python. It's also noticeable that deep learning knowledge is a diferential;
> - **Pandas** and **Numpy** are the top 2 packages among all, which could imply a large necessity for manipulating the data in all jobs;
> - The Deep Learning packages **Tensorflow** and **Pytorch** comes right behind;



### **2.2.4 Data Visualization Tools:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229181986-83551ba0-ce4e-49ba-b37e-b752bb334c68.png" />
</p>

>The charts presented show the number of times different Business Intelligence (BI) tools were mentioned in job advertisements for Data Science, Data Analyst, and Data Engineer roles;
> - Overall, **Tableau** is the most mentioned BI tool, followed by **Power BI** and **Looker**;
> - BI tools are more relevant for **Data Analyst** and **Data Scientist** roles than for **Data Engineer** roles, as can be seen by the number of mentions in each;
> - Among the three roles, the distribution of mentions of BI tools is relatively similar, with **Tableau** and **Power BI** being the most mentioned;

### **2.2.5 All technologies:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229181721-394b2406-b344-486e-926d-895a1b068bb1.png" />
</p>

> Overall, the data presented suggest that a strong technical background in SQL and Python is important for Data Science, Data Analyst, and Data Engineer roles. Cloud-based solutions, such as Azure and AWS, are also becoming increasingly popular for data storage and processing.
> - In **Data Science** and **Data Analyst** roles the top 5 are quite similar:
>     - **Python** and **SQL** are the most mentioned technology, which is expected, as Python is widely used in data roles for data manipulation, analysis, and modeling. As SQL is used for data querying and manipulation; 
>     - **Tableau** and **Azure** are also relevant in Data Analyst roles, as data visualization and cloud-based solutions are becoming increasingly popular;
>     - **R** is also a relevant technology in those roles, as **R** is commonly used for statistical analysis and data visualization;  
> -  **Data Engineer** roles:
>     - The big diference for the other roles are **Java**, **AWS**, and **Azure** being more mentioned, once again indicating something expected, as Data Engineers need to have a strong technical background in data storage, manipulation, and processing;


### **2.2.6 Level of Education:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/91922356/229193274-3cdce684-fbc4-46ff-90e6-eca37d2afe52.png" />
</p>


> There isn't any major diferences between the diferent careers, despite Data Engineering asking for slightly higher degrees and Data Aalyst slightly lower, all of them presents a similar proportion with Bachelors degree leading with **~90%**, Masters degree with **~8%** and Doctorate degree with **~2%**;
> - **Data Science** diferences from the overall numbers;
>   - Bachelors degree **(-0,98%)**
>   - Master degree **(-0,53%)**
>   - Doctorate degree **(+0,59%)**
> - **Data Analyst** diferences from the overall numbers; 
>   - Bachelors degree **(+1,92%)**
>   - Master degree **(-1,26%)**
>   - Doctorate degree **(-0,65%)**
> - **Data Engineer** diferences from the overall numbers;
>   - Bachelors degree **(-2,29%)**
>   - Master degree **(+1,7%)**
>   - Doctorate degree **(+0,59%)**

# **Extra info:**

- **[Web Scraping script:]()** Python script with the web scraping code.
- **[Jupyter notebook EDA:]()** Notebook with all the data wrangling (cleaning, replacing, transforming, grouping, joining) and data visualization.
- **[Data Jobs Dashboard:]()** For a better visualization of the information provided by the data source, check out the dashboard created and posted on my Tableau Public profile.


# **Contact:**
**LinkedIn** - https://www.linkedin.com/in/vinicius-andrade-308597203/

**email** - v.andrade343@gmail.com