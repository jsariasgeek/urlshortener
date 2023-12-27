
# URL Shortening

## Overview
This project implements a basic URL shortening algorithm in Python. The algorithm is designed to take a long URL and convert it into a shorter, more manageable version. This is particularly useful for sharing links on platforms where character space is limited.

## How It Works

### Key Generation
The core of the URL shortening algorithm lies in the key generation process. For each URL, we generate a unique key using the following steps:

1. **Hash the URL**: We use the SHA-256 hashing algorithm to generate a hash of the original URL. This ensures that each URL maps to a unique hash value.

2. **Base62 Encoding**: We convert the hash value into a base62 string. Base62 encoding uses characters `0-9`, `a-z`, and `A-Z`, providing a good balance between compactness and readability.

3. **Truncate the Hash**: To keep the URL short, we truncate the hash to a fixed length (8 characters in this implementation).

## Example Usage (How to run the APP)
```
./bin/up.sh
./bin/sync_db.sh
```
You should have a server running on http://localhost:8000

## Limitations and Improvements
- This implementation uses an in-memory dictionary for storing URL mappings, which is not persistent. For production use, integrating a database is recommended.
- The algorithm does not handle potential hash collisions or repeated URLs.
- Scalability and performance optimizations may be necessary for handling a large number of URLs.

## Conclusion
This URL shortening algorithm provides a basic yet functional approach to shortening URLs in Python. It is suitable for small-scale applications and can be extended for more robust and scalable solutions.
