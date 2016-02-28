from behave import given, when, then


@given('{name} is logged in')
def given_logged_in(context, name):
    context.loggedin = True
    context.mails = {name: "old"}


@when('{name} changes her email to {newmail}')
def when_user_changes_mail(context, name, newmail):
    assert getattr(context, "loggedin", False)
    context.mails[name] = newmail


@then('in her user profile {name} sees {expected} as her email')
def then_user_profile_shows(context, name, expected):
    assert getattr(context, "loggedin", False)
    assert context.mails[name] == expected
