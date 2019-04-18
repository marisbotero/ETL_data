import argparse
import logging
logging.basicConfig(level = logging.INFO)

from common import config


logger = logging.getLogger(__name__)

def __news_scraper(news_site_uid):
    host = config()['news_sites'][news_site]['url']

    logging.info('Beginning scraper for {}'.format(host))
    logging.info('Finding links in homepage...')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys()
    parser.add_argument('news_site',
                         help = 'The news site that you want to scrape',
                         type = str,
                         choices=news_site_choices)
    arg = parser.parse_args()
    __news_scraper(args.news_site)