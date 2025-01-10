import json
import boto3
import streamlit as st

# Initialize AWS Bedrock client
client_bedrock = boto3.client('bedrock-agent-runtime', region_name='ap-southeast-2')

# Function to query AWS Bedrock Knowledge Base
def query_bedrock_knowledgebase(prompt):
    """Query the AWS Bedrock Knowledge Base and return the response."""
    try:
        response = client_bedrock.retrieve_and_generate(
            input={'text': prompt},
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': 'A0QXGE0PMC',
                    'modelArn': 'arn:aws:bedrock:ap-southeast-2:361769557998:inference-profile/apac.anthropic.claude-3-5-sonnet-20240620-v1:0'
                }
            }
        )
        return response['output']['text']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit application
st.title("Q&A with AWS Bedrock Knowledge Base")
st.markdown("Ask questions about the AI Knowledge Base!")

# Chat interface
user_prompt = st.text_input("Enter your question:")
if st.button("Submit"):
    if user_prompt.strip():
        with st.spinner("Querying the Knowledge Base..."):
            response = query_bedrock_knowledgebase(user_prompt)
            st.write(f"Response: {response}")
    else:
        st.warning("Please enter a question.")
