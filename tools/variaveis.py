def token():
    return 'OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o'


def changeUser(id):
    nome_lista = [('270928429925269518', 'LK'),
                  ('268198611941195776', 'Rafão'),
                  ('107332797332508672', 'Dashtail'),
                  ('109427358162817024', 'Pseudão'),
                  ('112262967101255680', 'Luorhane'),
                  ('115948020360675329', 'Itala'),
                  ('192460714512744448', 'Matiserguei'),
                  ('112964615335321600', 'Peterola'),
                  ('114546184193835011', 'Paithias'),
                  ('115948643722330119', 'Gijas'),
                  ('209833913336463362', 'Aloens'),
                  ('114551380584169476', 'Juanas'),
                  ('204707355105951744', 'Maquisuel Daoboga'),
                  ('142751595258445825', 'Devedero'),
                  ('107295051910000640', 'Ganancioso'),
                  ('448541039133982730', 'Gui o homem')]

    dicio = dict(nome_lista)
    return dicio.get(id)