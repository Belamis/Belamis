import re

import pytest

from app import create_app


@pytest.fixture
def app(tmp_path):
    return create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.sqlite"), "SECRET_KEY": "test",
                       "ADMIN_INITIAL_PASSWORD": "admin"})


@pytest.fixture
def client(app):
    return app.test_client()


class Session:
    """Client connecté avec gestion automatique du jeton CSRF."""

    def __init__(self, client):
        self.client = client
        self.token = None

    def _csrf(self):
        if self.token is None:
            page = self.client.get("/login").get_data(as_text=True)
            self.token = re.search(r'name="_csrf" value="([^"]+)"', page).group(1)
        return self.token

    def login(self, login="admin", mdp="admin"):
        r = self.client.post("/login", data={"login": login, "mot_de_passe": mdp, "_csrf": self._csrf()})
        self.token = None  # la session est régénérée à la connexion : nouveau jeton
        return r

    def get(self, url, **kw):
        return self.client.get(url, **kw)

    def post(self, url, data=None, **kw):
        data = dict(data or {})
        data["_csrf"] = self._csrf()
        return self.client.post(url, data=data, **kw)


@pytest.fixture
def admin(client):
    s = Session(client)
    r = s.login()
    assert r.status_code == 302
    return s
