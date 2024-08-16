from openai import OpenAI
from dotenv import load_dotenv

from ..models import models
from ..schemas import schemas
import os
load_dotenv() 

client = OpenAI(
    api_key= os.environ.get("OPEN_API_KEY"),
)

def suggest_blog(content):
    try:
        # content = get_content(blog_id, db)
        if content:
            completion = client.chat.completions.create(model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are an assistant, skilled in suggesting ideas to improve self-awareness and helping with suggestions to improve mental health."},
                            {"role": "user", "content": content}
                        ]
                    )
            suggestions = completion.choices[0].message.content
            print(type(suggestions))
            return suggestions
    except Exception as e:
        print(f"Error while giving suggestions for the blog: {e}")
        return None
    
def get_content(blog_id, db):
    print("check2")
    blog_content = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    print("check3")
    print(blog_content.body)
    return blog_content.body
    # suggestions = suggest_blog(blog_content.body)
    # return suggestions


# content = "I feel overhwhelmed with all the task today."
# suggestions = suggest_blog(content)
# print("Suggestions",suggestions)

