# server.py
import asyncio
import argparse
from vllm.entrypoints.openai.api_server import run_server
from vllm.entrypoints.openai.cli_args import make_arg_parser

def main():
    parser = argparse.ArgumentParser()
    parser = make_arg_parser(parser)
    args = parser.parse_args([
        "--model", "/root/model_weights_W4A16",
        "--host", "0.0.0.0",
        "--port", "8000",
    ])
    asyncio.run(run_server(args))

if __name__ == "__main__":
    main()