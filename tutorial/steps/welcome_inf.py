import time

from behave import given, when, then, use_step_matcher, step

use_step_matcher("re")

pause = 1


@given("I am on the welcome page")
def step_impl(context):
    context.browser.get('http://localhost:' + str(context.port) + '/welcome.html')
    time.sleep(pause)


@when("I click on book recomendation")
def step_impl(context):
    context.browser.find_element_by_id('book_recomendation').click()
   

@then("A new popup is open")
def step_impl(context):
    assert context.browser.find_element_by_id('exampleModalLabel')
    
