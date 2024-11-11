from django.core.management.base import BaseCommand
from blog.models import Author, Post, Comment
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Author.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

        # Create authors
        author1 = Author.objects.create(name='John Doe', email='john@example.com')
        author2 = Author.objects.create(name='Jane Smith', email='jane@example.com')
        author3 = Author.objects.create(name='Alice Johnson', email='alice@example.com')

        # Create posts
        post1 = Post.objects.create(
            title='How to Learn Django',
            content=(
                "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. "
                "It was designed to help developers take applications from concept to completion as quickly as possible. "
                "In this blog post, we will explore the steps to learn Django effectively.\n\n"
                "1. **Understand the Basics of Python**: Before diving into Django, make sure you have a good understanding of Python. "
                "This includes knowledge of basic syntax, data structures, and object-oriented programming.\n\n"
                "2. **Set Up Your Development Environment**: Install Python, Django, and other necessary tools. "
                "You can use virtual environments to manage dependencies.\n\n"
                "3. **Follow the Official Django Tutorial**: The official Django documentation provides a comprehensive tutorial that covers the basics of Django. "
                "It is a great starting point for beginners.\n\n"
                "4. **Build a Simple Project**: Start with a simple project like a blog or a to-do list application. "
                "This will help you understand the core concepts of Django, such as models, views, templates, and forms.\n\n"
                "5. **Learn About Django's Advanced Features**: Once you are comfortable with the basics, explore Django's advanced features like class-based views, "
                "authentication, and middleware.\n\n"
                "6. **Join the Django Community**: Participate in forums, attend meetups, and contribute to open-source projects. "
                "The Django community is very welcoming and can provide valuable support and resources.\n\n"
                "By following these steps, you will be well on your way to becoming proficient in Django."
            ),
            published_date=datetime.now(),
            author=author1,
            status='published'
        )

        post2 = Post.objects.create(
            title='Understanding REST APIs',
            content=(
                "A REST API (also known as RESTful API) is an application programming interface (API or web API) that conforms to the constraints of REST "
                "architectural style and allows for interaction with RESTful web services. REST stands for Representational State Transfer and was created by "
                "computer scientist Roy Fielding.\n\n"
                "1. **What is REST?**: REST is an architectural style that uses HTTP requests to access and use data. The data can be used to GET, PUT, POST, and DELETE "
                "data types, which refers to the reading, updating, creating, and deleting of operations concerning resources.\n\n"
                "2. **Principles of REST**: REST is based on a few principles, including statelessness, client-server architecture, cacheability, layered system, and uniform interface.\n\n"
                "3. **HTTP Methods**: REST APIs use HTTP methods explicitly. The common HTTP methods used in REST are GET, POST, PUT, DELETE, and PATCH.\n\n"
                "4. **Endpoints**: Endpoints are the URLs where the API can access the resources. Each endpoint represents a specific resource.\n\n"
                "5. **Status Codes**: REST APIs use standard HTTP status codes to indicate the success or failure of an API request.\n\n"
                "6. **Authentication**: REST APIs can use various authentication methods, including basic authentication, token-based authentication, and OAuth.\n\n"
                "Understanding these concepts is crucial for working with REST APIs effectively. They provide a standardized way to interact with web services and are widely used in modern web development."
            ),
            published_date=datetime.now(),
            author=author2,
            status='published'
        )

        post3 = Post.objects.create(
            title='Tips for Effective Remote Work',
            content=(
                "Remote work has become increasingly popular, especially in the tech industry. While it offers flexibility and convenience, it also comes with its own set of challenges. "
                "Here are some tips to stay productive while working remotely:\n\n"
                "1. **Create a Dedicated Workspace**: Set up a specific area in your home where you can work without distractions. This helps in creating a boundary between work and personal life.\n\n"
                "2. **Stick to a Routine**: Establish a daily routine that includes regular working hours, breaks, and time for exercise. Consistency helps in maintaining productivity.\n\n"
                "3. **Use Technology to Stay Connected**: Utilize communication tools like Slack, Zoom, and Microsoft Teams to stay in touch with your colleagues. Regular check-ins and virtual meetings can help in staying connected.\n\n"
                "4. **Set Clear Goals and Priorities**: Define your tasks and set clear goals for each day. Prioritize your work to ensure that you are focusing on the most important tasks.\n\n"
                "5. **Take Breaks**: Taking regular breaks is essential to avoid burnout. Step away from your desk, go for a walk, or do some stretching exercises.\n\n"
                "6. **Stay Organized**: Use tools like Trello, Asana, or Notion to keep track of your tasks and projects. Staying organized helps in managing your workload effectively.\n\n"
                "7. **Maintain Work-Life Balance**: It is important to maintain a healthy work-life balance. Set boundaries and make sure to disconnect from work at the end of the day.\n\n"
                "By following these tips, you can stay productive and maintain a healthy work-life balance while working remotely."
            ),
            published_date=datetime.now(),
            author=author3,
            status='published'
        )

        # Create comments
        Comment.objects.create(
            post=post1,
            content='Great article! I found it very helpful.',
            created=datetime.now()
        )

        Comment.objects.create(
            post=post1,
            content='Thanks for sharing this information.',
            created=datetime.now()
        )

        Comment.objects.create(
            post=post2,
            content='This is a very informative post about REST APIs.',
            created=datetime.now()
        )

        Comment.objects.create(
            post=post3,
            content='These tips are really useful for remote workers.',
            created=datetime.now()
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
