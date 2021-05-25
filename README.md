# Linked Data Serverless Proxy
Serverless LD Proxy implementation as Lambda function created on Amazon AWS.

# Installation
Install aws cli and run configuration setup

```aws configure```

Install the AWS Serverless Application Model (SAM)

```pip install aws-sam-cli```

Build LD Proxy image:

```sam build --use-container```

Deploy on AWS following the instruction 

```sam deploy --guided```

Go to AWS console in the [APIs section](https://console.aws.amazon.com/apigateway/main/apis?region=us-east-1), find function called ld-proxy, to Prod stage and check the Invoke URL, for example, [https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod](https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod)

Check if LD Proxy is operational:

```curl https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod/ping```

OpenAPI specification should be available on /prod/docs path, try this:

```curl https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod/docs```

Further instructions are coming...
