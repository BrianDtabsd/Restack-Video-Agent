import asyncio
import logging
import webbrowser
from pathlib import Path

from watchfiles import run_process

from src.agents.agent import AgentVideo
from src.client import client
from src.functions.context_docs import context_docs
from src.functions.llm_chat import llm_chat
from src.functions.pipeline import pipecat_pipeline
from src.workflows.room import RoomWorkflow


async def main() -> None:
    await client.start_service(
        agents=[AgentVideo],
        workflows=[RoomWorkflow],
        functions=[
            llm_chat,
            pipecat_pipeline,
            context_docs,
        ],
    )


def run_services() -> None:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Service interrupted by user. Exiting gracefully.")


def watch_services() -> None:
    watch_path = Path.cwd()
    logging.info("Watching %s and its subdirectories for changes...", watch_path)
    webbrowser.open("https://reli5mem.clj5khk.gcp.restack.it")  # Your cloud engine URL
    run_process(watch_path, recursive=True, target=run_services)


if __name__ == "__main__":
    run_services()
