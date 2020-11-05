"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
 

说明：

你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

进阶：

你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
 

示例：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

提示：

1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

"""

"""
思路：
1、用两个数组来实现队列，一个正向存储，一个逆向存储
2、当push的时候，就存储到正向的数组中，然后在逆向存储
3、pop的时候直接返回逆向存储的第一个
4、peek的时候直接返回逆向存储的倒数第一个
5、直接判断数组是否为空，如果是返回Ture，否则False
"""


class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.stack = []
		self.stack2 = []

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		while self.stack2:
			self.stack.append(self.stack2.pop())
		self.stack.append(x)
		while self.stack:
			self.stack2.append(self.stack.pop())

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		return self.stack2.pop()

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		return self.stack2[-1]

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		if not self.stack2:
			return True
		else:
			return False

# 复杂度分析
# 时间复杂度：除了push为O(n),其他都是O(1)
# 空间复杂度：O(n)