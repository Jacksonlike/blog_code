import yaml


class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'

  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks

  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,      
       self.attacks)


monster1 = yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""", Loader=yaml.Loader)

monster2 = yaml.dump(Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT']))

print(type(monster1), monster1)
print(yaml.dump(monster2))
print(yaml.load(monster2, Loader=yaml.Loader))
