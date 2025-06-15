import boto3
import json

bedrock = boto3.client("bedrock-runtime")

def generate_text(prompt):
    body = json.dumps({"inputText": prompt})
    response = bedrock.invoke_model(
        modelId="amazon.titan-text-premier-v1:0",
        contentType="application/json",
        accept="application/json",
        body=body
    )
    result = response["body"].read().decode("utf-8")
    return json.loads(result).get("results", [{}])[0].get("outputText", "No response")