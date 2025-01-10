import json
import boto3

# Initialize Bedrock client
client_bedrock = boto3.client('bedrock-agent-runtime', region_name='ap-southeast-2')

def lambda_handler(event, context):
    """Lambda function to handle queries to AWS Bedrock Knowledge Base."""
    try:
        # Validate input
        user_prompt = event.get("prompt")
        if not user_prompt:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Missing 'prompt' in the event payload"})
            }
        
        # Query AWS Bedrock
        response = client_bedrock.retrieve_and_generate(
            input={'text': user_prompt},
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': 'A0QXGE0PMC',
                    'modelArn': 'arn:aws:bedrock:ap-southeast-2:361769557998:inference-profile/apac.anthropic.claude-3-5-sonnet-20240620-v1:0'
                }
            }
        )
        response_text = response['output']['text']

        return {
            'statusCode': 200,
            'body': response_text
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
