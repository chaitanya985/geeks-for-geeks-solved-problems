<h2><a href="https://www.geeksforgeeks.org/problems/given-a-linked-list-reverse-alternate-nodes-and-append-at-the-end/1?page=2&difficulty%5B%5D=1&category%5B%5D=Linked%2520List&sortBy=submissions">Reverse alternate nodes in Link List</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 12pt;">Given a linked list, you have to perform&nbsp;the following task:</span></p>
<ol>
<li><span style="font-size: 12pt;">Extract the alternative nodes starting from the second node.</span></li>
<li><span style="font-size: 12pt;">Reverse the extracted list.</span></li>
<li><span style="font-size: 12pt;">Append the extracted list at the end of the original list.</span></li>
</ol>
<p><span style="font-size: 12pt;"><strong>Note</strong>: Try to solve the problem without using any extra memory.</span></p>
<p><span style="font-size: 12pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 12pt;"><strong>Input: </strong>LinkedList: 10-&gt;4-&gt;9-&gt;1-&gt;3-&gt;5-&gt;9-&gt;4
<strong>Output: </strong>10-&gt;9-&gt;3-&gt;9-&gt;4-&gt;5-&gt;1-&gt;4<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700006/Web/Other/blobid0_1723815304.png" width="417" height="94"><strong>
Explanation: </strong>Alternative nodes in the given linked list are 4,1,5,4. Reversing the alternative nodes from the given list, and then appending them to the end of the list results in a list 10-&gt;9-&gt;3-&gt;9-&gt;4-&gt;5-&gt;1-&gt;4.
</span></pre>
<pre><span style="font-size: 12pt;"><strong>Input: </strong>LinkedList: 1-&gt;2-&gt;3-&gt;4-&gt;5
<strong>Output: </strong>1-&gt;3-&gt;5-&gt;4-&gt;2 <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700006/Web/Other/blobid1_1723815319.png" width="417" height="94"><strong>
Explanation: </strong>Alternative nodes in the given linked list are 2 and 4. Reversing the alternative nodes from the given list, and then appending them to the end of the list results in a list of 1-&gt;3-&gt;5-&gt;4-&gt;2.</span></pre>
<p><span style="font-size: 12pt;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Space&nbsp;</strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Complexity</strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">:</strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&nbsp;O(1)</span></span></p>
<p><span style="font-size: 12pt;"><strong>Constraints:</strong><br>1 &lt;= size of linked list &lt;= 10<sup>6</sup><br>0 &lt;= Node_value &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Walmart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Linked List</code>&nbsp;<code>Data Structures</code>&nbsp;