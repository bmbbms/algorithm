class QuickSort:
    unsort_list = []

    def __init__(self, unsort_list):
        self.unsort_list = unsort_list

    def sort(self):
        return self.quick_sort(self.unsort_list, 0, len(self.unsort_list) - 1)

    def quick_sort(self, unsort_list, left, right):
        if left < right:
            partitionIndex = QuickSort.partition(unsort_list, left, right)
            self.quick_sort(unsort_list, left, partitionIndex - 1)
            self.quick_sort(unsort_list, partitionIndex + 1, right)

        return unsort_list

    @staticmethod
    def partition(unsort_list, left, right):

        pivot = left
        index = pivot + 1
        for i in range(index, right + 1):
            if unsort_list[i] < unsort_list[pivot]:
                unsort_list[i], unsort_list[index] = unsort_list[index], unsort_list[i]
                index += 1

        unsort_list[pivot], unsort_list[index - 1] = unsort_list[index - 1], unsort_list[pivot]
        return index - 1


if __name__ == "__main__":
    a = QuickSort([7,5,8,4,3,8,9])
    print(a.sort())
