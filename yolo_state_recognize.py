from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="http://localhost:9001", # use local inference server
    api_key="6HwRjgPea8UYvpzIyVLp"
)

result = client.run_workflow(
    workspace_name="bedidentification",
    workflow_id="custom-workflow-2",
    images={
        "image": "YOUR_IMAGE.jpg"
    }
)