# **ETL Pipeline Automation using Apache Airflow**  

This project demonstrates an automated **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow** to process data from **Twitter** and **YouTube** APIs. The pipeline runs on an **Azure VM**, stores processed data in **Azure SQL**, and generates insights.  

---

## **Overall End-to-End Architecture**  

Below is the diagram representing the overall architecture of the pipeline:  

![image](https://github.com/user-attachments/assets/20c0b75d-2e1f-4465-934c-d3915a6294c9)  

### **Process Overview**  
1. **Data Source**: Tweets and YouTube data are retrieved using respective APIs.  
2. **ETL in Apache Airflow**:  
   - **Extract**: Calls APIs to retrieve data.  
   - **Transform**: Cleans and preprocesses data (e.g., removing unnecessary characters, converting to DataFrame).  
   - **Load**: Inserts the transformed data into Azure SQL for storage.  
3. **Insights Generation**: Data is analyzed locally to derive insights.  

---

## **ETL Pipeline in Apache Airflow**  

The following diagram illustrates the structure of the ETL pipeline:  

![image](https://github.com/user-attachments/assets/e564b7bd-fcb0-44e2-ab45-8dd3c08651e1)  

### **Pipeline Tasks**  
1. **Extract**:  
   - Calls the Twitter and YouTube APIs to fetch raw data.  
   - Managed by the `complete_twitter_extract` and `complete_youtube_extract` tasks.  

2. **Transform**:  
   - Cleans and processes raw data to remove noise and prepare it for analysis.  
   - Managed by the `complete_twitter_transform` and `complete_youtube_transform` tasks.  

3. **Load**:  
   - Connects to Azure SQL and inserts the processed data for long-term storage.  
   - Managed by the `complete_twitter_load` and `complete_youtube_load` tasks.  

---

## **Full Explanation**  

For an in-depth explanation of the project, watch the accompanying YouTube video:  
[Full Explanation on YouTube](https://youtu.be/zMOsm0L1V40)  

---

## **Acknowledgments**  

- **Apache Airflow**: For orchestration and automation.  
- **Azure SQL**: For scalable data storage.  
- **Twitter and YouTube APIs**: For data retrieval.  
- **Python Libraries**: Used for data transformation and processing.  

### **Feel free to explore!**  
