from uuid import uuid4
from enum import Enum


class CardType(Enum):
    protection = 'protection'
    attack = 'attack'
    protection_attack = 'protection_attack'
    trick = 'trick'


class AttackType(Enum):
    melee = False
    ranged = True


class EffectType(Enum):
    before = 'before'
    during = 'during'
    after = 'after'


class Node:
    def __init__(self): ...


class Map:
    def __init__(self): ...


class Effect:
    def __init__(self, effect_type: EffectType = EffectType.during, description: str = ''):
        self.effect_type = effect_type
        self.description = description


class Card:
    def __init__(self, card_type: CardType = CardType.attack,
                 power: int = 0,
                 strengthening: int = 0,
                 effect: Effect = None):
        self._type = card_type,
        self.power = power
        self.strengthening = strengthening
        self.effect = effect if effect else Effect()


class Character:
    def __init__(self, name: str = '',
                 position: Node = None,
                 movement_length: int = 0,
                 attack_type: AttackType = AttackType.melee,
                 minions: list = None):
        self.name = name
        self.position = position
        self.movement_length = movement_length
        self.attack_type = attack_type
        self.minions = minions if minions else []

    def add_minion(self, minion):
        self.minions.append(minion)


class Player:
    def __init__(self, name: str,
                 character: Character = None):
        self.name = name
        self.character = character if character else Character()
        self.cards = []
        self.cards_in_hand = []
        self.discard = []


class Game:
    def __init__(self, _map=None, _id: str = None):
        self._id = _id if _id else str(uuid4())
        self._map = _map if _map else Map()
        self.players = []

    def check_player_name(self, name: str):
        return name not in [p.name for p in self.players]

    def add_player(self, player: Player):
        if self.check_player_name(player.name):
            self.players.append(Player)
