def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s recibido: %s se esperaba: %s' % (prefix, repr(got), repr(expected))