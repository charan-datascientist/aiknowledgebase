Here’s a detailed **README.md** file for your application:

---

# **AWS Bedrock Chatbot**

## **Objective**
The AWS Bedrock Chatbot is a conversational application designed to interact with knowledge bases stored in AWS Bedrock. Using the **Retrieve API** and **RetrieveAndGenerate API**, the chatbot retrieves or generates responses from the knowledge base, making it suitable for use cases like FAQ systems, documentation support, and knowledge retrieval tasks.

---
## **Architecture Diagram**
![
    Architecture Diagram for AWS Bedrock Chatbot
](ai_knowledgebase.jpg)
---

## **Tech Stack**
1. **Backend:**
   - **AWS Bedrock**: For Knowledge Base queries and response generation.
   - **AWS Lambda**: Serverless function to handle the API logic.
   - **AWS API Gateway**: REST API for integrating with the Lambda function.

2. **Frontend:**
   - **Streamlit**: Python-based framework for building the chatbot interface.

3. **Storage:**
   - **Amazon S3**: For storing documents used in the Knowledge Base.

4. **Programming Language**: Python 3.8+
5. **Dependencies**:
   - `boto3`: AWS SDK for Python.
   - `streamlit`: Framework for creating the chatbot UI.
   - `requests`: For making API calls.

---

## **What We Have Done So Far**
### 1. **Created a Knowledge Base in AWS Bedrock**
   - Uploaded documents to an **Amazon S3 bucket**.
   - Created a Knowledge Base in AWS Bedrock linked to the S3 bucket.
   - Configured chunking, embedding, and vector store for efficient query processing.

### 2. **Implemented AWS Lambda Function**
   - Created a Lambda function with the `retrieve_and_generate` API to query the Bedrock Knowledge Base.
   - Integrated the Lambda function with an API Gateway for external access.

### 3. **Built REST APIs**
   - Developed two REST APIs using **AWS API Gateway**:
     1. **Retrieve API**: For retrieving raw information from the Knowledge Base.
     2. **RetrieveAndGenerate API**: For retrieving and generating contextual responses.

### 4. **Integrated with Streamlit**
   - Built a chatbot UI using Streamlit.
   - Connected the Streamlit app to the REST APIs for interaction.

---

## **How to Create the Lambda Function**

### **Step 1: Create a Lambda Function**
1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create Function**.
3. Choose **Author from Scratch**.
4. Provide:
   - **Function Name**: `bedrock-chatbot-lambda`.
   - **Runtime**: Python 3.8+.

### **Step 2: Configure IAM Role**
1. Attach an IAM role with the following permissions:
   - `bedrock:InvokeModel`
   - `bedrock:RetrieveAndGenerate`
   - `s3:GetObject` (if accessing S3 documents).

### **Step 3: Deploy Code**
1. Zip the Lambda code:
   ```bash
   cd lambda_function
   zip -r lambda_function.zip .
   ```
2. Upload the `lambda_function.zip` file to the Lambda function.

### **Step 4: Increase Timeout**
1. In the Lambda function configuration, increase the timeout to 30 seconds to handle large queries.

---

## **How to Create a REST API**

### **Step 1: Open API Gateway Console**
1. Open the [API Gateway Console](https://console.aws.amazon.com/apigateway/).
2. Create a new **REST API**.

### **Step 2: Create Resources**
1. Add a resource:
   - **Resource Name**: `/chatbot`.

### **Step 3: Create Methods**
1. Under the `/chatbot` resource, create a **GET method**.
2. Configure **Integration Type**:
   - **Integration Type**: Lambda Function.
   - Select the Lambda function you created earlier.

### **Step 4: Configure Method Request**
1. Enable **URL Query String Parameters**:
   - **Parameter Name**: `prompt`.
   - Set the request validator to validate query string parameters and headers.

### **Step 5: Configure Integration Request**
1. Map the query string parameter to the Lambda function:
   - **Mapping Template**:
     ```json
     {
         "prompt": "$input.params('prompt')"
     }
     ```

### **Step 6: Deploy the API**
1. Deploy the API to a new stage:
   - **Stage Name**: `Dev`.
2. Note the API endpoint URL (e.g., `https://<api-id>.execute-api.ap-southeast-2.amazonaws.com/Dev/chatbot`).

---

## **Run Locally**
### **Step 1: Install Dependencies**
Install required packages:

```bash
pip install -r requirements.txt
```

### **Step 2: Run the Streamlit App**
Run the app locally:

```bash
streamlit run app.py
```

### **Step 3: Test the Chatbot**
1. Open the Streamlit app in your browser.
2. Enter a query and validate the response from the Knowledge Base.

---

## **Testing the REST API**
### **Using Postman**
1. Open Postman.
2. Create a **GET request** to the API Gateway endpoint:
   ```plaintext
   https://<api-id>.execute-api.ap-southeast-2.amazonaws.com/Dev/chatbot?prompt=What is deep learning?
   ```
3. Verify the response.