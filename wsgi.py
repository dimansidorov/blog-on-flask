from blog.app import create_app, db

app = create_app()


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.users.models import User
    admin = User(username="admin", is_staff=True, email='admin@admin.ad')
    james = User(username="james", email='james@james.js')
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print(f"done! created users: {admin}, {james}")


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
