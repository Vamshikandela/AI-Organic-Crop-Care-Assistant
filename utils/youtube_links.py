from urllib.parse import quote

def generate_youtube_links(crop, weather, issue):

    # Better search queries focused on SOLUTIONS
    search_queries = [
        {
            "title": f"Best solutions for {issue} in {crop}",
            "query": f"{crop} {issue} solution telugu"
        },

        {
            "title": f"How to overcome {issue} naturally",
            "query": f"how to overcome {issue} naturally in {crop} telugu"
        },

        {
            "title": f"Organic treatment for {issue}",
            "query": f"{issue} organic treatment telugu"
        },

        {
            "title": f"Weather-based solution for {crop}",
            "query": f"{crop} farming tips in {weather} weather telugu"
        },

        {
            "title": f"Increase {crop} growth naturally",
            "query": f"increase {crop} growth naturally telugu"
        },

        {
            "title": f"Natural fertilizers for better {crop} yield",
            "query": f"best natural fertilizer for {crop} telugu"
        },

        {
            "title": f"Organic pest and disease control",
            "query": f"{crop} pest disease control organic telugu"
        }
    ]

    youtube_links = ""

    for idx, item in enumerate(search_queries, start=1):

        encoded_query = quote(item["query"])

        youtube_links += f"""
{idx}. {item['title']}
https://www.youtube.com/results?search_query={encoded_query}

"""

    return youtube_links