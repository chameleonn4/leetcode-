# LeetCode 刷题记录

> 记录题号与代码

记录我的 LeetCode 刷题过程。每道题的代码放在 `solutions/` 目录下，题号与文件一一对应，并按题目记录在下面的索引表里。

- **仓库地址**：<https://github.com/chameleonn4/leetcode->
- **已刷题目**：21 题（简单 13、中等 8，持续更新中）
- **使用语言**：Python3

## 题目索引

| # | 题目 | 难度 | 语言 | 思路 | 代码 | 日期 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [两数之和](https://leetcode.cn/problems/two-sum/) | 简单 | Python3 | 哈希表 | [0001-two-sum.py](solutions/0001-two-sum.py) | 2026-10-07 |
| 2 | [两数相加](https://leetcode.cn/problems/add-two-numbers/) | 中等 | Python3 | 哑结点 + 逐位相加 | [0002-add-two-numbers.py](solutions/0002-add-two-numbers.py) | 2026-10-08 |
| 3 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 | Python3 | 滑动窗口 + 哈希表 | [0003-longest-substring-without-repeating-characters.py](solutions/0003-longest-substring-without-repeating-characters.py) | 2026-10-16 |
| 16 | [最接近的三数之和](https://leetcode.cn/problems/3sum-closest/) | 中等 | Python3 | 排序 + 双指针 | [0016-3sum-closest.py](solutions/0016-3sum-closest.py) | 2026-10-08 |
| 20 | [有效的括号](https://leetcode.cn/problems/valid-parentheses/) | 简单 | Python3 | 栈 | [0020-valid-parentheses.py](solutions/0020-valid-parentheses.py) | 2026-10-12 |
| 26 | [删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) | 简单 | Python3 | 快慢指针 | [0026-remove-duplicates-from-sorted-array.py](solutions/0026-remove-duplicates-from-sorted-array.py) | 2026-10-08 |
| 27 | [移除元素](https://leetcode.cn/problems/remove-element/) | 简单 | Python3 | 快慢指针 | [0027-remove-element.py](solutions/0027-remove-element.py) | 2026-10-08 |
| 28 | [找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 简单 | Python3 | 朴素匹配（双指针） | [0028-find-the-index-of-the-first-occurrence-in-a-string.py](solutions/0028-find-the-index-of-the-first-occurrence-in-a-string.py) | 2026-10-10 |
| 36 | [有效的数独](https://leetcode.cn/problems/valid-sudoku/) | 中等 | Python3 | 一遍遍历 + 行/列/宫三个哈希表 | [0036-valid-sudoku.py](solutions/0036-valid-sudoku.py) | 2026-10-20 |
| 48 | [旋转图像](https://leetcode.cn/problems/rotate-image/) | 中等 | Python3 | 转置 + 翻转每行 | [0048-rotate-image.py](solutions/0048-rotate-image.py) | 2026-10-10 |
| 88 | [合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) | 简单 | Python3 | 双指针 + 临时数组 | [0088-merge-sorted-array.py](solutions/0088-merge-sorted-array.py) | 2026-10-12 |
| 104 | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 简单 | Python3 | 递归 DFS（左右取较大 +1） | [0104-maximum-depth-of-binary-tree.py](solutions/0104-maximum-depth-of-binary-tree.py) | 2026-10-20 |
| 219 | [存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/) | 简单 | Python3 | 哈希表维护长度 k 的滑动窗口 | [0219-contains-duplicate-ii.py](solutions/0219-contains-duplicate-ii.py) | 2026-10-20 |
| 234 | [回文链表](https://leetcode.cn/problems/palindrome-linked-list/) | 简单 | Python3 | 转数组后首尾比较 | [0234-palindrome-linked-list.py](solutions/0234-palindrome-linked-list.py) | 2026-10-12 |
| 349 | [两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/) | 简单 | Python3 | 排序 + 双指针（利用有序天然去重） | [0349-intersection-of-two-arrays.py](solutions/0349-intersection-of-two-arrays.py) | 2026-10-16 |
| 455 | [分发饼干](https://leetcode.cn/problems/assign-cookies/) | 简单 | Python3 | 贪心 + 双指针（小饼干喂小胃口） | [0455-assign-cookies.py](solutions/0455-assign-cookies.py) | 2026-10-20 |
| 509 | [斐波那契数](https://leetcode.cn/problems/fibonacci-number/) | 简单 | Python3 | 按定义递归（进阶可改迭代） | [0509-fibonacci-number.py](solutions/0509-fibonacci-number.py) | 2026-10-20 |
| 622 | [设计循环队列](https://leetcode.cn/problems/design-circular-queue/) | 中等 | Python3 | 多开一格 + 取模区分空/满 | [0622-design-circular-queue.py](solutions/0622-design-circular-queue.py) | 2026-10-12 |
| 686 | [重复叠加字符串匹配](https://leetcode.cn/problems/repeated-string-match/) | 中等 | Python3 | KMP 跑在 a 的无限重复串上（[图解](notes/0686-KMP回退原理图解.png)、[笔记](#686-重复叠加字符串匹配--kmp-在无限重复串上匹配)） | [0686-repeated-string-match.py](solutions/0686-repeated-string-match.py) | 2026-10-12 |
| 912 | [排序数组](https://leetcode.cn/problems/sort-array/) | 中等 | Python3 | 随机基准 + 三路快排（[图解](notes/0912-三路快排分区图解.png)、[笔记](#912-排序数组--三路快排的分区过程)） | [0912-sort-array.py](solutions/0912-sort-array.py) | 2026-10-10 |
| 1122 | [数组的相对排序](https://leetcode.cn/problems/relative-sort-array/) | 简单 | Python3 | 计数排序（下标即值，剩余自动升序） | [1122-relative-sort-array.py](solutions/1122-relative-sort-array.py) | 2026-10-16 |

## 题解笔记

### 912. 排序数组 —— 三路快排的分区过程

![三路快排 partition 图解](notes/0912-三路快排分区图解.png)

一次分区把数组切成四段，`lt` / `i` / `gt` 三个指针分别卡在边界上：

| 指针 | 含义 |
| --- | --- |
| `lt` | 等于段的左边界：`[low, lt-1]` 全部 `< ref` |
| `i` | 当前扫描位置：`[lt, i-1]` 全部 `== ref` |
| `gt` | 大于段的左边界 - 1：`[i, gt]` 还没处理，`[gt+1, high]` 全部 `> ref` |

循环里三条分支的关键区别：

- `nums[i] < ref`：和 `nums[lt]` 交换，`lt++` 且 **`i++`** —— 从等于段换过来的元素一定是 `ref`，已经就位，不用再看；
- `nums[i] > ref`：和 `nums[gt]` 交换，`gt--`，**`i` 不动** —— 从待处理区换过来的是没见过的元素，下一轮必须重新判断；
- `nums[i] == ref`：`i++` —— 元素本来就该待在中间。

循环结束时 `[lt, gt]` 正好圈住整个等于段，所以只需要递归 `[low, lt-1]` 和 `[gt+1, high]`。等于段的元素一次分区就全部归位，这正是重复元素极多时三路快排不会退化成 O(n²) 的原因。

### 686. 重复叠加字符串匹配 —— KMP 在无限重复串上匹配

![KMP 回退原理](notes/0686-KMP回退原理图解.png)

![686 KMP 解法图解](notes/0686-重复叠加字符串匹配图解.png)

把 `a` 无限重复看成一条磁带 a∞，题目就变成「`b` 最早出现在 a∞ 的哪个位置 `s`」，答案 `= (s + m - 1) // n + 1`。

两个把"无限"变"有限"的结论：

- **起点一定 `< n`**：a∞ 的周期是 `n`。若 `b` 能在 `s ≥ n` 处匹配，把整个匹配左移 `n` 格也成立，与「`s` 最早」矛盾，所以起点只可能在前 `n` 个位置里；
- **只需要扫 `n + m - 1` 个字符**：起点最右是 `n-1`，`b` 长 `m`，终点最远 `(n-1) + (m-1) = n+m-2`。第 `i` 个字符直接取 `a[i % n]`，不用真的拼出无限长串。

KMP 在这里的角色：`i` 扫磁带（只增不减），`j` = 已经匹配上 `b` 的前缀长度。失配时 `j = next[j-1]`，相当于把尺子 `b` 往右滑 `j - next[j-1]` 格，让「`b` 的前缀」重新对上「刚匹配过的后缀」，而不是把尺子退回起点。

> ⚠️ 一个容易踩的坑：`generate_next` 里的回退必须是 `while`，**不能写成 `if`**——回退一次之后 `p[left]` 可能还是不等于 `p[right]`，得连续回退。
> 用 `if` 只回退一次，算出来的 `next` 数组不符合定义（例如 `"aaaba"` 会得到 `[0,1,2,1,2]`，标准是 `[0,1,2,0,1]`）。
> 本题因为 `kmp` 失配处用的也是 `while`，偏大的 `next` 会被继续回退"纠正"过来，结果侥幸正确；但换到别的 KMP 题就会出错。代码里已修正，并在那一行加了注释提醒。

## 目录结构

```
leetcode-/
├── README.md                  # 本文件：题目索引 + 题解笔记 + 上传流程
├── .gitignore                 # 忽略 __pycache__ 等无关文件
├── notes/                     # 题解笔记、手画/生成的图解
│   ├── 0686-KMP回退原理图解.png
│   ├── 0686-重复叠加字符串匹配图解.png
│   └── 0912-三路快排分区图解.png
└── solutions/                 # 所有题解代码
    ├── 0001-two-sum.py
    ├── 0002-add-two-numbers.py
    ├── 0003-longest-substring-without-repeating-characters.py
    ├── 0016-3sum-closest.py
    ├── 0020-valid-parentheses.py
    ├── 0026-remove-duplicates-from-sorted-array.py
    ├── 0027-remove-element.py
    ├── 0028-find-the-index-of-the-first-occurrence-in-a-string.py
    ├── 0036-valid-sudoku.py
    ├── 0048-rotate-image.py
    ├── 0088-merge-sorted-array.py
    ├── 0104-maximum-depth-of-binary-tree.py
    ├── 0219-contains-duplicate-ii.py
    ├── 0234-palindrome-linked-list.py
    ├── 0349-intersection-of-two-arrays.py
    ├── 0455-assign-cookies.py
    ├── 0509-fibonacci-number.py
    ├── 0622-design-circular-queue.py
    ├── 0686-repeated-string-match.py
    ├── 0912-sort-array.py
    └── 1122-relative-sort-array.py
```

## 文件命名规范

`solutions/题号-题目英文名.py`

- 题号补零到 4 位（例如第 1 题写 `0001`），这样按文件名排序就是按题号排序；
- 题目英文名全小写、单词之间用 `-` 连接，例如 `0001-two-sum.py`、`0002-add-two-numbers.py`。

图解、笔记等非代码文件放在 `notes/` 下，命名 `题号-说明.png`，并在 README 的「题解笔记」里内嵌引用。

## 每做完一题，如何上传（三步）

1. 把新代码存成 `solutions/题号-题目英文名.py`。文件开头用几行注释写上「思路 + 复杂度」当题解（可参考已有文件），本地自测代码可加可不加。
2. 在本文件（README.md）的「题目索引」表格里**新增一行**，填上题号、题目、难度、语言、思路、代码文件链接和日期。
3. 打开 PowerShell，执行下面三条命令：

```powershell
cd D:\leetcode刷题记录
git add .
git commit -m "add 2, 16, 26. 三题"
git push
```

`git commit -m` 后面的说明按当前这道题填写即可。

> 提示：如果 `git push` 报 `Failed to connect to github.com port 443`，一般是本机直连 GitHub 被重置。打开 Clash 后执行 `git config --global http.https://github.com.proxy http://127.0.0.1:7890` 再 push；不需要代理时用 `git config --global --unset http.https://github.com.proxy` 恢复直连。GitHub 的登录凭证已保存在 Windows 凭据管理器（`git:https://github.com`）里，正常情况下不会再要求登录。

## 本地运行某一题

```powershell
cd D:\leetcode刷题记录
python solutions\0026-remove-duplicates-from-sorted-array.py
```

（题解文件只包含 `Solution` 类和注释，直接运行不会有输出；想自查可以在 LeetCode 网页上点「运行」，或临时补一段自测。）
