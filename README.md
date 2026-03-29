# AWS EC2 → S3 Log Upload Lab

## Overview
This project is a hands-on AWS lab.
I launched an EC2 instance, connected via SSH, ran a Python log analysis script,
and uploaded the results to an S3 bucket using AWS CLI.

## Architecture
Local PC (WSL) → SSH → EC2 (Ubuntu) → S3

## AWS Services
- EC2
- S3
- IAM

## Environment
- Ubuntu 24.04 (EC2)
- AWS CLI v2
- Python 3

## Steps

### 1. Launch EC2 instance
- Created an EC2 instance (Ubuntu)
- Configured Security Group inbound rule for SSH (port 22)

### 2. SSH connection
```bash
ssh -i ~/keys/log-analysis-key.pem ubuntu@<PublicIPv4>
```

### 3. Install Python
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 4. Install AWS CLI v2
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### 5. Configure AWS CLI
```bash
aws configure
```

### 6. Upload files to S3
```bash
aws s3 cp log.txt s3://bucket-2026/
aws s3 cp result.txt s3://bucket-2026/
aws s3 ls s3://bucket-2026/
```

## Sample Output
Example:
192.168.1.20 2

## What I learned
- Difference between Stop and Terminate in EC2
- How Security Groups control SSH access
- How IAM Access Keys are used for AWS CLI
- How to upload files to S3 using AWS CLI

## Future improvements
- Add CloudWatch monitoring and alarms
- Automate uploads using cron
- Apply least privilege IAM policy for S3 access

## Alarm Test

I simulated high CPU usage on the EC2 instance and verified that the CloudWatch alarm was triggered successfully.

### Result
- CPU utilization exceeded 70%
- Alarm state changed from OK to ALARM
- Notification email was received via SNS

### Test Method
- Generated CPU load using `yes > /dev/null`
- Ran multiple processes to exceed CPU threshold
