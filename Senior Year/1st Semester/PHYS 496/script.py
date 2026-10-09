import random

# Topic dictionary
topic_dict = {
    "classical mechanics": 0,
    "EM": 1,
    "Quantum": 2,
    "Atomic": 3,
    "Special": 4,
    "Thermo": 5,
    "Optics": 6,
    "Lab": 7,
    "Specialized topics": 8
}

# Reverse dictionary: ID -> topic
id_to_topic = {value: key for key, value in topic_dict.items()}


def distribute_topics(topics, m, k):
    """
    Randomly distributes topics across m slots, guaranteeing
    that every slot contains at least k topics.

    Returns the topic names rather than their numerical IDs.
    """

    n = len(topics)

    if n < m * k:
        raise ValueError(
            f"Need at least {m * k} topics, but only have {n}."
        )

    # Convert topics to IDs
    topic_ids = [topic_dict[topic] for topic in topics]

    # Randomize
    random.shuffle(topic_ids)

    # Give each slot k values
    slots = [
        topic_ids[i * k:(i + 1) * k]
        for i in range(m)
    ]

    # Randomly distribute remaining values
    for topic_id in topic_ids[m * k:]:
        slot = random.randrange(m)
        slots[slot].append(topic_id)

    # Convert IDs back to topic names
    slots = [
        [id_to_topic[topic_id] for topic_id in slot]
        for slot in slots
    ]

    return slots


# Example
topics = [
    "classical mechanics",
    "EM",
    "Quantum",
    "Atomic",
    "Special",
    "Thermo",
    "Optics",
    "Lab",
    "Specialized topics",
]

m = 4
k = 2

slots = distribute_topics(topics, m, k)

for i, slot in enumerate(slots):
    print(f"Slot {i}:")
    for topic in slot:
        print(f"    {topic}")