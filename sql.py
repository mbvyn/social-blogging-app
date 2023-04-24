from hello import Role, User, db, app

app_ctx = app.app_context()
app_ctx.push()

db.drop_all()
db.create_all()

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='John', role=admin_role)
user_susan = User(username='Susan', role=user_role)
user_david = User(username='David', role=user_role)

db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])

db.session.commit()

print(user_john.id, user_john.username, user_john.role_id)

admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

db.session.delete(mod_role)
db.session.commit()


