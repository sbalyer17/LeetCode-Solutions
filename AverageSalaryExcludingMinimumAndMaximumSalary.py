class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        minSalary = salary[0]
        maxSalary = 0
        sumSalary = 0
        
        for index in range(len(salary)):
            if salary[index] > maxSalary:
                maxSalary = salary[index]
            if salary[index] < minSalary:
                minSalary = salary[index]
            sumSalary += salary[index]
        
        return ((sumSalary - minSalary - maxSalary)*1.0)/(len(salary)-2)
