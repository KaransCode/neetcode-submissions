class Solution:
    def countSeniors(self, details: List[str]) -> int:
        oldPerson = 0
        for detail in details:
            age = detail[-4:-2]
            if int(age) > 60:
                oldPerson += 1
        return oldPerson