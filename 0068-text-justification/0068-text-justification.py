class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

		if len(words) == 1:
			return [words[0] + ' ' * (maxWidth - len(words[0]))]

		ans = []
		cur_strs = []
		cur_strlen = 0
		for word in words:
			if cur_strlen == 0:
				cur_strs.append(word)
				cur_strlen += len(word)

			elif cur_strlen + len(word) + 1 <= maxWidth:
				cur_strs.append(word)
				cur_strlen += len(word) + 1

			else: 
				spaces = maxWidth - cur_strlen + len(cur_strs) - 1

				if len(cur_strs) == 1:
					ans.append(cur_strs[0] + ' ' * (maxWidth-cur_strlen))
				elif spaces % (len(cur_strs) - 1) == 0:
					aver_space = spaces // (len(cur_strs) - 1)
					ans.append((' '*aver_space).join(cur_strs))
				else:
					aver_space = spaces // (len(cur_strs) - 1)
					extra_spaces = spaces % (len(cur_strs) - 1)
					ans.append((' '*(aver_space+1)).join(cur_strs[:extra_spaces+1]) + 
								' '*aver_space + 
							   (' '*aver_space).join(cur_strs[extra_spaces+1:]))

				cur_strs = []
				cur_strlen = 0
				cur_strs.append(word)
				cur_strlen += len(word)

		ans.append(' '.join(cur_strs) + ' ' * (maxWidth-cur_strlen))

		return ans