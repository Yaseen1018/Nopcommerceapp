pytest -s -v -m "sanity" --html=./Reports/sanity.html TestCases/ --browser chrome
pytest -s -v -m "regression" --html=./Reports/sanity.html TestCases/ --browser chrome


rem pytest -s -v --html=Reports\report6.html TestCases/test_login_ddd.py --browser chrome


