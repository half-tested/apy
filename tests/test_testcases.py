from pytest import mark

ddt = {
    'argnames': 'name,description',
    'argvalues': [('hello', 'world'),
                  ('hello', ''),
                  ('123', 'world')],
    'ids': ['general test', 'test with no description', 'test with digits in name']
}


@mark.parametrize(**ddt)
def test_new_testcases(desktop_app_auth, name, description, get_db):
    tests = get_db.list_test_cases()
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_tests_exists(name)
    assert len(tests) + 1 == len(get_db.list_test_cases())
    desktop_app_auth.test_cases.delete_test_by_name(name)


def test_testcase_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    assert not desktop_app_auth.test_cases.check_tests_exists('dffsjfjskdfh')
    assert False


def test_delete_test_case(desktop_app_auth, get_webservice):
    test_name = 'test for delete'
    get_webservice.create_test(test_name, 'delete me pls')
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_tests_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)
    assert not desktop_app_auth.test_cases.check_tests_exists(test_name)

# PWDEBUG=1
