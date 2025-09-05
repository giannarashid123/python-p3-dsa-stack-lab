from Stack import Stack

class TestStack:
    '''Class Stack in Stack.py'''

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for index in range(len(expected)):
            assert(expected[index] == stk.items[index])

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1,2,3,4,5])
        stk.push(0)
        expected = [1,2,3,4,5,0]
        for index in range(0,len(expected)):
            assert(expected[index] == stk.items[index])

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1,2,3,4,5])
        stk.pop()
        expected = [1,2,3,4]
        for index in range(len(expected)):
            assert(expected[index] == stk.items[index])

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        assert(stk.size() == len(expected))

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert(stk.isEmpty())
        assert(stk.size() == 0)
        assert(stk.pop() == None)
        stk.push(1)
        assert(not stk.isEmpty())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

    def test_full(self):
        '''Test Stack full() method - allow overflow now'''
        stk = Stack([1], 1)

        # Initially full because limit = 1 and 1 item present
        assert(stk.full())
        assert(stk.size() == 1)

        # Pop item, now empty
        assert(stk.pop() == 1)

        # Push 1 item back
        stk.push(1)

        # Push another item beyond limit - allowed now
        stk.push(2)

        # Size should now be 2 (over limit)
        assert(stk.size() == 2)

        # full() should still return True because at least limit reached
        assert(stk.full())

        # Pop items to check correct order
        assert(stk.pop() == 2)
        assert(stk.pop() == 1)

        # Now stack is empty again
        assert(stk.isEmpty())

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack? '''
        stk = Stack([5,6,7,8,9,10])

        assert(stk.search(5) == 5)
        assert(stk.search(6) == 4)
        assert(stk.search(7) == 3)
        assert(stk.search(8) == 2)
        assert(stk.search(9) == 1)
        assert(stk.search(10) == 0)

        # Case with target not in Stack
        assert(stk.search(15) == -1)
