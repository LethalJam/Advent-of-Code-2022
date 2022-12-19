import copy
import parser_util


class Blueprint:
    def __init__(self) -> None:
        self.id = 0
        self.ore_rb_ore = 0
        self.clay_rb_ore = 0
        self.obsid_rb_ore_cly = (0, 0)
        self.geo_rb_ore_obsid = (0, 0)

    def __str__(self) -> str:
        return f"ID:{self.id}\n* Ore Rb:{self.ore_rb_ore}\n* Clay Rb:{self.clay_rb_ore}\n* Obsid Rb:{self.obsid_rb_ore_cly}\n* Geo Rb:{self.geo_rb_ore_obsid}"


class FactState:
    def __init__(self, oreRbs, clayRbs, obsidRbs, geoRbs, ore, clay, obsid, geo) -> None:
        self.oreRbs = oreRbs
        self.clayRbs = clayRbs
        self.obsidRbs = obsidRbs
        self.geoRbs = geoRbs

        self.ore = ore
        self.clay = clay
        self.obsid = obsid
        self.geo = geo
        self.childs = []


def parse_blueprints(inp):
    blueprints = list()
    for i in inp:
        blp = Blueprint()
        idSpl = i.split(":")
        costStrs = idSpl[1].split(".")
        blp.id = int(idSpl[0].split("Blueprint")[1])

        blp.ore_rb_ore = int(costStrs[0].split(" ")[5])
        blp.clay_rb_ore = int(costStrs[1].split(" ")[5])
        blp.obsid_rb_ore_cly = (int(costStrs[2].split(
            " ")[5]), int(costStrs[2].split(" ")[8]))
        blp.geo_rb_ore_obsid = (int(costStrs[3].split(
            " ")[5]), int(costStrs[3].split(" ")[8]))
        blueprints.append(blp)
    return blueprints


def build_state_tree(blp: Blueprint, state: FactState, iter):

    branches = list()

    noBuildState = copy.deepcopy(state)
    noBuildState.childs = []
    branches.append(noBuildState)

    if state.ore >= blp.ore_rb_ore:
        newState = copy.deepcopy(state)
        newState.ore -= blp.ore_rb_ore
        newState.oreRbs += 1
        newState.childs = []
        branches.append(newState)

    if state.ore >= blp.clay_rb_ore:
        newState = copy.deepcopy(state)
        newState.ore -= blp.clay_rb_ore
        newState.clayRbs += 1
        newState.childs = []
        branches.append(newState)

    if state.ore >= blp.obsid_rb_ore_cly[0] and state.clay >= blp.obsid_rb_ore_cly[1]:
        newState = copy.deepcopy(state)
        newState.ore -= blp.obsid_rb_ore_cly[0]
        newState.clay -= blp.obsid_rb_ore_cly[1]
        newState.obsidRbs += 1
        newState.childs = []
        branches.append(newState)

    if state.ore >= blp.geo_rb_ore_obsid[0] and state.obsid >= blp.geo_rb_ore_obsid[1]:
        newState = copy.deepcopy(state)
        newState.ore -= blp.geo_rb_ore_obsid[0]
        newState.obsid -= blp.geo_rb_ore_obsid[1]
        newState.geoRbs += 1
        newState.childs = []
        branches.append(newState)

    for nState in branches:
        nState.ore += state.oreRbs
        nState.clay += state.clayRbs
        nState.obsid += state.obsidRbs
        nState.geo += state.geoRbs

    print(iter)
    if iter == 24:
        return
    else:
        for b in branches:
            print("Geodes: ", b.geo)
            build_state_tree(blp, b, iter+1)
    state.childs = branches


def simulate_blueprint(blp: Blueprint):

    rootState = FactState(1, 0, 0, 0, 0, 0, 0, 0)
    build_state_tree(blp, rootState, 1)
    # DO BFS HERE ON STATE TREE
    xpl = [rootState]
    q = [rootState]
    maxQuality = 0

    while len(q) > 0:
        c = q.pop(0)
        nL = c.childs
        maxQuality = c.geo * blp.id

        for n in nL:
            if n not in xpl:
                xpl.append(n)
                q.append(n)

    return maxQuality


inp = parser_util.readList("inputs/19.txt", "string", True, False)

blueprints = parse_blueprints(inp)

qLevels = 0
for blp in blueprints:
    qLevels += simulate_blueprint(blp)
print(qLevels)
