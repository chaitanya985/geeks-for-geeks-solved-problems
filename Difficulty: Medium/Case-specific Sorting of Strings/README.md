<h2><a href="https://www.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/1?page=2&difficulty%5B%5D=1&category%5B%5D=Strings&sortBy=submissions">Case-specific Sorting of Strings</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string <strong>str </strong>consisting of <strong>only</strong>&nbsp;<strong>uppercase </strong>and <strong>lowercase </strong>characters. The task is to <strong>sort </strong>uppercase and lowercase letters <strong>separately </strong>such that if the i<sub>th</sub> place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.</span></p>
<p><strong><span style="font-size: 18px;">Examples : <br></span></strong></p>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">n = 12, str = defRTSersUXI
<strong>Output: </strong>deeIRSfrsTUX<strong>
Explanation: </strong>Sorted form of given string with the same case of character as that in original string is deeIRSfrsTUX</span>
</pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">n = 6, str = srbDKi
<strong>Output: </strong>birDKs<strong>
Explanation: </strong>Sorted form of given string with the same case of character will result in output as birDKs.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You only need to complete the function <strong>caseSort </strong>that takes&nbsp;a string str and length of the string n and&nbsp;<strong>returns </strong>sorted <strong>string</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(nlog(n)).<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(n).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong> </span><br><span style="font-size: 18px;">1 ≤ n ≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Sorting</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;