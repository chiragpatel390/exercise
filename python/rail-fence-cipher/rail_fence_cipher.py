from itertools import cycle, chain

def fence_pattern(rails, size):
	zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
	return zip(zig_zag, range(size))

def encode(message, rails):
	fence = fence_pattern(rails, len(message))
	return ''.join(message[i] for _, i in sorted(fence))


def decode(encoded_message, rails):
	fence = fence_pattern(rails, len(encoded_message))
	fence_encoded_message = zip(encoded_message, sorted(fence))
	return ''.join(char for char, _ in sorted(fence_encoded_message, key=lambda item: item[1][1]))
