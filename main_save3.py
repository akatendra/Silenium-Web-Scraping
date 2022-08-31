from datetime import datetime
import time
from scraper import *
from database import *
import logging.config
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor, wait
from random import randint


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


def sleep_time(max_sec):
    rand_time = randint(1, max_sec)
    time.sleep(rand_time)


def run_flow(URL, start_page, end_page):
    global browsers
    # Initialize web browser
    browser = scraper.get_firefox_browser()
    browsers.append(browser)
    scraper.connect_to_page(browser, URL, start_page)
    logger.debug(
        f'Browser for pages {URL} | {start_page}-{end_page} opened: {spent_time()}')
    # Wait random seconds
    sleep_time(5)
    current_page = start_page
    while current_page <= end_page:
        logger.debug(f'Take in work page: {current_page}')
        page_url = f'{URL}?p={current_page}'
        browser.get(page_url)
        page_processing_kvartiry_vtorichka(current_page, browser)
        current_page += 1

    # Stop script
    browser.quit()


def page_processing(parse_func, write_to_db_func, page_number, browser):
    logger.debug(
        '##################################################################')
    logger.debug(f'Scraping page #{page_number}...')
    logger.debug(
        '##################################################################')
    html = browser.page_source
    logger.debug(f'Page_source of page {page_number} received: {spent_time()}')
    output_data = parse_func(html)
    logger.debug(f'Output_data of page {page_number} received: {spent_time()}')
    # xlsx.append_xlsx_file(output_data, output_filename, page_number)
    write_to_db_func(output_data)

    # Go to pagination bar to simulate human behavior
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pagination_bar = browser.find_element(By.XPATH,
                                          '//div[@data-marker="pagination-button"]')
    browser.execute_script("arguments[0].scrollIntoView();", pagination_bar)

    current_url = browser.current_url
    logger.debug(f'Current URL in run_process: {current_url}')
    return current_url


def run_flow_kvartiry_vtorichka(URL, start_page, end_page):
    global browsers
    # Initialize web browser
    browser = scraper.get_firefox_browser()
    browsers.append(browser)
    scraper.connect_to_page(browser, URL, start_page)
    logger.debug(
        f'Browser for pages {URL} | {start_page}-{end_page} opened: {spent_time()}')
    # Wait random seconds
    sleep_time(5)
    current_page = start_page
    while current_page <= end_page:
        logger.debug(f'Take in work page: {current_page}')
        page_url = f'{URL}?p={current_page}'
        browser.get(page_url)
        page_processing_kvartiry_vtorichka(current_page, browser)
        current_page += 1

    # Stop script
    browser.quit()


def page_processing_kvartiry_vtorichka(page_number, browser):
    logger.debug(
        '##################################################################')
    logger.debug(f'Scraping page #{page_number}...')
    logger.debug(
        '##################################################################')
    html = browser.page_source
    logger.debug(f'Page_source of page {page_number} received: {spent_time()}')
    output_data = scraper.parse_html_kvartiry_vtorichka(html)
    logger.debug(f'Output_data of page {page_number} received: {spent_time()}')
    # xlsx.append_xlsx_file(output_data, output_filename, page_number)
    write_to_db_kvartiry_vtorichka(output_data)

    # Go to pagination bar to simulate human behavior
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pagination_bar = browser.find_element(By.XPATH,
                                          '//div[@data-marker="pagination-button"]')
    browser.execute_script("arguments[0].scrollIntoView();", pagination_bar)

    current_url = browser.current_url
    logger.debug(f'Current URL in run_process: {current_url}')
    return current_url


def run_flow_kvartiry_novostroyka(URL, start_page, end_page):
    global browsers
    # Initialize web browser
    browser = scraper.get_firefox_browser()
    browsers.append(browser)
    scraper.connect_to_page(browser, URL, start_page)
    logger.debug(
        f'Browser for pages {URL} | {start_page}-{end_page} opened: {spent_time()}')
    # Wait random seconds
    sleep_time(5)
    current_page = start_page
    while current_page <= end_page:
        logger.debug(f'Take in work page: {current_page}')
        page_url = f'{URL}?p={current_page}'
        browser.get(page_url)
        page_processing_kvartiry_novostroyka(current_page, browser)
        current_page += 1

    # Stop script
    browser.quit()


def page_processing_kvartiry_novostroyka(page_number, browser):
    logger.debug(
        '##################################################################')
    logger.debug(f'Scraping page #{page_number}...')
    logger.debug(
        '##################################################################')
    html = browser.page_source
    logger.debug(f'Page_source of page {page_number} received: {spent_time()}')
    output_data = scraper.parse_html_kvartiry_novostroyka(html)
    logger.debug(f'Output_data of page {page_number} received: {spent_time()}')
    write_to_db_kvartiry_novostroyka(output_data)

    # Go to pagination bar to simulate human behavior
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pagination_bar = browser.find_element(By.XPATH,
                                          '//div[@data-marker="pagination-button"]')
    browser.execute_script("arguments[0].scrollIntoView();", pagination_bar)

    current_url = browser.current_url
    logger.debug(f'Current URL in run_process: {current_url}')
    return current_url


def run_flow_doma_dachi_kottedzhi(URL, start_page, end_page):
    global browsers
    # Initialize web browser
    browser = scraper.get_firefox_browser()
    browsers.append(browser)
    scraper.connect_to_page(browser, URL, start_page)
    logger.debug(
        f'Browser for pages {URL} | {start_page}-{end_page} opened: {spent_time()}')
    # Wait random seconds
    sleep_time(5)
    current_page = start_page
    while current_page <= end_page:
        logger.debug(f'Take in work page: {current_page}')
        page_url = f'{URL}?p={current_page}'
        browser.get(page_url)
        page_processing_doma_dachi_kottedzhi(current_page, browser)
        current_page += 1

    # Stop script
    browser.quit()


def page_processing_doma_dachi_kottedzhi(page_number, browser):
    logger.debug(
        '##################################################################')
    logger.debug(f'Scraping page #{page_number}...')
    logger.debug(
        '##################################################################')
    html = browser.page_source
    logger.debug(f'Page_source of page {page_number} received: {spent_time()}')
    output_data = scraper.parse_html_doma_dachi_kottedzhi(html)
    logger.debug(f'Output_data of page {page_number} received: {spent_time()}')
    write_to_db_doma_dachi_kottedzhi(output_data)

    # Go to pagination bar to simulate human behavior
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pagination_bar = browser.find_element(By.XPATH,
                                          '//div[@data-marker="pagination-button"]')
    browser.execute_script("arguments[0].scrollIntoView();", pagination_bar)

    current_url = browser.current_url
    logger.debug(f'Current URL in run_process: {current_url}')
    return current_url


def thread_pool(func, url, pages):
    futures = []
    with ThreadPoolExecutor() as executor:
        for page in pages:
            futures.append(
                executor.submit(func, url, page[0], page[1]))
            # Wait random seconds
            sleep_time(10)
            logger.debug(
                f'ThreadPoolExecutor take in work pages: {url} | {page[0]}-{page[1]}')
    # Wait for ending of all running processes
    wait(futures)


if __name__ == "__main__":
    # Set up logging
    logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    # Set the variables values
    time_begin = start_time = time.time()
    url_kvartiry_vtorichka = 'https://www.avito.ru/respublika_krym/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg'
    url_kvartiry_novostroyka = 'https://www.avito.ru/respublika_krym/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg'
    url_doma_dachi_kottedzhi = 'https://www.avito.ru/respublika_krym/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ'
    current_page = 1
    last_page = 100
    output_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # output_filename = f'data_store/avito_{output_timestamp}.xlsx'
    browsers = []

    # End of variables values setting

    logger.info('Start...')

    # Adding multithreading

    # kvartiry_vtorichka

    # 6 threads
    # pages = [(1, 14), (15, 32), (33, 48), (49, 63), (64, 82), (83, 100)]
    # 8 threads
    pages = [(1, 11), (12, 24), (25, 36), (37, 49), (50, 63), (64, 77),
             (78, 90), (91, 100)]

    thread_pool(run_flow_kvartiry_vtorichka, url_kvartiry_vtorichka, pages)

    # kvartiry_novostroyka
    pages.clear()
    # 6 threads
    pages = [(1, 9), (10, 17), (18, 23), (24, 32), (33, 41), (42, 47)]
    # 8 threads
    # pages = [(1, 5), (6, 11), (12, 17), (18, 25), (26, 31), (32, 37), (38, 43), (44, 47)]

    thread_pool(run_flow_kvartiry_novostroyka, url_kvartiry_novostroyka, pages)

    # doma_dachi_kottedzhi
    pages.clear()
    # 6 threads
    # pages = [(1, 14), (15, 32), (33, 48), (49, 63), (64, 82), (83, 100)]

    # 8 threads
    pages = [(1, 11), (12, 24), (25, 36), (37, 49), (50, 63), (64, 77),
             (78, 90), (91, 100)]
    # pages = [(1, 3)]
    thread_pool(run_flow_doma_dachi_kottedzhi, url_doma_dachi_kottedzhi, pages)

    # Closing all unclosed browsers
    for browser in browsers:
        if browser.service.is_connectable():
            browser.quit()

    time_end = time.time()
    elapsed_time = time_end - time_begin
    if elapsed_time > 60:
        elapsed_minutes = elapsed_time // 60
        elapsed_sec = elapsed_time % 60
        elapsed_time_str = f'| {int(elapsed_minutes)} min {round(elapsed_sec, 1)} sec'
    else:
        elapsed_time_str = f'| {round(elapsed_time, 1)} sec'
    logger.info(
        f'Elapsed run time: {elapsed_time_str} seconds | New vtorichka items: {scraper.vtorichka_counter} | New novostroy items: {scraper.novostroy_counter} | New doma_dachi_kottedzhi items: {scraper.doma_dachi_kottedzhi_counter}')