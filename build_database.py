from scraper import get_posts, scrape_post


def build_db_content():

    cl_url = "https://vancouver.craigslist.org/search/cta?auto_bodytype=1&auto_bodytype=10&auto_bodytype=11&auto_bodytype=12&auto_bodytype=13&auto_bodytype=2&auto_bodytype=3&auto_bodytype=4&auto_bodytype=5&auto_bodytype=6&auto_bodytype=7&auto_bodytype=8&auto_bodytype=9&auto_cylinders=1&auto_cylinders=2&auto_cylinders=3&auto_cylinders=4&auto_cylinders=5&auto_cylinders=6&auto_cylinders=7&auto_cylinders=8&auto_drivetrain=1&auto_drivetrain=2&auto_drivetrain=3&auto_fuel_type=1&auto_fuel_type=2&auto_fuel_type=3&auto_fuel_type=4&auto_fuel_type=6&auto_paint=1&auto_paint=10&auto_paint=11&auto_paint=2&auto_paint=20&auto_paint=3&auto_paint=4&auto_paint=5&auto_paint=6&auto_paint=7&auto_paint=8&auto_paint=9&auto_size=1&auto_size=2&auto_size=3&auto_size=4&auto_title_status=1&auto_transmission=1&auto_transmission=2&auto_transmission=3&condition=10&condition=20&condition=30&condition=40&language=5&max_price=500000&min_price=1&postedToday=1#search=1~list~0~0"

    post_urls = get_posts(cl_url)
    db_content = []
    for url in post_urls:
        post_details = scrape_post(url)
        db_content.append(post_details)

    return db_content


