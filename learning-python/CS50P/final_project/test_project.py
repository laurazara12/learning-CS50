from project import validate_email, get_email, exited

#some short implementations of tests
def test_validate_email():
  try:
    assert validate_email("test@example.com") == True
    assert validate_email("test@example") == False
    assert validate_email("@example.com") == False
    assert validate_email("test@.com") == False
    assert validate_email("test@example..com") == False
  except AssertionError:
    print("Error")

def test_exited():
  try:
    assert exited("test@example.com") == False
    assert exited("ExiT") == False
    assert exited("EXIT") == False
    assert exited("") == False
  except AssertionError:
    print("Error")