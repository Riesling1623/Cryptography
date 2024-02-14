BLOCK_SIZE = 16

def bytes_to_chunks(b: bytes, chunk_size: int, quiet=True) -> list[bytes]:
    chunks = [b[ind:ind+chunk_size] for ind in range(0, len(b), chunk_size)]
    if not quiet:
        print(f"Chunked input with size {chunk_size}: {chunks}")
    return chunks