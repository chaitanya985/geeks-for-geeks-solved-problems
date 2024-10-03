<h2><a href="https://www.geeksforgeeks.org/problems/valid-expression1025/1?page=2&difficulty%5B%5D=1&category%5B%5D=Stack&sortBy=submissions">Valid Expression</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.<br></span><span style="font-size: 18px;">An input string is valid if:</span></p>
<p><span style="font-size: 18px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1. Open brackets must be closed by the same type of brackets.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2. Open brackets must be closed in the correct order.</span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
S = ()[]{}
<strong>Output:</strong> 1
<strong>Explanation: </strong>The arrangement is valid, as both the conditions are followed here.</span></pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
S = ())({}
<strong>Output:</strong> 0
<strong>Explanation: </strong>Arrangement is not valid, as for the bold closing bracket in ()<strong>)</strong>({}, there is no opening bracket of similar kind, before it</span>.</pre>
<p><span style="font-size: 18px;"><strong>Your Task: &nbsp;</strong><br>You dont need to read input or print anything. Complete the function <strong>valid()</strong> which takes <strong>s</strong> as input and returns a boolean value denoting whether the arrangement is valid or not.<br><br></span><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(N) where N is the length of s.<br><strong>Expected Auxiliary Space: </strong>O(N)&nbsp;<br><br></span><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Yatra.com</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Stack</code>&nbsp;<code>Data Structures</code>&nbsp;