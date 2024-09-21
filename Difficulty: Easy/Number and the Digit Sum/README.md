<h2><a href="https://www.geeksforgeeks.org/problems/number-and-the-digit-sum4021/1?page=2&difficulty%5B%5D=0&category%5B%5D=Searching&sortBy=submissions">Number and the Digit Sum</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a positive value N, we need to find the count of numbers smaller than or equal to N such that the difference between the number and sum of its digits is greater than or equal to the given specific value K.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>N = 13, K = 2
<strong>Output:</strong> 4
<strong>Explanation</strong>: 
10, 11, 12 and 13 satisfy the given condition shown below,&nbsp;
10 - sumofdigit(10) = 9 &gt;= 2
11 - sumofdigit(11) = 9 &gt;= 2
12 - sumofdigit(12) = 9 &gt;= 2
13 - sumofdigit(13) = 9 &gt;= 2&nbsp;
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 10, K = 5
<strong>Output:</strong> 1
<strong>Explanation</strong>: 
Only 10 satisfies the givencondition as 
10 - sumofdigit(10) = 9 &gt;= 5</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>numberCount()</strong>which takes an integer N and an integer K as inputs and returns the count of numbers less than or equal to N such that the difference between the number and its sum of digits is greater than K.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>Log(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N, K&lt;= 10<sup>9</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Mathematical</code>&nbsp;<code>Binary Search</code>&nbsp;<code>Algorithms</code>&nbsp;