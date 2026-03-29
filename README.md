# aws-ec2-s3-log-upload
Hands-on AWS project: EC2 SSH + Python log analysis + S3 upload

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
