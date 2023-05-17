import collections
from concurrent.futures import ThreadPoolExecutor, as_completed


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = '/'.join(startUrl.split('/')[:3])
        seen = {startUrl}

        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = collections.deque([executor.submit(htmlParser.getUrls, startUrl)])
            while futures and as_completed(futures):
                for url in futures.popleft().result():
                    if url not in seen and url.startswith(domain):
                        print(url)
                        seen.add(url)
                        futures.append(executor.submit(htmlParser.getUrls, url))

        return list(seen)