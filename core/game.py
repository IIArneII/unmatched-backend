from uuid import uuid4
from enum import Enum


class EffectType(Enum):
    protection = 'protection'
    attack = 'attack'
    protection_attack = 'protection_attack'
    trick = 'trick'


class AttackType(Enum):
    melee = False
    ranged = True


class UsageType(Enum):
    before = 'before'
    during = 'during'
    after = 'after'


class NodeColor(Enum):
    red = 'red'
    blue = 'blue'
    green = 'green'


class CharacterName(Enum):
    alice = 'Alice'
    jabberwock = 'Jabberwock'


class Node:
    def __init__(self, key, color: list = None, connections: list = None):
        self.key = key
        self.character = None
        self.color = color if color else [NodeColor.red]
        self.connections = {} if not connections else {i.id: i for i in connections}

    def add(self, node):
        if self.key not in node.connections:
            node.connections[self.key] = self
        self.connections[node.key] = node

    def __repr__(self):
        return f'Node(key=\'{str(self.key)}\', color={self.color}, connections={str(self.connections.keys())})'


class Map:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, color: list = None):
        if key not in self.nodes:
            node = Node(key, color)
            self.nodes[key] = node
            return node

    def add_connection(self, key1, key2):
        if key1 not in self.nodes:
            self.add_node(key1)
        if key2 not in self.nodes:
            self.add_node(key2)
        self.nodes[key1].add(self.nodes[key2])

    def __iter__(self):
        return iter(self.nodes.values())


class Effect:
    def __init__(self, usage_type: UsageType = UsageType.during,
                 effect_type: EffectType = EffectType.attack,
                 power: int = 0,
                 strengthening: int = 0,
                 description: str = ''):
        self.type = effect_type,
        self.power = power
        self.strengthening = strengthening
        self.usage_type = usage_type
        self.description = description


class Card:
    def __init__(self, effect: Effect, character: CharacterName = None):
        self.character = character
        self.effect = effect


class Character:
    def __init__(self, name: str = '',
                 position: Node = None,
                 movement_length: int = 0,
                 attack_type: AttackType = AttackType.melee,
                 minions: list = None,
                 hero: bool = True,
                 hp: int = 12):
        self.hp = hp
        self.name = name
        self.position = position
        self.movement_length = movement_length
        self.attack_type = attack_type
        self.minions = minions if minions else []
        self.hero = hero


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
        self.id = _id if _id else str(uuid4())
        self.map = _map if _map else Map()
        self.players = []

    def check_player_name(self, name: str):
        return name not in [p.name for p in self.players]

    def add_player(self, player: Player):
        if self.check_player_name(player.name):
            self.players.append(Player)
