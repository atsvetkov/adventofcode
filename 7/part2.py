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
            graph[outer_bag].append((int(number), kind, color))

# traverse the graph and find all nodes from which the target bag can be reached
target = ('shiny', 'gold')
total_bags = 0
nodes = [((number, kind, color)) for (number, kind, color) in graph[target]]
while nodes:
    number, kind, color = nodes.pop()
    total_bags += number
    for child_number, child_kind, child_color in graph[(kind, color)]:
        nodes.append((number*child_number, child_kind, child_color))

print(total_bags)
