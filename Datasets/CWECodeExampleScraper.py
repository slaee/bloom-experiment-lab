import requests
from pyquery import PyQuery
import re
import os
from concurrent.futures import ThreadPoolExecutor

os.chdir('.')

def scrape(url):
    session=requests.Session()
    session.headers.update(
            {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    response=session.get(url)    
    return response


def clean_code(text,codetype=None):
    # remove (bad code) from the text and remove the line
    text = re.sub(r'\(bad code\)', '', text)
    # remove (good code) from the text and remove the line
    text = re.sub(r'\(good code\)', '', text)
    # remove Example Language: PHP from the text
    text = re.sub(r'Example Language: PHP', '', text)
    text = re.sub(r'Example Language: JavaScript', '', text)
    text = re.sub(r'Example Language: HTML', '', text)
    # remove all [...] and /.../ from the text
    text = re.sub(r'\[\.\.\.\]', '', text)
    text = re.sub(r'\/\.\.\.\/', '', text)
    # remove all that are ... only in a line
    text = re.sub(r'^\.\.\.$', '', text, flags=re.MULTILINE)
    # remove the trailing and leading whitespaces
    text = text.strip()
    if codetype == "PHP":
        # add <?php to first line of the text
        text = "<?php\n" + text + "\n?>"
    return text


def process_cwe_definition(index):
    url = f"https://cwe.mitre.org/data/definitions/{index}.html"
    
    vuln_php_file_name = f"CWE-{index}.php"
    vuln_php_path_to_save = os.path.join("test/Vulnerable/PHP/", vuln_php_file_name)

    vuln_js_file_name = f"CWE-{index}.js"
    vuln_js_path_to_save = os.path.join("test/Vulnerable/JavaScript/", vuln_js_file_name)

    
    #scrape
    print(f"[+] Scraping {url}")
    response = scrape(url)

    html = response.content.decode('utf-8')
    pq = PyQuery(html)
    for elem in pq('div.indent.Bad'):
        if pq(elem).find("div.optheading:contains('PHP')"):
            print(f"[+] Found PHP code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts, codetype="PHP")
            print(f"[+] Saving to {vuln_php_path_to_save}")
            with open(vuln_php_path_to_save, "a") as f:
                f.write(texts + "\n")

        if pq(elem).find("div.optheading:contains('JavaScript')"):
            print(f"[+] Found JavaScript code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts)
            print(f"[+] Saving to {vuln_js_path_to_save}")
            with open(vuln_js_path_to_save, "a") as f:
                f.write(texts + "\n")

        if pq(elem).find("div.optheading:contains('HTML')"):
            print(f"[+] Found HTML code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts)
            html = PyQuery(texts)
            texts = html('script').text()
            if texts:
                print(f"[+] Saving to {vuln_js_path_to_save}")
                with open(vuln_js_path_to_save, "a") as f:
                    f.write(texts + "\n")

    nonvuln_php_file_name = f"CWE-{index}.php"
    nonvuln_php_path_to_save = os.path.join("test/NonVulnerable/PHP/", nonvuln_php_file_name)

    nonvuln_js_file_name = f"CWE-{index}.js"
    nonvuln_js_path_to_save = os.path.join("test/NonVulnerable/JavaScript/", nonvuln_js_file_name)

    for elem in pq('div.indent.Good'):
        if pq(elem).find("div.optheading:contains('PHP')"):
            print(f"[+] Found PHP code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts, codetype="PHP")
            print(f"[+] Saving to {nonvuln_php_path_to_save}")
            with open(nonvuln_php_path_to_save, "a") as f:
                f.write(texts + "\n")

        if pq(elem).find("div.optheading:contains('JavaScript')"):
            print(f"[+] Found JavaScript code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts)
            print(f"[+] Saving to {nonvuln_js_path_to_save}")
            with open(nonvuln_js_path_to_save, "a") as f:
                f.write(texts + "\n")

        if pq(elem).find("div.optheading:contains('HTML')"):
            print(f"[+] Found HTML code in {url}")
            texts = pq(elem).text()
            texts = clean_code(texts)
            html = PyQuery(texts)
            texts = html('script').text()
            if texts:
                print(f"[+] Saving to {nonvuln_js_path_to_save}")
                with open(nonvuln_js_path_to_save, "a") as f:
                    f.write(texts + "\n")

    return True


def main():
    # run with multithreading
    with ThreadPoolExecutor(max_workers=10) as executor:
        # https://cwe.mitre.org/data/definitions/2000.html
        executor.map(process_cwe_definition, range(1, 1420))


    # for i in range(20, 2000):
    #     url = f"https://cwe.mitre.org/data/definitions/{i}.html"
        
    #     file_name = f"CWE-{i}.php"
    #     path_to_save = os.path.join("test", file_name)

    #     #scrape
    #     print(f"[+] Scraping {url}")
    #     response = scrape(url)

    #     html = response.content.decode('utf-8')
    #     pq = PyQuery(html)
    #     for elem in pq('div.indent.Bad'):
    #         if pq(elem).find(".optheading:contains('PHP')"):
    #             print(f"[+] Found PHP code in {url}")
    #             texts = pq(elem).text()
    #             # remove (bad code) from the text and remove the line
    #             texts = re.sub(r'\(bad code\)', '', texts)
    #             # remove Example Language: PHP from the text
    #             texts = re.sub(r'Example Language: PHP', '', texts)
    #             # remove the trailing and leading whitespaces
    #             texts = texts.strip()
    #             # add <?php to first line of the text
    #             texts = "<?php\n" + texts + "\n?>"
    #             # save to file
    #             print(f"[+] Saving to {path_to_save}")
    #             with open(path_to_save, "w") as f:
    #                 f.write(texts)



    # filter to detect only PHP
    # php = tag.filter(lambda i, this: 'PHP' in PyQuery(this).text())
    

if __name__ == "__main__":
    main()