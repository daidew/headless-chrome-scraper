from lxml import html
import os

tid = 30000000
pages = None

with open(os.path.join('html_storage',f'{tid}.html'), 'r') as f:
    pages = f.readlines()
page = ''.join(pages)
tree = html.fromstring(bytes(page,encoding='utf-8'))
post_title = [s.strip() for s in tree.xpath('//div[@class="display-post-wrapper main-post type"]//h2[@class="display-post-title"]/text()') if len(s.strip()) != 0]
post_story = [s.strip() for s in tree.xpath('//div[@class="display-post-wrapper main-post type"]//div[@class="display-post-story"]/text()') if len(s.strip()) != 0]
post_comment = [s.strip() for s in tree.xpath('//div[@class="display-post-story-wrapper comment-wrapper"]//div[@class="display-post-story"]/text()') if len(s.strip()) != 0]

print('title:',post_title)
print('story:',post_story)
print('comment:',post_comment)

