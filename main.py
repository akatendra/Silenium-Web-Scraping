from datetime import datetime
import time
import scraper
import xlsx
import database


def spent_time():
    global start_time
    sec_all = time.time() - start_time
    if sec_all > 60:
        minutes = sec_all // 60
        sec = sec_all % 60
        time_str = f'| {int(minutes)} min {round(sec, 1)} sec'
    else:
        time_str = f'| {round(sec_all, 1)} sec'
    start_time = time.time()
    return time_str


def run_process(URL, page_number, filename, driver):
    scraper.connect_to_page(browser, URL, page_number)
    print('Browser opened:', spent_time())
    time.sleep(2)
    html = driver.page_source
    print('Page_source received:', spent_time())
    output_data = scraper.parse_html(html)
    print('Output_data received:', spent_time())
    xlsx.append_xlsx_file(output_data, filename, page_number)
    database.write_to_database(output_data)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


if __name__ == "__main__":
    # Set the values of auxiliary variables
    time_begin = start_time = time.time()
    URL = 'https://www.avito.ru/respublika_krym/kvartiry/prodam/vtorichka'
    current_page = 1
    output_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f'data_store/avito_{output_timestamp}.xlsx'

    print('Start...')
    # Initialize web browser
    browser = scraper.get_firefox_browser()
    # Run for first time to get real current URL
    print(f"Scraping page #{current_page}...")
    scraper.connect_to_page(browser, URL)
    print('Browser opened:', spent_time())
    time.sleep(2)
    html_data = browser.page_source
    print('Page_source received:', spent_time())
    data = scraper.parse_html(html_data)
    print('Output_data received:', spent_time())
    xlsx.write_to_xlsx_file(data, output_filename)
    database.write_to_database(data)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    current_url = browser.current_url
    print('Current URL:', current_url)

    current_page = 2
    # Going through the pages and gathering the information we need
    while current_page <= 3:
        print(f"Scraping page #{current_page}...")
        run_process(current_url, current_page, output_filename, browser)
        current_page += 1

    # Stop script
    browser.quit()
    time_end = time.time()
    elapsed_time = time_end - time_begin
    if elapsed_time > 60:
        elapsed_minutes = elapsed_time // 60
        elapsed_sec = elapsed_time % 60
        elapsed_time_str = f'| {int(elapsed_minutes)} min {round(elapsed_sec, 1)} sec'
    else:
        elapsed_time_str = f'| {round(elapsed_time, 1)} sec'
    print(f"Elapsed run time: {elapsed_time_str} seconds")
