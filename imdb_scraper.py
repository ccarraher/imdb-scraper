from requests import get
from bs4 import BeautifulSoup
import bs4
from datetime import date


# TODO: Implement cx-Oracle library in order to transfer scrapped data into the database
# TODO: Fix num_reviews, original code worked for some pages but not all

def scrape_actors_writers_directors():
    for id in range(1659543, 1659643):
        actor_director_writer_base_url = "https://www.imdb.com/name/nm" + str(id) + '/'
        page_html = get(actor_director_writer_base_url)
        soup = BeautifulSoup(page_html.content, 'html.parser')
        get_name(soup)
        get_birthplace(soup)
        get_bday(soup)
        get_known_for(soup)
        get_act_dir_writ_imdb_id(soup)
        print("\n")
        id += 1
    return soup


def scrape_movies_tv():
    for id in range(110912, 111062):
        movie_tv_base_url = "https://www.imdb.com/title/tt0" + str(id) + "/"
        page_html = get(movie_tv_base_url)
        soup1 = BeautifulSoup(page_html.content, 'html.parser')
        get_title(soup1)
        get_runtime(soup1)
        get_genre_and_release_date(soup1)
        get_plotkeywords(soup1)
        get_movie_num_reviews(soup1)
        get_review(soup1)
        get_mov_tv_imdb_id(soup1)
        print("\n")
        id += 1
    return soup1

#Title


def get_title(soup1):
    try:
        title_container = soup1.find_all("h1")
        title = title_container[0].text.strip()
        print("Title: ", title)
    except:
        print("Error retrieving title")



#Runtime


def get_runtime(soup1):
    try:
        runtime_container = soup1.find_all("time")
        runtime = runtime_container[0].text.strip()
        print("Runtime: ", runtime)
    except:
        print("Error retrieving runtime")

#Genre and release date


def get_genre_and_release_date(soup1):
    try:
        genre = soup1.find("div", {'class': "subtext"}).find_all('a')
        print("Genres: ")
        for i in genre:
            print(i.text.strip())
    except:
        print("Error retrieving genre and release date")


def get_movie_num_reviews():
    #try:
        movie_tv_base_url = "https://www.imdb.com/title/tt0110955/"
        page_html = get(movie_tv_base_url)
        soup1 = BeautifulSoup(page_html.content, 'html.parser')
        num_reviews_container = soup1.find("div", {"class": "user-comments"}).find_all("a")
        num_reviews_string = num_reviews_container[4].text.strip()
        num_reviews = num_reviews_string.split(" ", 4)
        #for num_reviews[] in range(2,4):
            #print("Number of reviews: ", num_reviews)
    #except:
        #print("Error retrieving number of reviews")


def get_plotkeywords(soup1):
    try:
        plotkeywords_container = soup1.find("div", {"class": "see-more inline canwrap"}).find_all("a", recursive=False)
        print("Plotkeywords: ")
        for p in plotkeywords_container:
            print(p.text.strip())
    except:
        print("Error retrieving plotkeywords")

def get_mov_tv_imdb_id(soup1):
    try:
        imdb_container = soup1.find('div', {"class": "uc-add-wl-button uc-add-wl--not-in-wl uc-add-wl"})
        imdb_id_mtv = imdb_container["data-title-id"]
        print("IMDB ID: ", imdb_id_mtv)
        return imdb_id_mtv
    except:
        print("Error retrieving IMDB ID")


def get_known_for(soup):
    try:
        print("Known For: ")
        for div in soup.find_all('div', {'class': 'knownfor-title-role'}):
            print(div.find('a').attrs['title'])
    except:
        print("Error retrieving known for")


def get_bday(soup):
    try:
        bday = soup.find("time")["datetime"]
        print("Birthday: ", bday)
    except:
        print("Error retrieving birthday")


def get_birthplace(soup):
    try:
        birthplace = soup.find("div", {"id": "name-born-info"}).findAll('a')
        print("Birthplace: ", birthplace[2].text.strip())
    except:
        print("Error retrieving birthplace")


def get_name(soup):
    try:
        name = soup.find("span", {"class": "itemprop"})
        print("Name: ", name.text.strip())
    except:
        print("Error retrieving name")


def get_total_episodes(soup):
    try:
        total_episodes_container = soup.find("span", {"class": "bp_sub_heading"})
        print("Total Episodes: ", total_episodes_container.text.strip())
    except:
        print("Error retrieving total episodes")

def get_review(soup1):
    try:
        stars_container = soup1.find("div", {"class": "tinystarbar"})
        stars = stars_container["title"]
        print("Stars: ", stars)
    except:
        print("Error retrieving stars")
    try:
        review_title_container = soup1.find("div", {"user-comments"}).find("span").find("strong")
        print("Review Title: ", review_title_container.text.strip())
    except:
        print("Error retrieving review title")
    try:
        review_date_container = soup1.find("div", {"class": "comment-meta"})
        review_date_string = review_date_container.text.strip()
        review_date_indexer = review_date_string.split("|", 1)
        review_date = review_date_indexer[0]
        print("Review Date: ", review_date)
    except:
        print("Error retrieving review date")
    try:
        review_user = soup1.find("div", {"class": "comment-meta"}).find("a")
        print("Username: ", review_user.text.strip())
    except:
        print("Error retrieving username")
    try:
        review_content = soup1.find("div", {"class": "user-comments"}).find("p")
        print("Review Content: ", review_content.text.strip())
    except:
        print("Error retrieving review content")


def get_act_dir_writ_imdb_id(soup):
    try:
        imdb_container_adw = soup.find('span', {"class": "nobr-only"}).find({'a': "href"})["href"]
        imdb_id_adw = imdb_container_adw.split("/", 3)
        print("IMDB ID: ", imdb_id_adw[2])
    #return imdb_id_adw
    except:
        print("Error retrieving IMDB ID")


def popular_tv_show_ids():
    url = "https://www.imdb.com/chart/tvmeter/"
    page_html = get(url)
    soup = BeautifulSoup(page_html.content, 'html.parser')
    id_container_container = soup.find_all("td", {"class": "titleColumn"})
    for id in id_container_container:
        id_string = (id.a['href'])
        id = id_string.split("/", 3)
        print(id[2])

def popular_actors_ids():
    url = "https://www.imdb.com/search/name/?gender=male,female&start=51&ref_=rlm"
    page_html = get(url)
    soup = BeautifulSoup(page_html.content, 'html.parser')
    id_container_container = soup.find_all("h3", {"class": "lister-item-header"})
    for id in id_container_container:
        id_string = (id.a['href'])
        id = id_string.split("/", 3)
        print(id[2])
