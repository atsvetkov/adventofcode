# build the graph with bag connections
graph = {}
for line in open('input.txt'):
    parts = line.strip().split('bags contain')
    outer_bag_parts = parts[0].strip().split()
    outer_bag = (outer_bag_parts[0], outer_bag_parts[1])
    inner_bags_part = parts[1]
    inner_bags_part = inner_bags_part.strip()
    graph[outer_bag] = []
    if inner_bags_part != 'no other bags.':
        for inner_bag in inner_bags_part.split(', '):
            number, kind, color = inner_bag.strip(
                '.').strip('bag').strip('bags').strip().split()
            graph[outer_bag].append((kind, color))

# traverse the graph and find all nodes from which the target bag can be reached
target = ('shiny', 'gold')
nodes = [(bag, []) for bag in graph.keys()]
reachable_from = set()
for bag in graph.keys():
    if bag == target:
        continue
    kind, color = bag
    visited = set()
    nodes = [bag]
    while nodes:
        node = nodes.pop()
        if node == target:
            reachable_from.add(bag)
            break
        else:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    nodes.append(child)

print('target can be reached from', len(reachable_from), 'colors')
