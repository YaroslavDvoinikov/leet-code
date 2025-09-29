class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        s = 0
        for operation in operations:
            if operation == 'C':
                s -= records.pop()
            elif operation == 'D':
                records.append(records[-1]*2)
                s+= records[-1]
            elif operation == '+':
                records.append(records[-1]+records[-2])
                s+= records[-1]
            else:
                records.append(int(operation))
                s+= records[-1]
        return s 