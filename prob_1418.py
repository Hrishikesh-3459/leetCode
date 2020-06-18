import copy
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_nums = {}
        foods = set()
        for i in orders:
            if int(i[1]) in table_nums:
                table_nums[int(i[1])].append(i[2])
            else:
                table_nums[int(i[1])] = [i[2]]
            foods.add(i[2])
        sorted_foods = sorted(list(foods))
        ans = [['Table']]
        ans[0].extend(sorted_foods)
        for i in sorted(table_nums):
            tmp = [str(i)]
            for food in ans[0][1:]:
                if food in table_nums[i]:
                    tmp.append(str(table_nums[i].count(food)))
                else:
                    tmp.append("0")
            t = copy.copy(tmp)
            ans.append(t)
            tmp.clear()
        return ans
                    
