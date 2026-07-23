import asyncio
from app.services.ingest_service import IngestService

async def main():
    # Use 'await IngestService.ingest()' if ingest() is defined as 'async def'
    result = IngestService.ingest() 
    print(result)

if __name__ == "__main__":
    asyncio.run(main())