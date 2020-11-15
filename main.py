import requests
from bs4 import BeautifulSoup
github_username = "Liam-Breen"
main_page_url = f"https://github.com/{github_username}?tab=repositories"
main_page = requests.get(url = main_page_url)
main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
repos = main_page_soup.find_all("a", itemprop="name codeRepository")

for repo in repos:

    repo_url = f"https://github.com/{github_username}/{repo.text.strip()}"
    print(repo_url)
    repo_page = requests.get(url = repo_url)
    repo_page_soup = BeautifulSoup(repo_page.content, 'html.parser')


    title = repo_page_soup.find("meta", {"property":"og:title"})['content']
    title = title.split('/')[1]
    print(f'title: {title}')

    desc_content = repo_page_soup.find("meta", {"name":"description"})['content']
    # This is needed add the end of your description to create the tags section
    desc_content_split = desc_content.split('END')
    description = desc_content_split[0]
    print(f'description: {description}')

    try:
        tags = desc_content_split[1]
        print(f'tags: {tags}')
    except IndexError:
        pass
