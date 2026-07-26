from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

def test_inference(input_text : str):
    model = init_chat_model("google_genai:gemma-4-26b-a4b-it", 
                            )
    response = model.invoke(input_text)
    return response


if __name__ == "__main__":
    print(test_inference("Hi"))