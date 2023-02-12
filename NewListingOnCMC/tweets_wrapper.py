import textwrap

def tweets_wrapper(description, max_length, break_character = '.'):
	wrapper = textwrap.TextWrapper(width = max_length, break_long_words=False, break_on_hyphens=False)
	description_wrapped = wrapper.wrap(description)

	len_wrapped = len(description_wrapped)
	
	blocks = []

	for block in description_wrapped :
		current_block = block
		while len(current_block) > max_length:
			split_index = current_block.rfind(break_character, 0, max_length)
			if split_index == -1:
				split_index = max_length
			blocks.append(current_block[:split_index])
			current_block = current_block[split_index:]
		blocks.append(current_block)
	return blocks


# description = 'AIon Mars (AIONMARS) is a cryptocurrency launched in 2023and operates on the BNB Smart Chain (BEP20) platform. AIon Mars has a current supply of 27,000,000 with 0 in circulation. The last known price of AIon Mars is 0.01425909 USD and is down -8.56 over the last 24 hours. It is currently trading on 1 active market(s) with $2,827,693.23 traded over the last 24 hours. More information can be found at https://aionmars.finance/.'

# print(description_wrapper(description, 235)[0])
# print("\n")
# print(description_wrapper(description,235)[1])
