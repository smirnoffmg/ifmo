from heapq import heappush, heappop, heapify
from collections import Counter


def huffman_encode(raw_message: str):
    freqs = Counter(raw_message)
    heap = [[weight, [sym, ""]] for sym, weight in freqs.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    tree = dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    encoded_message = "".join([tree[s] for s in raw_message])
    return tree, encoded_message


def huffman_decode(tree: dict, encoded_message: str):
    decoded = encoded_message
    for symb, code in sorted(tree.items(), key=lambda x: x[1]):
        decoded = decoded.replace(code, symb)
    return decoded
