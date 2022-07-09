from core.game import Effect, Character, UsageType, EffectType


class ClawsThatCatch(Effect):
    def __init__(self):
        super(ClawsThatCatch, self).__init__(usage_type=UsageType.during,
                                             effect_type=EffectType.attack,
                                             power=3,
                                             strengthening=2,
                                             description='if the opposing fighter is a hero, this card\'s value is 5 instead.')

    @staticmethod
    def effect(opposing_fighter: Character):
        if opposing_fighter.hero:
            opposing_fighter.hp -= 5
        else:
            opposing_fighter.hp -= 3


class MomentousShift(Effect):
    def __init__(self):
        super(MomentousShift, self).__init__(usage_type=UsageType.during,
                                             effect_type=EffectType.protection_attack,
                                             power=3,
                                             strengthening=1,
                                             description='If your fighter started this turn in a different space, this card\'s value is 5 instead.')

    @staticmethod
    def effect(opposing_fighter: Character):
        ...
