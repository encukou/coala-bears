from bears.coffee_script.CoffeeLintBear import CoffeeLintBear
from tests.LocalBearTestHelper import verify_local_bear

good_file = """
# Lint your CoffeeScript!

class Gangster

  wasItAGoodDay : () ->
    yes
"""


good_file_use_english_operator = """
1 or 1
1 and 1
1 isnt 1
1 is 1
"""


bad_file_use_english_operator = """
1 || 1
1 && 1
1 != 1
1 == 1
x = !y
"""


good_file_no_duplicate_keys = """
class SomeThing
  getConfig: ->
    @config =
      foo: 1
  @getConfig: ->
    config =
      foo: 1
"""


bad_file_no_duplicate_keys = """
class SomeThing
  getConfig: ->
    one = 1
    one = 5
    @config =
      keyA: one
      keyB: one
      keyA: 2
  getConfig: ->
    @config =
      foo: 1
  @getConfig: ->
    config =
      foo: 1"""


good_file_tab_width = """
# Lint your CoffeeScript!

class Gangster

    wasItAGoodDay : () ->
        yes
"""


good_file_allow_trailing_white_spaces = """
x = 1234
y = 1
"""


bad_file_allow_trailing_white_spaces = """
x = 1234      \ny = 1
"""


good_file_arrow_spacing = """
x(-> 3)
x( -> 3)
"""


bad_file_arrow_spacing = """
{x((a,b)-> 3)
"""


good_file_no_backticks = """
myFunction(a, b, c)
"""


bad_file_no_backticks = """
`myFunction a,b,c
"""


good_file_allow_trailing_semiColon = """
x = '1234'; console.log(x)
{spacing:true}
"""


bad_file_allow_trailing_semiColon = """
alert('end of line');
"""


good_file_no_empyty_functions_and_parameter_list = """
foo = (empty = (-> undefined)) -> undefined
{  a, b  }
{  }
foo = 'bar'
{  spacing : true  }
"""


bad_file_no_empyty_functions_and_parameter_list = """
-> =>
blah = () ->
y++
--x
{a, b}
{}
foo = "bar"
{spacing:true}
"""


good_file_disable_throwing_strings = """
x++;
x+=1
doSomething(foo = ',',bar)
myFunction a, b, {1:2, 3:4}
`with(document) alert(height);`
foo = "#{inter}foo#{polation}"
@::
"""


bad_file_disable_throwing_strings = """
throw 'my error'
throw "#{1234}"
throw '''
  long string
'''
foo = '#{inter}foo#{polation}'
myFunction a, b, 1:2, 3:4
"""


good_file_no_stand_alone_at_sign = """
@[ok]
@ok()
doSomething(foo = ',', bar)\nfooBar()
c = new Foo 1, 2
throw 'my error'
throw "#{1234}"
"""


bad_file_no_stand_alone_at_sign = """
@ notok
not(@).ok
@::
doSomething(foo = ',',bar)\nfooBar()
"""


good_file_no_this = """
class Y extends X
  constructor: ->
    @.hello
"""


bad_file_no_this = """
class Y extends X
  constructor: ->
    this.hello
"""


good_file_enforce_parentheses_on_constructors = """
g = new Foo(1, 2)
h = new Foo(
  config: 'parameter'
)
i = new bar.foo.Foo(1, 2)
j = new bar.foo.Foo(
  config: 'parameter'
)
myFunction a, b, 1:2, 3:4
foo = '#{bar}'
"""


bad_file_enforce_parentheses_on_constructors = """
c = new Foo 1, 2
d = new Foo
  config: 'parameter'
e = new bar.foo.Foo 1, 2
f = new bar.foo.Foo
  config: 'parameter'
"""


good_file_new_lines_after_classes = """
class Foo
  constructor: () ->
    bla()
  a: "b"
  c: "d"

class Bar extends Foo
  constructor: () ->
    bla()
"""


bad_file_new_lines_after_classes = """
class Foo
  constructor: () ->
      bla()
  a: "b"
  c: "d"
class Bar extends Foo
  constructor: () ->
    bla()
"""


bad_file_cyclomatic_complexity = """
x = () ->
  a = () ->
    1 or 2
"""


good_file_cyclomatic_complexity = """
x = () -> 1234
"""


warning_file = """
# Nested string interpolation
str = "Book by #{"#{firstName} #{lastName}".toUpperCase()}"
"""


error_file = """
# Wrong capitalization
class theGangster

  wasItAGoodDay : () ->
    yes
"""


invalid_file = """
# Coffeelint is buggy here and will generate an error with invalid CSV on this
var test
"""


CoffeeLintBearTest = verify_local_bear(CoffeeLintBear,
                                       valid_files=(good_file,),
                                       invalid_files=(warning_file,
                                                      error_file,
                                                      invalid_file))


CoffeeLintBearUseEnglishOperatorTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_use_english_operator,),
    invalid_files=(bad_file_use_english_operator,),
    settings={"use_english_operator": "true",
              "consistent_line_endings_style": "unix"})


CoffeeLintBearTabWidthTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_tab_width,),
    invalid_files=(good_file,),
    settings={"use_spaces": "false", "tab_width": 4})


CoffeeLintBearNoDuplicateKeysTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_no_duplicate_keys,),
    invalid_files=(bad_file_no_duplicate_keys,),
    settings={"prevent_duplicate_keys": "true",
              "enforce_newline_at_EOF": "true"})


CoffeeLintBearCamelCaseTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file,),
    invalid_files=(error_file,),
    settings={"class_naming_camelCase": "true"})


CoffeeLintBearAllowTrailingWhiteSpacesTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_allow_trailing_white_spaces,),
    invalid_files=(bad_file_allow_trailing_white_spaces,),
    settings={"allow_trailing_whitespaces": "false",
              "use_english_operator": "true",
              "spaces_around_operators": "true"})


CoffeLintBearArrowSpacingTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_arrow_spacing,),
    invalid_files=(bad_file_arrow_spacing,),
    settings={"space_before_and_after_arrow": "true"})


CoffeeLintBearNoBackticksTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_no_backticks,),
    invalid_files=(bad_file_no_backticks,),
    settings={"prohibit_embedding_javascript_snippet": "true",
              "space_after_comma": "true",
              "no_function_call_without_parentheses": "true"})


CoffeeLintBearAllowTrailingSemiColonTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_allow_trailing_semiColon,),
    invalid_files=(bad_file_allow_trailing_semiColon,),
    settings={"allow_trailing_semicolons": "false"})


CoffeeLintBearNoEmpytyFunctionsAndParameterListTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_no_empyty_functions_and_parameter_list,),
    invalid_files=(bad_file_no_empyty_functions_and_parameter_list,),
    settings={"no_empty_functions": "true",
              "no_empty_parameter_list": "true",
              "no_decr_or_incrementation_operators": "true",
              "check_braces_spacing": "true",
              "braces_spacing_width": 2,
              "spacing_in_empty_braces": 2,
              "no_unnecessary_double_quotes": "true",
              "spaces_before_and_after_colon": "true",
              "spaces_before_colon": 1,
              "no_implicit_parentheses": "true"})


CoffeeLintBearDisableThrowingStringsTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_disable_throwing_strings,),
    invalid_files=(bad_file_disable_throwing_strings,),
    settings={"disable_throwing_strings": "true",
              "allow_trailing_semicolons": "true",
              "allow_trailing_whitespaces": "true",
              "spaces_around_operators": "false",
              "space_after_comma": "false",
              "no_implicit_braces": "true",
              "no_implicit_parentheses": "false",
              "prohibit_embedding_javascript_snippet": "false",
              "no_interpolation_in_single_quotes": "true",
              "no_stand_alone_at_sign": "false"})


CoffeeLintBearNoStandAloneAtTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_no_stand_alone_at_sign, bad_file_no_duplicate_keys),
    invalid_files=(bad_file_no_stand_alone_at_sign,),
    settings={"no_stand_alone_at_sign": "true",
              "space_after_comma": "true",
              "enforce_parentheses_on_non_empty_constructors": "false",
              "prevent_duplicate_keys": "false",
              "disable_throwing_strings": "false"})


CoffeeLintBearNoThisTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_no_this,),
    invalid_files=(bad_file_no_this,),
    settings={"no_this": "true", "class_naming_camelCase": "false"})


CoffeeLintBearEnforceParenthesesOnConstructorsTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_enforce_parentheses_on_constructors,),
    invalid_files=(bad_file_enforce_parentheses_on_constructors,),
    settings={"enforce_parentheses_on_non_empty_constructors": "true",
              "no_function_call_without_parentheses": "false",
              "no_interpolation_in_single_quotes": "false"})


CoffeeLintBearNewLinesAfterClassesTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_new_lines_after_classes,),
    invalid_files=(bad_file_new_lines_after_classes,),
    settings={"number_of_newlines_after_classes": 1})


CoffeeLintBearCyclomaticComplexityTest = verify_local_bear(
    CoffeeLintBear,
    valid_files=(good_file_cyclomatic_complexity,),
    invalid_files=(bad_file_cyclomatic_complexity,),
    settings={"cyclomatic_complexity": 1})
