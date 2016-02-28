from behave import given, when, then


class BlackHole(object):
    pass


@given('we have {number:d} black holes')
def given_blackholes(context, number):
    context.response = tuple(BlackHole() for _ in range(number))
    context.collided = False


@given('a big L')
def given_big_l(context):
    context.has_l = True


@when('the holes collide')
def when_they_collide(context):
    context.collided = True


@then('we detect shockwaves')
def then_detect_shockwaves(context):
    assert getattr(context, "has_l", False) is True
    assert len(context.response) > 1
