import re
from src.util import read_input, result_print

def solve(day_num, input_file_name):
    monkey_list = construct_monkey_list(input_file_name)
    monkey_business_level = get_level_of_monkey_business(monkey_list)
    monkey_list = construct_monkey_list(input_file_name)
    worrisome_monkey_business_level = get_worrisome_level_of_monkey_business(monkey_list)
    result_print(
        day_num,
        "Monkey business level after 20 rounds of stuff-slinging simian shenanigans (product of inspected items of two busiest monkeys)",
        monkey_business_level,
        "Monkey business level after 10000 rounds of worrisome stuff-slinging simian shenanigans (product of inspected items of two busiest monkeys)",
        worrisome_monkey_business_level
    )

def construct_monkey_list(f_name):
    input_str_lst = read_input(f_name)
    monkeys = []
    info = []
    line = input_str_lst.pop(0).strip()
    while True:
        if line == '' or line == None:
            id = int(re.match("^Monkey (.+):$", info[0]).groups()[0])
            name = re.match("^(.+):$", info[0]).groups()[0]
            start_items = [ int(item) for item in re.match("^Starting items: (.+)$", info[1]).groups()[0].replace(' ', '').split(',') ]
            inspec_operation = eval(f"lambda old:{re.match('^Operation: new = (.+)$', info[2]).groups()[0]}")
            worry_recovery = lambda x: int(x/3)
            worry_test = eval(f"lambda x: (x % {re.match('^Test: divisible by (.+)$', info[3]).groups()[0]}) == 0")
            true_throw_target = int(re.match("^If true: throw to monkey (.+)$", info[4]).groups()[0])
            false_throw_target = int(re.match("^If false: throw to monkey (.+)$", info[5]).groups()[0])
            monkeys.append(Monkey(id, name, start_items, inspec_operation, worry_recovery, worry_test, true_throw_target, false_throw_target))
            info = []
            if line == None:
                break
        else:
            info.append(line)
        if input_str_lst:
            line = input_str_lst.pop(0).strip()
        else:
            line = None
    
    monkeys.sort(key=lambda m: m.id)

    for monkey in monkeys:
        monkey.true_target = monkeys[monkey.true_target]
        monkey.false_target = monkeys[monkey.false_target]

    return monkeys

class Monkey:
    def __init__(self, id, name, start_items, inspect_operation, worry_recovery, worry_test, true_throw_target, false_throw_target):
        self.id = id
        self.name = name
        self.items = start_items
        self.inspect_func = inspect_operation
        self.worry_recovery_func = worry_recovery
        self.worry_test_func = worry_test
        self.true_target = true_throw_target
        self.false_target = false_throw_target
        self.inspected_items = 0

    def turn(self, worry_recovery=True):
        while self.items:
            item = self.items.pop(0)
            worry = self.inspect_func(item)
            self.inspected_items += 1
            if worry_recovery:
                worry = self.worry_recovery_func(worry)
            if self.worry_test_func(worry):
                self.throw(worry, self.true_target)
            else:
                self.throw(worry, self.false_target)

    def throw(self, item, target_monkey):
        target_monkey.items.append(item)

    def __str__(self):
        return f"('{self.name}' ({self.id}) {self.items.__str__()})"



def get_level_of_monkey_business(monkeys):
    rounds = 20
    for round in range(1, rounds+1):
        for monkey in monkeys:
            monkey.turn(worry_recovery=True)

    inspections = sorted([ m.inspected_items for m in monkeys ], reverse=True)
    return inspections[0] * inspections[1]

def get_worrisome_level_of_monkey_business(monkeys):
    print("This function takes way too long since the worry numbers are being increasingly large")
    return None
    rounds = 10000
    for round in range(1, rounds+1):
        print(f"\r{round}/{rounds}", end='')
        for monkey in monkeys:
            monkey.turn(worry_recovery=False)
    print()

    inspections = sorted([ m.inspected_items for m in monkeys ], reverse=True)
    return inspections[0] * inspections[1]