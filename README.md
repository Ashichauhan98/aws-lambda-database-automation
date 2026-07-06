# AWS Lambda Automation for Database Management

## Overview

This project demonstrates how AWS serverless services can be used to automate database operations without managing any servers.

The application automatically processes employee data files uploaded to an Amazon S3 bucket. As soon as a new file is uploaded, an AWS Lambda function is triggered, which reads the file and stores the employee information in an Amazon DynamoDB table.

The entire workflow is event-driven and runs automatically without any manual intervention.

---

## Problem Statement

Updating databases manually whenever new files arrive can be time-consuming and error-prone. The goal of this project was to automate this process using AWS services so that new employee records are stored instantly after file upload.

---

## Solution

The solution uses AWS Lambda together with S3 and DynamoDB to create a fully automated pipeline.

- Employee data files are uploaded to an S3 bucket.
- S3 generates an event notification.
- The event invokes a Lambda function written in Python.
- The Lambda function extracts employee information from the uploaded file.
- The extracted data is saved in a DynamoDB table.
- CloudWatch logs record every execution for monitoring and debugging.

---

## Architecture

```text
Employee JSON File
        ↓
Amazon S3 Bucket
        ↓
S3 Event Notification
        ↓
AWS Lambda Function
        ↓
Amazon DynamoDB Table
        ↓
Amazon CloudWatch Logs
```

---

## Technologies Used

- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- Python
- Boto3 SDK

---

## Project Workflow

### Step 1
A JSON file containing employee details is uploaded to an S3 bucket.

### Step 2
The upload event automatically triggers the Lambda function.

### Step 3
The Lambda function reads the uploaded file and extracts employee information.

### Step 4
The extracted data is inserted into the DynamoDB table.

### Step 5
CloudWatch logs store execution details for monitoring and troubleshooting.

---

## Sample Input

```json
{
    "employee_id": "101",
    "name": "Ashi",
    "department": "IT",
    "salary": 50000
}
```

---

## AWS Resources Used

### Lambda Function
- EmployeeDataProcessor

### S3 Bucket
- employee-data-upload-ashi

### DynamoDB Table
- Employees

### CloudWatch Log Group
- /aws/lambda/EmployeeDataProcessor

---

## Features

- Automatic database updates without manual intervention.
- Event-driven serverless architecture.
- Real-time processing of uploaded employee records.
- Secure access management using IAM roles and policies.
- Monitoring and logging using CloudWatch.

---

## IAM Permissions

The Lambda execution role was configured with permissions to:

- Read files from Amazon S3
- Write records to DynamoDB
- Generate execution logs in CloudWatch

---

## Repository Structure

```text
aws-lambda-database-automation/
│
├── lambda_function.py
├── employee.json
├── README.md
└── screenshots/
    ├── lambda-function.png
    ├── lambda-code.png
    ├── s3-bucket.png
    ├── uploaded-file.png
    ├── dynamodb-table.png
    ├── inserted-record.png
    └── cloudwatch-logs.png
```

---

## Screenshots

### Lambda Function
Screenshot of the created Lambda function.

### Lambda Code
Screenshot of the Python code running inside Lambda.

### S3 Bucket
Screenshot of the S3 bucket used for file uploads.

### Uploaded Employee File
Screenshot showing the uploaded JSON file.

### DynamoDB Table
Screenshot of the created DynamoDB table.

### Stored Employee Record
Screenshot showing employee information successfully inserted into DynamoDB.

### CloudWatch Logs
Screenshot showing successful Lambda execution logs.

---

## Outcome

The project successfully automated the process of updating database records whenever a new file is uploaded. Using AWS serverless services removed the need for managing infrastructure while ensuring scalability and reliability.

---

## Future Enhancements

Possible improvements for this project include:

- Support for CSV files in addition to JSON files.
- Processing multiple employee records in a single upload.
- Email notifications after successful data insertion.
- Validation of uploaded data before database insertion.
- Automatic archival of processed files.

---

## What I Learned

Through this project I gained practical experience with:

- AWS Lambda
- Event-driven architectures
- Amazon S3 triggers
- DynamoDB operations
- IAM roles and permissions
- CloudWatch monitoring
- Python automation using Boto3

---

## Author

**Ashi Chauhan**

GitHub: https://github.com/your-github-username