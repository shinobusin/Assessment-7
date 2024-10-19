# Knowledge Base
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

def traverse_tree(tree):
    # Traverse the decision tree interactively
    question = list(tree.keys())[0]
    print(question)
    answer = input("Enter Yes or No: ")
    
    if answer in tree[question]:
        if isinstance(tree[question][answer], dict):
            traverse_tree(tree[question][answer])
        else:
            print(tree[question][answer])
    else:
        print("Invalid response, please enter Yes or No")

# Start the decision tree traversal
if __name__ == "__main__":
    traverse_tree(K_Base)
