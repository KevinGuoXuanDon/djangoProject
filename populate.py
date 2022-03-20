import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'djangoProject.settings')

django.setup()
from forum.models import *
import _sqlite3
from django.utils import timezone as datetime
import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
letters = string.ascii_letters


def getWords(number=80):
    word = ""
    while len(word) != number:
        word += random.choice(lowercase_letters)
    return word


def populate():
    conn = _sqlite3.connect("../db.sqlite3")
    cursor = conn.cursor()
    del2 = "delete from forum_userprofile;"
    del1 = "delete from auth_user;"
    del3 = "delete from forum_module"
    del4 = "delete from forum_post"
    cursor.execute(del2)
    cursor.execute(del1)
    cursor.execute(del3)
    cursor.execute(del4)
    conn.commit()
    conn.close()
    try:
        user1 = User.objects.create(username="admin2", password="admin", is_staff=1, is_superuser=1)
        UserProfile.objects.create(user=user1, name="admin3")
    except:
        pass
    try:
        hot_posts = add_module("hot posts")
        sale = add_module("sale of used item")
        f = add_module("flats to rent")
        a = add_module("activity")
        u = add_module("university")
        c = add_module("coffee break")
        new_user = User.objects.create(username="Hrishikesh", password="")
        author1 = UserProfile.objects.create(user=new_user, name="Hrishikesh Barua")
        title1 = "Software Supply Chain Security Project in-toto Accepted into CNCF Incubator"
        content1 = "The CNCF Technical Oversight Committee (TOC) has accepted the in-toto project as a CNCF incubating project. The in-toto project aims to cryptographically protect the entire software build and delivery process - the supply chain - from malicious actors.The in-toto project is a framework that cryptographically ensures the integrity of the software supply chain. The framework's core architecture is based on 3 design principles - resilience to being compromised, ensuring end-to-end presence in the chain, and being expressive enough to be adopted anywhere. Since joining the CNCF sandbox in 2019, in-toto has released version 1.0 in 2020 and focused on achieving stability, support for SPIFFE, more expressive evidence collection, and implementations in different languages. It has also seen adoption in production in various organizations.There are multiple steps (which in-toto refers to as the supply chain) in the build and release process for any software artifact. If an attacker gains access to any of the steps they can control the output of the step. Instead of securing the steps in the chain, in-toto's goal is to cryptographically verify the chain itself. This is noteworthy as each step can involve a different piece of infrastructure or software with different attack surfaces. According to a recent report, software supply chain attacks tripled in 2021 compared to 2020.The CNCF's Security Technical Advisory Group (TAG) laid out the 4 principles to create a secure software supply chain in a paper last year. These are establishing and verifying trust at every step, automation, clarity of scope in each step in the chain and of the role of each actor, and mutual authentication. As the TAG note in their paper, in-toto includes a verification workflow that analyzes the links to ensure that they meet the constraints set in the layout.Santiago Torres-Arias - one of the original authors of in-toto - in his USENIX Security 2019 talk elaborated on the design principles behind the in-toto project. The first principle - resilience to being compromised - is achieved by separation of roles and keeping revocation and key rotation as first class primitives. The second design principle of in-toto is to be an all-encompassing tool that covers the entire pipeline from the moment the first line of code is committed to the time that the end user installs or uses the software. This is achieved by being as tool-agnostic as possible, and thus aiming for seamless integration with the pipeline. The third design principle is to be expressive enough to be adopted everywhere.The architecture of in-toto is based on being able to verifiably define both the software supply chain steps and the authorized actors who can make it happen. It provides a tight binding of the artifacts as they flow through the chain. in-toto uses a DSL that has layouts which defines the actors, the public keys, and artifact rules which describe how the artifacts relate to the steps in the supply chain. The entire workflow is usually signed by a project owner - who can be a security team or an individual, depending on the project’s governance. in-toto assumes that an attacker can compromise core infra like source code repos, CI/CD systems, container orchestrators, inter-server communication channels and developer keys. It provides for graceful degradation of security in such circumstances.The in-toto project has been adopted by many organizations in production including Datadog, kubesec, SolarWinds and rebuilderd. The project is hosted on GitHub."
        Post.posts.create(title=title1, content=content1, poster=author1, create_time="2022-3-19",
                          parent_module=hot_posts)
        title2 = "Cloud Spanner Introduces Committed Use Discounts"
        content2 = "Once you make a commitment to spend a certain amount on an hourly basis on Spanner from a billing account, you can get discounts on instances in different instance configurations, regions, and projects associated with that billing account. Both regional and multi-region instances can utilize the same spend commitment. (...) If for business reasons you need to migrate your application from single region to multi-region in future, you can do so with the same commitment while continuing to enjoy the discounts."
        Post.posts.create(title=title2, content=content2, poster=author1, create_time="2022-3-19",
                          parent_module=hot_posts)

        new_user2 = User.objects.create(username="Kevin", password="kkk")
        author2 = UserProfile.objects.create(user=new_user2, name="Kevin")
        Post.posts.create(title="goods for sale!",
                          content="Tra train tickets in the UK are 30 percent off, after the first ticket, and Germany DB30 percent off. Worldwide, 60% off for BOOKING hotels, 60% off for game recharge, 60% off for tickets of major scenic spots",
                          poster=author2, create_time="2022-3-18", parent_module=sale)

        for i in range(10):
            try:
                name = getWords()
                temp_user = User.objects.create(username=name, password="")
                uAuthor = UserProfile.objects.create(user=temp_user, name=name)
                Post.posts.create(title=(str(i * random.randint(10, 98)) + "th tittle"), content=getWords(),
                                  poster=uAuthor, create_time="2022-3-18",
                                  parent_module=sale)
                Post.posts.create(title=(str(i * random.randint(10, 98)) + "th tittle"), content=getWords(),
                                  poster=uAuthor, create_time="2022-3-18",
                                  parent_module=f)
                Post.posts.create(title=(str(i * random.randint(10, 98)) + "th tittle"), content=getWords(),
                                  poster=uAuthor, create_time="2022-3-18",
                                  parent_module=a)
                Post.posts.create(title=(str(i * random.randint(10, 98)) + "th tittle"), content=getWords(),
                                  poster=uAuthor, create_time="2022-3-18",
                                  parent_module=u)
                Post.posts.create(title=(str(i * random.randint(10, 98)) + "th tittle"), content=getWords(),
                                  poster=uAuthor, create_time="2022-3-18",
                                  parent_module=c)
            except:
                pass
    except:
        pass


def add_module(name):
    c = Module.objects.create(name=name, create_time=datetime.now(), slug=name)
    return c


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print("done")
