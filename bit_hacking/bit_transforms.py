
def set_bit(num, bit_index):
	"""
	Sets bit at bit_index to 1
	"""
	return (num << bit_index) | num if bit_index > 0 and bit_index < 8 else num


if __name__ == "__main__":
  bit = set_bit(2, 8)
  print(bit)
  print(bin(bit))

