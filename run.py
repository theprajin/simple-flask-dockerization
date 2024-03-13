from app import app, db
from app.routes.user import (
    create_user,
    get_all_users,
    get_one_user,
    update_user,
    delete_user,
)

# User's CRUD API
create_user
get_all_users
get_one_user
update_user
delete_user


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
