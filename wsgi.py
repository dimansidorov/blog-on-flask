import os

from blog.app import create_app, db
from blog.users.models import User

app = create_app()


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    username = input('Введите имя пользователя')
    email = input('Введите адрес электронной почты')
    admin = User(username=username, is_staff=True, email=email)
    admin.password = os.environ("ADMIN_PASSWORD") or 'adminpass'

    db.session.add(admin)
    db.session.commit()

    print(f'Суперпользователь {username} создан')


@app.cli.command("create-articles")
def create_articles():
    """
    Run in your terminal:
    flask create-articles
    > done! created articles >
    """
    from blog.articles.models import Article
    article_one = Article(title="Тайна Коко",
                          body='12-летний Мигель живёт в мексиканской деревушке в семье сапожников и тайно мечтает стать музыкантом. Когда-то его прапрадед оставил жену, прапрабабку Мигеля, ради мечты, которая теперь не даёт спокойно жить и его праправнуку. С тех пор музыкальная тема в семье стала табу.',
                          creator_id=1)
    article_two = Article(title="Криминальное чтиво",
                          body='Двое бандитов Винсент Вега и Джулс Винфилд ведут философские беседы в перерывах между разборками и решением проблем с должниками криминального босса Марселласа Уоллеса.',
                          creator_id=1)
    db.session.add(article_one)
    db.session.add(article_two)
    db.session.commit()
    print(f"done! created users: {article_one}, {article_two}")


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            debug=True, )
