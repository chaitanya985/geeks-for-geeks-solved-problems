<h2><a href="https://www.geeksforgeeks.org/problems/root-to-leaf-paths-sum/1?page=3&difficulty%5B%5D=0&category%5B%5D=Tree&sortBy=submissions">Root to leaf paths sum</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a binary tree, where every node value is a number. Find the sum of all the numbers that are formed from root to leaf paths. The formation of the numbers would be like 10*parent + current (see the examples for more clarification).</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input :      </strong>
           6                               
         /   \                          
        3     5                      
      /   \     \
     2    5      4             
        /  \                        
       7    4  </span>

<span style="font-size: 18px;"><strong>Output:</strong> 13997</span>

<span style="font-size: 18px;"><strong>Explanation : </strong>There are 4 leaves, resulting in leaf path of 632, 6357, 6354, 654 sums to 13997.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input :    </strong>
           10                               
         /   \                          
        20     30                      
      /   \     
     40       60    </span>

<span style="font-size: 18px;"><strong>Output :</strong>  2630</span>

<span style="font-size: 18px;"><strong>Explanation: </strong>There are 3 leaves, resulting in leaf path of 1240, 1260, 130 sums to 2630.<br></span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Auxiliary Space: </strong>O(h)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ Number of nodes ≤ 31<br>1 ≤ Value of nodes ≤ 100<br></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;