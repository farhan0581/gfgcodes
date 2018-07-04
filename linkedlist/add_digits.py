from reverse_list import Node, LList

class AddNumbers(LList):
    """docstring for AddNumbers"""
    def __init__(self, *args, **kwargs):
        super(LList, self).__init__(*args, **kwargs)


def add_digits(head1, head2, sum):
    start1 = head1
    start2 = head2
    res = carry = 0
    data = []
    while start1 or start2:
        if start1:
            res += start1.value
            start1 = start1.next

        if start2:
            res += start2.value
            start2 = start2.next
        print res, carry
        res += carry
        carry = 0
        
        # if sum > 10
        if res >= 10:
            carry = res / 10
            res = res % 10
        data.append(res)
        res = 0
      
    if carry:
        data.append(carry)
    return data




l1 = AddNumbers()
l1.create([9,9])
l2 = AddNumbers()
l2.create([9,9,9])
l1.iterate()
l2.iterate()
l3 = AddNumbers()
print add_digits(l1.start, l2.start, l3)