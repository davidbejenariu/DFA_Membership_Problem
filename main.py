# lab1

with open("input_file.in", "r") as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    lines[i] = lines[i].replace("\t", "")
    lines[i] = lines[i].replace(",", "")

i = 0
sigma = set()
states = set()
finalStates = set()
transitions = dict()

while i < len(lines):
    if lines[i][0] != '#':
        if lines[i] == "Sigma:":
            i += 1

            while lines[i] != 'End':
                sigma.add(lines[i])
                i += 1
        elif lines[i] == "States:":
            i += 1

            while lines[i] != "End":
                temp = lines[i].split()
                states.add(temp[0])

                if len(temp) > 1:
                    if temp[1] == "S":
                        startState = temp[0]
                    else:
                        finalStates.add(temp[0])

                i += 1
        elif lines[i] == "Transitions:":
            i += 1

            while lines[i] != 'End':
                transition = lines[i].split()
                stateX, wordY, stateZ = transition[0], transition[1], transition[2]
                key = (stateX, wordY)

                if stateX in states and wordY in sigma and stateZ in states:
                    transitions[key] = stateZ
                else:
                    if stateX not in states:
                        print("Error! State", stateX, "does not exist.")
                    if stateZ not in states:
                        print("Error! State", stateZ, "does not exist.")
                    if wordY not in sigma:
                        print("Error! Word", wordY, "does not exist.")

                i += 1
    i += 1

from pprint import pprint

print("Sigma =", sigma)
print("States =", end=" ")
pprint(states)
print("The starting state is:", startState)

print("The final state(s) are:", end=" ")

for finalState in finalStates:
    print(finalState, end=" ")

print()
print("The transitions are:")
pprint(transitions)


# lab2

from dataclasses import dataclass


@dataclass()
class DFA:
    Sigma: set
    States: set
    StartState: str
    FinalStates: set
    Transitions: dict


dfa = DFA(sigma, states, startState, finalStates, transitions)
word = input("Give a string to check: ")

index = 0
currentState = dfa.StartState

while index < len(word):
    if (currentState, word[index]) not in dfa.Transitions:
        print("Rejected")
        currentState = -1
        break
    else:
        currentState = dfa.Transitions[(currentState, word[index])]
        index += 1

if currentState in dfa.FinalStates:
    print("Accepted")
else:
    print("Rejected")