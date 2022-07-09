from core.game import Character, Effect, UsageType
from core.game import AttackType


class Alice(Character):
    def __init__(self):
        super(Alice, self).__init__('Alice',
                                    movement_length=2,
                                    attack_type=AttackType.melee,
                                    minions=[Character('Cat', movement_length=2, attack_type=AttackType.melee)])
        self.height = True

    def set_height(self, height: bool):
        self.height = height
