import aiohttp
from restack_ai.function import NonRetryableError, function, log


async def fetch_content_from_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            error_message = f"Failed to fetch content: {response.status}"
            raise NonRetryableError(error_message)


@function.defn()
async def context_docs() -> str:
    try:
        # Return basic instructions instead of fetching from URL
        docs_content = """
        I am a video assistant that can help you with:
        1. Answering questions about video content
        2. Providing information and assistance
        3. Having natural conversations
        
        I aim to keep my responses concise and natural for seamless text-to-speech conversion.
        """
        log.info("Using basic instructions", content=len(docs_content))

        return docs_content

    except Exception as e:
        error_message = f"context_docs function failed: {e}"
        raise NonRetryableError(error_message) from e
