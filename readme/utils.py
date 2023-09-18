def is_ting_pai(hand_tiles):
    # 统计每张牌的数量
    tile_count = [0] * 34
    for tile in hand_tiles:
        tile_count[tile] += 1

    # 遍历每一张牌，尝试判断是否能够打出这张牌后听牌
    for tile in range(34):
        if tile_count[tile] < 4:
            # 打出这张牌后，手牌数+1，再进行判断
            tile_count[tile] += 1
            if can_ting(tile_count):
                return True
            tile_count[tile] -= 1

    return False


def can_ting(tile_count):
    # 这里可以根据具体的规则和算法来判断是否听牌
    # 实现逻辑需要考虑牌型、顺子、刻子、对子、七对子等情况
    # 这里只是一个示例，具体实现需要根据你所使用的规则进行调整
    for tile in range(34):
        if tile_count[tile] >= 2:
            # 移除一对牌后，判断是否能够胡牌
            tile_count[tile] -= 2
            if can_hu(tile_count):
                return True
            tile_count[tile] += 2

    return False


def can_hu(tile_count):
    # 这里可以根据具体的规则和算法来判断是否胡牌
    # 实现逻辑需要考虑牌型、顺子、刻子、对子、七对子等情况
    # 这里只是一个示例，具体实现需要根据你所使用的规则进行调整
    # 假设这里判断手牌是否胡牌的逻辑是直接判断是否存在四个连续的牌
    for tile in range(34):
        if tile_count[tile] >= 4:
            return True

    return False


def can_form_sets(tile_count):
    # 递归终止条件：所有牌都被使用完
    if sum(tile_count) == 0:
        return True

    # 遍历所有索引
    for tile in range(34):
        # 判断是否可以组成刻子
        if tile_count[tile] >= 3:
            tile_count[tile] -= 3
            if can_form_sets(tile_count):
                return True
            tile_count[tile] += 3

        # 判断是否可以组成顺子
        if (
            tile < 27
            and tile_count[tile] > 0
            and tile_count[tile + 1] > 0
            and tile_count[tile + 2] > 0
        ):
            tile_count[tile] -= 1
            tile_count[tile + 1] -= 1
            tile_count[tile + 2] -= 1
            if can_form_sets(tile_count):
                return True
            tile_count[tile] += 1
            tile_count[tile + 1] += 1
            tile_count[tile + 2] += 1

    # 无法组成刻子或顺子
    return False
