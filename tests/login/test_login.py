import pytest


@pytest.mark.parametrize("email, password, result", [
    ("test@gmail.com", "qsa", False),
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
])
def test_user_login(user_login_fixture, email, password, result):
    if result is True:
        assert user_login_fixture.login_test(email, password)
        assert user_login_fixture.sidebar_test()
    else:
        assert not user_login_fixture.login_test(email, password) is False

