from base64 import b64encode
import json
from requests_html import HTML, HTMLSession


def get_match_report_urls(season_name):
    base_url = "https://i7k8x8j8.ssl.hwcdn.net/premier/en/5d5279306be21288657b23c6?params="
    prefix = "&&CompSeason="
    decoded_param = prefix + season_name
    encoded_param = b64encode(decoded_param.encode("ascii")).decode("utf-8")
    session = HTMLSession()
    r = session.get(base_url + encoded_param)
    r.html.render(sleep=1, keep_page=True, timeout=50)
    r_text = r.html.text
    json_string = r_text[r_text.find("{"):r_text.rfind("}") + 1]
    content = json.loads(json_string)["content"]
    html = HTML(html=content)
    links = html.links
    return links





