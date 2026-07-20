from vllm import LLM, SamplingParams

def main():
    llm = LLM(model="./model_weights", dtype="bfloat16")

    sampling_params = SamplingParams(temperature=0.7, max_tokens=256)

    conversation = [
        {"role": "user", "content": "自己紹介してください"}
    ]

    outputs = llm.chat(conversation, sampling_params)

    print("vllm出力👇")
    for output in outputs:
        print(output.outputs[0].text)

if __name__ == "__main__":
    main()