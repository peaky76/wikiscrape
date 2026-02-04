# Next Steps

## Development Opportunities

### Caching Implementation

**Priority:** High
**Complexity:** Low-Medium

Implement file-based caching for HTML content to reduce redundant Wikipedia requests.

**Key Points:**
- Cache HTML content with configurable TTL (default 24 hours)
- Use URL hash as cache key
- Maintain backward compatibility with existing API
- Add cache invalidation and cleanup

**Files to Modify:**
- `wikiscrape/wikipage.py` - Add caching to `text` property
- `wikiscrape/cache.py` - New caching module
- `tests/test_cache.py` - New test file

### Async Support

**Priority:** Medium
**Complexity:** Medium

Add asynchronous variants for bulk operations and concurrent page fetching.

**Key Points:**
- Add `aiohttp` dependency for async HTTP
- Create `AsyncWikipage` class alongside existing `Wikipage`
- Maintain full backward compatibility
- Add batch processing utilities

**Files to Add/Modify:**
- `wikiscrape/async_wikipage.py` - New async implementation
- `wikiscrape/async_utils.py` - Batch processing utilities
- `tests/test_async.py` - Async test suite
- `pyproject.toml` - Add aiohttp dependency

## Implementation Notes

- Follow existing code conventions and patterns
- Add comprehensive tests for new functionality
- Maintain backward compatibility
- Use conventional commit messages
- Keep changes small and focused