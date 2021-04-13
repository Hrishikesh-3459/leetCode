class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans = 0
        i = 0
        while True:
            stu = students.pop(0)
            sand = sandwiches[0]
            if stu == sand:
                sandwiches.pop(0)
                i = 0
            else:
                students.append(stu)
                i += 1
                if i == 100:
                    break
            if not students or not sandwiches:
                return 0
        return len(students)
