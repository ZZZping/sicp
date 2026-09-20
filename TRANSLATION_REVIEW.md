# 中文译文逐句校订记录

本次在现有中文译文上校订。Ollama 的 qwen3:8b 仅提供建议；编辑复核原文后单独记录决定，建议不会自动写入正文。

- 对照范围：39 个页面，4233 个文本块，9837 个英文句子及短文本片段。
- 修订文本块：637；其余保留原有译文。
- 本地模型返回有效格式建议的文本块：4,217；另有 16 个未取得符合格式要求的模型输出。全体 4,233 个文本块均已独立完成原文对照，模型建议不充当最终复核决定。
- 计数包含标题、导航、术语及保留原始出版信息的参考文献条目；句子切分器也会把部分缩写和代码片段单独计数。
- 英文文件哈希保持不变；中文页面均通过 XML、块结构、属性、代码、公式、插图、脚注及内部锚点校验。
- 本记录位于书籍页面之外，不向正文添加解释、答案或译者注。

## 修改前后对照

### 1_002e1:0011

**原文**

One easy way to get started at programming is to examine some typical interactions with an interpreter for the Scheme dialect of Lisp. Imagine that you are sitting at a computer terminal. You type an expression, and the interpreter responds by displaying the result of its evaluating that expression.

**校订前**

开始学习程序设计的一种简单方法是考察与 Lisp 的 Scheme 方言解释器的一些典型交互。设想你正坐在计算机终端前。你输入一个 表达式，解释器则通过显示它 求值该表达式的结果来作出响应。

**校订后**

开始学习程序设计的一种简单方法，是考察与 Lisp 的 Scheme 方言解释器进行的一些典型交互。设想你正坐在计算机终端前。你输入一个表达式，解释器则显示对该表达式求值所得的结果，作为响应。

### 1_002e1:0012

**原文**

One kind of primitive expression you might type is a number. (More precisely, the expression that you type consists of the numerals that represent the number in base 10.) If you present Lisp with a number

**校订前**

你可能输入的一种基本表达式是数字。（更确切地说，你输入的表达式由以10为基数表示该数字的数字组成。）如果你向 Lisp 提供一个数字

**校订后**

你可能输入的一种基本表达式是一个数。（更确切地说，你输入的表达式由以10为基数表示这个数的数码组成。）如果你向 Lisp 提供一个数

### 1_002e1:0014

**原文**

Expressions representing numbers may be combined with an expression representing a primitive procedure (such as `+` or `*`) to form a compound expression that represents the application of the procedure to those numbers. For example:

**校订前**

表示数字的表达式可以与表示基本过程（例如`+`或`*`）的表达式组合，形成表示将这些过程应用于这些数字的复合表达式。例如：

**校订后**

表示数字的表达式可以与表示基本过程（例如`+`或`*`）的表达式组合，形成表示将该过程应用于这些数的复合表达式。例如：

### 1_002e1:0031

**原文**

One of our goals in this chapter is to isolate issues about thinking procedurally. As a case in point, let us consider that, in evaluating combinations, the interpreter is itself following a procedure.

**校订前**

本章的目标之一是分离出关于过程性思考的问题。作为一个例子，让我们考虑一下，在求值组合式时，解释器本身就在遵循一个过程。

**校订后**

本章的目标之一，是单独考察按过程思考所涉及的问题。举例来说，在对组合式求值时，解释器本身也在遵循一个过程。

### 1_002e1:0036

**原文**

Notice how succinctly the idea of recursion can be used to express what, in the case of a deeply nested combination, would otherwise be viewed as a rather complicated process. For example, evaluating

**校订前**

注意递归的思想可以多么简洁地表达出，在一个深度嵌套的组合式的情况下，否则会被视为相当复杂的过程。例如，求值

**校订后**

请注意，对于深度嵌套的组合式，本来会被视为相当复杂的计算过程，利用递归的思想却可以表达得十分简洁。例如，对

### 1_002e1:0039

**原文**

Next, observe that the repeated application of the first step brings us to the point where we need to evaluate, not combinations, but primitive expressions such as numerals, built-in operators, or other names. We take care of the primitive cases by stipulating that

**校订前**

接下来，注意第一步的重复应用将我们带到这样一个点：我们需要求值的不是组合式，而是基本表达式，例如数字、内置运算符或其他名字。我们通过规定以下内容来处理这些基本情形：

**校订后**

接下来，注意第一步的重复应用将我们带到这样一个点：我们需要求值的不是组合式，而是基本表达式，例如数码、内置运算符或其他名字。我们通过规定以下内容来处理这些基本情形：

### 1_002e1:0040

**原文**

the values of numerals are the numbers that they name,

**校订前**

数字的值就是它们所命名的数，

**校订后**

数码的值就是它们所表示的数，

### 1_002e1:0081

**原文**

Lisp uses applicative-order evaluation, partly because of the additional efficiency obtained from avoiding multiple evaluations of expressions such as those illustrated with `(+ 5 1)` and `(* 5 2)` above and, more significantly, because normal-order evaluation becomes much more complicated to deal with when we leave the realm of procedures that can be modeled by substitution. On the other hand, normal-order evaluation can be an extremely valuable tool, and we will investigate some of its implications in Chapter 3 and Chapter 4.[注16]

**校订前**

Lisp使用应用序求值，部分原因是避免了像上面用`(+ 5 1)`和`(* 5 2)`说明的那类表达式的多次求值所带来的额外效率，更重要的是，因为当我们离开可以用代换建模的过程领域时，正则序求值变得复杂得多。另一方面，正则序求值可以是一个极其有价值的工具，我们将在第3章和第4章中研究它的一些含义。[注16]

**校订后**

Lisp使用应用序求值，部分原因在于，对像上面用`(+ 5 1)`和`(* 5 2)`说明的那类表达式避免多次求值，可以提高效率；更重要的是，因为当我们离开可以用代换建模的过程领域时，正则序求值变得复杂得多。另一方面，正则序求值可以是一个极其有价值的工具，我们将在第3章和第4章中研究它的一些含义。[注16]

### 1_002e1:0108

**原文**

What behavior will Ben observe with an interpreter that uses applicative-order evaluation? What behavior will he observe with an interpreter that uses normal-order evaluation? Explain your answer. (Assume that the evaluation rule for the special form `if` is the same whether the interpreter is using normal or applicative order: The predicate expression is evaluated first, and the result determines whether to evaluate the consequent or the alternative expression.)

**校订前**

对于使用应用序求值的解释器，Ben 会观察到什么行为？对于使用正则序求值的解释器，他会观察到什么行为？解释你的答案。（假设特殊形式`if`的求值规则无论解释器使用正则序还是应用序都是相同的：谓词表达式首先被求值，其结果决定是求值推论表达式还是替代表达式。）

**校订后**

对于使用应用序求值的解释器，Ben 会观察到什么行为？对于使用正则序求值的解释器，他会观察到什么行为？解释你的答案。（假设特殊形式`if`的求值规则无论解释器使用正则序还是应用序都是相同的：谓词表达式首先被求值，其结果决定是求值结果表达式还是替代表达式。）

### 1_002e1:0110

**原文**

Procedures, as introduced above, are much like ordinary mathematical functions. They specify a value that is determined by one or more parameters. But there is an important difference between mathematical functions and computer procedures. Procedures must be effective.

**校订前**

如上所述，过程很像普通的数学函数。它们指定一个由一个或多个参数确定的值。但数学函数和计算机过程之间有一个重要区别。过程必须是有效的。

**校订后**

如上所述，过程很像普通的数学函数。它们指定一个由一个或多个参数确定的值。但数学函数和计算机过程之间有一个重要区别。过程必须是可实际执行的。

### 1_002e1:0116

**原文**

Now let’s formalize the process in terms of procedures. We start with a value for the radicand (the number whose square root we are trying to compute) and a value for the guess. If the guess is good enough for our purposes, we are done; if not, we must repeat the process with an improved guess. We write this basic strategy as a procedure:

**校订前**

现在让我们用过程来形式化这个过程。我们从一个被开方数（我们试图计算其平方根的数）的值和一个猜测值开始。如果猜测值对我们的目的来说足够好，我们就完成了；如果不是，我们必须用改进后的猜测值重复这个过程。我们将这个基本策略写成一个过程：

**校订后**

现在让我们用过程来形式化地描述这一计算过程。我们从一个被开方数（我们试图计算其平方根的数）的值和一个猜测值开始。如果猜测值对我们的目的来说足够好，我们就完成了；如果不是，我们必须用改进后的猜测值重复这个过程。我们将这个基本策略写成一个过程：

### 1_002e1:0117

**原文**

A guess is improved by averaging it with the quotient of the radicand and the old guess:

**校订前**

通过将猜测值与被开方数和旧猜测值的商取平均来改进猜测值：

**校订后**

通过将猜测值与被开方数除以旧猜测值所得的商取平均，可以改进猜测值：

### 1_002e1:0119

**原文**

We also have to say what we mean by “good enough.” The following will do for illustration, but it is not really a very good test. (See Exercise 1.7.) The idea is to improve the answer until it is close enough so that its square differs from the radicand by less than a predetermined tolerance (here 0.001):[注22]

**校订前**

我们还必须说明“足够接近”是什么意思。下面这个例子可以说明问题，但它并不是一个很好的测试。（见习题1.7。）其思想是不断改进答案，直到它足够接近，使得其平方与被开方数之差小于一个预先确定的容差（这里是0.001）：[注22]

**校订后**

我们还必须说明“足够好”是什么意思。下面这个例子可以说明问题，但它并不是一个很好的测试。（见习题1.7。）其思想是不断改进答案，直到它足够接近，使得其平方与被开方数之差小于一个预先确定的容差（这里是0.001）：[注22]

### 1_002e1:0127

**原文**

Exercise 1.7: The `good-enough?` test used in computing square roots will not be very effective for finding the square roots of very small numbers. Also, in real computers, arithmetic operations are almost always performed with limited precision. This makes our test inadequate for very large numbers. Explain these statements, with examples showing how the test fails for small and large numbers. An alternative strategy for implementing `good-enough?` is to watch how `guess` changes from one iteration to the next and to stop when the change is a very small fraction of the guess. Design a square-root procedure that uses this kind of end test. Does this work better for small and large numbers?

**校订前**

习题1.7：用于计算平方根的`good-enough?`测试对于求非常小的数的平方根不会很有效。此外，在真实的计算机中，算术运算几乎总是以有限的精度进行的。这使得我们的测试对于非常大的数也不够用。请解释这些说法，并举例说明该测试在小的数和大的数情况下如何失效。实现`good-enough?`的另一种策略是观察`guess`在相邻两次迭代中如何变化，并在变化量是猜测值的一个非常小的分数时停止。设计一个使用这种结束测试的求平方根过程。对于小的数和大的数，它是否工作得更好？

**校订后**

习题1.7：用于计算平方根的`good-enough?`测试对于求非常小的数的平方根不会很有效。此外，在真实的计算机中，算术运算几乎总是以有限的精度进行的。这使得我们的测试对于非常大的数也不够用。请解释这些说法，并举例说明该测试在小的数和大的数情况下如何失效。实现`good-enough?`的另一种策略是观察`guess`在相邻两次迭代中如何变化，并在变化量是猜测值的极小一部分时停止。设计一个使用这种结束测试的求平方根过程。对于小的数和大的数，它是否工作得更好？

### 1_002e1:0141

**原文**

A formal parameter of a procedure has a very special role in the procedure definition, in that it doesn’t matter what name the formal parameter has. Such a name is called a bound variable, and we say that the procedure definition binds its formal parameters. The meaning of a procedure definition is unchanged if a bound variable is consistently renamed throughout the definition.[注26] If a variable is not bound, we say that it is free. The set of expressions for which a binding defines a name is called the scope of that name. In a procedure definition, the bound variables declared as the formal parameters of the procedure have the body of the procedure as their scope.

**校订前**

过程的形参在过程定义中扮演着非常特殊的角色，因为形参叫什么名字并不重要。这样的名字称为 约束变量，我们说过程定义 约束了它的形参。如果在整个定义中一致地重命名一个约束变量，过程定义的意义保持不变。[注26]如果一个变量未被约束，我们说它是自由的。一个绑定为某个名字定义名称的那些表达式的集合称为该名字的作用域。在过程定义中，声明为过程形参的约束变量以过程体作为它们的作用域。

**校订后**

过程的形参在过程定义中扮演着非常特殊的角色，因为形参叫什么名字并不重要。这样的名字称为 约束变量，我们说过程定义 约束了它的形参。如果在整个定义中一致地重命名一个约束变量，过程定义的意义保持不变。[注26]如果一个变量未被约束，我们说它是自由的。某个名字的绑定在其中有效的表达式集合称为该名字的作用域。在过程定义中，声明为过程形参的约束变量以过程体作为它们的作用域。

### 1_002e1:0163

**原文**

[注18] `Abs` also uses the “minus” operator `-`, which, when used with a single operand, as in `(- x)`, indicates negation.

**校订前**

[注18]`Abs` 还使用了“减号”运算符 `-`，当它与单个操作数一起使用时，如 `(- x)` 中那样，表示取负。

**校订后**

[注18]`Abs` 还使用了“减号”运算符 `-`，当它与单个运算对象一起使用时，如 `(- x)` 中那样，表示取负。

### 1_002e1:0165

**原文**

[注20] Declarative and imperative descriptions are intimately related, as indeed are mathematics and computer science. For instance, to say that the answer produced by a program is “correct” is to make a declarative statement about the program. There is a large amount of research aimed at establishing techniques for proving that programs are correct, and much of the technical difficulty of this subject has to do with negotiating the transition between imperative statements (from which programs are constructed) and declarative statements (which can be used to deduce things). In a related vein, an important current area in programming-language design is the exploration of so-called very high-level languages, in which one actually programs in terms of declarative statements. The idea is to make interpreters sophisticated enough so that, given “what is” knowledge specified by the programmer, they can generate “how to” knowledge automatically. This cannot be done in general, but there are important areas where progress has been made. We shall revisit this idea in Chapter 4.

**校订前**

[注20]声明式描述和命令式描述密切相关，正如数学和计算机科学确实密切相关一样。例如，说一个程序产生的答案是“正确的”，就是对该程序做出一个声明式陈述。有大量研究旨在建立证明程序正确性的技术，而这一主题的许多技术困难都与处理命令式陈述（程序由之构造）和声明式陈述（可用于推导事物）之间的转换有关。与此相关，当前编程语言设计的一个重要领域是探索所谓的甚高级语言，在这种语言中，人们实际上是用声明式陈述来编程。其想法是让解释器足够复杂，以至于给定程序员指定的“是什么”知识，它们能够自动生成“如何做”知识。这通常无法做到，但在一些重要领域已经取得了进展。我们将在第 4 章重新讨论这个想法。

**校订后**

[注20]声明式描述和命令式描述密切相关，正如数学和计算机科学确实密切相关一样。例如，说一个程序产生的答案是“正确的”，就是对该程序做出一个声明式陈述。有大量研究旨在建立证明程序正确性的技术，而这一主题的许多技术困难都与处理命令式陈述（程序由之构造）和声明式陈述（可用于推导事物）之间的转换有关。与此相关，当前编程语言设计的一个重要领域是探索所谓的甚高级语言，在这种语言中，人们实际上是用声明式陈述来编程。其想法是让解释器足够完善，以至于给定程序员指定的“是什么”知识，它们能够自动生成“如何做”知识。这在一般情况下无法做到，但在一些重要领域已经取得了进展。我们将在第 4 章重新讨论这个想法。

### 1_002e2:0006

**原文**

A procedure is a pattern for the local evolution of a computational process. It specifies how each stage of the process is built upon the previous stage. We would like to be able to make statements about the overall, or global, behavior of a process whose local evolution has been specified by a procedure. This is very difficult to do in general, but we can at least try to describe some typical patterns of process evolution.

**校订前**

过程是计算过程的局部演化的模式。它指定了过程的每个阶段如何建立在前一阶段之上。我们希望能够对局部演化已由过程指定的过程的整体行为，即全局行为，做出陈述。这在一般情况下非常困难，但我们至少可以尝试描述一些典型的过程演化模式。

**校订后**

过程是计算过程局部演化的一种模式。它规定了计算过程的每个阶段如何建立在前一阶段之上。对于局部演化已经由某个过程规定的计算过程，我们希望能够描述其整体行为，也就是全局行为。一般来说，这很难做到，但我们至少可以尝试描述计算过程演化的一些典型模式。

### 1_002e2:0007

**原文**

In this section we will examine some common “shapes” for processes generated by simple procedures. We will also investigate the rates at which these processes consume the important computational resources of time and space. The procedures we will consider are very simple. Their role is like that played by test patterns in photography: as oversimplified prototypical patterns, rather than practical examples in their own right.

**校订前**

在本节中，我们将考察由简单过程生成的计算过程的一些常见“形状”。我们还将研究这些过程消耗重要计算资源——时间和空间——的速率。我们将考虑的过程非常简单。它们的作用就像摄影中的测试图案：作为过度简化的原型模式，而不是本身的实际例子。

**校订后**

在本节中，我们将考察由简单过程生成的计算过程的一些常见“形状”。我们还将研究这些计算过程消耗重要计算资源——时间和空间——的速率。我们将考虑的过程非常简单。它们的作用就像摄影中的测试图案：作为过度简化的原型模式，而不是本身具有实用价值的例子。

### 1_002e2:0011

**原文**

Figure 1.3: A linear recursive process for computing 6!.

**校订前**

图1.3： 计算6!的线性递归过程。

**校订后**

图1.3： 计算6!的线性递归计算过程。

### 1_002e2:0012

**原文**

Now let’s take a different perspective on computing factorials. We could describe a rule for computing $n!$ by specifying that we first multiply 1 by 2, then multiply the result by 3, then by 4, and so on until we reach $n$. More formally, we maintain a running product, together with a counter that counts from 1 up to $n$. We can describe the computation by saying that the counter and the product simultaneously change from one step to the next according to the rule

**校订前**

现在让我们从不同的角度来看待阶乘的计算。我们可以通过指定先1乘以2，然后将结果乘以3，再乘以4，依此类推直到达到$n$，来描述计算$n!$的规则。更形式化地说，我们维护一个运行中的乘积，以及一个从1计数到$n$的计数器。我们可以通过说计数器和乘积根据以下规则同时从一步变化到下一步来描述计算

**校订后**

现在让我们从不同的角度来看待阶乘的计算。我们可以通过指定先1乘以2，然后将结果乘以3，再乘以4，依此类推直到达到$n$，来描述计算$n!$的规则。更形式化地说，我们维护一个累计乘积，以及一个从1计数到$n$的计数器。我们可以通过说计数器和乘积根据以下规则同时从一步变化到下一步来描述计算

### 1_002e2:0016

**原文**

Figure 1.4: A linear iterative process for computing 6!.

**校订前**

图1.4： 计算6!的线性迭代过程。

**校订后**

图1.4： 计算6!的线性迭代计算过程。

### 1_002e2:0018

**原文**

Consider the first process. The substitution model reveals a shape of expansion followed by contraction, indicated by the arrow in Figure 1.3. The expansion occurs as the process builds up a chain of deferred operations (in this case, a chain of multiplications). The contraction occurs as the operations are actually performed. This type of process, characterized by a chain of deferred operations, is called a recursive process. Carrying out this process requires that the interpreter keep track of the operations to be performed later on. In the computation of $n!$, the length of the chain of deferred multiplications, and hence the amount of information needed to keep track of it, grows linearly with $n$ (is proportional to $n$), just like the number of steps. Such a process is called a linear recursive process.

**校订前**

考虑第一个过程。代换模型揭示了一种先展开后收缩的形状，如图1.3中的箭头所示。展开发生在过程构建起一条延迟操作链（在这种情况下，是一系列乘法）时。收缩发生在操作实际执行时。这种以延迟操作链为特征的过程类型称为递归过程。执行这个过程要求解释器跟踪稍后要执行的操作。在计算$n!$时，延迟乘法链的长度，以及因此跟踪它所需的信息量，随$n$线性增长（与$n$成正比），就像步数一样。这样的过程称为线性递归过程。

**校订后**

考虑第一个计算过程。代换模型揭示了一种先展开后收缩的形状，如图1.3中的箭头所示。展开发生在计算过程构建起一条延迟操作链（在这种情况下，是一系列乘法）时。收缩发生在操作实际执行时。这种以延迟操作链为特征的计算过程类型称为递归计算过程。执行这个计算过程要求解释器跟踪稍后要执行的操作。在计算$n!$时，延迟乘法链的长度，以及因此跟踪它所需的信息量，随$n$线性增长（与$n$成正比），就像步数一样。这样的计算过程称为线性递归计算过程。

### 1_002e2:0020

**原文**

The contrast between the two processes can be seen in another way. In the iterative case, the program variables provide a complete description of the state of the process at any point. If we stopped the computation between steps, all we would need to do to resume the computation is to supply the interpreter with the values of the three program variables. Not so with the recursive process. In this case there is some additional “hidden” information, maintained by the interpreter and not contained in the program variables, which indicates “where the process is” in negotiating the chain of deferred operations. The longer the chain, the more information must be maintained.[注30]

**校订前**

这两个计算过程之间的对比还可以从另一个角度来看。在迭代的情况下，程序变量提供了计算过程在任意点的状态的完整描述。如果我们在步骤之间停止计算，要恢复计算，我们只需向解释器提供这三个程序变量的值。递归计算过程则不然。在这种情况下，存在一些额外的“隐藏”信息，由解释器维护而不包含在程序变量中，它指示在协商延迟操作链时“计算过程进行到了哪里”。链越长，必须维护的信息就越多。[注30]

**校订后**

这两个计算过程之间的对比还可以从另一个角度来看。在迭代的情况下，程序变量提供了计算过程在任意点的状态的完整描述。如果我们在步骤之间停止计算，要恢复计算，我们只需向解释器提供这三个程序变量的值。递归计算过程则不然。在这种情况下，存在一些额外的“隐藏”信息，由解释器维护而不包含在程序变量中，它指示在处理延迟操作链时“计算过程进行到了哪里”。链越长，必须维护的信息就越多。[注30]

### 1_002e2:0029

**原文**

1.2.2 Tree Recursion

**校订前**

1.2.2 树递归

**校订后**

1.2.2 树形递归

### 1_002e2:0030

**原文**

Another common pattern of computation is called tree recursion. As an example, consider computing the sequence of Fibonacci numbers, in which each number is the sum of the preceding two:

**校订前**

另一种常见的计算模式称为树递归。作为一个例子，考虑计算斐波那契数列，其中每个数是前两个数之和：

**校订后**

另一种常见的计算模式称为树形递归。作为一个例子，考虑计算斐波那契数列，其中每个数是前两个数之和：

### 1_002e2:0033

**原文**

Figure 1.5: The tree-recursive process generated in computing `(fib 5)`.

**校订前**

图1.5：计算`(fib 5)`时生成的树递归计算过程。

**校订后**

图1.5：计算`(fib 5)`时生成的树形递归计算过程。

### 1_002e2:0034

**原文**

This procedure is instructive as a prototypical tree recursion, but it is a terrible way to compute Fibonacci numbers because it does so much redundant computation. Notice in Figure 1.5 that the entire computation of `(fib 3)`—almost half the work—is duplicated. In fact, it is not hard to show that the number of times the procedure will compute `(fib 1)` or `(fib 0)` (the number of leaves in the above tree, in general) is precisely $Fib(n+1)$. To get an idea of how bad this is, one can show that the value of $Fib(n)$ grows exponentially with $n$. More precisely (see Exercise 1.13), $Fib(n)$ is the closest integer to $φ^(n)/sqrt(5)$, where $φ=(1+sqrt(5))/(2)≈1.6180$ is the golden ratio, which satisfies the equation $φ^(2)=φ+1.$ Thus, the process uses a number of steps that grows exponentially with the input. On the other hand, the space required grows only linearly with the input, because we need keep track only of which nodes are above us in the tree at any point in the computation. In general, the number of steps required by a tree-recursive process will be proportional to the number of nodes in the tree, while the space required will be proportional to the maximum depth of the tree.

**校订前**

这个过程作为典型的树形递归具有教育意义，但用它计算 Fibonacci 数却很糟糕，因为它做了太多冗余计算。注意图1.5中，`(fib 3)`的整个计算——几乎一半的工作——被重复了。事实上，不难证明，该过程计算`(fib 1)`或`(fib 0)`的次数（即上述树中叶节点的数目，一般而言）恰好是$Fib(n+1)$。为了了解这有多糟糕，可以证明$Fib(n)$的值随$n$呈指数增长。更确切地说（见习题1.13），$Fib(n)$是最接近$φ^(n)/sqrt(5)$的整数，其中$φ=(1+sqrt(5))/(2)≈1.6180$是黄金分割率，它满足方程$φ^(2)=φ+1.$。因此，该计算过程所需的步数随输入呈指数增长。另一方面，所需的空间仅随输入线性增长，因为在计算的任何时刻，我们只需要记录树中位于我们上方的节点。一般而言，树形递归过程所需的步数与树中的节点数成正比，而所需的空间与树的最大深度成正比。

**校订后**

这个过程作为典型的树形递归具有教育意义，但用它计算 斐波那契数却很糟糕，因为它做了太多冗余计算。注意图1.5中，`(fib 3)`的整个计算——几乎一半的工作——被重复了。事实上，不难证明，该过程计算`(fib 1)`或`(fib 0)`的次数（即上述树中叶节点的数目，一般而言）恰好是$Fib(n+1)$。为了了解这有多糟糕，可以证明$Fib(n)$的值随$n$呈指数增长。更确切地说（见习题1.13），$Fib(n)$是最接近$φ^(n)/sqrt(5)$的整数，其中$φ=(1+sqrt(5))/(2)≈1.6180$是黄金分割比，它满足方程$φ^(2)=φ+1.$。因此，该计算过程所需的步数随输入呈指数增长。另一方面，所需的空间仅随输入线性增长，因为在计算的任何时刻，我们只需要记录树中位于我们上方的节点。一般而言，树形递归计算过程所需的步数与树中的节点数成正比，而所需的空间与树的最大深度成正比。

### 1_002e2:0035

**原文**

We can also formulate an iterative process for computing the Fibonacci numbers. The idea is to use a pair of integers $a$ and $b$, initialized to $Fib(1)=1$ and $Fib(0)=0$, and to repeatedly apply the simultaneous transformations

**校订前**

我们也可以构造一个计算 Fibonacci 数的迭代过程。其思路是使用一对整数$a$和$b$，初始化为$Fib(1)=1$和$Fib(0)=0$，并反复应用同时变换

**校订后**

我们也可以构造一个计算 斐波那契数的迭代计算过程。其思路是使用一对整数$a$和$b$，初始化为$Fib(1)=1$和$Fib(0)=0$，并反复应用同时变换

### 1_002e2:0036

**原文**

It is not hard to show that, after applying this transformation $n$ times, $a$ and $b$ will be equal, respectively, to $Fib(n+1)$ and $Fib(n)$. Thus, we can compute Fibonacci numbers iteratively using the procedure

**校订前**

不难证明，在应用此变换$n$次之后，$a$和$b$将分别等于$Fib(n+1)$和$Fib(n)$。因此，我们可以使用以下过程迭代地计算 Fibonacci 数

**校订后**

不难证明，在应用此变换$n$次之后，$a$和$b$将分别等于$Fib(n+1)$和$Fib(n)$。因此，我们可以使用以下过程迭代地计算 斐波那契数

### 1_002e2:0038

**原文**

One should not conclude from this that tree-recursive processes are useless. When we consider processes that operate on hierarchically structured data rather than numbers, we will find that tree recursion is a natural and powerful tool.[注32] But even in numerical operations, tree-recursive processes can be useful in helping us to understand and design programs. For instance, although the first `fib` procedure is much less efficient than the second one, it is more straightforward, being little more than a translation into Lisp of the definition of the Fibonacci sequence. To formulate the iterative algorithm required noticing that the computation could be recast as an iteration with three state variables.

**校订前**

不应由此得出结论说树形递归过程是无用的。当我们考虑操作分层结构数据而非数字的过程时，我们会发现树形递归是一种自然且强大的工具。[注32]但即使在数值运算中，树形递归过程也有助于我们理解和设计程序。例如，尽管第一个`fib`过程比第二个效率低得多，但它更直截了当，几乎只是将 Fibonacci 序列的定义翻译成 Lisp。要构造迭代算法，需要注意到计算可以重新表述为具有三个状态变量的迭代。

**校订后**

不应由此得出结论说树形递归计算过程是无用的。当我们考虑操作分层结构数据而非数的计算过程时，我们会发现树形递归是一种自然且强大的工具。[注32]但即使在数值运算中，树形递归计算过程也有助于我们理解和设计程序。例如，尽管第一个`fib`过程比第二个效率低得多，但它更直截了当，几乎只是将 斐波那契数列的定义翻译成 Lisp。要构造迭代算法，需要注意到计算可以重新表述为具有三个状态变量的迭代。

### 1_002e2:0039

**原文**

Example: Counting change

**校订前**

示例：计数找零

**校订后**

示例：换零钱方式的计数

### 1_002e2:0061

**原文**

For instance, with the linear recursive process for computing factorial described in 1.2.1 the number of steps grows proportionally to the input $n$. Thus, the steps required for this process grows as $Θ(n)$. We also saw that the space required grows as $Θ(n)$. For the iterative factorial, the number of steps is still $Θ(n)$ but the space is $Θ(1)$—that is, constant.[注36] The tree-recursive Fibonacci computation requires $Θ(φ^(n))$ steps and space $Θ(n)$, where $φ$ is the golden ratio described in 1.2.2.

**校订前**

例如，对于 1.2.1 中描述的用于计算阶乘的线性递归计算过程，步数按与输入 $n$ 成比例的方式增长。因此，此计算过程所需的步数按 $Θ(n)$ 增长。我们还看到所需的空间按 $Θ(n)$ 增长。对于迭代式阶乘，步数仍然是 $Θ(n)$，但空间是 $Θ(1)$——即常数。[注36] 树递归的 Fibonacci 计算需要 $Θ(φ^(n))$ 步和 $Θ(n)$ 空间，其中 $φ$ 是 1.2.2 中描述的金分割比。

**校订后**

例如，对于 1.2.1 中描述的用于计算阶乘的线性递归计算过程，步数按与输入 $n$ 成比例的方式增长。因此，此计算过程所需的步数按 $Θ(n)$ 增长。我们还看到所需的空间按 $Θ(n)$ 增长。对于迭代式阶乘，步数仍然是 $Θ(n)$，但空间是 $Θ(1)$——即常数。[注36] 树形递归的 斐波那契 计算需要 $Θ(φ^(n))$ 步和 $Θ(n)$ 空间，其中 $φ$ 是 1.2.2 中描述的黄金分割比。

### 1_002e2:0064

**原文**

Exercise 1.15: The sine of an angle (specified in radians) can be computed by making use of the approximation $sin⁡x≈x$ if $x$ is sufficiently small, and the trigonometric identity $sin⁡x=3sin⁡(x)/(3)−4sin^(3)⁡(x)/(3)$ to reduce the size of the argument of sin. (For purposes of this exercise an angle is considered “sufficiently small” if its magnitude is not greater than 0.1 radians.) These ideas are incorporated in the following procedures:

**校订前**

习题 1.15： 一个角（以弧度指定）的正弦可以通过利用近似 $sin⁡x≈x$（如果 $x$ 足够小）以及三角恒等式 $sin⁡x=3sin⁡(x)/(3)−4sin^(3)⁡(x)/(3)$ 来减小 sin 的自变量的大小，从而计算出来。（就本题而言，如果一个角的幅度不大于 0.1 弧度，则认为它“足够小”。）这些思想体现在以下过程中：

**校订后**

习题 1.15： 一个角（以弧度指定）的正弦可以通过利用近似 $sin⁡x≈x$（如果 $x$ 足够小）以及三角恒等式 $sin⁡x=3sin⁡(x)/(3)−4sin^(3)⁡(x)/(3)$ 来减小 sin 的自变量的大小，从而计算出来。（就本题而言，如果一个角的绝对值不大于 0.1 弧度，则认为它“足够小”。）这些思想体现在以下过程中：

### 1_002e2:0068

**原文**

Consider the problem of computing the exponential of a given number. We would like a procedure that takes as arguments a base $b$ and a positive integer exponent $n$ and computes $b^(n)$. One way to do this is via the recursive definition $b^(n)=b⋅b^(n−1),b^(0)=1,$ which translates readily into the procedure

**校订前**

考虑计算给定数的指数的问题。我们希望有一个过程，它接受一个底数 $b$ 和一个正整数指数 $n$ 作为参数，并计算 $b^(n)$。做到这一点的一种方式是通过递归定义 $b^(n)=b⋅b^(n−1),b^(0)=1,$，这可以很容易地转化为过程

**校订后**

考虑计算给定数的幂的问题。我们希望有一个过程，它接受一个底数 $b$ 和一个正整数指数 $n$ 作为参数，并计算 $b^(n)$。做到这一点的一种方式是通过递归定义 $b^(n)=b⋅b^(n−1),b^(0)=1,$，这可以很容易地转化为过程

### 1_002e2:0071

**原文**

We can compute exponentials in fewer steps by using successive squaring. For instance, rather than computing $b^(8)$ as $b⋅(b⋅(b⋅(b⋅(b⋅(b⋅(b⋅b)))))),$ we can compute it using three multiplications: $b^(2)=b⋅b,b^(4)=b^(2)⋅b^(2),b^(8)=b^(4)⋅b^(4).$ This method works fine for exponents that are powers of 2. We can also take advantage of successive squaring in computing exponentials in general if we use the rule $b^(n)=(b^(n/2))^(2)ifniseven,b^(n)=b⋅b^(n−1)ifnisodd.$ We can express this method as a procedure:

**校订前**

我们可以通过使用逐次平方来以更少的步数计算指数。例如，与其将 $b^(8)$ 计算为 $b⋅(b⋅(b⋅(b⋅(b⋅(b⋅(b⋅b)))))),$，我们可以用三次乘法来计算它：$b^(2)=b⋅b,b^(4)=b^(2)⋅b^(2),b^(8)=b^(4)⋅b^(4).$ 这种方法对于指数是 2 的幂的情况效果很好。如果我们使用规则 $b^(n)=(b^(n/2))^(2)ifniseven,b^(n)=b⋅b^(n−1)ifnisodd.$，我们也可以利用逐次平方来一般地计算指数。我们可以将此方法表示为一个过程：

**校订后**

我们可以通过使用逐次平方来以更少的步数求幂。例如，与其将 $b^(8)$ 计算为 $b⋅(b⋅(b⋅(b⋅(b⋅(b⋅(b⋅b)))))),$，我们可以用三次乘法来计算它：$b^(2)=b⋅b,b^(4)=b^(2)⋅b^(2),b^(8)=b^(4)⋅b^(4).$ 这种方法对于指数是 2 的幂的情况效果很好。如果我们使用规则 $b^(n)=(b^(n/2))^(2)ifniseven,b^(n)=b⋅b^(n−1)ifnisodd.$，我们也可以利用逐次平方来一般地求幂。我们可以将此方法表示为一个过程：

### 1_002e2:0074

**原文**

The difference between $Θ(log⁡n)$ growth and $Θ(n)$ growth becomes striking as $n$ becomes large. For example, `fast-expt` for $n$ = 1000 requires only 14 multiplications.[注38] It is also possible to use the idea of successive squaring to devise an iterative algorithm that computes exponentials with a logarithmic number of steps (see Exercise 1.16), although, as is often the case with iterative algorithms, this is not written down so straightforwardly as the recursive algorithm.[注39]

**校订前**

随着 $n$ 变大，$Θ(log⁡n)$ 增长与 $Θ(n)$ 增长之间的差异变得惊人。例如，对于 $n$ = 1000，`fast-expt` 只需要 14 次乘法。[注38] 也可以利用逐次平方的思想来设计一种以对数步数计算指数的迭代算法（见 习题 1.16），尽管正如迭代算法常见的情况那样，这并不像递归算法那样直截了当地写出来。[注39]

**校订后**

随着 $n$ 变大，$Θ(log⁡n)$ 增长与 $Θ(n)$ 增长之间的差异变得惊人。例如，对于 $n$ = 1000，`fast-expt` 只需要 14 次乘法。[注38] 也可以利用逐次平方的思想来设计一种以对数步数求幂的迭代算法（见 习题 1.16），尽管正如迭代算法常见的情况那样，这并不像递归算法那样直截了当地写出来。[注39]

### 1_002e2:0075

**原文**

Exercise 1.16: Design a procedure that evolves an iterative exponentiation process that uses successive squaring and uses a logarithmic number of steps, as does `fast-expt`. (Hint: Using the observation that $(b^(n/2))^(2)=(b^(2))^(n/2)$, keep, along with the exponent $n$ and the base $b$, an additional state variable $a$, and define the state transformation in such a way that the product $ab^(n)$ is unchanged from state to state. At the beginning of the process $a$ is taken to be 1, and the answer is given by the value of $a$ at the end of the process. In general, the technique of defining an invariant quantity that remains unchanged from state to state is a powerful way to think about the design of iterative algorithms.)

**校订前**

习题1.16：设计一个过程，它演化出一个迭代的求幂计算过程，该过程使用连续平方，并且像`fast-expt`那样使用对数步数。（提示：利用$(b^(n/2))^(2)=(b^(2))^(n/2)$这一观察，在指数$n$和底数$b$之外，再保留一个附加的状态变量$a$，并以这样的方式定义状态变换：乘积$ab^(n)$在状态之间保持不变。在计算过程开始时，$a$取为1，而答案由计算过程结束时的$a$值给出。一般来说，定义一个在状态之间保持不变的不变量的技术，是思考迭代算法设计的一种强大方式。）

**校订后**

习题1.16：设计一个过程，它演化出一个迭代的求幂计算过程，该过程使用逐次平方，并且像`fast-expt`那样使用对数步数。（提示：利用$(b^(n/2))^(2)=(b^(2))^(n/2)$这一观察，在指数$n$和底数$b$之外，再保留一个附加的状态变量$a$，并以这样的方式定义状态变换：乘积$ab^(n)$在状态之间保持不变。在计算过程开始时，$a$取为1，而答案由计算过程结束时的$a$值给出。一般来说，定义一个在状态之间保持不变的不变量的技术，是思考迭代算法设计的一种强大方式。）

### 1_002e2:0079

**原文**

Exercise 1.19: There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps. Recall the transformation of the state variables $a$ and $b$ in the `fib-iter` process of 1.2.2: $a←a+b$ and $b←a$. Call this transformation $T$, and observe that applying $T$ over and over again $n$ times, starting with 1 and 0, produces the pair $Fib(n+1)$ and $Fib(n)$. In other words, the Fibonacci numbers are produced by applying $T^(n)$, the $n^(th)$ power of the transformation $T$, starting with the pair (1, 0). Now consider $T$ to be the special case of $p=0$ and $q=1$ in a family of transformations $T_{pq}$, where $T_{pq}$ transforms the pair $(a,b)$ according to $a←bq+aq+ap$ and $b←bp+aq$. Show that if we apply such a transformation $T_{pq}$ twice, the effect is the same as using a single transformation $T_{p^(′)q^(′)}$ of the same form, and compute $p^(′)$ and $q^(′)$ in terms of $p$ and $q$. This gives us an explicit way to square these transformations, and thus we can compute $T^(n)$ using successive squaring, as in the `fast-expt` procedure. Put this all together to complete the following procedure, which runs in a logarithmic number of steps:[注41]

**校订前**

习题1.19：有一种巧妙的算法可以在对数步数内计算斐波那契数。回想1.2.2的`fib-iter`计算过程中状态变量$a$和$b$的变换：$a←a+b$和$b←a$。称这个变换为$T$，并观察到从1和0开始，将$T$重复应用$n$次，产生序对$Fib(n+1)$和$Fib(n)$。换句话说，斐波那契数是通过从序对（1，0）开始应用变换$T$的$n^(th)$次幂$T^(n)$而产生的。现在考虑$T$是变换族$T_{pq}$中$p=0$和$q=1$的特殊情况，其中$T_{pq}$根据$a←bq+aq+ap$和$b←bp+aq$变换序对$(a,b)$。证明如果我们应用这样的变换$T_{pq}$两次，其效果等同于使用一个相同形式的单一变换$T_{p^(′)q^(′)}$，并用$p$和$q$计算$p^(′)$和$q^(′)$。这给了我们一种显式的方法来平方这些变换，因此我们可以像`fast-expt`过程那样，使用连续平方来计算$T^(n)$。将所有这些放在一起，完成下面的过程，它运行在对数步数内：[注41]

**校订后**

习题1.19：有一种巧妙的算法可以在对数步数内计算斐波那契数。回想1.2.2的`fib-iter`计算过程中状态变量$a$和$b$的变换：$a←a+b$和$b←a$。称这个变换为$T$，并观察到从1和0开始，将$T$重复应用$n$次，产生序对$Fib(n+1)$和$Fib(n)$。换句话说，斐波那契数是通过从序对（1，0）开始应用变换$T$的$n^(th)$次幂$T^(n)$而产生的。现在考虑$T$是变换族$T_{pq}$中$p=0$和$q=1$的特殊情况，其中$T_{pq}$根据$a←bq+aq+ap$和$b←bp+aq$变换序对$(a,b)$。证明如果我们应用这样的变换$T_{pq}$两次，其效果等同于使用一个相同形式的单一变换$T_{p^(′)q^(′)}$，并用$p$和$q$计算$p^(′)$和$q^(′)$。这给了我们一种显式的方法来平方这些变换，因此我们可以像`fast-expt`过程那样，使用逐次平方来计算$T^(n)$。将所有这些放在一起，完成下面的过程，它运行在对数步数内：[注41]

### 1_002e2:0100

**原文**

(Two numbers are said to be congruent modulo $n$ if they both have the same remainder when divided by $n$. The remainder of a number $a$ when divided by $n$ is also referred to as the remainder of $a$ modulo $n$, or simply as $a$ modulo $n$.)

**校订前**

（两个数被称为 模$n$同余，如果它们除以 $n$ 时都有相同的余数。一个数 $a$ 除以 $n$ 的余数也被称为 $a$ 的余数模$n$，或者简称为 $a$模$n$。）

**校订后**

（如果两个数除以 $n$ 时余数相同，就称它们模$n$同余。一个数 $a$ 除以 $n$ 的余数也称为 $a$ 模$n$ 的余数，或者简称为 $a$ 模$n$。）

### 1_002e2:0109

**原文**

There are variations of the Fermat test that cannot be fooled. In these tests, as with the Fermat method, one tests the primality of an integer $n$ by choosing a random integer $a<n$ and checking some condition that depends upon $n$ and $a$. (See Exercise 1.28 for an example of such a test.) On the other hand, in contrast to the Fermat test, one can prove that, for any $n$, the condition does not hold for most of the integers $a<n$ unless $n$ is prime. Thus, if $n$ passes the test for some random choice of $a$, the chances are better than even that $n$ is prime. If $n$ passes the test for two random choices of $a$, the chances are better than 3 out of 4 that $n$ is prime. By running the test with more and more randomly chosen values of $a$ we can make the probability of error as small as we like.

**校订前**

有一些费马测试的变体是不会被欺骗的。在这些测试中，与费马方法一样，人们通过选择一个随机整数 $a<n$ 并检查某个依赖于 $n$ 和 $a$ 的条件来测试整数 $n$ 的素性。（关于这种测试的一个例子，参见 习题 1.28。）另一方面，与费马测试不同，人们可以证明，对于任何 $n$，除非 $n$ 是素数，否则该条件对大多数整数 $a<n$ 不成立。因此，如果 $n$ 在随机选择某个 $a$ 时通过了测试，那么 $n$ 是素数的机会比一半还大。如果 $n$ 在随机选择两个 $a$ 时通过了测试，那么 $n$ 是素数的机会大于 3 比 4。通过用越来越多随机选择的 $a$ 值运行测试，我们可以使错误的概率小到我们想要的任何程度。

**校订后**

有一些费马测试的变体是不会被欺骗的。在这些测试中，与费马方法一样，人们通过选择一个随机整数 $a<n$ 并检查某个依赖于 $n$ 和 $a$ 的条件来测试整数 $n$ 的素性。（关于这种测试的一个例子，参见 习题 1.28。）另一方面，与费马测试不同，人们可以证明，对于任何 $n$，除非 $n$ 是素数，否则该条件对大多数整数 $a<n$ 不成立。因此，如果 $n$ 在随机选择某个 $a$ 时通过了测试，那么 $n$ 是素数的概率比一半还大。如果 $n$ 在随机选择两个 $a$ 时通过了测试，那么 $n$ 是素数的概率大于 4 分之 3。通过用越来越多随机选择的 $a$ 值运行测试，我们可以使错误的概率小到我们想要的任何程度。

### 1_002e2:0116

**原文**

Exercise 1.25: Alyssa P. Hacker complains that we went to a lot of extra work in writing `expmod`. After all, she says, since we already know how to compute exponentials, we could have simply written

**校订前**

习题 1.25： Alyssa P. Hacker 抱怨说我们在编写 `expmod` 时做了很多额外的工作。她说，毕竟，既然我们已经知道如何计算指数，我们本可以简单地写成

**校订后**

习题 1.25： Alyssa P. Hacker 抱怨说我们在编写 `expmod` 时做了很多额外的工作。她说，毕竟，既然我们已经知道如何求幂，我们本可以简单地写成

### 1_002e2:0128

**原文**

[注33] For example, work through in detail how the reduction rule applies to the problem of making change for 10 cents using pennies and nickels.

**校订前**

[注33]例如，详细推演归约规则如何应用于用便士和镍币为10美分找零的问题。

**校订后**

[注33]例如，详细推演归约规则如何应用于用一美分和五美分硬币为10美分找零的问题。

### 1_002e2:0130

**原文**

[注35] The elements of Pascal’s triangle are called the binomial coefficients, because the $n^(th)$ row consists of the coefficients of the terms in the expansion of $(x+y)^(n)$. This pattern for computing the coefficients appeared in Blaise Pascal’s 1653 seminal work on probability theory, Traité du triangle arithmétique. According to Knuth (1973), the same pattern appears in the Szu-yuen Yü-chien (“The Precious Mirror of the Four Elements”), published by the Chinese mathematician Chu Shih-chieh in 1303, in the works of the twelfth-century Persian poet and mathematician Omar Khayyam, and in the works of the twelfth-century Hindu mathematician Bháscara Áchárya.

**校订前**

[注35]帕斯卡三角形的元素称为 二项式系数，因为第$n^(th)$行由$(x+y)^(n)$展开式中各项的系数组成。这种计算系数的模式出现在 Blaise Pascal 关于概率论的1653开创性著作Traité du triangle arithmétique中。根据Knuth（1973），同样的模式出现在中国数学家朱世杰于1303年出版的Szu-yuen Yü-chien（“四元玉鉴”）中，出现在十二世纪波斯诗人兼数学家 Omar Khayyam 的著作中，以及出现在十二世纪印度数学家 Bháscara Áchárya 的著作中。

**校订后**

[注35]帕斯卡三角形的元素称为 二项式系数，因为第$n^(th)$行由$(x+y)^(n)$展开式中各项的系数组成。这种计算系数的模式出现在 Blaise Pascal 关于概率论的1653年的开创性著作Traité du triangle arithmétique中。根据Knuth（1973），同样的模式出现在中国数学家朱世杰于1303年出版的Szu-yuen Yü-chien（“四元玉鉴”）中，出现在十二世纪波斯诗人兼数学家 Omar Khayyam 的著作中，以及出现在十二世纪印度数学家 Bháscara Áchárya 的著作中。

### 1_002e2:0134

**原文**

[注39] This iterative algorithm is ancient. It appears in the Chandah-sutra by Áchárya Pingala, written before 200 B.C. See Knuth 1981, section 4.6.3, for a full discussion and analysis of this and other methods of exponentiation.

**校订前**

[注39] 这个迭代算法非常古老。它出现在 Áchárya Pingala 所著的Chandah-sutra中，该书成书于200 公元前之前。关于此方法以及其他求幂方法的完整讨论和分析，请参见Knuth 1981，第4.6.3节。

**校订后**

[注39] 这个迭代算法非常古老。它出现在 Áchárya Pingala 所著的Chandah-sutra中，该书成书于公元前200年之前。关于此方法以及其他求幂方法的完整讨论和分析，请参见Knuth 1981，第4.6.3节。

### 1_002e2:0135

**原文**

[注40] This algorithm, which is sometimes known as the “Russian peasant method” of multiplication, is ancient. Examples of its use are found in the Rhind Papyrus, one of the two oldest mathematical documents in existence, written about 1700 B.C. (and copied from an even older document) by an Egyptian scribe named A’h-mose.

**校订前**

[注40] 这个算法，有时被称为乘法的“俄罗斯农民方法”，非常古老。其使用实例见于莱因德纸草书，这是现存最古老的两份数学文献之一，大约成书于1700 公元前（并且是从一份更古老的文献抄写而来），作者是一位名叫 A’h-mose 的埃及抄写员。

**校订后**

[注40] 这个算法，有时被称为乘法的“俄罗斯农民方法”，非常古老。其使用实例见于莱因德纸草书，这是现存最古老的两份数学文献之一，大约成书于公元前1700年（并且是从一份更古老的文献抄写而来），作者是一位名叫 A’h-mose 的埃及抄写员。

### 1_002e2:0137

**原文**

[注42] Euclid’s Algorithm is so called because it appears in Euclid’s Elements (Book 7, ca. 300 B.C.). According to Knuth (1973), it can be considered the oldest known nontrivial algorithm. The ancient Egyptian method of multiplication (Exercise 1.18) is surely older, but, as Knuth explains, Euclid’s algorithm is the oldest known to have been presented as a general algorithm, rather than as a set of illustrative examples.

**校订前**

[注42] 欧几里得算法之所以如此称呼，是因为它出现在欧几里得的Elements中（第7卷，约300 公元前）。根据Knuth（1973），它可以被认为是已知最古老的非平凡算法。古埃及的乘法方法（习题1.18）肯定更古老，但正如 Knuth 所解释的，欧几里得算法是已知最古老的被作为通用算法提出的算法，而不是作为一组说明性例子。

**校订后**

[注42] 欧几里得算法之所以如此称呼，是因为它出现在欧几里得的Elements中（第7卷，约公元前300年）。根据Knuth（1973），它可以被认为是已知最古老的非平凡算法。古埃及的乘法方法（习题1.18）肯定更古老，但正如 Knuth 所解释的，欧几里得算法是已知最古老的被作为通用算法提出的算法，而不是作为一组说明性例子。

### 1_002e2:0138

**原文**

[注43] This theorem was proved in 1845 by Gabriel Lamé, a French mathematician and engineer known chiefly for his contributions to mathematical physics. To prove the theorem, we consider pairs $(a_{k},b_{k})$, where $a_{k}≥b_{k}$, for which Euclid’s Algorithm terminates in $k$ steps. The proof is based on the claim that, if $(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$ are three successive pairs in the reduction process, then we must have $b_{k+1}≥b_{k}+b_{k−1}$. To verify the claim, consider that a reduction step is defined by applying the transformation $a_{k−1}=b_{k}$, $b_{k−1}=$ remainder of $a_{k}$ divided by $b_{k}$. The second equation means that $a_{k}=qb_{k}+b_{k−1}$ for some positive integer $q$. And since $q$ must be at least 1 we have $a_{k}=qb_{k}+b_{k−1}≥b_{k}+b_{k−1}$. But in the previous reduction step we have $b_{k+1}=a_{k}$. Therefore, $b_{k+1}=a_{k}≥b_{k}+b_{k−1}$. This verifies the claim. Now we can prove the theorem by induction on $k$, the number of steps that the algorithm requires to terminate. The result is true for $k=1$, since this merely requires that $b$ be at least as large as $Fib(1)=1$. Now, assume that the result is true for all integers less than or equal to $k$ and establish the result for $k+1$. Let $(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$ be successive pairs in the reduction process. By our induction hypotheses, we have $b_{k−1}≥Fib(k−1)$ and $b_{k}≥Fib(k)$. Thus, applying the claim we just proved together with the definition of the Fibonacci numbers gives $b_{k+1}≥b_{k}+b_{k−1}≥Fib(k)+Fib(k−1)=Fib(k+1)$, which completes the proof of Lamé’s Theorem.

**校订前**

[注43] 这个定理是由加布里埃尔·拉梅于1845年证明的，他是一位法国数学家和工程师，主要以对数学物理的贡献而闻名。为了证明这个定理，我们考虑序对$(a_{k},b_{k})$，其中$a_{k}≥b_{k}$，对于这些序对，欧几里得算法在$k$步内终止。证明基于这样一个论断：如果在归约过程中$(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$是三个相继的序对，那么我们必须有$b_{k+1}≥b_{k}+b_{k−1}$。为了验证这个论断，考虑归约步骤是由应用变换$a_{k−1}=b_{k}$，$b_{k−1}=$$a_{k}$除以$b_{k}$的余数来定义的。第二个等式意味着对于某个正整数$q$，有$a_{k}=qb_{k}+b_{k−1}$。并且由于$q$必须至少为1，我们有$a_{k}=qb_{k}+b_{k−1}≥b_{k}+b_{k−1}$。但在前一个归约步骤中我们有$b_{k+1}=a_{k}$。因此，$b_{k+1}=a_{k}≥b_{k}+b_{k−1}$。这验证了该论断。现在我们可以通过对$k$，即算法终止所需的步数，进行归纳来证明这个定理。对于$k=1$，结果是成立的，因为这仅仅要求$b$至少与$Fib(1)=1$一样大。现在，假设对于所有小于或等于$k$的整数结果都成立，并确立$k+1$的结果。设$(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$为归约过程中的相继序对。根据我们的归纳假设，我们有$b_{k−1}≥Fib(k−1)$和$b_{k}≥Fib(k)$。因此，应用我们刚刚证明的论断以及斐波那契数的定义，得到$b_{k+1}≥b_{k}+b_{k−1}≥Fib(k)+Fib(k−1)=Fib(k+1)$，这就完成了拉梅定理的证明。

**校订后**

[注43] 这个定理是由加布里埃尔·拉梅于1845年证明的，他是一位法国数学家和工程师，主要以对数学物理的贡献而闻名。为了证明这个定理，我们考虑序对$(a_{k},b_{k})$，其中$a_{k}≥b_{k}$，对于这些序对，欧几里得算法在$k$步后终止。证明基于这样一个论断：如果在归约过程中$(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$是三个相继的序对，那么我们必须有$b_{k+1}≥b_{k}+b_{k−1}$。为了验证这个论断，考虑归约步骤是由应用变换$a_{k−1}=b_{k}$，$b_{k−1}=$$a_{k}$除以$b_{k}$的余数来定义的。第二个等式意味着对于某个正整数$q$，有$a_{k}=qb_{k}+b_{k−1}$。并且由于$q$必须至少为1，我们有$a_{k}=qb_{k}+b_{k−1}≥b_{k}+b_{k−1}$。但在前一个归约步骤中我们有$b_{k+1}=a_{k}$。因此，$b_{k+1}=a_{k}≥b_{k}+b_{k−1}$。这验证了该论断。现在我们可以通过对$k$，即算法终止所需的步数，进行归纳来证明这个定理。对于$k=1$，结果是成立的，因为这仅仅要求$b$至少与$Fib(1)=1$一样大。现在，假设对于所有小于或等于$k$的整数结果都成立，并确立$k+1$的结果。设$(a_{k+1},b_{k+1})→(a_{k},b_{k})→(a_{k−1},b_{k−1})$为归约过程中的相继序对。根据我们的归纳假设，我们有$b_{k−1}≥Fib(k−1)$和$b_{k}≥Fib(k)$。因此，应用我们刚刚证明的论断以及斐波那契数的定义，得到$b_{k+1}≥b_{k}+b_{k−1}≥Fib(k)+Fib(k−1)=Fib(k+1)$，这就完成了拉梅定理的证明。

### 1_002e2:0139

**原文**

[注44] If $d$ is a divisor of $n$, then so is $n/d$. But $d$ and $n/d$ cannot both be greater than $sqrt(n)$.

**校订前**

[注44] 如果$d$是$n$的除数，那么$n/d$也是。但$d$和$n/d$不可能都大于$sqrt(n)$。

**校订后**

[注44] 如果$d$是$n$的因子，那么$n/d$也是。但$d$和$n/d$不可能都大于$sqrt(n)$。

### 1_002e2:0142

**原文**

[注47] Numbers that fool the Fermat test are called Carmichael numbers, and little is known about them other than that they are extremely rare. There are 255 Carmichael numbers below 100,000,000. The smallest few are 561, 1105, 1729, 2465, 2821, and 6601. In testing primality of very large numbers chosen at random, the chance of stumbling upon a value that fools the Fermat test is less than the chance that cosmic radiation will cause the computer to make an error in carrying out a “correct” algorithm. Considering an algorithm to be inadequate for the first reason but not for the second illustrates the difference between mathematics and engineering.

**校订前**

[注47] 能骗过费马测试的数被称为 Carmichael 数，除了它们极其罕见之外，人们对它们知之甚少。在100,000,000以下有255个 Carmichael 数。最小的几个是561、1105、1729、2465、2821和6601。在测试随机选取的非常大的数的素性时，碰巧遇到一个能骗过费马测试的值的概率，小于宇宙辐射导致计算机在执行“正确”算法时出错的概率。认为一个算法因第一个原因而不充分，但不因第二个原因而不充分，这说明了数学与工程之间的区别。

**校订后**

[注47] 能骗过费马测试的数被称为 Carmichael 数，除了它们极其罕见之外，人们对它们知之甚少。在100,000,000以下有255个 Carmichael 数。最小的几个是561、1105、1729、2465、2821和6601。在测试随机选取的非常大的数的素性时，碰巧遇到一个能骗过费马测试的值的概率，小于宇宙辐射导致计算机在执行“正确”算法时出错的概率。认为一个算法因第一个原因而不适用，但不因第二个原因而不适用，这说明了数学与工程之间的区别。

### 1_002e3:0004

**原文**

We have seen that procedures are, in effect, abstractions that describe compound operations on numbers independent of the particular numbers. For example, when we

**校订前**

我们已经看到，过程实际上是一种抽象，它描述了对数字的复合操作，而不依赖于具体的数字。例如，当我们

**校订后**

我们已经看到，过程实际上是一种抽象，它描述了对数的复合操作，而不依赖于具体的数。例如，当我们

### 1_002e3:0005

**原文**

we are not talking about the cube of a particular number, but rather about a method for obtaining the cube of any number. Of course we could get along without ever defining this procedure, by always writing expressions such as

**校订前**

我们谈论的不是某个特定数字的立方，而是获得任意数字立方的一种方法。当然，我们完全可以不定义这个过程，而总是写出这样的表达式

**校订后**

我们谈论的不是某个特定数的立方，而是获得任意数立方的一种方法。当然，我们完全可以不定义这个过程，而总是写出这样的表达式

### 1_002e3:0007

**原文**

Yet even in numerical processing we will be severely limited in our ability to create abstractions if we are restricted to procedures whose parameters must be numbers. Often the same programming pattern will be used with a number of different procedures. To express such patterns as concepts, we will need to construct procedures that can accept procedures as arguments or return procedures as values. Procedures that manipulate procedures are called higher-order procedures. This section shows how higher-order procedures can serve as powerful abstraction mechanisms, vastly increasing the expressive power of our language.

**校订前**

然而，即使在数值处理中，如果我们局限于参数必须是数字的过程，我们创建抽象的能力也会受到严重限制。通常，同一个编程模式会被用于许多不同的过程。为了将这类模式表达为概念，我们需要构造能够接受过程作为参数或返回过程作为值的过程。操作过程的过程称为高阶过程。本节展示高阶过程如何作为强大的抽象机制，极大地增强我们语言的表达能力。

**校订后**

然而，即使在数值处理中，如果我们局限于参数必须是数的过程，我们创建抽象的能力也会受到严重限制。通常，同一个编程模式会被用于许多不同的过程。为了将这类模式表达为概念，我们需要构造能够接受过程作为参数或返回过程作为值的过程。操作过程的过程称为高阶过程。本节展示高阶过程如何作为强大的抽象机制，极大地增强我们语言的表达能力。

### 1_002e3:0011

**原文**

The third computes the sum of a sequence of terms in the series $(1)/(1⋅3)+(1)/(5⋅7)+(1)/(9⋅11)+…,$ which converges to $π/8$ (very slowly):[注49]

**校订前**

第三个计算级数$(1)/(1⋅3)+(1)/(5⋅7)+(1)/(9⋅11)+…,$中各项之和，该级数收敛到$π/8$（非常缓慢）：[注49]

**校订后**

第三个计算级数$(1)/(1⋅3)+(1)/(5⋅7)+(1)/(9⋅11)+…,$中一段连续项之和，该级数收敛到$π/8$（非常缓慢）：[注49]

### 1_002e3:0012

**原文**

These three procedures clearly share a common underlying pattern. They are for the most part identical, differing only in the name of the procedure, the function of `a` used to compute the term to be added, and the function that provides the next value of `a`. We could generate each of the procedures by filling in slots in the same template:

**校订前**

这三个过程显然共享一个共同的基本模式。它们大部分是相同的，区别仅在于过程的名称、用于计算待加项的函数`a`，以及提供`a`下一个值的函数。我们可以通过填充同一模板中的空位来生成每一个过程：

**校订后**

这三个过程显然共享一个共同的基本模式。它们大部分是相同的，区别仅在于过程的名称、用于计算待加项的、以`a`为自变量的函数，以及提供`a`下一个值的函数。我们可以通过填充同一模板中的空位来生成每一个过程：

### 1_002e3:0015

**原文**

Notice that `sum` takes as its arguments the lower and upper bounds `a` and `b` together with the procedures `term` and `next`. We can use `sum` just as we would any procedure. For example, we can use it (along with a procedure `inc` that increments its argument by 1) to define `sum-cubes`:

**校订前**

注意`sum`接受上下界`a`和`b`以及过程`term`和`next`作为参数。我们可以像使用任何过程一样使用`sum`。例如，我们可以用它（连同将其参数增加1的过程`inc`）来定义`sum-cubes`：

**校订后**

注意`sum`接受下界和上界`a`和`b`以及过程`term`和`next`作为参数。我们可以像使用任何过程一样使用`sum`。例如，我们可以用它（连同将其参数增加1的过程`inc`）来定义`sum-cubes`：

### 1_002e3:0017

**原文**

With the aid of an identity procedure to compute the term, we can define `sum-integers` in terms of `sum`:

**校订前**

借助一个计算项的单位过程，我们可以用`sum`来定义`sum-integers`：

**校订后**

借助一个计算项的恒等过程，我们可以用`sum`来定义`sum-integers`：

### 1_002e3:0021

**原文**

Once we have `sum`, we can use it as a building block in formulating further concepts. For instance, the definite integral of a function $f$ between the limits $a$ and $b$ can be approximated numerically using the formula $∫abf=[f(a+(dx)/(2))+f(a+dx+(dx)/(2))+f(a+2dx+(dx)/(2))+…]dx$ for small values of $dx$. We can express this directly as a procedure:

**校订前**

一旦我们有了`sum`，就可以将它作为构建进一步概念的构件。例如，函数$f$在极限$a$和$b$之间的定积分可以用公式$∫abf=[f(a+(dx)/(2))+f(a+dx+(dx)/(2))+f(a+2dx+(dx)/(2))+…]dx$在$dx$取小值时进行数值近似。我们可以直接将其表达为一个过程：

**校订后**

一旦我们有了`sum`，就可以将它作为构建进一步概念的构件。例如，函数$f$在积分限$a$和$b$之间的定积分可以用公式$∫abf=[f(a+(dx)/(2))+f(a+dx+(dx)/(2))+f(a+2dx+(dx)/(2))+…]dx$在$dx$取小值时进行数值近似。我们可以直接将其表达为一个过程：

### 1_002e3:0036

**原文**

In using `sum` as in 1.3.1, it seems terribly awkward to have to define trivial procedures such as `pi-term` and `pi-next` just so we can use them as arguments to our higher-order procedure. Rather than define `pi-next` and `pi-term`, it would be more convenient to have a way to directly specify “the procedure that returns its input incremented by 4” and “the procedure that returns the reciprocal of its input times its input plus 2.” We can do this by introducing the special form `lambda`, which creates procedures. Using `lambda` we can describe what we want as

**校订前**

在如 1.3.1 那样使用 `sum` 时，为了能把像 `pi-term` 和 `pi-next` 这样平凡的过程用作高阶过程的参数而不得不定义它们，似乎非常别扭。与其定义 `pi-next` 和 `pi-term`，更方便的是有一种方式直接指定“返回其输入加 4 的过程”和“返回其输入乘以其输入加 2 所得结果的倒数的过程”。我们可以通过引入特殊形式 `lambda` 来做到这一点，它创建过程。使用 `lambda`，我们可以把我们想要的东西描述为

**校订后**

在如 1.3.1 那样使用 `sum` 时，为了能把像 `pi-term` 和 `pi-next` 这样平凡的过程用作高阶过程的参数而不得不定义它们，似乎非常别扭。与其定义 `pi-next` 和 `pi-term`，更方便的是有一种方式直接指定“返回其输入加 4 的过程”和“返回其输入与（其输入加 2）的乘积的倒数的过程”。我们可以通过引入特殊形式 `lambda` 来做到这一点，它创建过程。使用 `lambda`，我们可以把我们想要的东西描述为

### 1_002e3:0065

**原文**

We introduced compound procedures in 1.1.4 as a mechanism for abstracting patterns of numerical operations so as to make them independent of the particular numbers involved. With higher-order procedures, such as the `integral` procedure of 1.3.1, we began to see a more powerful kind of abstraction: procedures used to express general methods of computation, independent of the particular functions involved. In this section we discuss two more elaborate examples—general methods for finding zeros and fixed points of functions—and show how these methods can be expressed directly as procedures.

**校订前**

我们在 1.1.4 中引入了复合过程，作为一种抽象数值运算模式以使它们独立于所涉及的具体数字的机制。借助高阶过程，例如 1.3.1 的 `integral` 过程，我们开始看到一种更强大的抽象：用于表达通用计算方法的过程，独立于所涉及的具体函数。在本节中，我们讨论两个更精细的例子——求函数零点和不动点的通用方法——并展示这些方法如何能直接表达为过程。

**校订后**

我们在 1.1.4 中引入了复合过程，作为一种抽象数值运算模式以使它们独立于所涉及的具体数的机制。借助高阶过程，例如 1.3.1 的 `integral` 过程，我们开始看到一种更强大的抽象：用于表达通用计算方法的过程，独立于所涉及的具体函数。在本节中，我们讨论两个更精细的例子——求函数零点和不动点的通用方法——并展示这些方法如何能直接表达为过程。

### 1_002e3:0068

**原文**

We assume that we are initially given the function $f$ together with points at which its values are negative and positive. We first compute the midpoint of the two given points. Next we check to see if the given interval is small enough, and if so we simply return the midpoint as our answer. Otherwise, we compute as a test value the value of $f$ at the midpoint. If the test value is positive, then we continue the process with a new interval running from the original negative point to the midpoint. If the test value is negative, we continue with the interval from the midpoint to the positive point. Finally, there is the possibility that the test value is 0, in which case the midpoint is itself the root we are searching for.

**校订前**

我们假设最初给定函数 $f$ 以及其值为负和为正的点。我们首先计算两个给定点的中点。接着我们检查给定区间是否足够小，如果是，我们就简单地返回中点作为答案。否则，我们计算 $f$ 在中点处的值作为测试值。如果测试值为正，则我们用从原始负点到中点的新区间继续该过程。如果测试值为负，我们用从中点到正点的区间继续。最后，还有一种可能是测试值为 0，在这种情况下中点本身就是我们要寻找的根。

**校订后**

我们假设最初给定函数 $f$ 以及其值为负和为正的点。我们首先计算两个给不动点的中点。接着我们检查给定区间是否足够小，如果是，我们就简单地返回中点作为答案。否则，我们计算 $f$ 在中点处的值作为测试值。如果测试值为正，则我们用从原来函数值为负的点到中点的新区间继续该过程。如果测试值为负，我们用从中点到函数值为正的点的区间继续。最后，还有一种可能是测试值为 0，在这种情况下中点本身就是我们要寻找的根。

### 1_002e3:0070

**原文**

`Search` is awkward to use directly, because we can accidentally give it points at which $f$’s values do not have the required sign, in which case we get a wrong answer. Instead we will use `search` via the following procedure, which checks to see which of the endpoints has a negative function value and which has a positive value, and calls the `search` procedure accordingly. If the function has the same sign on the two given points, the half-interval method cannot be used, in which case the procedure signals an error.[注56]

**校订前**

`Search` 直接使用起来很别扭，因为我们可能不小心给它提供 $f$ 的值不具有所需符号的点，在这种情况下我们会得到错误的答案。相反，我们将通过以下过程使用 `search`，该过程检查哪个端点的函数值为负、哪个为正，并相应地调用 `search` 过程。如果函数在两个给定点上具有相同的符号，则无法使用半区间法，在这种情况下该过程发出错误信号。[注56]

**校订后**

`Search` 直接使用起来很别扭，因为我们可能不小心给它提供 $f$ 的值不具有所需符号的点，在这种情况下我们会得到错误的答案。相反，我们将通过以下过程使用 `search`，该过程检查哪个端点的函数值为负、哪个为正，并相应地调用 `search` 过程。如果函数在两个给不动点上具有相同的符号，则无法使用半区间法，在这种情况下该过程发出错误信号。[注56]

### 1_002e3:0082

**原文**

Exercise 1.35: Show that the golden ratio $φ$ (1.2.2) is a fixed point of the transformation $x↦1+1/x$, and use this fact to compute $φ$ by means of the `fixed-point` procedure.

**校订前**

习题 1.35： 证明黄金分割率 $φ$（1.2.2）是变换 $x↦1+1/x$ 的一个不动点，并利用这一事实通过 `fixed-point` 过程来计算 $φ$。

**校订后**

习题 1.35： 证明黄金分割比 $φ$（1.2.2）是变换 $x↦1+1/x$ 的一个不动点，并利用这一事实通过 `fixed-point` 过程来计算 $φ$。

### 1_002e3:0088

**原文**

Exercise 1.38: In 1737, the Swiss mathematician Leonhard Euler published a memoir De Fractionibus Continuis, which included a continued fraction expansion for $e−2$, where $e$ is the base of the natural logarithms. In this fraction, the $N_{i}$ are all 1, and the $D_{i}$ are successively 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, …. Write a program that uses your `cont-frac` procedure from Exercise 1.37 to approximate $e$, based on Euler’s expansion.

**校订前**

习题 1.38： 在 1737 年，瑞士数学家 Leonhard Euler 发表了一篇论文 De Fractionibus Continuis，其中包含 $e−2$ 的连分数展开，其中 $e$ 是自然对数的底。在这个分数中，$N_{i}$ 全都等于 1，而 $D_{i}$ 依次为 1、2、1、1、4、1、1、6、1、1、8、…。编写一个程序，使用你在 习题 1.37 中的 `cont-frac` 过程，基于 Euler 的展开来近似 $e$。

**校订后**

习题 1.38： 在 1737 年，瑞士数学家 Leonhard Euler 发表了一篇论文 De Fractionibus Continuis，其中包含 $e−2$ 的连分式展开，其中 $e$ 是自然对数的底。在这个分数中，$N_{i}$ 全都等于 1，而 $D_{i}$ 依次为 1、2、1、1、4、1、1、6、1、1、8、…。编写一个程序，使用你在 习题 1.37 中的 `cont-frac` 过程，基于 Euler 的展开来近似 $e$。

### 1_002e3:0089

**原文**

Exercise 1.39: A continued fraction representation of the tangent function was published in 1770 by the German mathematician J.H. Lambert: $tan⁡x=(x)/(1−(x^(2))/(3−(x^(2))/(5−…))),$ where $x$ is in radians. Define a procedure `(tan-cf x k)` that computes an approximation to the tangent function based on Lambert’s formula. `k` specifies the number of terms to compute, as in Exercise 1.37.

**校订前**

习题 1.39： 德国数学家 J.H. Lambert 在 1770 年发表了正切函数的连分数表示：$tan⁡x=(x)/(1−(x^(2))/(3−(x^(2))/(5−…))),$ 其中 $x$ 以弧度为单位。定义一个过程 `(tan-cf x k)`，基于 Lambert 的公式计算正切函数的近似值。`k` 指定要计算的项数，如同在 习题 1.37 中那样。

**校订后**

习题 1.39： 德国数学家 J.H. Lambert 在 1770 年发表了正切函数的连分式表示：$tan⁡x=(x)/(1−(x^(2))/(3−(x^(2))/(5−…))),$ 其中 $x$ 以弧度为单位。定义一个过程 `(tan-cf x k)`，基于 Lambert 的公式计算正切函数的近似值。`k` 指定要计算的项数，如同在 习题 1.37 中那样。

### 1_002e3:0092

**原文**

We can illustrate this idea by looking again at the fixed-point example described at the end of 1.3.3. We formulated a new version of the square-root procedure as a fixed-point search, starting with the observation that $sqrt(x)$ is a fixed-point of the function $y↦x/y$. Then we used average damping to make the approximations converge. Average damping is a useful general technique in itself. Namely, given a function $f$, we consider the function whose value at $x$ is equal to the average of $x$ and $f(x)$.

**校订前**

我们可以通过再次考察在1.3.3末尾描述的定点示例来说明这一思想。我们将平方根过程的新版本表述为定点搜索，从观察到$sqrt(x)$是函数$y↦x/y$的一个定点开始。然后我们使用平均值阻尼来使近似值收敛。平均值阻尼本身是一种有用的通用技术。即，给定一个函数$f$，我们考虑这样一个函数，它在$x$处的值等于$x$和$f(x)$的平均值。

**校订后**

我们可以通过再次考察在1.3.3末尾描述的不动点示例来说明这一思想。我们将平方根过程的新版本表述为不动点搜索，从观察到$sqrt(x)$是函数$y↦x/y$的一个不动点开始。然后我们使用平均阻尼来使近似值收敛。平均阻尼本身是一种有用的通用技术。即，给定一个函数$f$，我们考虑这样一个函数，它在$x$处的值等于$x$和$f(x)$的平均值。

### 1_002e3:0093

**原文**

We can express the idea of average damping by means of the following procedure:

**校订前**

我们可以通过以下过程来表达平均值阻尼的思想：

**校订后**

我们可以通过以下过程来表达平均阻尼的思想：

### 1_002e3:0096

**原文**

Notice how this formulation makes explicit the three ideas in the method: fixed-point search, average damping, and the function $y↦x/y$. It is instructive to compare this formulation of the square-root method with the original version given in 1.1.7. Bear in mind that these procedures express the same process, and notice how much clearer the idea becomes when we express the process in terms of these abstractions. In general, there are many ways to formulate a process as a procedure. Experienced programmers know how to choose procedural formulations that are particularly perspicuous, and where useful elements of the process are exposed as separate entities that can be reused in other applications. As a simple example of reuse, notice that the cube root of $x$ is a fixed point of the function $y↦x/y^(2)$, so we can immediately generalize our square-root procedure to one that extracts cube roots:[注60]

**校订前**

注意这种表述如何明确地体现了该方法中的三个思想：定点搜索、平均值阻尼和函数$y↦x/y$。将这种平方根方法的表述与1.1.7中给出的原始版本进行比较是有启发性的。请记住，这些过程表达的是同一个计算过程，并注意当我们用这些抽象来表达该过程时，思想变得清晰了多少。一般来说，将计算过程表述为过程有许多方式。有经验的程序员知道如何选择特别清晰的过程表述，并且将计算过程中有用的元素作为可以复用于其他应用的独立实体暴露出来。作为一个简单的复用示例，注意$x$的立方根是函数$y↦x/y^(2)$的一个定点，因此我们可以立即将我们的平方根过程推广为一个提取立方根的过程：[注60]

**校订后**

注意这种表述如何明确地体现了该方法中的三个思想：不动点搜索、平均阻尼和函数$y↦x/y$。将这种平方根方法的表述与1.1.7中给出的原始版本进行比较是有启发性的。请记住，这些过程表达的是同一个计算过程，并注意当我们用这些抽象来表达该过程时，思想变得清晰了多少。一般来说，将计算过程表述为过程有许多方式。有经验的程序员知道如何选择特别清晰的过程表述，并且将计算过程中有用的元素作为可以复用于其他应用的独立实体暴露出来。作为一个简单的复用示例，注意$x$的立方根是函数$y↦x/y^(2)$的一个不动点，因此我们可以立即将我们的平方根过程推广为一个提取立方根的过程：[注60]

### 1_002e3:0098

**原文**

When we first introduced the square-root procedure, in 1.1.7, we mentioned that this was a special case of Newton’s method. If $x↦g(x)$ is a differentiable function, then a solution of the equation $g(x)=0$ is a fixed point of the function $x↦f(x)$ where $f(x)=x−(g(x))/(Dg(x))$ and $Dg(x)$ is the derivative of $g$ evaluated at $x$. Newton’s method is the use of the fixed-point method we saw above to approximate a solution of the equation by finding a fixed point of the function $f$.[注61]

**校订前**

当我们在1.1.7中首次引入平方根过程时，我们提到这是牛顿法的一个特例。如果$x↦g(x)$是一个可微函数，那么方程$g(x)=0$的一个解是函数$x↦f(x)$的一个定点，其中$f(x)=x−(g(x))/(Dg(x))$，而$Dg(x)$是$g$在$x$处的导数。牛顿法是使用我们上面看到的定点方法来通过寻找函数$f$的定点来近似方程的解。[注61]

**校订后**

当我们在1.1.7中首次引入平方根过程时，我们提到这是牛顿法的一个特例。如果$x↦g(x)$是一个可微函数，那么方程$g(x)=0$的一个解是函数$x↦f(x)$的一个不动点，其中$f(x)=x−(g(x))/(Dg(x))$，而$Dg(x)$是$g$在$x$处的导数。牛顿法是使用我们上面看到的不动点方法来通过寻找函数$f$的不动点来近似方程的解。[注61]

### 1_002e3:0100

**原文**

In order to implement Newton’s method as a procedure, we must first express the idea of derivative. Note that “derivative,” like average damping, is something that transforms a function into another function. For instance, the derivative of the function $x↦x^(3)$ is the function $x↦3x^(2)$. In general, if $g$ is a function and $dx$ is a small number, then the derivative $Dg$ of $g$ is the function whose value at any number $x$ is given (in the limit of small $dx$) by $Dg(x)=(g(x+dx)−g(x))/(dx).$ Thus, we can express the idea of derivative (taking $dx$ to be, say, 0.00001) as the procedure

**校订前**

为了将牛顿法实现为一个过程，我们必须首先表达导数的概念。注意，“导数”和平均值阻尼一样，是将一个函数变换为另一个函数的东西。例如，函数$x↦x^(3)$的导数是函数$x↦3x^(2)$。一般来说，如果$g$是一个函数，而$dx$是一个小的数，那么$g$的导数$Dg$是这样一个函数，它在任意数$x$处的值（在$dx$趋于零的极限下）由$Dg(x)=(g(x+dx)−g(x))/(dx).$给出。因此，我们可以将导数的概念（取$dx$为，比如说，0.00001）表达为过程

**校订后**

为了将牛顿法实现为一个过程，我们必须首先表达导数的概念。注意，“导数”和平均阻尼一样，是将一个函数变换为另一个函数的东西。例如，函数$x↦x^(3)$的导数是函数$x↦3x^(2)$。一般来说，如果$g$是一个函数，而$dx$是一个小的数，那么$g$的导数$Dg$是这样一个函数，它在任意数$x$处的值（在$dx$趋于零的极限下）由$Dg(x)=(g(x+dx)−g(x))/(dx).$给出。因此，我们可以将导数的概念（取$dx$为，比如说，0.00001）表达为过程

### 1_002e3:0103

**原文**

With the aid of `deriv`, we can express Newton’s method as a fixed-point process:

**校订前**

借助`deriv`，我们可以将牛顿法表达为一个定点过程：

**校订后**

借助`deriv`，我们可以将牛顿法表达为一个不动点过程：

### 1_002e3:0104

**原文**

The `newton-transform` procedure expresses the formula at the beginning of this section, and `newtons-method` is readily defined in terms of this. It takes as arguments a procedure that computes the function for which we want to find a zero, together with an initial guess. For instance, to find the square root of $x$, we can use Newton’s method to find a zero of the function $y↦y^(2)−x$ starting with an initial guess of 1.[注63]

**校订前**

`newton-transform`过程表达了本节开头的公式，而`newtons-method`可以很容易地基于它来定义。它接受一个计算我们想要求零的函数的过程，以及一个初始猜测作为参数。例如，为了求$x$的平方根，我们可以使用牛顿法来求函数$y↦y^(2)−x$的零点，从初始猜测1开始。[注63]

**校订后**

`newton-transform`过程表达了本节开头的公式，而`newtons-method`可以很容易地基于它来定义。它接受一个计算我们想要求零点的函数的过程，以及一个初始猜测作为参数。例如，为了求$x$的平方根，我们可以使用牛顿法来求函数$y↦y^(2)−x$的零点，从初始猜测1开始。[注63]

### 1_002e3:0107

**原文**

We’ve seen two ways to express the square-root computation as an instance of a more general method, once as a fixed-point search and once using Newton’s method. Since Newton’s method was itself expressed as a fixed-point process, we actually saw two ways to compute square roots as fixed points. Each method begins with a function and finds a fixed point of some transformation of the function. We can express this general idea itself as a procedure:

**校订前**

我们已经看到了两种将平方根计算表达为更一般方法实例的方式，一次作为定点搜索，一次使用牛顿法。由于牛顿法本身被表达为定点过程，我们实际上看到了两种将平方根计算为定点的方式。每种方法都从一个函数开始，并找到该函数的某种变换的定点。我们可以将这个一般思想本身表达为一个过程：

**校订后**

我们已经看到了两种将平方根计算表达为更一般方法实例的方式，一次作为不动点搜索，一次使用牛顿法。由于牛顿法本身被表达为不动点过程，我们实际上看到了两种将平方根计算为不动点的方式。每种方法都从一个函数开始，并找到该函数的某种变换的不动点。我们可以将这个一般思想本身表达为一个过程：

### 1_002e3:0108

**原文**

This very general procedure takes as its arguments a procedure `g` that computes some function, a procedure that transforms `g`, and an initial guess. The returned result is a fixed point of the transformed function.

**校订前**

这个非常一般的过程接受一个计算某个函数的过程`g`、一个变换`g`的过程以及一个初始猜测作为参数。返回的结果是变换后函数的定点。

**校订后**

这个非常一般的过程接受一个计算某个函数的过程`g`、一个变换`g`的过程以及一个初始猜测作为参数。返回的结果是变换后函数的不动点。

### 1_002e3:0109

**原文**

Using this abstraction, we can recast the first square-root computation from this section (where we look for a fixed point of the average-damped version of $y↦x/y$) as an instance of this general method:

**校订前**

使用这个抽象，我们可以将本节中的第一个平方根计算（其中我们寻找$y↦x/y$的平均值阻尼版本的定点）重新表述为这个一般方法的一个实例：

**校订后**

使用这个抽象，我们可以将本节中的第一个平方根计算（其中我们寻找$y↦x/y$的平均阻尼版本的不动点）重新表述为这个一般方法的一个实例：

### 1_002e3:0110

**原文**

Similarly, we can express the second square-root computation from this section (an instance of Newton’s method that finds a fixed point of the Newton transform of $y↦y^(2)−x$) as

**校订前**

类似地，我们可以将本节中的第二个平方根计算（牛顿法的一个实例，它寻找$y↦y^(2)−x$的牛顿变换的定点）表达为

**校订后**

类似地，我们可以将本节中的第二个平方根计算（牛顿法的一个实例，它寻找$y↦y^(2)−x$的牛顿变换的不动点）表达为

### 1_002e3:0120

**原文**

to approximate zeros of the cubic $x^(3)+ax^(2)+bx+c$.

**校订前**

以近似三次方程 $x^(3)+ax^(2)+bx+c$ 的零点。

**校订后**

以近似三次多项式 $x^(3)+ax^(2)+bx+c$ 的零点。

### 1_002e3:0122

**原文**

Exercise 1.42: Let $f$ and $g$ be two one-argument functions. The composition $f$ after $g$ is defined to be the function $x↦f(g(x))$. Define a procedure `compose` that implements composition. For example, if `inc` is a procedure that adds 1 to its argument,

**校订前**

习题 1.42： 设 $f$ 和 $g$ 是两个单参数函数。 复合 $f$ 在 $g$ 之后被定义为函数 $x↦f(g(x))$。定义一个实现复合的过程 `compose`。例如，如果 `inc` 是一个将其参数加 1 的过程，

**校订后**

习题 1.42： 设 $f$ 和 $g$ 是两个单参数函数。先应用 $g$ 再应用 $f$ 的复合定义为函数 $x↦f(g(x))$。定义一个实现复合的过程 `compose`。例如，如果 `inc` 是一个将其参数加 1 的过程，

### 1_002e3:0125

**原文**

Exercise 1.44: The idea of smoothing a function is an important concept in signal processing. If $f$ is a function and $dx$ is some small number, then the smoothed version of $f$ is the function whose value at a point $x$ is the average of $f(x−dx)$, $f(x)$, and $f(x+dx)$. Write a procedure `smooth` that takes as input a procedure that computes $f$ and returns a procedure that computes the smoothed $f$. It is sometimes valuable to repeatedly smooth a function (that is, smooth the smoothed function, and so on) to obtain the n-fold smoothed function. Show how to generate the n-fold smoothed function of any given function using `smooth` and `repeated` from Exercise 1.43.

**校订前**

习题 1.44： 对函数进行 平滑 的思想是信号处理中的一个重要概念。如果 $f$ 是一个函数，且 $dx$ 是某个小数，那么 $f$ 的平滑版本是在点 $x$ 处的值为 $f(x−dx)$、$f(x)$ 和 $f(x+dx)$ 的平均值的函数。编写一个过程 `smooth`，它接受一个计算 $f$ 的过程作为输入，并返回一个计算平滑后的 $f$ 的过程。有时反复平滑一个函数（即，平滑平滑后的函数，依此类推）以获得 n重平滑函数 是很有价值的。展示如何使用 习题 1.43 中的 `smooth` 和 `repeated` 生成任何给定函数的 n重平滑函数。

**校订后**

习题 1.44： 对函数进行 平滑 的思想是信号处理中的一个重要概念。如果 $f$ 是一个函数，且 $dx$ 是某个很小的数，那么 $f$ 的平滑版本是在点 $x$ 处的值为 $f(x−dx)$、$f(x)$ 和 $f(x+dx)$ 的平均值的函数。编写一个过程 `smooth`，它接受一个计算 $f$ 的过程作为输入，并返回一个计算平滑后的 $f$ 的过程。有时反复平滑一个函数（即，平滑平滑后的函数，依此类推）以获得 n重平滑函数 是很有价值的。展示如何使用 `smooth` 和 习题 1.43 中的 `repeated` 生成任何给定函数的 n重平滑函数。

### 2_002e1:0028

**原文**

We can envision the structure of the rational-number system as shown in Figure 2.1. The horizontal lines represent abstraction barriers that isolate different “levels” of the system. At each level, the barrier separates the programs (above) that use the data abstraction from the programs (below) that implement the data abstraction. Programs that use rational numbers manipulate them solely in terms of the procedures supplied “for public use” by the rational-number package: `add-rat`, `sub-rat`, `mul-rat`, `div-rat`, and `equal-rat?`. These, in turn, are implemented solely in terms of the constructor and selectors `make-rat`, `numer`, and `denom`, which themselves are implemented in terms of pairs. The details of how pairs are implemented are irrelevant to the rest of the rational-number package so long as pairs can be manipulated by the use of `cons`, `car`, and `cdr`. In effect, procedures at each level are the interfaces that define the abstraction barriers and connect the different levels.

**校订前**

我们可以将有理数系统的结构设想为图2.1所示。水平线表示抽象屏障，它们隔离了系统中不同的“层次”。在每一层，屏障将使用数据抽象的程序（上方）与实现数据抽象的程序（下方）分开。使用有理数的程序仅通过有理数包“供公共使用”所提供的过程来操作它们：`add-rat`、`sub-rat`、`mul-rat`、`div-rat`和`equal-rat?`。而这些过程又仅通过构造器和选择器`make-rat`、`numer`和`denom`来实现，后者本身又是基于序对实现的。只要序对可以通过`cons`、`car`和`cdr`来操作，序对如何实现的细节对于有理数包的其余部分就是无关紧要的。实际上，每一层的过程都是定义抽象屏障并连接不同层次的接口。

**校订后**

我们可以将有理数系统的结构设想为图2.1所示。水平线表示抽象屏障，它们隔离了系统中不同的“层次”。在每一层，屏障将使用数据抽象的程序（上方）与实现数据抽象的程序（下方）分开。使用有理数的程序仅通过有理数包“供公共使用”所提供的过程来操作它们：`add-rat`、`sub-rat`、`mul-rat`、`div-rat`和`equal-rat?`。而这些过程又仅通过构造函数和选择函数`make-rat`、`numer`和`denom`来实现，后者本身又是基于序对实现的。只要序对可以通过`cons`、`car`和`cdr`来操作，序对如何实现的细节对于有理数包的其余部分就是无关紧要的。实际上，每一层的过程都是定义抽象屏障并连接不同层次的接口。

### 2_002e1:0031

**原文**

For example, an alternate way to address the problem of reducing rational numbers to lowest terms is to perform the reduction whenever we access the parts of a rational number, rather than when we construct it. This leads to different constructor and selector procedures:

**校订前**

例如，解决将有理数约简为最简形式这一问题的另一种方法是在我们访问有理数的各部分时执行约简，而不是在构造它时执行。这导致了不同的构造器和选择器过程：

**校订后**

例如，解决将有理数约简为最简形式这一问题的另一种方法是在我们访问有理数的各部分时执行约简，而不是在构造它时执行。这导致了不同的构造函数和选择函数过程：

### 2_002e1:0034

**原文**

Exercise 2.2: Consider the problem of representing line segments in a plane. Each segment is represented as a pair of points: a starting point and an ending point. Define a constructor `make-segment` and selectors `start-segment` and `end-segment` that define the representation of segments in terms of points. Furthermore, a point can be represented as a pair of numbers: the $x$ coordinate and the $y$ coordinate. Accordingly, specify a constructor `make-point` and selectors `x-point` and `y-point` that define this representation. Finally, using your selectors and constructors, define a procedure `midpoint-segment` that takes a line segment as argument and returns its midpoint (the point whose coordinates are the average of the coordinates of the endpoints). To try your procedures, you’ll need a way to print points:

**校订前**

习题2.2：考虑在平面中表示线段的问题。每条线段表示为一对点：一个起点和一个终点。定义一个构造器`make-segment`以及选择器`start-segment`和`end-segment`，它们基于点来定义线段的表示。此外，一个点可以表示为一对数字：$x$坐标和$y$坐标。相应地，指定一个构造器`make-point`以及选择器`x-point`和`y-point`来定义这种表示。最后，使用你的选择器和构造器，定义一个过程`midpoint-segment`，它接受一条线段作为参数并返回其中点（其坐标是端点坐标平均值的点）。为了试验你的过程，你需要一种打印点的方法：

**校订后**

习题2.2：考虑在平面中表示线段的问题。每条线段表示为一对点：一个起点和一个终点。定义一个构造函数`make-segment`以及选择函数`start-segment`和`end-segment`，它们基于点来定义线段的表示。此外，一个点可以表示为一对数字：$x$坐标和$y$坐标。相应地，指定一个构造函数`make-point`以及选择函数`x-point`和`y-point`来定义这种表示。最后，使用你的选择函数和构造函数，定义一个过程`midpoint-segment`，它接受一条线段作为参数并返回其中点（其坐标是端点坐标平均值的点）。为了试验你的过程，你需要一种打印点的方法：

### 2_002e1:0035

**原文**

Exercise 2.3: Implement a representation for rectangles in a plane. (Hint: You may want to make use of Exercise 2.2.) In terms of your constructors and selectors, create procedures that compute the perimeter and the area of a given rectangle. Now implement a different representation for rectangles. Can you design your system with suitable abstraction barriers, so that the same perimeter and area procedures will work using either representation?

**校订前**

习题2.3：实现平面中矩形的一种表示。（提示：你可能想利用习题2.2。）基于你的构造器和选择器，创建计算给定矩形的周长和面积的过程。现在实现矩形的另一种表示。你能用合适的抽象屏障来设计你的系统，使得相同的周长和面积过程在两种表示下都能工作吗？

**校订后**

习题2.3：实现平面中矩形的一种表示。（提示：你可能想利用习题2.2。）基于你的构造函数和选择函数，创建计算给定矩形的周长和面积的过程。现在实现矩形的另一种表示。你能用合适的抽象屏障来设计你的系统，使得相同的周长和面积过程在两种表示下都能工作吗？

### 2_002e1:0038

**原文**

But exactly what is meant by data? It is not enough to say “whatever is implemented by the given selectors and constructors.” Clearly, not every arbitrary set of three procedures can serve as an appropriate basis for the rational-number implementation. We need to guarantee that, if we construct a rational number `x` from a pair of integers `n` and `d`, then extracting the `numer` and the `denom` of `x` and dividing them should yield the same result as dividing `n` by `d`. In other words, `make-rat`, `numer`, and `denom` must satisfy the condition that, for any integer `n` and any non-zero integer `d`, if `x` is `(make-rat n d)`, then $((numerx))/((denomx))=(n)/(d).$ In fact, this is the only condition `make-rat`, `numer`, and `denom` must fulfill in order to form a suitable basis for a rational-number representation. In general, we can think of data as defined by some collection of selectors and constructors, together with specified conditions that these procedures must fulfill in order to be a valid representation.[注71]

**校订前**

但数据究竟是什么意思呢？仅仅说“由给定的选择器和构造器所实现的任何东西”是不够的。显然，并非任意三个过程的集合都能作为有理数实现的合适基础。我们需要保证，如果我们从一对整数`n`和`d`构造出一个有理数`x`，那么提取`x`的`numer`和`denom`并将它们相除，应该得到与`n`除以`d`相同的结果。换句话说，`make-rat`、`numer`和`denom`必须满足这样的条件：对于任意整数`n`和任意非零整数`d`，如果`x`是`(make-rat n d)`，那么$((numerx))/((denomx))=(n)/(d).$。事实上，这就是`make-rat`、`numer`和`denom`为了构成有理数表示的合适基础所必须满足的唯一条件。一般来说，我们可以把数据看作是由某个选择器和构造器的集合，连同这些过程为了成为有效表示所必须满足的指定条件一起定义的。[注71]

**校订后**

但数据究竟是什么意思呢？仅仅说“由给定的选择函数和构造函数所实现的任何东西”是不够的。显然，并非任意三个过程的集合都能作为有理数实现的合适基础。我们需要保证，如果我们从一对整数`n`和`d`构造出一个有理数`x`，那么提取`x`的`numer`和`denom`并将它们相除，应该得到与`n`除以`d`相同的结果。换句话说，`make-rat`、`numer`和`denom`必须满足这样的条件：对于任意整数`n`和任意非零整数`d`，如果`x`是`(make-rat n d)`，那么$((numerx))/((denomx))=(n)/(d).$。事实上，这就是`make-rat`、`numer`和`denom`为了构成有理数表示的合适基础所必须满足的唯一条件。一般来说，我们可以把数据看作是由某个选择函数和构造函数的集合，连同这些过程为了成为有效表示所必须满足的指定条件一起定义的。[注71]

### 2_002e1:0047

**原文**

This representation is known as Church numerals, after its inventor, Alonzo Church, the logician who invented the λ-calculus.

**校订前**

这种表示被称为丘奇计数，以其发明者阿隆佐·丘奇命名，他是发明了 λ 演算的逻辑学家。

**校订后**

这种表示被称为丘奇数，以其发明者阿隆佐·丘奇命名，他是发明了 λ 演算的逻辑学家。

### 2_002e1:0051

**原文**

Electrical engineers will be using Alyssa’s system to compute electrical quantities. It is sometimes necessary for them to compute the value of a parallel equivalent resistance $R_{p}$ of two resistors $R_{1}$ and $R_{2}$ using the formula $R_{p}=(1)/(1/R_{1}+1/R_{2}).$ Resistance values are usually known only up to some tolerance guaranteed by the manufacturer of the resistor. For example, if you buy a resistor labeled “6.8 ohms with 10% tolerance” you can only be sure that the resistor has a resistance between 6.8 $−$ 0.68 = 6.12 and 6.8 + 0.68 = 7.48 ohms. Thus, if you have a 6.8-ohm 10% resistor in parallel with a 4.7-ohm 5% resistor, the resistance of the combination can range from about 2.58 ohms (if the two resistors are at the lower bounds) to about 2.97 ohms (if the two resistors are at the upper bounds).

**校订前**

电气工程师将使用 Alyssa 的系统来计算电量。他们有时需要计算两个电阻 $R_{1}$ 和 $R_{2}$ 的并联等效电阻 $R_{p}$ 的值，使用公式 $R_{p}=(1)/(1/R_{1}+1/R_{2}).$ 电阻值通常只知道在电阻制造商保证的某个容差范围内。例如，如果你买了一个标有“6.8 欧姆，容差 10%”的电阻，你只能确定该电阻的阻值在 6.8 $−$ 0.68 = 6.12 和 6.8 + 0.68 = 7.48 欧姆之间。因此，如果你有一个 6.8 欧姆 10% 的电阻与一个 4.7 欧姆 5% 的电阻并联，组合的电阻范围大约从 2.58 欧姆（如果两个电阻都处于下界）到大约 2.97 欧姆（如果两个电阻都处于上界）。

**校订后**

电气工程师将使用 Alyssa 的系统来计算电气量。他们有时需要计算两个电阻 $R_{1}$ 和 $R_{2}$ 的并联等效电阻 $R_{p}$ 的值，使用公式 $R_{p}=(1)/(1/R_{1}+1/R_{2}).$ 电阻值通常只知道在电阻制造商保证的某个容差范围内。例如，如果你买了一个标有“6.8 欧姆，容差 10%”的电阻，你只能确定该电阻的阻值在 6.8 $−$ 0.68 = 6.12 和 6.8 + 0.68 = 7.48 欧姆之间。因此，如果你有一个 6.8 欧姆 10% 的电阻与一个 4.7 欧姆 5% 的电阻并联，组合的电阻范围大约从 2.58 欧姆（如果两个电阻都处于下界）到大约 2.97 欧姆（如果两个电阻都处于上界）。

### 2_002e1:0053

**原文**

Alyssa postulates the existence of an abstract object called an “interval” that has two endpoints: a lower bound and an upper bound. She also presumes that, given the endpoints of an interval, she can construct the interval using the data constructor `make-interval`. Alyssa first writes a procedure for adding two intervals. She reasons that the minimum value the sum could be is the sum of the two lower bounds and the maximum value it could be is the sum of the two upper bounds:

**校订前**

Alyssa 假设存在一个称为“区间”的抽象对象，它有两个端点：下界和上界。她还假定，给定区间的端点，她可以使用数据构造器 `make-interval` 来构造该区间。Alyssa 首先编写了一个将两个区间相加的过程。她推断，和可能的最小值是两个下界之和，可能的最大值是两个上界之和：

**校订后**

Alyssa 假设存在一个称为“区间”的抽象对象，它有两个端点：下界和上界。她还假定，给定区间的端点，她可以使用数据构造函数 `make-interval` 来构造该区间。Alyssa 首先编写了一个将两个区间相加的过程。她推断，和可能的最小值是两个下界之和，可能的最大值是两个上界之和：

### 2_002e1:0055

**原文**

To divide two intervals, Alyssa multiplies the first by the reciprocal of the second. Note that the bounds of the reciprocal interval are the reciprocal of the upper bound and the reciprocal of the lower bound, in that order.

**校订前**

为了除以两个区间，Alyssa 将第一个区间乘以第二个区间的倒数。注意，倒数区间的边界是上界的倒数和下界的倒数，按此顺序。

**校订后**

为了将两个区间相除，Alyssa 将第一个区间乘以第二个区间的倒数。注意，倒数区间的边界是上界的倒数和下界的倒数，按此顺序。

### 2_002e1:0056

**原文**

Exercise 2.7: Alyssa’s program is incomplete because she has not specified the implementation of the interval abstraction. Here is a definition of the interval constructor:

**校订前**

习题 2.7： Alyssa 的程序不完整，因为她没有指定区间抽象的实现。下面是区间构造器的一个定义：

**校订后**

习题 2.7： Alyssa 的程序不完整，因为她没有指定区间抽象的实现。下面是区间构造函数的一个定义：

### 2_002e1:0062

**原文**

After debugging her program, Alyssa shows it to a potential user, who complains that her program solves the wrong problem. He wants a program that can deal with numbers represented as a center value and an additive tolerance; for example, he wants to work with intervals such as 3.5 $±$ 0.15 rather than [3.35, 3.65]. Alyssa returns to her desk and fixes this problem by supplying an alternate constructor and alternate selectors:

**校订前**

在调试完她的程序后，Alyssa 将其展示给一位潜在用户，该用户抱怨她的程序解决的是错误的问题。他想要一个能够处理以中心值和加法容差表示的数的程序；例如，他想要处理诸如 3.5 $±$ 0.15 这样的区间，而不是 [3.35, 3.65]。Alyssa 回到她的办公桌，通过提供另一个构造器和另一个选择函数来修复这个问题：

**校订后**

在调试完她的程序后，Alyssa 将其展示给一位潜在用户，该用户抱怨她的程序解决的是错误的问题。他想要一个能够处理以中心值和加法容差表示的数的程序；例如，他想要处理诸如 3.5 $±$ 0.15 这样的区间，而不是 [3.35, 3.65]。Alyssa 回到她的办公桌，通过提供另一个构造函数和另一组选择函数来修复这个问题：

### 2_002e1:0064

**原文**

Exercise 2.12: Define a constructor `make-center-percent` that takes a center and a percentage tolerance and produces the desired interval. You must also define a selector `percent` that produces the percentage tolerance for a given interval. The `center` selector is the same as the one shown above.

**校订前**

习题 2.12： 定义一个构造器 `make-center-percent`，它接受一个中心值和一个百分比容差，并产生所需的区间。你还必须定义一个选择函数 `percent`，它产生给定区间的百分比容差。`center` 选择函数与上面所示相同。

**校订后**

习题 2.12： 定义一个构造函数 `make-center-percent`，它接受一个中心值和一个百分比容差，并产生所需的区间。你还必须定义一个选择函数 `percent`，它产生给定区间的百分比容差。`center` 选择函数与上面所示相同。

### 2_002e2:0003

**原文**

2.2 Hierarchical Data and the Closure Property

**校订前**

2.2 层次化数据和闭包性质

**校订后**

2.2 层次化数据和闭合性质

### 2_002e2:0004

**原文**

As we have seen, pairs provide a primitive “glue” that we can use to construct compound data objects. Figure 2.2 shows a standard way to visualize a pair—in this case, the pair formed by `(cons 1 2)`. In this representation, which is called box-and-pointer notation, each object is shown as a pointer to a box. The box for a primitive object contains a representation of the object. For example, the box for a number contains a numeral. The box for a pair is actually a double box, the left part containing (a pointer to) the `car` of the pair and the right part containing the `cdr`.

**校订前**

正如我们所见，序对提供了一种基本的“粘合剂”，我们可以用它来构造复合数据对象。图 2.2 展示了可视化序对的标准方式——在本例中，是由 `(cons 1 2)` 形成的序对。在这种称为 盒指针表示法 的表示中，每个对象都显示为指向一个盒子的 指针。基本对象的盒子包含该对象的表示。例如，数字的盒子包含一个数字符号。序对的盒子实际上是一个双盒子，左边部分包含（指向）该序对的 `car`，右边部分包含 `cdr`。

**校订后**

正如我们所见，序对提供了一种基本的“粘合剂”，我们可以用它来构造复合数据对象。图 2.2 展示了可视化序对的标准方式——在本例中，是由 `(cons 1 2)` 形成的序对。在这种称为 盒指针表示法 的表示中，每个对象都显示为指向一个盒子的 指针。基本对象的盒子包含该对象的表示。例如，表示数的盒子包含一个数码。序对的盒子实际上是一个双盒子，左边部分包含（指向该序对的 `car`的指针），右边部分包含 `cdr`。

### 2_002e2:0008

**原文**

The ability to create pairs whose elements are pairs is the essence of list structure’s importance as a representational tool. We refer to this ability as the closure property of `cons`. In general, an operation for combining data objects satisfies the closure property if the results of combining things with that operation can themselves be combined using the same operation.[注72] Closure is the key to power in any means of combination because it permits us to create hierarchical structures—structures made up of parts, which themselves are made up of parts, and so on.

**校订前**

创建其元素也是序对的序对的能力，是表结构作为表示工具之所以重要的本质所在。我们将这种能力称为闭包性质，即`cons`的闭包性质。一般来说，如果使用某个操作组合事物所得到的结果本身还能用同一个操作来组合，那么用于组合数据对象的操作就满足闭包性质。[注72]闭包是任何组合手段具有威力的关键，因为它允许我们创建层次结构——这种结构由部分组成，而部分本身又由部分组成，如此等等。

**校订后**

创建其元素也是序对的序对的能力，是表结构作为表示工具之所以重要的本质所在。我们将这种能力称为闭合性质，即`cons`的闭合性质。一般来说，如果使用某个操作组合事物所得到的结果本身还能用同一个操作来组合，那么用于组合数据对象的操作就满足闭合性质。[注72]闭合性是任何组合手段具有威力的关键，因为它允许我们创建层次结构——这种结构由部分组成，而部分本身又由部分组成，如此等等。

### 2_002e2:0009

**原文**

From the outset of Chapter 1, we’ve made essential use of closure in dealing with procedures, because all but the very simplest programs rely on the fact that the elements of a combination can themselves be combinations. In this section, we take up the consequences of closure for compound data. We describe some conventional techniques for using pairs to represent sequences and trees, and we exhibit a graphics language that illustrates closure in a vivid way.[注73]

**校订前**

从第1章一开始，我们就已经在处理过程时必不可少地使用了闭包，因为除了最简单的程序之外，所有程序都依赖于组合式的元素本身也可以是组合式这一事实。在本节中，我们讨论闭包对复合数据的影响。我们描述一些使用序对表示序列和树的常规技术，并展示一种图形语言，它以生动的方式说明了闭包。[注73]

**校订后**

从第1章一开始，我们就已经在处理过程时必不可少地使用了闭合性，因为除了最简单的程序之外，所有程序都依赖于组合式的元素本身也可以是组合式这一事实。在本节中，我们讨论闭合性对复合数据的影响。我们描述一些使用序对表示序列和树的常规技术，并展示一种图形语言，它以生动的方式说明了闭合性。[注73]

### 2_002e2:0017

**原文**

We can think of `car` as selecting the first item in the list, and of `cdr` as selecting the sublist consisting of all but the first item. Nested applications of `car` and `cdr` can be used to extract the second, third, and subsequent items in the list.[注75] The constructor `cons` makes a list like the original one, but with an additional item at the beginning.

**校订前**

我们可以把`car`看作选择表中的第一项，把`cdr`看作选择由除第一项之外的所有项组成的子表。嵌套应用`car`和`cdr`可以用来提取表中的第二项、第三项以及后续项。[注75]构造器`cons`构造一个像原来那样的表，但在开头增加了一项。

**校订后**

我们可以把`car`看作选择表中的第一项，把`cdr`看作选择由除第一项之外的所有项组成的子表。嵌套应用`car`和`cdr`可以用来提取表中的第二项、第三项以及后续项。[注75]构造函数`cons`构造一个像原来那样的表，但在开头增加了一项。

### 2_002e2:0032

**原文**

Otherwise, `append` the `cdr` of `list1` and `list2`, and `cons` the `car` of `list1` onto the result:

**校订前**

否则，`append``list1`和`list2`的`cdr`，并将`list1`的`car``cons`到结果上：

**校订后**

否则，将`list1`的`cdr`与`list2`用`append`连接，并将`list1`的`car`用`cons`添加到结果前面：

### 2_002e2:0034

**原文**

Exercise 2.18: Define a procedure `reverse` that takes a list as argument and returns a list of the same elements in reverse order:

**校订前**

习题2.18： 定义一个过程`reverse`，它接受一个表作为参数，并返回一个包含相同元素但顺序相反的列表：

**校订后**

习题2.18： 定义一个过程`reverse`，它接受一个表作为参数，并返回一个包含相同元素但顺序相反的表：

### 2_002e2:0036

**原文**

We want to rewrite the procedure `cc` so that its second argument is a list of the values of the coins to use rather than an integer specifying which coins to use. We could then have lists that defined each kind of currency:

**校订前**

我们想要重写过程`cc`，使其第二个参数是一个要使用的硬币值的表，而不是一个指定使用哪些硬币的整数。然后我们就可以用表来定义每种货币：

**校订后**

我们想要重写过程`cc`，使其第二个参数是一个要使用的硬币面额的表，而不是一个指定使用哪些硬币的整数。然后我们就可以用表来定义每种货币：

### 2_002e2:0076

**原文**

Exercise 2.24: Suppose we evaluate the expression `(list 1 (list 2 (list 3 4)))`. Give the result printed by the interpreter, the corresponding box-and-pointer structure, and the interpretation of this as a tree (as in Figure 2.6).

**校订前**

习题 2.24：假设我们求值表达式`(list 1 (list 2 (list 3 4)))`。给出解释器打印的结果、相应的箱指针结构，以及将其解释为树的结果（如图 2.6中那样）。

**校订后**

习题 2.24：假设我们求值表达式`(list 1 (list 2 (list 3 4)))`。给出解释器打印的结果、相应的盒指针结构，以及将其解释为树的结果（如图 2.6中那样）。

### 2_002e2:0096

**原文**

Exercise 2.32: We can represent a set as a list of distinct elements, and we can represent the set of all subsets of the set as a list of lists. For example, if the set is `(1 2 3)`, then the set of all subsets is `(() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))`. Complete the following definition of a procedure that generates the set of subsets of a set and give a clear explanation of why it works:

**校订前**

习题 2.32：我们可以将一个集合表示为一个不同元素的表，并且我们可以将该集合的所有子集表示为一个表的表。例如，如果集合是`(1 2 3)`，那么所有子集的集合是`(() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))`。完成以下生成集合的所有子集的过程的定义，并给出清晰的解释说明它为什么有效：

**校订后**

习题 2.32：我们可以将一个集合表示为一个由互不相同的元素组成的表，并且我们可以将该集合的所有子集表示为一个表的表。例如，如果集合是`(1 2 3)`，那么所有子集的集合是`(() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))`。完成以下生成集合的所有子集的过程的定义，并给出清晰的解释说明它为什么有效：

### 2_002e2:0097

**原文**

2.2.3 Sequences as Conventional Interfaces

**校订前**

2.2.3 序列作为常规接口

**校订后**

2.2.3 序列作为约定接口

### 2_002e2:0098

**原文**

In working with compound data, we’ve stressed how data abstraction permits us to design programs without becoming enmeshed in the details of data representations, and how abstraction preserves for us the flexibility to experiment with alternative representations. In this section, we introduce another powerful design principle for working with data structures—the use of conventional interfaces.

**校订前**

在处理复合数据时，我们强调了数据抽象如何使我们能够设计程序而不陷入数据表示的细节，以及抽象如何为我们保留了尝试其他表示的灵活性。在本节中，我们介绍另一种处理数据结构的强大设计原则——使用常规接口。

**校订后**

在处理复合数据时，我们强调了数据抽象如何使我们能够设计程序而不陷入数据表示的细节，以及抽象如何为我们保留了尝试其他表示的灵活性。在本节中，我们介绍另一种处理数据结构的强大设计原则——使用约定接口。

### 2_002e2:0113

**原文**

Unfortunately, the two procedure definitions above fail to exhibit this signal-flow structure. For instance, if we examine the `sum-odd-squares` procedure, we find that the enumeration is implemented partly by the `null?` and `pair?` tests and partly by the tree-recursive structure of the procedure. Similarly, the accumulation is found partly in the tests and partly in the addition used in the recursion. In general, there are no distinct parts of either procedure that correspond to the elements in the signal-flow description. Our two procedures decompose the computations in a different way, spreading the enumeration over the program and mingling it with the map, the filter, and the accumulation. If we could organize our programs to make the signal-flow structure manifest in the procedures we write, this would increase the conceptual clarity of the resulting code.

**校订前**

不幸的是，上面的两个过程定义未能展示这种信号流结构。例如，如果我们检查`sum-odd-squares`过程，我们发现枚举部分由`null?`和`pair?`测试实现，部分由过程的树递归结构实现。类似地，累加部分在测试中，部分在递归中使用的加法中。一般来说，两个过程中都没有与信号流描述中的元素相对应的不同部分。我们的两个过程以不同的方式分解计算，将枚举分散在程序中，并与映射、过滤和累加混合在一起。如果我们能够组织程序，使信号流结构在我们编写的过程中显现出来，这将增加所得代码的概念清晰度。

**校订后**

不幸的是，上面的两个过程定义未能展示这种信号流结构。例如，如果我们检查`sum-odd-squares`过程，我们发现枚举部分由`null?`和`pair?`测试实现，部分由过程的树形递归结构实现。类似地，累加部分在测试中，部分在递归中使用的加法中。一般来说，两个过程中都没有与信号流描述中的元素相对应的独立部分。我们的两个过程以不同的方式分解计算，将枚举分散在程序中，并与映射、过滤和累加混合在一起。如果我们能够组织程序，使信号流结构在我们编写的过程中显现出来，这将增加所得代码的概念清晰度。

### 2_002e2:0123

**原文**

The value of expressing programs as sequence operations is that this helps us make program designs that are modular, that is, designs that are constructed by combining relatively independent pieces. We can encourage modular design by providing a library of standard components together with a conventional interface for connecting the components in flexible ways.

**校订前**

将程序表达为序列操作的价值在于，这有助于我们进行模块化的程序设计，即通过组合相对独立的部件来构造设计。我们可以通过提供标准组件库以及用于以灵活方式连接组件的常规接口来鼓励模块化设计。

**校订后**

将程序表达为序列操作的价值在于，这有助于我们进行模块化的程序设计，即通过组合相对独立的部件来构造设计。我们可以通过提供标准组件库以及用于以灵活方式连接组件的约定接口来鼓励模块化设计。

### 2_002e2:0124

**原文**

Modular construction is a powerful strategy for controlling complexity in engineering design. In real signal-processing applications, for example, designers regularly build systems by cascading elements selected from standardized families of filters and transducers. Similarly, sequence operations provide a library of standard program elements that we can mix and match. For instance, we can reuse pieces from the `sum-odd-squares` and `even-fibs` procedures in a program that constructs a list of the squares of the first $n+1$ Fibonacci numbers:

**校订前**

模块化构造是控制工程设计复杂性的有力策略。例如，在实际的信号处理应用中，设计者经常通过级联从标准化的滤波器和传感器系列中选择的元件来构建系统。类似地，序列操作为我们提供了一组标准程序元素的库，我们可以混合和匹配这些元素。例如，我们可以在一个构造前 $n+1$ 个 Fibonacci 数的平方的表的程序中重用来自 `sum-odd-squares` 和 `even-fibs` 过程的片段：

**校订后**

模块化构造是控制工程设计复杂性的有力策略。例如，在实际的信号处理应用中，设计者经常通过级联从标准化的滤波器和转换器系列中选择的元件来构建系统。类似地，序列操作为我们提供了一组标准程序元素的库，我们可以混合和匹配这些元素。例如，我们可以在一个构造前 $n+1$ 个 斐波那契数的平方的表的程序中重用来自 `sum-odd-squares` 和 `even-fibs` 过程的片段：

### 2_002e2:0126

**原文**

We can also formulate conventional data-processing applications in terms of sequence operations. Suppose we have a sequence of personnel records and we want to find the salary of the highest-paid programmer. Assume that we have a selector `salary` that returns the salary of a record, and a predicate `programmer?` that tests if a record is for a programmer. Then we can write

**校订前**

我们也可以用序列操作来表述传统的数据处理应用。假设我们有一个人员记录的序列，我们想要找到薪水最高的程序员的薪水。假设我们有一个选择器 `salary` 返回一条记录的薪水，以及一个谓词 `programmer?` 测试一条记录是否是程序员的。那么我们可以写

**校订后**

我们也可以用序列操作来表述传统的数据处理应用。假设我们有一个人员记录的序列，我们想要找到薪水最高的程序员的薪水。假设我们有一个选择函数 `salary` 返回一条记录的薪水，以及一个谓词 `programmer?` 测试一条记录是否是程序员的。那么我们可以写

### 2_002e2:0128

**原文**

Sequences, implemented here as lists, serve as a conventional interface that permits us to combine processing modules. Additionally, when we uniformly represent structures as sequences, we have localized the data-structure dependencies in our programs to a small number of sequence operations. By changing these, we can experiment with alternative representations of sequences, while leaving the overall design of our programs intact. We will exploit this capability in 3.5, when we generalize the sequence-processing paradigm to admit infinite sequences.

**校订前**

序列，在这里实现为表，作为一种常规接口，允许我们组合处理模块。此外，当我们统一地将结构表示为序列时，我们将程序中的数据结构依赖局部化到少数几个序列操作中。通过改变这些操作，我们可以试验序列的替代表示，同时保持程序的整体设计不变。我们将在 3.5 中利用这一能力，那时我们将序列处理范式推广到允许无限序列。

**校订后**

序列，在这里实现为表，作为一种约定接口，允许我们组合处理模块。此外，当我们统一地将结构表示为序列时，我们将程序中的数据结构依赖局部化到少数几个序列操作中。通过改变这些操作，我们可以试验序列的替代表示，同时保持程序的整体设计不变。我们将在 3.5 中利用这一能力，那时我们将序列处理范式推广到允许无限序列。

### 2_002e2:0144

**原文**

The combination of mapping and accumulating with `append` is so common in this sort of program that we will isolate it as a separate procedure:

**校订前**

在这种程序中，用`append`进行映射和累积的组合非常常见，因此我们将把它单独提取为一个过程：

**校订后**

在这种程序中，映射与用`append`进行累积的组合非常常见，因此我们将把它单独提取为一个过程：

### 2_002e2:0158

**原文**

2.2.4 Example: A Picture Language

**校订前**

2.2.4 示例：图片语言

**校订后**

2.2.4 示例：图画语言

### 2_002e2:0159

**原文**

This section presents a simple language for drawing pictures that illustrates the power of data abstraction and closure, and also exploits higher-order procedures in an essential way. The language is designed to make it easy to experiment with patterns such as the ones in Figure 2.9, which are composed of repeated elements that are shifted and scaled.[注88] In this language, the data objects being combined are represented as procedures rather than as list structure. Just as `cons`, which satisfies the closure property, allowed us to easily build arbitrarily complicated list structure, the operations in this language, which also satisfy the closure property, allow us to easily build arbitrarily complicated patterns.

**校订前**

本节介绍一种用于画图的简单语言，它展示了数据抽象和闭包的威力，并且以一种本质的方式利用了高阶过程。这种语言的设计使得试验诸如图2.9中那样的图案变得容易，这些图案由重复的元素经过平移和缩放组成。[注88]在这种语言中，被组合的数据对象表示为过程，而不是表结构。正如满足闭包性质的`cons`使我们能够轻松构建任意复杂的表结构一样，这种语言中的操作也满足闭包性质，使我们能够轻松构建任意复杂的图案。

**校订后**

本节介绍一种用于画图的简单语言，它展示了数据抽象和闭合性的威力，并且以一种本质的方式利用了高阶过程。这种语言的设计使得试验诸如图2.9中那样的图案变得容易，这些图案由重复的元素经过平移和缩放组成。[注88]在这种语言中，被组合的数据对象表示为过程，而不是表结构。正如满足闭合性质的`cons`使我们能够轻松构建任意复杂的表结构一样，这种语言中的操作也满足闭合性质，使我们能够轻松构建任意复杂的图案。

### 2_002e2:0160

**原文**

Figure 2.9: Designs generated with the picture language.

**校订前**

图2.9：用图片语言生成的设计。

**校订后**

图2.9：用图画语言生成的设计。

### 2_002e2:0161

**原文**

The picture language

**校订前**

图片语言

**校订后**

图画语言

### 2_002e2:0163

**原文**

Part of the elegance of this picture language is that there is only one kind of element, called a painter. A painter draws an image that is shifted and scaled to fit within a designated parallelogram-shaped frame. For example, there’s a primitive painter we’ll call `wave` that makes a crude line drawing, as shown in Figure 2.10. The actual shape of the drawing depends on the frame—all four images in figure 2.10 are produced by the same `wave` painter, but with respect to four different frames. Painters can be more elaborate than this: The primitive painter called `rogers` paints a picture of MIT’s founder, William Barton Rogers, as shown in Figure 2.11.[注89] The four images in figure 2.11 are drawn with respect to the same four frames as the `wave` images in figure 2.10.

**校订前**

这种图片语言的优雅之处部分在于只有一种元素，称为画家。画家绘制一幅图像，该图像经过平移和缩放以适合指定的平行四边形框架。例如，有一个我们将称为`wave`的基本画家，它绘制一幅粗略的线条画，如图2.10所示。绘图的实际形状取决于框架——图2.10中的所有四幅图像都是由同一个`wave`画家产生的，但相对于四个不同的框架。画家可以比这更精细：称为`rogers`的基本画家绘制了一幅MIT创始人William Barton Rogers的画像，如图2.11所示。[注89]图2.11中的四幅图像是相对于与图2.10中`wave`图像相同的四个框架绘制的。

**校订后**

这种图画语言的优雅之处部分在于只有一种元素，称为画家。画家绘制一幅图像，该图像经过平移和缩放以适合指定的平行四边形框架。例如，有一个我们将称为`wave`的基本画家，它绘制一幅粗略的线条画，如图2.10所示。绘图的实际形状取决于框架——图2.10中的所有四幅图像都是由同一个`wave`画家产生的，但相对于四个不同的框架。画家可以比这更精细：称为`rogers`的基本画家绘制了一幅MIT创始人William Barton Rogers的画像，如图2.11所示。[注89]图2.11中的四幅图像是相对于与图2.10中`wave`图像相同的四个框架绘制的。

### 2_002e2:0167

**原文**

Figure 2.12 shows the drawing of a painter called `wave4` that is built up in two stages starting from `wave`:

**校订前**

图2.12展示了称为`wave4`的画家的绘制，它是从`wave`开始分两个阶段构建的：

**校订后**

图2.12展示了称为`wave4`的画家绘制的图像，它是从`wave`开始分两个阶段构建的：

### 2_002e2:0170

**原文**

Once we can combine painters, we would like to be able to abstract typical patterns of combining painters. We will implement the painter operations as Scheme procedures. This means that we don’t need a special abstraction mechanism in the picture language: Since the means of combination are ordinary Scheme procedures, we automatically have the capability to do anything with painter operations that we can do with procedures. For example, we can abstract the pattern in `wave4` as

**校订前**

一旦我们能够组合画家，我们就希望能够抽象出组合画家的典型模式。我们将把画家操作实现为Scheme过程。这意味着我们不需要在图片语言中引入特殊的抽象机制：由于组合手段是普通的Scheme过程，我们自动获得了对画家操作做任何我们能对过程做的事情的能力。例如，我们可以将`wave4`中的模式抽象为

**校订后**

一旦我们能够组合画家，我们就希望能够抽象出组合画家的典型模式。我们将把画家操作实现为Scheme过程。这意味着我们不需要在图画语言中引入特殊的抽象机制：由于组合手段是普通的Scheme过程，我们自动获得了对画家操作做任何我们能对过程做的事情的能力。例如，我们可以将`wave4`中的模式抽象为

### 2_002e2:0186

**原文**

Before we can show how to implement painters and their means of combination, we must first consider frames. A frame can be described by three vectors—an origin vector and two edge vectors. The origin vector specifies the offset of the frame’s origin from some absolute origin in the plane, and the edge vectors specify the offsets of the frame’s corners from its origin. If the edges are perpendicular, the frame will be rectangular. Otherwise the frame will be a more general parallelogram.

**校订前**

在我们能够展示如何实现画家及其组合手段之前，我们必须首先考虑框架。一个框架可以用三个向量来描述——一个原点向量和两个边缘向量。原点向量指定框架的原点相对于平面中某个绝对原点的偏移，而边缘向量指定框架的角相对于其原点的偏移。如果边缘垂直，框架将是矩形的。否则框架将是一个更一般的平行四边形。

**校订后**

在我们能够展示如何实现画家及其组合手段之前，我们必须首先考虑框架。一个框架可以用三个向量来描述——一个原点向量和两个边向量。原点向量指定框架的原点相对于平面中某个绝对原点的偏移，而边向量指定框架的角相对于其原点的偏移。如果两条边互相垂直，框架将是矩形的。否则框架将是一个更一般的平行四边形。

### 2_002e2:0187

**原文**

Figure 2.15 shows a frame and its associated vectors. In accordance with data abstraction, we need not be specific yet about how frames are represented, other than to say that there is a constructor `make-frame`, which takes three vectors and produces a frame, and three corresponding selectors `origin-frame`, `edge1-frame`, and `edge2-frame` (see Exercise 2.47).

**校订前**

图2.15展示了一个框架及其关联的向量。根据数据抽象，我们暂时不需要具体说明框架是如何表示的，只需说明有一个构造器`make-frame`，它接受三个向量并产生一个框架，以及三个相应的选择器`origin-frame`、`edge1-frame`和`edge2-frame`（见习题2.47）。

**校订后**

图2.15展示了一个框架及其关联的向量。根据数据抽象，我们暂时不需要具体说明框架是如何表示的，只需说明有一个构造函数`make-frame`，它接受三个向量并产生一个框架，以及三个相应的选择函数`origin-frame`、`edge1-frame`和`edge2-frame`（见习题2.47）。

### 2_002e2:0188

**原文**

Figure 2.15: A frame is described by three vectors — an origin and two edges.

**校订前**

图2.15：一个框架由三个向量描述——一个原点和两个边缘。

**校订后**

图2.15：一个框架由三个向量描述——一个原点和两个边。

### 2_002e2:0192

**原文**

Exercise 2.46: A two-dimensional vector $v$ running from the origin to a point can be represented as a pair consisting of an $x$-coordinate and a $y$-coordinate. Implement a data abstraction for vectors by giving a constructor `make-vect` and corresponding selectors `xcor-vect` and `ycor-vect`. In terms of your selectors and constructor, implement procedures `add-vect`, `sub-vect`, and `scale-vect` that perform the operations vector addition, vector subtraction, and multiplying a vector by a scalar: $(x_{1},y_{1})+(x_{2},y_{2})=(x_{1}+x_{2},y_{1}+y_{2}),(x_{1},y_{1})−(x_{2},y_{2})=(x_{1}−x_{2},y_{1}−y_{2}),s⋅(x,y)=(sx,sy).$

**校订前**

习题2.46：一个从原点到一个点的二维向量$v$可以表示为一个由$x$坐标和$y$坐标组成的序对。通过给出构造器`make-vect`和相应的选择器`xcor-vect`和`ycor-vect`，为向量实现一个数据抽象。根据你的选择器和构造器，实现过程`add-vect`、`sub-vect`和`scale-vect`，它们执行向量加法、向量减法和向量乘以标量的操作：$(x_{1},y_{1})+(x_{2},y_{2})=(x_{1}+x_{2},y_{1}+y_{2}),(x_{1},y_{1})−(x_{2},y_{2})=(x_{1}−x_{2},y_{1}−y_{2}),s⋅(x,y)=(sx,sy).$

**校订后**

习题2.46：一个从原点到一个点的二维向量$v$可以表示为一个由$x$坐标和$y$坐标组成的序对。通过给出构造函数`make-vect`和相应的选择函数`xcor-vect`和`ycor-vect`，为向量实现一个数据抽象。根据你的选择函数和构造函数，实现过程`add-vect`、`sub-vect`和`scale-vect`，它们执行向量加法、向量减法和向量乘以标量的操作：$(x_{1},y_{1})+(x_{2},y_{2})=(x_{1}+x_{2},y_{1}+y_{2}),(x_{1},y_{1})−(x_{2},y_{2})=(x_{1}−x_{2},y_{1}−y_{2}),s⋅(x,y)=(sx,sy).$

### 2_002e2:0193

**原文**

Exercise 2.47: Here are two possible constructors for frames:

**校订前**

习题2.47：这里是框架的两种可能的构造器：

**校订后**

习题2.47：这里是框架的两种可能的构造函数：

### 2_002e2:0194

**原文**

For each constructor supply the appropriate selectors to produce an implementation for frames.

**校订前**

为每个构造器提供适当的选择器，以产生框架的实现。

**校订后**

为每个构造函数提供适当的选择函数，以产生框架的实现。

### 2_002e2:0197

**原文**

The details of how primitive painters are implemented depend on the particular characteristics of the graphics system and the type of image to be drawn. For instance, suppose we have a procedure `draw-line` that draws a line on the screen between two specified points. Then we can create painters for line drawings, such as the `wave` painter in Figure 2.10, from lists of line segments as follows:[注93]

**校订前**

基本画家如何实现的细节取决于图形系统的特定特征和要绘制的图像类型。例如，假设我们有一个过程`draw-line`，它在屏幕上两个指定点之间画一条线。那么我们可以从线段列表创建线条画的画家，例如图2.10中的`wave`画家，如下所示：[注93]

**校订后**

基本画家如何实现的细节取决于图形系统的特定特征和要绘制的图像类型。例如，假设我们有一个过程`draw-line`，它在屏幕上两个指定点之间画一条线。那么我们可以从线段表创建线条画的画家，例如图2.10中的`wave`画家，如下所示：[注93]

### 2_002e2:0198

**原文**

The segments are given using coordinates with respect to the unit square. For each segment in the list, the painter transforms the segment endpoints with the frame coordinate map and draws a line between the transformed points.

**校订前**

线段使用相对于单位正方形的坐标给出。对于列表中的每条线段，画家用框架坐标映射变换线段的端点，并在变换后的点之间画一条线。

**校订后**

线段使用相对于单位正方形的坐标给出。对于表中的每条线段，画家用框架坐标映射变换线段的端点，并在变换后的点之间画一条线。

### 2_002e2:0199

**原文**

Representing painters as procedures erects a powerful abstraction barrier in the picture language. We can create and intermix all sorts of primitive painters, based on a variety of graphics capabilities. The details of their implementation do not matter. Any procedure can serve as a painter, provided that it takes a frame as argument and draws something scaled to fit the frame.[注94]

**校订前**

将画家表示为过程在图片语言中建立了一个强大的抽象屏障。我们可以基于各种图形能力创建和混合各种基本画家。它们实现的细节无关紧要。任何过程都可以作为画家，只要它接受一个框架作为参数并绘制一些缩放以适合该框架的东西。[注94]

**校订后**

将画家表示为过程在图画语言中建立了一个强大的抽象屏障。我们可以基于各种图形能力创建和混合各种基本画家。它们实现的细节无关紧要。任何过程都可以作为画家，只要它接受一个框架作为参数并绘制一些缩放以适合该框架的东西。[注94]

### 2_002e2:0200

**原文**

Exercise 2.48: A directed line segment in the plane can be represented as a pair of vectors—the vector running from the origin to the start-point of the segment, and the vector running from the origin to the end-point of the segment. Use your vector representation from Exercise 2.46 to define a representation for segments with a constructor `make-segment` and selectors `start-segment` and `end-segment`.

**校订前**

习题2.48：平面中的有向线段可以表示为一对向量——从原点到线段起点的向量，以及从原点到线段终点的向量。使用你在习题2.46中的向量表示，为线段定义一个表示，带有构造器`make-segment`和选择器`start-segment`和`end-segment`。

**校订后**

习题2.48：平面中的有向线段可以表示为一对向量——从原点到线段起点的向量，以及从原点到线段终点的向量。使用你在习题2.46中的向量表示，为线段定义一个表示，带有构造函数`make-segment`和选择函数`start-segment`和`end-segment`。

### 2_002e2:0218

**原文**

The picture language exercises some of the critical ideas we’ve introduced about abstraction with procedures and data. The fundamental data abstractions, painters, are implemented using procedural representations, which enables the language to handle different basic drawing capabilities in a uniform way. The means of combination satisfy the closure property, which permits us to easily build up complex designs. Finally, all the tools for abstracting procedures are available to us for abstracting means of combination for painters.

**校订前**

图片语言练习了我们引入的关于过程和数据的抽象的一些关键思想。基本数据抽象，即画家，是使用过程表示实现的，这使得语言能够以统一的方式处理不同的基本绘制能力。组合方法满足闭包性质，这使我们能够轻松构建复杂的设计。最后，所有用于抽象过程的工具都可用于抽象画家的组合方法。

**校订后**

图画语言运用了我们引入的关于过程和数据的抽象的一些关键思想。基本数据抽象，即画家，是使用过程表示实现的，这使得语言能够以统一的方式处理不同的基本绘制能力。组合方法满足闭合性质，这使我们能够轻松构建复杂的设计。最后，所有用于抽象过程的工具都可用于抽象画家的组合方法。

### 2_002e2:0219

**原文**

We have also obtained a glimpse of another crucial idea about languages and program design. This is the approach of stratified design, the notion that a complex system should be structured as a sequence of levels that are described using a sequence of languages. Each level is constructed by combining parts that are regarded as primitive at that level, and the parts constructed at each level are used as primitives at the next level. The language used at each level of a stratified design has primitives, means of combination, and means of abstraction appropriate to that level of detail.

**校订前**

我们还瞥见了关于语言和程序设计的另一个关键思想。这就是 分层设计 的方法，即复杂系统应该被构造为一系列层次，这些层次使用一系列语言来描述。每一层通过组合在该层被视为原始的部分来构造，而在每一层构造的部分在下一层被用作原始部分。分层设计中每一层使用的语言都有适合该细节层次的原始部分、组合方法和抽象方法。

**校订后**

我们还瞥见了关于语言和程序设计的另一个关键思想。这就是 分层设计 的方法，即复杂系统应该被构造为一系列层次，这些层次使用一系列语言来描述。每一层通过组合在该层被视为基本的部分来构造，而在每一层构造的部分在下一层被用作基本部分。分层设计中每一层使用的语言都有适合该细节层次的基本部分、组合方法和抽象方法。

### 2_002e2:0220

**原文**

Stratified design pervades the engineering of complex systems. For example, in computer engineering, resistors and transistors are combined (and described using a language of analog circuits) to produce parts such as and-gates and or-gates, which form the primitives of a language for digital-circuit design.[注97] These parts are combined to build processors, bus structures, and memory systems, which are in turn combined to form computers, using languages appropriate to computer architecture. Computers are combined to form distributed systems, using languages appropriate for describing network interconnections, and so on.

**校订前**

分层设计遍及复杂系统的工程。例如，在计算机工程中，电阻和晶体管被组合（并使用模拟电路的语言描述）以产生诸如与门和或门之类的部件，这些部件构成了数字电路设计语言的原始部分。[注97] 这些部件被组合以构建处理器、总线结构和存储器系统，这些又使用适合计算机体系结构的语言被组合以形成计算机。计算机被组合以形成分布式系统，使用适合描述网络互连的语言，等等。

**校订后**

分层设计遍及复杂系统的工程。例如，在计算机工程中，电阻和晶体管被组合（并使用模拟电路的语言描述）以产生诸如与门和或门之类的部件，这些部件构成了数字电路设计语言的基本部分。[注97] 这些部件被组合以构建处理器、总线结构和存储器系统，这些又使用适合计算机体系结构的语言被组合以形成计算机。计算机被组合以形成分布式系统，使用适合描述网络互连的语言，等等。

### 2_002e2:0221

**原文**

As a tiny example of stratification, our picture language uses primitive elements (primitive painters) that are created using a language that specifies points and lines to provide the lists of line segments for `segments->painter`, or the shading details for a painter like `rogers`. The bulk of our description of the picture language focused on combining these primitives, using geometric combiners such as `beside` and `below`. We also worked at a higher level, regarding `beside` and `below` as primitives to be manipulated in a language whose operations, such as `square-of-four`, capture common patterns of combining geometric combiners.

**校订前**

作为分层的一个小例子，我们的图片语言使用原始元素（原始画家），这些元素是使用指定点和线的语言创建的，以提供 `segments->painter` 的线段列表，或像 `rogers` 这样的画家的着色细节。我们对图片语言的大部分描述集中在组合这些原始部分上，使用诸如 `beside` 和 `below` 之类的几何组合器。我们也在更高的层次上工作，将 `beside` 和 `below` 视为原始部分，在一种语言中操作，该语言的操作，如 `square-of-four`，捕捉组合几何组合器的常见模式。

**校订后**

作为分层的一个小例子，我们的图画语言使用基本元素（基本画家），这些元素是使用指定点和线的语言创建的，以提供 `segments->painter` 的线段表，或像 `rogers` 这样的画家的着色细节。我们对图画语言的大部分描述集中在组合这些基本部分上，使用诸如 `beside` 和 `below` 之类的几何组合器。我们也在更高的层次上工作，将 `beside` 和 `below` 视为基本部分，在一种语言中操作，该语言的操作，如 `square-of-four`，捕捉组合几何组合器的常见模式。

### 2_002e2:0228

**原文**

[注72] The use of the word “closure” here comes from abstract algebra, where a set of elements is said to be closed under an operation if applying the operation to elements in the set produces an element that is again an element of the set. The Lisp community also (unfortunately) uses the word “closure” to describe a totally unrelated concept: A closure is an implementation technique for representing procedures with free variables. We do not use the word “closure” in this second sense in this book.

**校订前**

[注72]这里使用“闭包”一词来自抽象代数，其中如果对一个集合中的元素应用某个运算所产生的结果仍然是该集合中的元素，则称该集合在该运算下是封闭的。Lisp社区也（不幸地）使用“闭包”一词来描述一个完全无关的概念：闭包是一种用于表示带有自由变量的过程的实现技术。在本书中我们不使用“闭包”的第二种含义。

**校订后**

[注72]这里使用“closure”一词来自抽象代数，其中如果对一个集合中的元素应用某个运算所产生的结果仍然是该集合中的元素，则称该集合在该运算下是封闭的。Lisp社区也（不幸地）使用“closure”一词来描述一个完全无关的概念：闭包是一种用于表示带有自由变量的过程的实现技术。在本书中我们不使用“closure”的第二种含义。

### 2_002e2:0229

**原文**

[注73] The notion that a means of combination should satisfy closure is a straightforward idea. Unfortunately, the data combiners provided in many popular programming languages do not satisfy closure, or make closure cumbersome to exploit. In Fortran or Basic, one typically combines data elements by assembling them into arrays—but one cannot form arrays whose elements are themselves arrays. Pascal and C admit structures whose elements are structures. However, this requires that the programmer manipulate pointers explicitly, and adhere to the restriction that each field of a structure can contain only elements of a prespecified form. Unlike Lisp with its pairs, these languages have no built-in general-purpose glue that makes it easy to manipulate compound data in a uniform way. This limitation lies behind Alan Perlis’s comment in his foreword to this book: “In Pascal the plethora of declarable data structures induces a specialization within functions that inhibits and penalizes casual cooperation. It is better to have 100 functions operate on one data structure than to have 10 functions operate on 10 data structures.”

**校订前**

[注73]组合手段应满足闭包性这一观念是一个直截了当的想法。不幸的是，许多流行编程语言中提供的数据组合手段并不满足闭包性，或者使闭包性的利用变得笨拙。在Fortran或Basic中，人们通常通过将数据元素组装成数组来组合它们——但无法形成元素本身是数组的数组。Pascal和C允许元素是结构体的结构体。然而，这要求程序员显式地操作指针，并遵守每个结构体字段只能包含预先指定形式的元素这一限制。与具有序对的Lisp不同，这些语言没有内置的通用粘合剂，使得以统一的方式操作复合数据变得容易。这一局限性正是Alan Perlis在本书前言中所评论的背景：“在Pascal中，可声明数据结构的繁多导致了函数内部的专门化，这抑制并惩罚了随意的合作。让100个函数操作一个数据结构，比让10个函数操作10个数据结构要好。”

**校订后**

[注73]组合手段应满足闭合性这一观念是一个直截了当的想法。不幸的是，许多流行编程语言中提供的数据组合手段并不满足闭合性，或者使闭合性的利用变得笨拙。在Fortran或Basic中，人们通常通过将数据元素组装成数组来组合它们——但无法形成元素本身是数组的数组。Pascal和C允许元素是结构体的结构体。然而，这要求程序员显式地操作指针，并遵守每个结构体字段只能包含预先指定形式的元素这一限制。与具有序对的Lisp不同，这些语言没有内置的通用粘合剂，使得以统一的方式操作复合数据变得容易。这一局限性正是Alan Perlis在本书前言中所评论的背景：“在Pascal中，可声明数据结构的繁多导致了函数内部的专门化，这抑制并惩罚了随意的合作。让100个函数操作一个数据结构，比让10个函数操作10个数据结构要好。”

### 2_002e2:0233

**原文**

[注76] It’s remarkable how much energy in the standardization of Lisp dialects has been dissipated in arguments that are literally over nothing: Should `nil` be an ordinary name? Should the value of `nil` be a symbol? Should it be a list? Should it be a pair? In Scheme, `nil` is an ordinary name, which we use in this section as a variable whose value is the end-of-list marker (just as `true` is an ordinary variable that has a true value). Other dialects of Lisp, including Common Lisp, treat `nil` as a special symbol. The authors of this book, who have endured too many language standardization brawls, would like to avoid the entire issue. Once we have introduced quotation in 2.3, we will denote the empty list as `'()` and dispense with the variable `nil` entirely.

**校订前**

[注76]令人瞩目的是，Lisp方言标准化中如此多的精力被消耗在字面上毫无意义的争论上：`nil`应该是一个普通名称吗？`nil`的值应该是一个符号吗？它应该是一个表吗？它应该是一个序对吗？在Scheme中，`nil`是一个普通名称，我们在本节中将其用作一个变量，其值是表结束标记（就像`true`是一个普通变量，其值为真一样）。其他Lisp方言，包括Common Lisp，将`nil`视为一个特殊符号。本书的作者们，已经忍受了太多语言标准化的争吵，希望避免整个问题。一旦我们在2.3中引入了引用，我们将把空表表示为`'()`并完全省去变量`nil`。

**校订后**

[注76]令人瞩目的是，Lisp方言标准化中如此多的精力被消耗在确实是关于“无”的争论上：`nil`应该是一个普通名称吗？`nil`的值应该是一个符号吗？它应该是一个表吗？它应该是一个序对吗？在Scheme中，`nil`是一个普通名称，我们在本节中将其用作一个变量，其值是表结束标记（就像`true`是一个普通变量，其值为真一样）。其他Lisp方言，包括Common Lisp，将`nil`视为一个特殊符号。本书的作者们，已经忍受了太多语言标准化的争吵，希望避免整个问题。一旦我们在2.3中引入了引用，我们将把空表表示为`'()`并完全省去变量`nil`。

### 2_002e2:0239

**原文**

[注82] According to Knuth 1981, this rule was formulated by W. G. Horner early in the nineteenth century, but the method was actually used by Newton over a hundred years earlier. Horner’s rule evaluates the polynomial using fewer additions and multiplications than does the straightforward method of first computing $a_{n}x^(n)$, then adding $a_{n−1}x^(n−1)$, and so on. In fact, it is possible to prove that any algorithm for evaluating arbitrary polynomials must use at least as many additions and multiplications as does Horner’s rule, and thus Horner’s rule is an optimal algorithm for polynomial evaluation. This was proved (for the number of additions) by A. M. Ostrowski in a 1954 paper that essentially founded the modern study of optimal algorithms. The analogous statement for multiplications was proved by V. Y. Pan in 1966. The book by Borodin and Munro (1975) provides an overview of these and other results about optimal algorithms.

**校订前**

[注82]根据Knuth1981的说法，这个规则是由W. G. Horner在十九世纪初提出的，但该方法实际上在一百多年前就被牛顿使用了。Horner规则在计算多项式时使用的加法和乘法比先计算$a_{n}x^(n)$，然后加上$a_{n−1}x^(n−1)$，依此类推的直接方法要少。事实上，可以证明任何用于计算任意多项式的算法都必须至少使用与Horner规则一样多的加法和乘法，因此Horner规则是多项式求值的最优算法。这一点（对于加法次数）由A. M. Ostrowski在一篇1954论文中证明，该论文基本上奠定了最优算法的现代研究。关于乘法的类似陈述由V. Y. Pan在1966年证明。Borodin和Munro（1975）的书概述了这些以及其他关于最优算法的结果。

**校订后**

[注82]根据Knuth1981的说法，这个规则是由W. G. Horner在十九世纪初提出的，但该方法实际上在比这早一百多年的时候就被牛顿使用了。Horner规则在计算多项式时使用的加法和乘法比先计算$a_{n}x^(n)$，然后加上$a_{n−1}x^(n−1)$，依此类推的直接方法要少。事实上，可以证明任何用于计算任意多项式的算法都必须至少使用与Horner规则一样多的加法和乘法，因此Horner规则是多项式求值的最优算法。这一点（对于加法次数）由A. M. Ostrowski在一篇1954年的论文中证明，该论文基本上奠定了最优算法的现代研究。关于乘法的类似陈述由V. Y. Pan在1966年证明。Borodin和Munro（1975）的书概述了这些以及其他关于最优算法的结果。

### 2_002e2:0245

**原文**

[注88] The picture language is based on the language Peter Henderson created to construct images like M.C. Escher’s “Square Limit” woodcut (see Henderson 1982). The woodcut incorporates a repeated scaled pattern, similar to the arrangements drawn using the `square-limit` procedure in this section.

**校订前**

[注88]图片语言基于Peter Henderson创建的语言，用于构建像M.C. Escher的“Square Limit”木刻版画这样的图像（见Henderson1982）。木刻版画包含重复的缩放图案，类似于本节中使用`square-limit`过程绘制的排列。

**校订后**

[注88]图画语言基于Peter Henderson创建的语言，用于构建像M.C. Escher的“Square Limit”木刻版画这样的图像（见Henderson1982）。木刻版画包含重复的缩放图案，类似于本节中使用`square-limit`过程绘制的排列。

### 2_002e2:0247

**原文**

When MIT was established in 1861, Rogers was elected its first president. Rogers espoused an ideal of “useful learning” that was different from the university education of the time, with its overemphasis on the classics, which, as he wrote, “stand in the way of the broader, higher and more practical instruction and discipline of the natural and social sciences.” This education was likewise to be different from narrow trade-school education. In Rogers’s words:

**校订前**

当MIT于1861年成立时，Rogers被选为第一任校长。Rogers倡导“有用学习”的理想，这与当时的大学教育不同，当时的大学教育过分强调古典学，正如他写道，古典学“阻碍了更广泛、更高和更实用的自然科学和社会科学的教学和训练。”这种教育同样不同于狭隘的贸易学校教育。用Rogers的话说：

**校订后**

当MIT于1861年成立时，Rogers被选为第一任校长。Rogers倡导“有用学习”的理想，这与当时的大学教育不同，当时的大学教育过分强调古典学，正如他写道，古典学“阻碍了更广泛、更高和更实用的自然科学和社会科学的教学和训练。”这种教育同样不同于狭隘的职业学校教育。用Rogers的话说：

### 2_002e2:0249

**原文**

Rogers served as president of MIT until 1870, when he resigned due to ill health. In 1878 the second president of MIT, John Runkle, resigned under the pressure of a financial crisis brought on by the Panic of 1873 and strain of fighting off attempts by Harvard to take over MIT. Rogers returned to hold the office of president until 1881.

**校订前**

Rogers担任MIT校长直到1870年，因健康不佳而辞职。1878年，MIT的第二任校长John Runkle在1873年恐慌引发的金融危机和哈佛试图接管MIT的压力下辞职。Rogers回来担任校长直到1881年。

**校订后**

Rogers担任MIT校长直到1870年，因健康不佳而辞职。1878年，MIT的第二任校长John Runkle在1873年恐慌引发的金融危机和抵制哈佛接管MIT的企图所带来的压力下辞职。Rogers回来担任校长直到1881年。

### 2_002e2:0251

**原文**

“As I stand here today and see what the Institute is, … I call to mind the beginnings of science. I remember one hundred and fifty years ago Stephen Hales published a pamphlet on the subject of illuminating gas, in which he stated that his researches had demonstrated that 128 grains of bituminous coal – ” “Bituminous coal,” these were his last words on earth. Here he bent forward, as if consulting some notes on the table before him, then slowly regaining an erect position, threw up his hands, and was translated from the scene of his earthly labors and triumphs to “the tomorrow of death,” where the mysteries of life are solved, and the disembodied spirit finds unending satisfaction in contemplating the new and still unfathomable mysteries of the infinite future.

**校订前**

“当我今天站在这里，看到学院是什么样子，……我想起了科学的开端。我记得一百五十年前，Stephen Hales发表了一本关于照明气体的手册，其中他说他的研究表明128粒烟煤——” “烟煤，”这是他在世上的最后的话。他向前弯腰，仿佛在查看面前桌子上的笔记，然后慢慢恢复直立姿势，举起双手，从尘世劳作和胜利的场景被转移到“死亡的明天”，在那里生命的奥秘得到解答，脱离肉体的灵魂在沉思无限未来的新而仍然深不可测的奥秘中找到无尽的满足。

**校订后**

“当我今天站在这里，看到学院是什么样子，……我想起了科学的开端。我记得一百五十年前，Stephen Hales发表了一本关于照明用煤气的手册，其中他说他的研究表明128格令烟煤——” “烟煤，”这是他在世上的最后的话。他向前弯腰，仿佛在查看面前桌子上的笔记，然后慢慢恢复直立姿势，举起双手，从尘世劳作和胜利的场景被转移到“死亡的明天”，在那里生命的奥秘得到解答，脱离肉体的灵魂在沉思无限未来的新而仍然深不可测的奥秘中找到无尽的满足。

### 2_002e2:0253

**原文**

All his life he had borne himself most faithfully and heroically, and he died as so good a knight would surely have wished, in harness, at his post, and in the very part and act of public duty.

**校订前**

他一生都最为忠诚、最为英勇地立身行事，而他死得正像这样一位优秀骑士必定会希望的那样：在工作之中，在自己的岗位上，在履行公职职责的那一具体部分和行动之中。

**校订后**

他一生都最为忠诚、最为英勇地立身行事，而他死得正像这样一位优秀骑士必定会希望的那样：在工作之中，在自己的岗位上，就在履行公共职责的当时。

### 2_002e3:0028

**原文**

To embody these rules in a procedure we indulge in a little wishful thinking, as we did in designing the rational-number implementation. If we had a means for representing algebraic expressions, we should be able to tell whether an expression is a sum, a product, a constant, or a variable. We should be able to extract the parts of an expression. For a sum, for example we want to be able to extract the addend (first term) and the augend (second term). We should also be able to construct expressions from parts. Let us assume that we already have procedures to implement the following selectors, constructors, and predicates:

**校订前**

为了将这些规则体现在一个过程中，我们进行一点一厢情愿的设想，就像我们在设计有理数实现时所做的那样。如果我们有表示代数表达式的手段，我们应该能够判断一个表达式是和、积、常量还是变量。我们应该能够提取表达式的部分。例如，对于一个和，我们希望能够提取加数（第一项）和被加数（第二项）。我们还应该能够从部分构造表达式。让我们假设我们已经有了实现以下选择器、构造器和谓词的过程：

**校订后**

为了将这些规则体现在一个过程中，我们进行一点一厢情愿的设想，就像我们在设计有理数实现时所做的那样。如果我们有表示代数表达式的手段，我们应该能够判断一个表达式是和、积、常量还是变量。我们应该能够提取表达式的部分。例如，对于一个和，我们希望能够提取加数（第一项）和被加数（第二项）。我们还应该能够从部分构造表达式。让我们假设我们已经有了实现以下选择函数、构造函数和谓词的过程：

### 2_002e3:0030

**原文**

This `deriv` procedure incorporates the complete differentiation algorithm. Since it is expressed in terms of abstract data, it will work no matter how we choose to represent algebraic expressions, as long as we design a proper set of selectors and constructors. This is the issue we must address next.

**校订前**

这个`deriv`过程包含了完整的求导算法。由于它是用抽象数据表达的，无论我们选择如何表示代数表达式，只要设计了一组合适的选择器和构造器，它都能工作。这是我们接下来必须处理的问题。

**校订后**

这个`deriv`过程包含了完整的求导算法。由于它是用抽象数据表达的，无论我们选择如何表示代数表达式，只要设计了一组合适的选择函数和构造函数，它都能工作。这是我们接下来必须处理的问题。

### 2_002e3:0044

**原文**

Our difficulty is much like the one we encountered with the rational-number implementation: we haven’t reduced answers to simplest form. To accomplish the rational-number reduction, we needed to change only the constructors and the selectors of the implementation. We can adopt a similar strategy here. We won’t change `deriv` at all. Instead, we will change `make-sum` so that if both summands are numbers, `make-sum` will add them and return their sum. Also, if one of the summands is 0, then `make-sum` will return the other summand:

**校订前**

我们的困难很像我们在有理数实现中遇到的困难：我们还没有将答案化为最简形式。为了实现有理数化简，我们只需要改变实现中的构造器和选择器。我们可以在这里采用类似的策略。我们完全不改变`deriv`。相反，我们将改变`make-sum`，使得如果两个加数都是数字，`make-sum`将把它们相加并返回它们的和。此外，如果其中一个加数是0，那么`make-sum`将返回另一个加数：

**校订后**

我们的困难很像我们在有理数实现中遇到的困难：我们还没有将答案化为最简形式。为了实现有理数化简，我们只需要改变实现中的构造函数和选择函数。我们可以在这里采用类似的策略。我们完全不改变`deriv`。相反，我们将改变`make-sum`，使得如果两个加数都是数字，`make-sum`将把它们相加并返回它们的和。此外，如果其中一个加数是0，那么`make-sum`将返回另一个加数：

### 2_002e3:0057

**原文**

Informally, a set is simply a collection of distinct objects. To give a more precise definition we can employ the method of data abstraction. That is, we define “set” by specifying the operations that are to be used on sets. These are `union-set`, `intersection-set`, `element-of-set?`, and `adjoin-set`. `Element-of-set?` is a predicate that determines whether a given element is a member of a set. `Adjoin-set` takes an object and a set as arguments and returns a set that contains the elements of the original set and also the adjoined element. `Union-set` computes the union of two sets, which is the set containing each element that appears in either argument. `Intersection-set` computes the intersection of two sets, which is the set containing only elements that appear in both arguments. From the viewpoint of data abstraction, we are free to design any representation that implements these operations in a way consistent with the interpretations given above.[注103]

**校订前**

非形式地说，集合就是不同对象的汇集。为了给出更精确的定义，我们可以采用数据抽象的方法。也就是说，我们通过指定将用于集合上的操作来定义“集合”。这些操作是`union-set`、`intersection-set`、`element-of-set?`和`adjoin-set`。`Element-of-set?`是一个谓词，用于确定给定元素是否是集合的成员。`Adjoin-set`接受一个对象和一个集合作为参数，并返回一个包含原集合的元素以及被加入元素的集合。`Union-set`计算两个集合的并集，即包含出现在任一参数中的每个元素的集合。`Intersection-set`计算两个集合的交集，即只包含同时出现在两个参数中的元素的集合。从数据抽象的观点来看，我们可以自由地设计任何表示，只要它以与上述解释一致的方式实现这些操作。[注103]

**校订后**

非形式地说，集合就是互不相同的对象的汇集。为了给出更精确的定义，我们可以采用数据抽象的方法。也就是说，我们通过指定将用于集合上的操作来定义“集合”。这些操作是`union-set`、`intersection-set`、`element-of-set?`和`adjoin-set`。`Element-of-set?`是一个谓词，用于确定给定元素是否是集合的成员。`Adjoin-set`接受一个对象和一个集合作为参数，并返回一个包含原集合的元素以及被加入元素的集合。`Union-set`计算两个集合的并集，即包含出现在任一参数中的每个元素的集合。`Intersection-set`计算两个集合的交集，即只包含同时出现在两个参数中的元素的集合。从数据抽象的观点来看，我们可以自由地设计任何表示，只要它以与上述解释一致的方式实现这些操作。[注103]

### 2_002e3:0068

**原文**

How many steps does this save? In the worst case, the item we are looking for may be the largest one in the set, so the number of steps is the same as for the unordered representation. On the other hand, if we search for items of many different sizes we can expect that sometimes we will be able to stop searching at a point near the beginning of the list and that other times we will still need to examine most of the list. On the average we should expect to have to examine about half of the items in the set. Thus, the average number of steps required will be about $n/2$. This is still $Θ(n)$ growth, but it does save us, on the average, a factor of 2 in number of steps over the previous implementation.

**校订前**

这节省了多少步？在最坏情况下，我们要找的项可能是集合中最大的元素，因此步数与无序表示相同。另一方面，如果我们查找许多不同大小的项，可以预期有时我们能在表接近开头的位置停止搜索，而其他时候我们仍然需要检查表的大部分。平均而言，我们应该预期需要检查集合中大约一半的元素。因此，所需的平均步数大约为$n/2$。这仍然是$Θ(n)$增长，但平均而言，它确实比之前的实现节省了2倍的步数。

**校订后**

这节省了多少步？在最坏情况下，我们要找的项可能是集合中最大的元素，因此步数与无序表示相同。另一方面，如果我们查找许多不同大小的项，可以预期有时我们能在表接近开头的位置停止搜索，而其他时候我们仍然需要检查表的大部分。平均而言，我们应该预期需要检查集合中大约一半的元素。因此，所需的平均步数大约为$n/2$。这仍然是$Θ(n)$增长，但平均而言，它确实将之前实现所需的步数缩减为原来的2分之一。

### 2_002e3:0091

**原文**

Consider a data base containing a large number of individual records, such as the personnel files for a company or the transactions in an accounting system. A typical data-management system spends a large amount of time accessing or modifying the data in the records and therefore requires an efficient method for accessing records. This is done by identifying a part of each record to serve as an identifying key. A key can be anything that uniquely identifies the record. For a personnel file, it might be an employee’s ID number. For an accounting system, it might be a transaction number. Whatever the key is, when we define the record as a data structure we should include a `key` selector procedure that retrieves the key associated with a given record.

**校订前**

考虑一个包含大量独立记录的数据基，例如一家公司的人事档案或会计系统中的交易记录。典型的数据管理系统会花费大量时间访问或修改记录中的数据，因此需要一种高效的方法来访问记录。这是通过标识每条记录的一部分来作为标识键来实现的。键可以是任何能唯一标识记录的东西。对于人事档案，它可能是员工的ID号。对于会计系统，它可能是交易号。无论键是什么，当我们将记录定义为数据结构时，我们应该包含一个`key`选择过程，用于检索与给定记录关联的键。

**校订后**

考虑一个包含大量独立记录的数据库，例如一家公司的人事档案或会计系统中的交易记录。典型的数据管理系统会花费大量时间访问或修改记录中的数据，因此需要一种高效的方法来访问记录。这是通过标识每条记录的一部分来作为标识键来实现的。键可以是任何能唯一标识记录的东西。对于人事档案，它可能是员工的ID号。对于会计系统，它可能是交易号。无论键是什么，当我们将记录定义为数据结构时，我们应该包含一个`key`选择过程，用于检索与给定记录关联的键。

### 2_002e3:0092

**原文**

Now we represent the data base as a set of records. To locate the record with a given key we use a procedure `lookup`, which takes as arguments a key and a data base and which returns the record that has that key, or false if there is no such record. `Lookup` is implemented in almost the same way as `element-of-set?`. For example, if the set of records is implemented as an unordered list, we could use

**校订前**

现在我们将数据基表示为一组记录。为了定位具有给定键的记录，我们使用过程`lookup`，它接受一个键和一个数据基作为参数，并返回具有该键的记录，如果没有这样的记录则返回false。`Lookup`的实现方式几乎与`element-of-set?`相同。例如，如果记录集实现为无序表，我们可以使用

**校订后**

现在我们将数据库表示为一组记录。为了定位具有给定键的记录，我们使用过程`lookup`，它接受一个键和一个数据库作为参数，并返回具有该键的记录，如果没有这样的记录则返回false。`Lookup`的实现方式几乎与`element-of-set?`相同。例如，如果记录集实现为无序表，我们可以使用

### 2_002e3:0093

**原文**

Of course, there are better ways to represent large sets than as unordered lists. Information-retrieval systems in which records have to be “randomly accessed” are typically implemented by a tree-based method, such as the binary-tree representation discussed previously. In designing such a system the methodology of data abstraction can be a great help. The designer can create an initial implementation using a simple, straightforward representation such as unordered lists. This will be unsuitable for the eventual system, but it can be useful in providing a “quick and dirty” data base with which to test the rest of the system. Later on, the data representation can be modified to be more sophisticated. If the data base is accessed in terms of abstract selectors and constructors, this change in representation will not require any changes to the rest of the system.

**校订前**

当然，有比无序表更好的方式来表示大型集合。必须“随机访问”记录的信息检索系统通常通过基于树的方法实现，例如前面讨论的二叉树表示。在设计这样的系统时，数据抽象的方法论可以大有帮助。设计者可以使用简单直接的表示（如无序表）创建初始实现。这对于最终系统来说是不合适的，但它可以用于提供一个“快速而粗糙”的数据基来测试系统的其余部分。之后，数据表示可以被修改得更加复杂。如果数据基是通过抽象选择器和构造器来访问的，那么这种表示的变化将不需要对系统的其余部分做任何修改。

**校订后**

当然，有比无序表更好的方式来表示大型集合。必须“随机访问”记录的信息检索系统通常通过基于树的方法实现，例如前面讨论的二叉树表示。在设计这样的系统时，数据抽象的方法论可以大有帮助。设计者可以使用简单直接的表示（如无序表）创建初始实现。这对于最终系统来说是不合适的，但它可以用于提供一个“快速而粗糙”的数据库来测试系统的其余部分。之后，数据表示可以被修改得更加精巧。如果数据库是通过抽象选择函数和构造函数来访问的，那么这种表示的变化将不需要对系统的其余部分做任何修改。

### 2_002e3:0095

**原文**

2.3.4 Example: Huffman Encoding Trees

**校订前**

2.3.4 示例：Huffman编码树

**校订后**

2.3.4 示例：霍夫曼编码树

### 2_002e3:0103

**原文**

In general, we can attain significant savings if we use variable-length prefix codes that take advantage of the relative frequencies of the symbols in the messages to be encoded. One particular scheme for doing this is called the Huffman encoding method, after its discoverer, David Huffman. A Huffman code can be represented as a binary tree whose leaves are the symbols that are encoded. At each non-leaf node of the tree there is a set containing all the symbols in the leaves that lie below the node. In addition, each symbol at a leaf is assigned a weight (which is its relative frequency), and each non-leaf node contains a weight that is the sum of all the weights of the leaves lying below it. The weights are not used in the encoding or the decoding process. We will see below how they are used to help construct the tree.

**校订前**

一般来说，如果我们使用变长前缀码，利用要编码的消息中符号的相对频率，我们可以获得显著的节省。用于此目的的一种特定方案称为Huffman编码方法，以其发现者David Huffman命名。Huffman编码可以表示为一棵二叉树，其叶子是所编码的符号。在树的每个非叶节点处，有一个包含该节点下方叶子中所有符号的集合。此外，叶子处的每个符号被赋予一个权重（即其相对频率），每个非叶节点包含一个权重，该权重是其下方所有叶子权重的总和。权重不用于编码或解码过程。我们将在下面看到它们如何用于帮助构建树。

**校订后**

一般来说，如果我们使用变长前缀码，利用要编码的消息中符号的相对频率，我们可以获得显著的节省。用于此目的的一种特定方案称为霍夫曼编码方法，以其发现者David Huffman命名。霍夫曼编码可以表示为一棵二叉树，其叶子是所编码的符号。在树的每个非叶节点处，有一个包含该节点下方叶子中所有符号的集合。此外，叶子处的每个符号被赋予一个权重（即其相对频率），每个非叶节点包含一个权重，该权重是其下方所有叶子权重的总和。权重不用于编码或解码过程。我们将在下面看到它们如何用于帮助构建树。

### 2_002e3:0117

**原文**

The procedures `symbols` and `weight` must do something slightly different depending on whether they are called with a leaf or a general tree. These are simple examples of generic procedures (procedures that can handle more than one kind of data), which we will have much more to say about in 2.4 and 2.5.

**校订前**

过程 `symbols` 和 `weight` 必须根据它们是用叶子还是一般树调用而略有不同。这些是 泛型过程（可以处理多种数据的过程）的简单例子，我们将在 2.4 和 2.5 中对此有更多讨论。

**校订后**

过程 `symbols` 和 `weight` 必须根据它们是用叶子还是一般树调用而略有不同。这些是 通用过程（可以处理多种数据的过程）的简单例子，我们将在 2.4 和 2.5 中对此有更多讨论。

### 2_002e3:0123

**原文**

We will represent a set of leaves and trees as a list of elements, arranged in increasing order of weight. The following `adjoin-set` procedure for constructing sets is similar to the one described in Exercise 2.61; however, items are compared by their weights, and the element being added to the set is never already in it.

**校订前**

我们将叶子和树的集合表示为一个元素表，按权重递增排列。下面的`adjoin-set`过程用于构造集合，与习题2.61中描述的过程类似；然而，项按其权重进行比较，并且被添加到集合中的元素从不在其中。

**校订后**

我们将叶子和树的集合表示为一个元素表，按权重递增排列。下面的`adjoin-set`过程用于构造集合，与习题2.61中描述的过程类似；然而，项按其权重进行比较，并且要添加的元素此前都不在集合中。

### 2_002e3:0124

**原文**

The following procedure takes a list of symbol-frequency pairs such as `((A 4) (B 2) (C 1) (D 1))` and constructs an initial ordered set of leaves, ready to be merged according to the Huffman algorithm:

**校订前**

下面的过程接受一个符号-频率对的表，例如`((A 4) (B 2) (C 1) (D 1))`，并构造一个初始的有序叶子集合，准备好根据 Huffman 算法进行合并：

**校订后**

下面的过程接受一个符号-频率对的表，例如`((A 4) (B 2) (C 1) (D 1))`，并构造一个初始的有序叶子集合，准备好根据 霍夫曼 算法进行合并：

### 2_002e3:0129

**原文**

Exercise 2.69: The following procedure takes as its argument a list of symbol-frequency pairs (where no symbol appears in more than one pair) and generates a Huffman encoding tree according to the Huffman algorithm.

**校订前**

习题2.69： 下面的过程接受一个符号-频率对的表作为参数（其中没有符号出现在多于一个对中），并根据 Huffman 算法生成一棵 Huffman 编码树。

**校订后**

习题2.69： 下面的过程接受一个符号-频率对的表作为参数（其中没有符号出现在多于一个对中），并根据 霍夫曼 算法生成一棵 霍夫曼 编码树。

### 2_002e3:0130

**原文**

`Make-leaf-set` is the procedure given above that transforms the list of pairs into an ordered set of leaves. `Successive-merge` is the procedure you must write, using `make-code-tree` to successively merge the smallest-weight elements of the set until there is only one element left, which is the desired Huffman tree. (This procedure is slightly tricky, but not really complicated. If you find yourself designing a complex procedure, then you are almost certainly doing something wrong. You can take significant advantage of the fact that we are using an ordered set representation.)

**校订前**

`Make-leaf-set`是上面给出的过程，它将符号-频率对的表转换为有序的叶子集合。`Successive-merge`是你必须编写的过程，使用`make-code-tree`依次合并集合中权重最小的元素，直到只剩下一个元素，即所需的 Huffman 树。（这个过程稍微有点棘手，但并不真正复杂。如果你发现自己正在设计一个复杂的过程，那么你几乎肯定做错了什么。你可以显著利用我们使用有序集合表示这一事实。）

**校订后**

`Make-leaf-set`是上面给出的过程，它将符号-频率对的表转换为有序的叶子集合。`Successive-merge`是你必须编写的过程，使用`make-code-tree`依次合并集合中权重最小的元素，直到只剩下一个元素，即所需的 霍夫曼 树。（这个过程稍微有点棘手，但并不真正复杂。如果你发现自己正在设计一个复杂的过程，那么你几乎肯定做错了什么。你可以显著利用我们使用有序集合表示这一事实。）

### 2_002e3:0132

**原文**

Use `generate-huffman-tree` (Exercise 2.69) to generate a corresponding Huffman tree, and use `encode` (Exercise 2.68) to encode the following message:

**校订前**

使用`generate-huffman-tree`（习题2.69）生成相应的 Huffman 树，并使用`encode`（习题2.68）编码以下消息：

**校订后**

使用`generate-huffman-tree`（习题2.69）生成相应的 霍夫曼 树，并使用`encode`（习题2.68）编码以下消息：

### 2_002e3:0134

**原文**

Exercise 2.71: Suppose we have a Huffman tree for an alphabet of $n$ symbols, and that the relative frequencies of the symbols are $1,2,4,…,2^(n−1)$. Sketch the tree for $n=5$; for $n=10$. In such a tree (for general $n$) how many bits are required to encode the most frequent symbol? The least frequent symbol?

**校订前**

习题2.71： 假设我们有一个针对$n$个符号的字母表的 Huffman 树，并且这些符号的相对频率为$1,2,4,…,2^(n−1)$。画出$n=5$的树；画出$n=10$的树。在这样的树中（对于一般的$n$），编码最频繁的符号需要多少位？最不频繁的符号呢？

**校订后**

习题2.71： 假设我们有一个针对$n$个符号的字母表的 霍夫曼 树，并且这些符号的相对频率为$1,2,4,…,2^(n−1)$。画出$n=5$的树；画出$n=10$的树。在这样的树中（对于一般的$n$），编码最频繁的符号需要多少位？最不频繁的符号呢？

### 2_002e3:0150

**原文**

[注108] See Hamming 1980 for a discussion of the mathematical properties of Huffman codes.

**校订前**

[注108] 关于Huffman码的数学性质的讨论，参见Hamming1980。

**校订后**

[注108] 关于霍夫曼码的数学性质的讨论，参见Hamming1980。

### 2_002e4:0009

**原文**

We begin with the simple complex-number example. We will see how type tags and data-directed style enable us to design separate rectangular and polar representations for complex numbers while maintaining the notion of an abstract “complex-number” data object. We will accomplish this by defining arithmetic procedures for complex numbers (`add-complex`, `sub-complex`, `mul-complex`, and `div-complex`) in terms of generic selectors that access parts of a complex number independent of how the number is represented. The resulting complex-number system, as shown in Figure 2.19, contains two different kinds of abstraction barriers. The “horizontal” abstraction barriers play the same role as the ones in Figure 2.1. They isolate “higher-level” operations from “lower-level” representations. In addition, there is a “vertical” barrier that gives us the ability to separately design and install alternative representations.

**校订前**

我们从简单的复数例子开始。我们将看到类型标签和数据导向风格如何使我们能够为复数设计独立的直角坐标和极坐标表示，同时保持抽象“复数”数据对象的概念。我们将通过根据通用选择器来定义复数的算术过程（`add-complex`、`sub-complex`、`mul-complex`和`div-complex`）来实现这一点，这些选择器访问复数的各个部分，而与数字如何表示无关。由此得到的复数系统，如图2.19所示，包含两种不同的抽象屏障。“水平”抽象屏障与图2.1中的屏障作用相同。它们将“高层”操作与“低层”表示隔离开来。此外，还有一个“垂直”屏障，使我们能够分别设计和安装替代表示。

**校订后**

我们从简单的复数例子开始。我们将看到类型标签和数据导向风格如何使我们能够为复数设计独立的直角坐标和极坐标表示，同时保持抽象“复数”数据对象的概念。我们将通过根据通用选择函数来定义复数的算术过程（`add-complex`、`sub-complex`、`mul-complex`和`div-complex`）来实现这一点，这些选择函数访问复数的各个部分，而与数字如何表示无关。由此得到的复数系统，如图2.19所示，包含两种不同的抽象屏障。“水平”抽象屏障与图2.1中的屏障作用相同。它们将“高层”操作与“低层”表示隔离开来。此外，还有一个“垂直”屏障，使我们能够分别设计和安装替代表示。

### 2_002e4:0034

**原文**

Each generic selector is implemented as a procedure that checks the tag of its argument and calls the appropriate procedure for handling data of that type. For example, to obtain the real part of a complex number, `real-part` examines the tag to determine whether to use Ben’s `real-part-rectangular` or Alyssa’s `real-part-polar`. In either case, we use `contents` to extract the bare, untagged datum and send this to the rectangular or polar procedure as required:

**校订前**

每个通用选择器都实现为一个过程，它检查其参数的类型标签，并调用适当的过程来处理该类型的数据。例如，为了获得一个复数的实部，`real-part` 检查类型标签，以确定是使用 Ben 的 `real-part-rectangular` 还是 Alyssa 的 `real-part-polar`。无论哪种情况，我们都使用 `contents` 提取出裸的、无标签的数据，并按需将其发送给直角坐标或极坐标过程：

**校订后**

每个通用选择函数都实现为一个过程，它检查其参数的类型标签，并调用适当的过程来处理该类型的数据。例如，为了获得一个复数的实部，`real-part` 检查类型标签，以确定是使用 Ben 的 `real-part-rectangular` 还是 Alyssa 的 `real-part-polar`。无论哪种情况，我们都使用 `contents` 提取出裸的、无标签的数据，并按需将其发送给直角坐标或极坐标过程：

### 2_002e4:0035

**原文**

To implement the complex-number arithmetic operations, we can use the same procedures `add-complex`, `sub-complex`, `mul-complex`, and `div-complex` from 2.4.1, because the selectors they call are generic, and so will work with either representation. For example, the procedure `add-complex` is still

**校订前**

为了实现复数算术运算，我们可以使用来自 2.4.1 的相同过程 `add-complex`、`sub-complex`、`mul-complex` 和 `div-complex`，因为它们调用的选择器是通用的，所以对两种表示都适用。例如，过程 `add-complex` 仍然是

**校订后**

为了实现复数算术运算，我们可以使用来自 2.4.1 的相同过程 `add-complex`、`sub-complex`、`mul-complex` 和 `div-complex`，因为它们调用的选择函数是通用的，所以对两种表示都适用。例如，过程 `add-complex` 仍然是

### 2_002e4:0037

**原文**

The resulting complex-number system has the structure shown in Figure 2.21. The system has been decomposed into three relatively independent parts: the complex-number-arithmetic operations, Alyssa’s polar implementation, and Ben’s rectangular implementation. The polar and rectangular implementations could have been written by Ben and Alyssa working separately, and both of these can be used as underlying representations by a third programmer implementing the complex-arithmetic procedures in terms of the abstract constructor/selector interface.

**校订前**

由此得到的复数系统具有 图 2.21 所示的结构。该系统已被分解为三个相对独立的部分：复数算术运算、Alyssa 的极坐标实现和 Ben 的直角坐标实现。极坐标和直角坐标实现本可以由 Ben 和 Alyssa 分别编写，而这两者都可以被第三位程序员用作底层表示，以基于抽象构造器/选择器接口来实现复数算术过程。

**校订后**

由此得到的复数系统具有 图 2.21 所示的结构。该系统已被分解为三个相对独立的部分：复数算术运算、Alyssa 的极坐标实现和 Ben 的直角坐标实现。极坐标和直角坐标实现本可以由 Ben 和 Alyssa 分别编写，而这两者都可以被第三位程序员用作底层表示，以基于抽象构造函数/选择函数接口来实现复数算术过程。

### 2_002e4:0039

**原文**

Since each data object is tagged with its type, the selectors operate on the data in a generic manner. That is, each selector is defined to have a behavior that depends upon the particular type of data it is applied to. Notice the general mechanism for interfacing the separate representations: Within a given representation implementation (say, Alyssa’s polar package) a complex number is an untyped pair (magnitude, angle). When a generic selector operates on a number of `polar` type, it strips off the tag and passes the contents on to Alyssa’s code. Conversely, when Alyssa constructs a number for general use, she tags it with a type so that it can be appropriately recognized by the higher-level procedures. This discipline of stripping off and attaching tags as data objects are passed from level to level can be an important organizational strategy, as we shall see in 2.5.

**校订前**

由于每个数据对象都带有其类型标签，选择器以通用方式作用于数据。也就是说，每个选择器被定义为具有一种行为，该行为取决于它所应用的数据的特定类型。注意用于连接各个独立表示的通用机制：在给定的表示实现内部（比如 Alyssa 的极坐标包），复数是一个无类型的序对（模，幅角）。当一个通用选择器作用于一个 `polar` 类型的数时，它剥去标签，并将内容传递给 Alyssa 的代码。反过来，当 Alyssa 构造一个供一般使用的数时，她给它加上类型标签，以便它能被更高层的过程适当地识别。这种在数据对象逐层传递时剥去和附加标签的规则可以是一种重要的组织策略，我们将在 2.5 中看到。

**校订后**

由于每个数据对象都带有其类型标签，选择函数以通用方式作用于数据。也就是说，每个选择函数被定义为具有一种行为，该行为取决于它所应用的数据的特定类型。注意用于连接各个独立表示的通用机制：在给定的表示实现内部（比如 Alyssa 的极坐标包），复数是一个无类型的序对（模，幅角）。当一个通用选择函数作用于一个 `polar` 类型的数时，它剥去标签，并将内容传递给 Alyssa 的代码。反过来，当 Alyssa 构造一个供一般使用的数时，她给它加上类型标签，以便它能被更高层的过程适当地识别。这种在数据对象逐层传递时剥去和附加标签的规则可以是一种重要的组织策略，我们将在 2.5 中看到。

### 2_002e4:0041

**原文**

The general strategy of checking the type of a datum and calling an appropriate procedure is called dispatching on type. This is a powerful strategy for obtaining modularity in system design. On the other hand, implementing the dispatch as in 2.4.2 has two significant weaknesses. One weakness is that the generic interface procedures (`real-part`, `imag-part`, `magnitude`, and `angle`) must know about all the different representations. For instance, suppose we wanted to incorporate a new representation for complex numbers into our complex-number system. We would need to identify this new representation with a type, and then add a clause to each of the generic interface procedures to check for the new type and apply the appropriate selector for that representation.

**校订前**

检查数据的类型并调用适当过程的一般策略称为 基于类型的分派。这是在系统设计中获得模块化的一种强大策略。另一方面，像 2.4.2 那样实现分派有两个显著弱点。一个弱点是通用接口过程（`real-part`、`imag-part`、`magnitude` 和 `angle`）必须知道所有不同的表示。例如，假设我们想将一种新的复数表示纳入我们的复数系统。我们需要用类型来标识这种新表示，然后向每个通用接口过程添加一个子句，以检查新类型并应用该表示的适当选择器。

**校订后**

检查数据的类型并调用适当过程的一般策略称为 基于类型的分派。这是在系统设计中获得模块化的一种强大策略。另一方面，像 2.4.2 那样实现分派有两个显著弱点。一个弱点是通用接口过程（`real-part`、`imag-part`、`magnitude` 和 `angle`）必须知道所有不同的表示。例如，假设我们想将一种新的复数表示纳入我们的复数系统。我们需要用类型来标识这种新表示，然后向每个通用接口过程添加一个子句，以检查新类型并应用该表示的适当选择函数。

### 2_002e4:0042

**原文**

Another weakness of the technique is that even though the individual representations can be designed separately, we must guarantee that no two procedures in the entire system have the same name. This is why Ben and Alyssa had to change the names of their original procedures from 2.4.1.

**校订前**

该技术的另一个弱点是，即使各个表示可以分别设计，我们也必须保证整个系统中没有两个过程具有相同的名称。这就是为什么 Ben 和 Alyssa 不得不从 2.4.1 更改他们原始过程的名称。

**校订后**

该技术的另一个弱点是，即使各个表示可以分别设计，我们也必须保证整个系统中没有两个过程具有相同的名称。这就是为什么 Ben 和 Alyssa 不得不更改 2.4.1 中他们原始过程的名称。

### 2_002e4:0043

**原文**

The issue underlying both of these weaknesses is that the technique for implementing generic interfaces is not additive. The person implementing the generic selector procedures must modify those procedures each time a new representation is installed, and the people interfacing the individual representations must modify their code to avoid name conflicts. In each of these cases, the changes that must be made to the code are straightforward, but they must be made nonetheless, and this is a source of inconvenience and error. This is not much of a problem for the complex-number system as it stands, but suppose there were not two but hundreds of different representations for complex numbers. And suppose that there were many generic selectors to be maintained in the abstract-data interface. Suppose, in fact, that no one programmer knew all the interface procedures or all the representations. The problem is real and must be addressed in such programs as large-scale data-base-management systems.

**校订前**

这两个弱点的根本问题在于，实现通用接口的技术不是可加的。实现通用选择器过程的人必须在每次安装新表示时修改这些过程，而与各个表示接口的人必须修改他们的代码以避免名称冲突。在每种情况下，必须对代码进行的更改都是直截了当的，但无论如何都必须进行，这是不便和错误的来源。对于目前的复数系统来说，这不是什么大问题，但假设复数不是有两种而是有数百种不同的表示。再假设抽象数据接口中有许多通用选择器需要维护。事实上，假设没有一个程序员知道所有的接口过程或所有的表示。这个问题是真实存在的，必须在大规模数据库管理系统这样的程序中加以解决。

**校订后**

这两个弱点的根本问题在于，实现通用接口的技术不是可加的。实现通用选择函数过程的人必须在每次安装新表示时修改这些过程，而负责将各个表示接入系统的人必须修改他们的代码以避免名称冲突。在每种情况下，必须对代码进行的更改都是直截了当的，但无论如何都必须进行，这是不便和错误的来源。对于目前的复数系统来说，这不是什么大问题，但假设复数不是有两种而是有数百种不同的表示。再假设抽象数据接口中有许多通用选择函数需要维护。事实上，假设没有一个程序员知道所有的接口过程或所有的表示。这个问题是真实存在的，必须在大规模数据库管理系统这样的程序中加以解决。

### 2_002e4:0052

**原文**

Notice that the internal procedures here are the same procedures from 2.4.1 that Ben wrote when he was working in isolation. No changes are necessary in order to interface them to the rest of the system. Moreover, since these procedure definitions are internal to the installation procedure, Ben needn’t worry about name conflicts with other procedures outside the rectangular package. To interface these to the rest of the system, Ben installs his `real-part` procedure under the operation name `real-part` and the type `(rectangular)`, and similarly for the other selectors.[注111] The interface also defines the constructors to be used by the external system.[注112] These are identical to Ben’s internally defined constructors, except that they attach the tag.

**校订前**

注意，这里的内部过程与 Ben 在孤立工作时所写的2.4.1中的过程相同。为了将它们与系统的其余部分接口，不需要任何更改。此外，由于这些过程定义是安装过程的内部定义，Ben 不必担心与直角坐标包外部其他过程的名称冲突。为了将这些过程与系统的其余部分接口，Ben 将他的`real-part`过程安装在操作名`real-part`和类型`(rectangular)`下，其他选择器也类似。[注111]接口还定义了供外部系统使用的构造函数。[注112]这些与 Ben 内部定义的构造函数相同，只是它们附加了标签。

**校订后**

注意，这里的内部过程与 Ben 在孤立工作时所写的2.4.1中的过程相同。为了将它们与系统的其余部分接口，不需要任何更改。此外，由于这些过程定义是安装过程的内部定义，Ben 不必担心与直角坐标包外部其他过程的名称冲突。为了将这些过程与系统的其余部分接口，Ben 将他的`real-part`过程安装在操作名`real-part`和类型`(rectangular)`下，其他选择函数也类似。[注111]接口还定义了供外部系统使用的构造函数。[注112]这些与 Ben 内部定义的构造函数相同，只是它们附加了标签。

### 2_002e4:0055

**原文**

The complex-arithmetic selectors access the table by means of a general “operation” procedure called `apply-generic`, which applies a generic operation to some arguments. `Apply-generic` looks in the table under the name of the operation and the types of the arguments and applies the resulting procedure if one is present:[注113]

**校订前**

复数算术选择器通过一个称为`apply-generic`的通用“操作”过程访问表，该过程将通用操作应用于某些参数。`Apply-generic`在表中查找操作名称和参数类型，如果存在相应的过程，则应用它：[注113]

**校订后**

复数算术选择函数通过一个称为`apply-generic`的通用“操作”过程访问表，该过程将通用操作应用于某些参数。`Apply-generic`在表中查找操作名称和参数类型，如果存在相应的过程，则应用它：[注113]

### 2_002e4:0056

**原文**

Using `apply-generic`, we can define our generic selectors as follows:

**校订前**

使用`apply-generic`，我们可以如下定义通用选择器：

**校订后**

使用`apply-generic`，我们可以如下定义通用选择函数：

### 2_002e4:0063

**原文**

Choose any additional differentiation rule that you like, such as the one for exponents (Exercise 2.56), and install it in this data-directed system.

**校订前**

选择任何你喜欢的额外求导规则，例如指数运算的规则（习题2.56），并将其安装到这个数据导向系统中。

**校订后**

选择任何你喜欢的额外求导规则，例如幂运算的规则（习题2.56），并将其安装到这个数据导向系统中。

### 2_002e4:0070

**原文**

Implement for headquarters a `find-employee-record` procedure. This should search all the divisions’ files for the record of a given employee and return the record. Assume that this procedure takes as arguments an employee’s name and a list of all the divisions’ files.

**校订前**

为总部实现一个`find-employee-record`过程。它应搜索所有部门的文件，查找给定员工的记录并返回该记录。假设该过程以员工姓名和所有部门文件的列表作为参数。

**校订后**

为总部实现一个`find-employee-record`过程。它应搜索所有部门的文件，查找给定员工的记录并返回该记录。假设该过程以员工姓名和所有部门文件的表作为参数。

### 2_002e4:0074

**原文**

An alternative implementation strategy is to decompose the table into columns and, instead of using “intelligent operations” that dispatch on data types, to work with “intelligent data objects” that dispatch on operation names. We can do this by arranging things so that a data object, such as a rectangular number, is represented as a procedure that takes as input the required operation name and performs the operation indicated. In such a discipline, `make-from-real-imag` could be written as

**校订前**

另一种实现策略是将表分解为列，并且不使用根据数据类型进行分派的“智能操作”，而是使用根据操作名称进行分派的“智能数据对象”。我们可以通过这样安排来实现：让一个数据对象（例如矩形数）表示为一个过程，该过程接受所需操作名称作为输入并执行所指示的操作。在这种方式下，`make-from-real-imag`可以写成：

**校订后**

另一种实现策略是将表分解为列，并且不使用根据数据类型进行分派的“智能操作”，而是使用根据操作名称进行分派的“智能数据对象”。我们可以通过这样安排来实现：让一个数据对象（例如直角坐标形式的复数）表示为一个过程，该过程接受所需操作名称作为输入并执行所指示的操作。在这种方式下，`make-from-real-imag`可以写成：

### 2_002e5:0008

**原文**

The task of designing generic arithmetic operations is analogous to that of designing the generic complex-number operations. We would like, for instance, to have a generic addition procedure `add` that acts like ordinary primitive addition `+` on ordinary numbers, like `add-rat` on rational numbers, and like `add-complex` on complex numbers. We can implement `add`, and the other generic arithmetic operations, by following the same strategy we used in 2.4.3 to implement the generic selectors for complex numbers. We will attach a type tag to each kind of number and cause the generic procedure to dispatch to an appropriate package according to the data type of its arguments.

**校订前**

设计通用算术操作的任务类似于设计通用复数操作的任务。例如，我们希望有一个通用加法过程 `add`，它对普通数的作用像普通基本加法 `+`，对有理数的作用像 `add-rat`，对复数的作用像 `add-complex`。我们可以按照在 2.4.3 中实现复数通用选择器时所用的相同策略来实现 `add` 以及其他通用算术操作。我们将为每种数附加一个类型标签，并使通用过程根据其参数的数据类型分派到适当的包。

**校订后**

设计通用算术操作的任务类似于设计通用复数操作的任务。例如，我们希望有一个通用加法过程 `add`，它对普通数的作用像普通基本加法 `+`，对有理数的作用像 `add-rat`，对复数的作用像 `add-complex`。我们可以按照在 2.4.3 中实现复数通用选择函数时所用的相同策略来实现 `add` 以及其他通用算术操作。我们将为每种数附加一个类型标签，并使通用过程根据其参数的数据类型分派到适当的包。

### 2_002e5:0014

**原文**

Programs outside the complex-number package can construct complex numbers either from real and imaginary parts or from magnitudes and angles. Notice how the underlying procedures, originally defined in the rectangular and polar packages, are exported to the complex package, and exported from there to the outside world.

**校订前**

复数包之外的程序既可以从实部和虚部构造复数，也可以从模和辐角构造复数。注意，原本定义在直角坐标包和极坐标包中的底层过程是如何导出到复数包，再从那里导出到外部世界的。

**校订后**

复数包之外的程序既可以从实部和虚部构造复数，也可以从模和幅角构造复数。注意，原本定义在直角坐标包和极坐标包中的底层过程是如何导出到复数包，再从那里导出到外部世界的。

### 2_002e5:0018

**原文**

Exercise 2.77: Louis Reasoner tries to evaluate the expression `(magnitude z)` where `z` is the object shown in Figure 2.24. To his surprise, instead of the answer 5 he gets an error message from `apply-generic`, saying there is no method for the operation `magnitude` on the types `(complex)`. He shows this interaction to Alyssa P. Hacker, who says “The problem is that the complex-number selectors were never defined for `complex` numbers, just for `polar` and `rectangular` numbers. All you have to do to make this work is add the following to the `complex` package:”

**校订前**

习题2.77： Louis Reasoner 试图求值表达式`(magnitude z)`，其中`z`是图2.24所示的对象。令他惊讶的是，他没有得到答案5，反而从`apply-generic`收到一条错误消息，说对于类型`(complex)`没有用于操作`magnitude`的方法。他把这个交互展示给 Alyssa P. Hacker，她说：“问题在于，复数选择器从未为`complex`数定义过，只为`polar`数和`rectangular`数定义过。要让这个工作，你只需将以下内容添加到`complex`包中：”

**校订后**

习题2.77： Louis Reasoner 试图求值表达式`(magnitude z)`，其中`z`是图2.24所示的对象。令他惊讶的是，他没有得到答案5，反而从`apply-generic`收到一条错误消息，说对于类型`(complex)`没有用于操作`magnitude`的方法。他把这个交互展示给 Alyssa P. Hacker，她说：“问题在于，复数选择函数从未为`complex`数定义过，只为`polar`数和`rectangular`数定义过。要让这个工作，你只需将以下内容添加到`complex`包中：”

### 2_002e5:0026

**原文**

This technique works, but it is cumbersome. With such a system, the cost of introducing a new type is not just the construction of the package of procedures for that type but also the construction and installation of the procedures that implement the cross-type operations. This can easily be much more code than is needed to define the operations on the type itself. The method also undermines our ability to combine separate packages additively, or at least to limit the extent to which the implementors of the individual packages need to take account of other packages. For instance, in the example above, it seems reasonable that handling mixed operations on complex numbers and ordinary numbers should be the responsibility of the complex-number package. Combining rational numbers and complex numbers, however, might be done by the complex package, by the rational package, or by some third package that uses operations extracted from these two packages. Formulating coherent policies on the division of responsibility among packages can be an overwhelming task in designing systems with many packages and many cross-type operations.

**校订前**

这种技术可行，但很笨拙。使用这样的系统，引入一个新类型的代价不仅是构造该类型的过程包，还包括构造和安装实现跨类型运算的过程。这很容易比定义该类型本身上的运算所需的代码多得多。这种方法还削弱了我们以可加方式组合独立包的能力，或者至少限制了各个包的实现者需要考虑其他包的程度。例如，在上面的例子中，处理复数和普通数的混合运算似乎应该是复数包的责任。然而，组合有理数和复数可能由复数包、有理数包或某个使用从这两个包中提取的运算的第三方包来完成。在涉及许多包和许多跨类型运算的系统设计中，制定关于包之间责任划分的一致策略可能是一项艰巨的任务。

**校订后**

这种技术可行，但很笨拙。使用这样的系统，引入一个新类型的代价不仅是构造该类型的过程包，还包括构造和安装实现跨类型运算的过程。这很容易比定义该类型本身上的运算所需的代码多得多。这种方法还削弱了我们以可加方式组合独立包的能力，或者至少削弱了我们限制各个包的实现者需要考虑其他包的程度的能力。例如，在上面的例子中，处理复数和普通数的混合运算似乎应该是复数包的责任。然而，组合有理数和复数可能由复数包、有理数包或某个使用从这两个包中提取的运算的第三方包来完成。在涉及许多包和许多跨类型运算的系统设计中，制定关于包之间责任划分的一致策略可能是一项艰巨的任务。

### 2_002e5:0027

**原文**

Coercion

**校订前**

强制

**校订后**

强制转换

### 2_002e5:0028

**原文**

In the general situation of completely unrelated operations acting on completely unrelated types, implementing explicit cross-type operations, cumbersome though it may be, is the best that one can hope for. Fortunately, we can usually do better by taking advantage of additional structure that may be latent in our type system. Often the different data types are not completely independent, and there may be ways by which objects of one type may be viewed as being of another type. This process is called coercion. For example, if we are asked to arithmetically combine an ordinary number with a complex number, we can view the ordinary number as a complex number whose imaginary part is zero. This transforms the problem to that of combining two complex numbers, which can be handled in the ordinary way by the complex-arithmetic package.

**校订前**

在完全无关的运算作用于完全无关的类型的一般情况下，实现显式的跨类型运算，尽管可能笨拙，但已是人们所能期望的最好办法。幸运的是，我们通常可以通过利用类型系统中可能潜藏的额外结构来做得更好。通常不同的数据类型并非完全独立，可能存在将一种类型的对象视为另一种类型的方法。这个过程称为强制。例如，如果要求我们将一个普通数与一个复数进行算术组合，我们可以将普通数视为虚部为零的复数。这将问题转化为组合两个复数的问题，可以由复数算术包以通常方式处理。

**校订后**

在完全无关的运算作用于完全无关的类型的一般情况下，实现显式的跨类型运算，尽管可能笨拙，但已是人们所能期望的最好办法。幸运的是，我们通常可以通过利用类型系统中可能潜藏的额外结构来做得更好。通常不同的数据类型并非完全独立，可能存在将一种类型的对象视为另一种类型的方法。这个过程称为强制转换。例如，如果要求我们将一个普通数与一个复数进行算术组合，我们可以将普通数视为虚部为零的复数。这将问题转化为组合两个复数的问题，可以由复数算术包以通常方式处理。

### 2_002e5:0029

**原文**

In general, we can implement this idea by designing coercion procedures that transform an object of one type into an equivalent object of another type. Here is a typical coercion procedure, which transforms a given ordinary number to a complex number with that real part and zero imaginary part:

**校订前**

一般来说，我们可以通过设计强制过程来实现这个想法，这些过程将一种类型的对象转换为另一种类型的等价对象。下面是一个典型的强制过程，它将给定的普通数转换为具有该实部和零虚部的复数：

**校订后**

一般来说，我们可以通过设计强制转换过程来实现这个想法，这些过程将一种类型的对象转换为另一种类型的等价对象。下面是一个典型的强制转换过程，它将给定的普通数转换为具有该实部和零虚部的复数：

### 2_002e5:0030

**原文**

We install these coercion procedures in a special coercion table, indexed under the names of the two types:

**校订前**

我们将这些强制过程安装在一个特殊的强制表中，以两个类型的名称为索引：

**校订后**

我们将这些强制转换过程安装在一个特殊的强制转换表中，以两个类型的名称为索引：

### 2_002e5:0032

**原文**

Once the coercion table has been set up, we can handle coercion in a uniform manner by modifying the `apply-generic` procedure of 2.4.3. When asked to apply an operation, we first check whether the operation is defined for the arguments’ types, just as before. If so, we dispatch to the procedure found in the operation-and-type table. Otherwise, we try coercion. For simplicity, we consider only the case where there are two arguments.[注116] We check the coercion table to see if objects of the first type can be coerced to the second type. If so, we coerce the first argument and try the operation again. If objects of the first type cannot in general be coerced to the second type, we try the coercion the other way around to see if there is a way to coerce the second argument to the type of the first argument. Finally, if there is no known way to coerce either type to the other type, we give up. Here is the procedure:

**校订前**

一旦强制表设置好，我们就可以通过修改 2.4.3 的 `apply-generic` 过程来以统一的方式处理强制。当要求应用一个运算时，我们首先像之前一样检查该运算是否对参数的类型有定义。如果有，我们就分派到运算-类型表中找到的过程。否则，我们尝试强制。为简单起见，我们只考虑有两个参数的情况。[注116]我们检查强制表，看第一种类型的对象是否可以强制转换为第二种类型。如果可以，我们强制转换第一个参数并再次尝试该运算。如果第一种类型的对象通常不能强制转换为第二种类型，我们尝试另一种方向的强制，看是否有办法将第二个参数强制转换为第一个参数的类型。最后，如果没有已知的方法将任一类型强制转换为另一类型，我们就放弃。以下是该过程：

**校订后**

一旦强制转换表设置好，我们就可以通过修改 2.4.3 的 `apply-generic` 过程来以统一的方式处理强制转换。当要求应用一个运算时，我们首先像之前一样检查该运算是否对参数的类型有定义。如果有，我们就分派到运算-类型表中找到的过程。否则，我们尝试强制转换。为简单起见，我们只考虑有两个参数的情况。[注116]我们检查强制转换表，看第一种类型的对象是否可以强制转换为第二种类型。如果可以，我们强制转换第一个参数并再次尝试该运算。如果第一种类型的对象通常不能强制转换为第二种类型，我们尝试另一种方向的强制转换，看是否有办法将第二个参数强制转换为第一个参数的类型。最后，如果没有已知的方法将任一类型强制转换为另一类型，我们就放弃。以下是该过程：

### 2_002e5:0033

**原文**

This coercion scheme has many advantages over the method of defining explicit cross-type operations, as outlined above. Although we still need to write coercion procedures to relate the types (possibly $n^(2)$ procedures for a system with $n$ types), we need to write only one procedure for each pair of types rather than a different procedure for each collection of types and each generic operation.[注117] What we are counting on here is the fact that the appropriate transformation between types depends only on the types themselves, not on the operation to be applied.

**校订前**

如上所述，这种强制方案比定义显式跨类型运算的方法有许多优点。尽管我们仍然需要编写强制过程来关联类型（对于具有 $n$ 个类型的系统，可能需要 $n^(2)$ 个过程），但我们只需要为每一对类型编写一个过程，而不是为每个类型集合和每个通用运算编写不同的过程。[注117]我们在这里依赖的事实是，类型之间的适当转换仅取决于类型本身，而不取决于要应用的运算。

**校订后**

如上所述，这种强制转换方案比定义显式跨类型运算的方法有许多优点。尽管我们仍然需要编写强制转换过程来关联类型（对于具有 $n$ 个类型的系统，可能需要 $n^(2)$ 个过程），但我们只需要为每一对类型编写一个过程，而不是为每个类型集合和每个通用运算编写不同的过程。[注117]我们在这里依赖的事实是，类型之间的适当转换仅取决于类型本身，而不取决于要应用的运算。

### 2_002e5:0034

**原文**

On the other hand, there may be applications for which our coercion scheme is not general enough. Even when neither of the objects to be combined can be converted to the type of the other it may still be possible to perform the operation by converting both objects to a third type. In order to deal with such complexity and still preserve modularity in our programs, it is usually necessary to build systems that take advantage of still further structure in the relations among types, as we discuss next.

**校订前**

另一方面，可能存在我们的强制方案不够通用的应用。即使要组合的两个对象都不能转换为对方的类型，仍然可能通过将两个对象都转换为第三种类型来执行运算。为了处理这种复杂性并在程序中保持模块性，通常有必要构建利用类型之间关系中更深层结构的系统，正如我们接下来讨论的那样。

**校订后**

另一方面，可能存在我们的强制转换方案不够通用的应用。即使要组合的两个对象都不能转换为对方的类型，仍然可能通过将两个对象都转换为第三种类型来执行运算。为了处理这种复杂性并在程序中保持模块性，通常有必要构建利用类型之间关系中更深层结构的系统，正如我们接下来讨论的那样。

### 2_002e5:0036

**原文**

The coercion scheme presented above relied on the existence of natural relations between pairs of types. Often there is more “global” structure in how the different types relate to each other. For instance, suppose we are building a generic arithmetic system to handle integers, rational numbers, real numbers, and complex numbers. In such a system, it is quite natural to regard an integer as a special kind of rational number, which is in turn a special kind of real number, which is in turn a special kind of complex number. What we actually have is a so-called hierarchy of types, in which, for example, integers are a subtype of rational numbers (i.e., any operation that can be applied to a rational number can automatically be applied to an integer). Conversely, we say that rational numbers form a supertype of integers. The particular hierarchy we have here is of a very simple kind, in which each type has at most one supertype and at most one subtype. Such a structure, called a tower, is illustrated in Figure 2.25.

**校订前**

上面给出的强制方案依赖于类型对之间存在自然关系。通常，不同类型之间如何相互关联有着更“全局”的结构。例如，假设我们正在构建一个通用算术系统来处理整数、有理数、实数和复数。在这样的系统中，很自然地将整数视为一种特殊的有理数，而有理数又是一种特殊的实数，实数又是一种特殊的复数。我们实际拥有的是一个所谓的类型层次，其中，例如，整数是有理数的一个子类型（即，任何可以应用于有理数的操作都可以自动应用于整数）。反过来，我们说有理数构成整数的超类型。我们这里的特定层次属于非常简单的一类，其中每个类型至多有一个超类型和至多有一个子类型。这种结构称为塔，如图2.25所示。

**校订后**

上面给出的强制转换方案依赖于类型对之间存在自然关系。通常，不同类型之间如何相互关联有着更“全局”的结构。例如，假设我们正在构建一个通用算术系统来处理整数、有理数、实数和复数。在这样的系统中，很自然地将整数视为一种特殊的有理数，而有理数又是一种特殊的实数，实数又是一种特殊的复数。我们实际拥有的是一个所谓的类型层次，其中，例如，整数是有理数的一个子类型（即，任何可以应用于有理数的操作都可以自动应用于整数）。反过来，我们说有理数构成整数的超类型。我们这里的特定层次属于非常简单的一类，其中每个类型至多有一个超类型和至多有一个子类型。这种结构称为塔，如图2.25所示。

### 2_002e5:0038

**原文**

If we have a tower structure, then we can greatly simplify the problem of adding a new type to the hierarchy, for we need only specify how the new type is embedded in the next supertype above it and how it is the supertype of the type below it. For example, if we want to add an integer to a complex number, we need not explicitly define a special coercion procedure `integer->complex`. Instead, we define how an integer can be transformed into a rational number, how a rational number is transformed into a real number, and how a real number is transformed into a complex number. We then allow the system to transform the integer into a complex number through these steps and then add the two complex numbers.

**校订前**

如果我们有一个塔结构，那么我们可以极大地简化向层次中添加新类型的问题，因为我们只需指定新类型如何嵌入其上一级超类型中，以及它如何成为其下一级类型的超类型。例如，如果我们要将一个整数加到一个复数上，我们不需要显式地定义一个特殊的强制过程`integer->complex`。相反，我们定义整数如何转换为有理数，有理数如何转换为实数，以及实数如何转换为复数。然后我们允许系统通过这些步骤将整数转换为复数，然后将两个复数相加。

**校订后**

如果我们有一个塔结构，那么我们可以极大地简化向层次中添加新类型的问题，因为我们只需指定新类型如何嵌入其上一级超类型中，以及它如何成为其下一级类型的超类型。例如，如果我们要将一个整数加到一个复数上，我们不需要显式地定义一个特殊的强制转换过程`integer->complex`。相反，我们定义整数如何转换为有理数，有理数如何转换为实数，以及实数如何转换为复数。然后我们允许系统通过这些步骤将整数转换为复数，然后将两个复数相加。

### 2_002e5:0043

**原文**

If the data types in our system can be naturally arranged in a tower, this greatly simplifies the problems of dealing with generic operations on different types, as we have seen. Unfortunately, this is usually not the case. Figure 2.26 illustrates a more complex arrangement of mixed types, this one showing relations among different types of geometric figures. We see that, in general, a type may have more than one subtype. Triangles and quadrilaterals, for instance, are both subtypes of polygons. In addition, a type may have more than one supertype. For example, an isosceles right triangle may be regarded either as an isosceles triangle or as a right triangle. This multiple-supertypes issue is particularly thorny, since it means that there is no unique way to “raise” a type in the hierarchy. Finding the “correct” supertype in which to apply an operation to an object may involve considerable searching through the entire type network on the part of a procedure such as `apply-generic`. Since there generally are multiple subtypes for a type, there is a similar problem in coercing a value “down” the type hierarchy. Dealing with large numbers of interrelated types while still preserving modularity in the design of large systems is very difficult, and is an area of much current research.[注118]

**校订前**

如果我们系统中的数据类型可以自然地排列成塔，正如我们所看到的，这极大地简化了处理不同类型上的通用操作的问题。不幸的是，通常情况并非如此。图2.26展示了一种更复杂的混合类型排列，这个图显示了不同类型的几何图形之间的关系。我们看到，一般来说，一个类型可能有多个子类型。例如，三角形和四边形都是多边形的子类型。此外，一个类型可能有多个超类型。例如，等腰直角三角形既可以视为等腰三角形，也可以视为直角三角形。这种多超类型的问题特别棘手，因为它意味着在层次中没有唯一的方式来“提升”一个类型。为对象找到应用操作的“正确”超类型可能需要像`apply-generic`这样的过程在整个类型网络中进行大量搜索。由于一个类型通常有多个子类型，在将值沿类型层次“向下”强制时也存在类似的问题。处理大量相互关联的类型，同时在大系统设计中保持模块化是非常困难的，并且是当前许多研究的一个领域。[注118]

**校订后**

如果我们系统中的数据类型可以自然地排列成塔，正如我们所看到的，这极大地简化了处理不同类型上的通用操作的问题。不幸的是，通常情况并非如此。图2.26展示了一种更复杂的混合类型排列，这个图显示了不同类型的几何图形之间的关系。我们看到，一般来说，一个类型可能有多个子类型。例如，三角形和四边形都是多边形的子类型。此外，一个类型可能有多个超类型。例如，等腰直角三角形既可以视为等腰三角形，也可以视为直角三角形。这种多超类型的问题特别棘手，因为它意味着在层次中没有唯一的方式来“提升”一个类型。为对象找到应用操作的“正确”超类型可能需要像`apply-generic`这样的过程在整个类型网络中进行大量搜索。由于一个类型通常有多个子类型，在将值沿类型层次“向下”强制转换时也存在类似的问题。处理大量相互关联的类型，同时在大系统设计中保持模块化是非常困难的，并且是当前许多研究的一个领域。[注118]

### 2_002e5:0045

**原文**

Exercise 2.81: Louis Reasoner has noticed that `apply-generic` may try to coerce the arguments to each other’s type even if they already have the same type. Therefore, he reasons, we need to put procedures in the coercion table to coerce arguments of each type to their own type. For example, in addition to the `scheme-number->complex` coercion shown above, he would do:

**校订前**

习题2.81： Louis Reasoner注意到`apply-generic`可能会尝试将参数强制转换为彼此的类型，即使它们已经是相同的类型。因此，他推理说，我们需要在强制表中放入过程，以将每种类型的参数强制为其自身的类型。例如，除了上面显示的`scheme-number->complex`强制转换之外，他还会这样做：

**校订后**

习题2.81： Louis Reasoner注意到`apply-generic`可能会尝试将参数强制转换为彼此的类型，即使它们已经是相同的类型。因此，他推理说，我们需要在强制转换表中放入过程，以将每种类型的参数强制转换为其自身的类型。例如，除了上面显示的`scheme-number->complex`强制转换之外，他还会这样做：

### 2_002e5:0053

**原文**

Exercise 2.84: Using the `raise` operation of Exercise 2.83, modify the `apply-generic` procedure so that it coerces its arguments to have the same type by the method of successive raising, as discussed in this section. You will need to devise a way to test which of two types is higher in the tower. Do this in a manner that is “compatible” with the rest of the system and will not lead to problems in adding new levels to the tower.

**校订前**

习题 2.84： 使用 习题 2.83 的 `raise` 操作，修改 `apply-generic` 过程，使其通过逐次提升的方法强制其参数具有相同类型，如本节所讨论的。你需要设计一种方法来测试两种类型中哪一种在塔中更高。以一种与系统其余部分“兼容”且不会在向塔中添加新层级时导致问题的方式来实现这一点。

**校订后**

习题 2.84： 使用 习题 2.83 的 `raise` 操作，修改 `apply-generic` 过程，使其通过逐次提升的方法将其参数强制转换为相同类型，如本节所讨论的。你需要设计一种方法来测试两种类型中哪一种在塔中更高。以一种与系统其余部分“兼容”且不会在向塔中添加新层级时导致问题的方式来实现这一点。

### 2_002e5:0057

**原文**

The manipulation of symbolic algebraic expressions is a complex process that illustrates many of the hardest problems that occur in the design of large-scale systems. An algebraic expression, in general, can be viewed as a hierarchical structure, a tree of operators applied to operands. We can construct algebraic expressions by starting with a set of primitive objects, such as constants and variables, and combining these by means of algebraic operators, such as addition and multiplication. As in other languages, we form abstractions that enable us to refer to compound objects in simple terms. Typical abstractions in symbolic algebra are ideas such as linear combination, polynomial, rational function, or trigonometric function. We can regard these as compound “types,” which are often useful for directing the processing of expressions. For example, we could describe the expression $x^(2)sin⁡(y^(2)+1)+xcos⁡2y+cos⁡(y^(3)−2y^(2))$ as a polynomial in $x$ with coefficients that are trigonometric functions of polynomials in $y$ whose coefficients are integers.

**校订前**

符号代数表达式的操作是一个复杂的过程，它展示了许多在大型系统设计中出现的最困难的问题。一个代数表达式通常可以看作一个层次结构，即应用于操作数的操作符树。我们可以从一组基本对象（如常量和变量）开始，并通过代数操作符（如加法和乘法）组合这些对象来构造代数表达式。与其他语言一样，我们形成抽象，使我们能够用简单的术语指代复合对象。符号代数中典型的抽象是诸如线性组合、多项式、有理函数或三角函数等概念。我们可以将这些视为复合“类型”，它们通常有助于指导表达式的处理。例如，我们可以将表达式 $x^(2)sin⁡(y^(2)+1)+xcos⁡2y+cos⁡(y^(3)−2y^(2))$ 描述为关于 $x$ 的多项式，其系数是关于 $y$ 的多项式的三角函数，而这些多项式的系数是整数。

**校订后**

符号代数表达式的操作是一个复杂的过程，它展示了许多在大型系统设计中出现的最困难的问题。一个代数表达式通常可以看作一个层次结构，即应用于运算对象的运算符树。我们可以从一组基本对象（如常量和变量）开始，并通过代数运算符（如加法和乘法）组合这些对象来构造代数表达式。与其他语言一样，我们形成抽象，使我们能够用简单的术语指代复合对象。符号代数中典型的抽象是诸如线性组合、多项式、有理函数或三角函数等概念。我们可以将这些视为复合“类型”，它们通常有助于指导表达式的处理。例如，我们可以将表达式 $x^(2)sin⁡(y^(2)+1)+xcos⁡2y+cos⁡(y^(3)−2y^(2))$ 描述为关于 $x$ 的多项式，其系数是关于 $y$ 的多项式的三角函数，而这些多项式的系数是整数。

### 2_002e5:0060

**原文**

Our first task in designing a system for performing arithmetic on polynomials is to decide just what a polynomial is. Polynomials are normally defined relative to certain variables (the indeterminates of the polynomial). For simplicity, we will restrict ourselves to polynomials having just one indeterminate ( univariate polynomials).[注120] We will define a polynomial to be a sum of terms, each of which is either a coefficient, a power of the indeterminate, or a product of a coefficient and a power of the indeterminate. A coefficient is defined as an algebraic expression that is not dependent upon the indeterminate of the polynomial. For example, $5x^(2)+3x+7$ is a simple polynomial in $x$, and $(y^(2)+1)x^(3)+(2y)x+1$ is a polynomial in $x$ whose coefficients are polynomials in $y$.

**校订前**

在设计一个用于对多项式进行算术运算的系统时，我们的首要任务是确定多项式究竟是什么。多项式通常是相对于某些变量（即多项式的未定元）来定义的。为简单起见，我们将自己限制在只有一个未定元的多项式（即一元多项式）。[注120]我们将多项式定义为一个项的和，其中每一项要么是一个系数，要么是未定元的一个幂，要么是一个系数与未定元的一个幂的乘积。系数被定义为不依赖于多项式的未定元的代数表达式。例如，$5x^(2)+3x+7$是$x$中的一个简单多项式，而$(y^(2)+1)x^(3)+(2y)x+1$是$x$中的一个多项式，其系数是$y$中的多项式。

**校订后**

在设计一个用于对多项式进行算术运算的系统时，我们的首要任务是确定多项式究竟是什么。多项式通常是相对于某些变量（即多项式的未定元）来定义的。为简单起见，我们将自己限制在只有一个未定元的多项式（即一元多项式）。[注120]我们将多项式定义为若干项的和，其中每一项要么是一个系数，要么是未定元的一个幂，要么是一个系数与未定元的一个幂的乘积。系数被定义为不依赖于多项式的未定元的代数表达式。例如，$5x^(2)+3x+7$是$x$中的一个简单多项式，而$(y^(2)+1)x^(3)+(2y)x+1$是$x$中的一个多项式，其系数是$y$中的多项式。

### 2_002e5:0061

**原文**

Already we are skirting some thorny issues. Is the first of these polynomials the same as the polynomial $5y^(2)+3y+7$, or not? A reasonable answer might be “yes, if we are considering a polynomial purely as a mathematical function, but no, if we are considering a polynomial to be a syntactic form.” The second polynomial is algebraically equivalent to a polynomial in $y$ whose coefficients are polynomials in $x$. Should our system recognize this, or not? Furthermore, there are other ways to represent a polynomial—for example, as a product of factors, or (for a univariate polynomial) as the set of roots, or as a listing of the values of the polynomial at a specified set of points.[注121] We can finesse these questions by deciding that in our algebraic-manipulation system a “polynomial” will be a particular syntactic form, not its underlying mathematical meaning.

**校订前**

我们已经在绕开一些棘手的问题。这些多项式中的第一个是否与多项式$5y^(2)+3y+7$相同？一个合理的回答可能是“是的，如果我们纯粹把多项式视为一个数学函数；但如果我们把多项式视为一种语法形式，则不是。”第二个多项式在代数上等价于$y$中的一个多项式，其系数是$x$中的多项式。我们的系统是否应该识别这一点？此外，还有其他表示多项式的方式——例如，表示为因子的乘积，或者（对于一元多项式）表示为根的集合，或者表示为多项式在一组指定点上的值的列表。[注121]我们可以通过决定在我们的代数操作系统中“多项式”将是一种特定的语法形式，而不是其底层的数学含义，来回避这些问题。

**校订后**

我们已经在绕开一些棘手的问题。这些多项式中的第一个是否与多项式$5y^(2)+3y+7$相同？一个合理的回答可能是“是的，如果我们纯粹把多项式视为一个数学函数；但如果我们把多项式视为一种语法形式，则不是。”第二个多项式在代数上等价于$y$中的一个多项式，其系数是$x$中的多项式。我们的系统是否应该识别这一点？此外，还有其他表示多项式的方式——例如，表示为因子的乘积，或者（对于一元多项式）表示为根的集合，或者表示为多项式在一组指定点上的值的表。[注121]我们可以通过决定在我们的代数操作系统中“多项式”将是一种特定的语法形式，而不是其底层的数学含义，来回避这些问题。

### 2_002e5:0063

**原文**

We will approach the design of our system by following the familiar discipline of data abstraction. We will represent polynomials using a data structure called a poly, which consists of a variable and a collection of terms. We assume that we have selectors `variable` and `term-list` that extract those parts from a poly and a constructor `make-poly` that assembles a poly from a given variable and a term list. A variable will be just a symbol, so we can use the `same-variable?` procedure of 2.3.2 to compare variables. The following procedures define addition and multiplication of polys:

**校订前**

我们将遵循熟悉的数据抽象准则来设计我们的系统。我们将使用一种称为poly的数据结构来表示多项式，它由一个变量和一个项的集合组成。我们假设有选择函数`variable`和`term-list`，它们从poly中提取这些部分，以及一个构造函数`make-poly`，它从给定的变量和项列表组装出一个poly。变量将只是一个符号，因此我们可以使用2.3.2的`same-variable?`过程来比较变量。以下过程定义了多项式的加法和乘法：

**校订后**

我们将遵循熟悉的数据抽象准则来设计我们的系统。我们将使用一种称为poly的数据结构来表示多项式，它由一个变量和一个项的集合组成。我们假设有选择函数`variable`和`term-list`，它们从poly中提取这些部分，以及一个构造函数`make-poly`，它从给定的变量和项表组装出一个poly。变量将只是一个符号，因此我们可以使用2.3.2的`same-variable?`过程来比较变量。以下过程定义了多项式的加法和乘法：

### 2_002e5:0065

**原文**

Polynomial addition is performed termwise. Terms of the same order (i.e., with the same power of the indeterminate) must be combined. This is done by forming a new term of the same order whose coefficient is the sum of the coefficients of the addends. Terms in one addend for which there are no terms of the same order in the other addend are simply accumulated into the sum polynomial being constructed.

**校订前**

多项式加法是逐项进行的。相同阶数（即具有相同未定元幂次）的项必须合并。这是通过形成一个同阶的新项来完成的，其系数是相加项系数的和。在一个加数中，如果在另一个加数中没有相同阶数的项，则这些项被简单地累积到正在构造的和多项式中。

**校订后**

多项式加法是逐项进行的。相同次数（即具有相同未定元幂次）的项必须合并。这是通过形成一个同次的新项来完成的，其系数是相加项系数的和。在一个加数中，如果在另一个加数中没有相同次数的项，则这些项被简单地累积到正在构造的和多项式中。

### 2_002e5:0066

**原文**

In order to manipulate term lists, we will assume that we have a constructor `the-empty-termlist` that returns an empty term list and a constructor `adjoin-term` that adjoins a new term to a term list. We will also assume that we have a predicate `empty-termlist?` that tells if a given term list is empty, a selector `first-term` that extracts the highest-order term from a term list, and a selector `rest-terms` that returns all but the highest-order term. To manipulate terms, we will suppose that we have a constructor `make-term` that constructs a term with given order and coefficient, and selectors `order` and `coeff` that return, respectively, the order and the coefficient of the term. These operations allow us to consider both terms and term lists as data abstractions, whose concrete representations we can worry about separately.

**校订前**

为了操作项列表，我们假设有一个构造函数`the-empty-termlist`返回空项列表，以及一个构造函数`adjoin-term`将一个新项添加到项列表。我们还假设有一个谓词`empty-termlist?`判断给定的项列表是否为空，一个选择函数`first-term`从项列表中提取最高阶项，以及一个选择函数`rest-terms`返回除最高阶项之外的所有项。为了操作项，我们假设有一个构造函数`make-term`，它用给定的阶数和系数构造一个项，以及选择函数`order`和`coeff`，分别返回项的阶数和系数。这些操作允许我们将项和项列表都视为数据抽象，其具体表示我们可以单独考虑。

**校订后**

为了操作项表，我们假设有一个构造函数`the-empty-termlist`返回空项表，以及一个构造函数`adjoin-term`将一个新项添加到项表。我们还假设有一个谓词`empty-termlist?`判断给定的项表是否为空，一个选择函数`first-term`从项表中提取最高次项，以及一个选择函数`rest-terms`返回除最高次项之外的所有项。为了操作项，我们假设有一个构造函数`make-term`，它用给定的次数和系数构造一个项，以及选择函数`order`和`coeff`，分别返回项的次数和系数。这些操作允许我们将项和项表都视为数据抽象，其具体表示我们可以单独考虑。

### 2_002e5:0067

**原文**

Here is the procedure that constructs the term list for the sum of two polynomials:[注122]

**校订前**

以下是构造两个多项式之和的项列表的过程：[注122]

**校订后**

以下是构造两个多项式之和的项表的过程：[注122]

### 2_002e5:0068

**原文**

The most important point to note here is that we used the generic addition procedure `add` to add together the coefficients of the terms being combined. This has powerful consequences, as we will see below.

**校订前**

这里要注意的最重要的一点是，我们使用了通用加法过程`add`来将正在合并的项的系数相加。这具有强大的后果，我们将在下面看到。

**校订后**

这里要注意的最重要的一点是，我们使用了通用加法过程`add`来将正在合并的项的系数相加。这会带来很大的能力提升，我们将在下面看到。

### 2_002e5:0069

**原文**

In order to multiply two term lists, we multiply each term of the first list by all the terms of the other list, repeatedly using `mul-term-by-all-terms`, which multiplies a given term by all terms in a given term list. The resulting term lists (one for each term of the first list) are accumulated into a sum. Multiplying two terms forms a term whose order is the sum of the orders of the factors and whose coefficient is the product of the coefficients of the factors:

**校订前**

为了将两个项列表相乘，我们将第一个列表的每一项与另一个列表的所有项相乘，反复使用`mul-term-by-all-terms`，它将给定的项与给定项列表中的所有项相乘。得到的项列表（第一个列表的每一项对应一个）被累积成一个和。两个项相乘形成一个项，其阶数是因子的阶数之和，其系数是因子的系数之积：

**校订后**

为了将两个项表相乘，我们将第一个表的每一项与另一个表的所有项相乘，反复使用`mul-term-by-all-terms`，它将给定的项与给定项表中的所有项相乘。得到的项表（第一个表的每一项对应一个）被累积成一个和。两个项相乘形成一个项，其次数是因子的次数之和，其系数是因子的系数之积：

### 2_002e5:0070

**原文**

This is really all there is to polynomial addition and multiplication. Notice that, since we operate on terms using the generic procedures `add` and `mul`, our polynomial package is automatically able to handle any type of coefficient that is known about by the generic arithmetic package. If we include a coercion mechanism such as one of those discussed in 2.5.2, then we also are automatically able to handle operations on polynomials of different coefficient types, such as $[3x^(2)+(2+3i)x+7]⋅[x^(4)+(2)/(3)x^(2)+(5+3i)].$ Because we installed the polynomial addition and multiplication procedures `add-poly` and `mul-poly` in the generic arithmetic system as the `add` and `mul` operations for type `polynomial`, our system is also automatically able to handle polynomial operations such as $[(y+1)x^(2)+(y^(2)+1)x+(y−1)]⋅[(y−2)x+(y^(3)+7)].$ The reason is that when the system tries to combine coefficients, it will dispatch through `add` and `mul`. Since the coefficients are themselves polynomials (in $y$), these will be combined using `add-poly` and `mul-poly`. The result is a kind of “data-directed recursion” in which, for example, a call to `mul-poly` will result in recursive calls to `mul-poly` in order to multiply the coefficients. If the coefficients of the coefficients were themselves polynomials (as might be used to represent polynomials in three variables), the data direction would ensure that the system would follow through another level of recursive calls, and so on through as many levels as the structure of the data dictates.[注123]

**校订前**

多项式加法和乘法的内容实际上就这么多。注意，由于我们使用通用过程 `add` 和 `mul` 对项进行操作，我们的多项式包自动能够处理通用算术包所知的任何类型的系数。如果我们加入一种强制机制，例如在 2.5.2 中讨论的机制之一，那么我们也能自动处理不同系数类型的多项式上的运算，例如 $[3x^(2)+(2+3i)x+7]⋅[x^(4)+(2)/(3)x^(2)+(5+3i)].$。因为我们将多项式加法和乘法过程 `add-poly` 和 `mul-poly` 作为类型 `polynomial` 的 `add` 和 `mul` 操作安装到通用算术系统中，我们的系统也自动能够处理多项式运算，例如 $[(y+1)x^(2)+(y^(2)+1)x+(y−1)]⋅[(y−2)x+(y^(3)+7)].$。原因是当系统试图组合系数时，它将通过 `add` 和 `mul` 进行分派。由于系数本身是多项式（在 $y$ 中），这些将使用 `add-poly` 和 `mul-poly` 进行组合。结果是一种“数据导向的递归”，例如，对 `mul-poly` 的调用将导致对 `mul-poly` 的递归调用，以便乘以系数。如果系数的系数本身是多项式（可能用于表示三个变量的多项式），数据导向将确保系统遵循另一层递归调用，并依此类推，按照数据结构所指示的尽可能多的层级进行。[注123]

**校订后**

多项式加法和乘法的内容实际上就这么多。注意，由于我们使用通用过程 `add` 和 `mul` 对项进行操作，我们的多项式包自动能够处理通用算术包所知的任何类型的系数。如果我们加入一种强制转换机制，例如在 2.5.2 中讨论的机制之一，那么我们也能自动处理不同系数类型的多项式上的运算，例如 $[3x^(2)+(2+3i)x+7]⋅[x^(4)+(2)/(3)x^(2)+(5+3i)].$。因为我们将多项式加法和乘法过程 `add-poly` 和 `mul-poly` 作为类型 `polynomial` 的 `add` 和 `mul` 操作安装到通用算术系统中，我们的系统也自动能够处理多项式运算，例如 $[(y+1)x^(2)+(y^(2)+1)x+(y−1)]⋅[(y−2)x+(y^(3)+7)].$。原因是当系统试图组合系数时，它将通过 `add` 和 `mul` 进行分派。由于系数本身是多项式（在 $y$ 中），这些将使用 `add-poly` 和 `mul-poly` 进行组合。结果是一种“数据导向的递归”，例如，对 `mul-poly` 的调用将导致对 `mul-poly` 的递归调用，以便乘以系数。如果系数的系数本身是多项式（可能用于表示三个变量的多项式），数据导向将确保系统遵循另一层递归调用，并依此类推，按照数据结构所指示的尽可能多的层级进行。[注123]

### 2_002e5:0072

**原文**

Finally, we must confront the job of implementing a good representation for term lists. A term list is, in effect, a set of coefficients keyed by the order of the term. Hence, any of the methods for representing sets, as discussed in 2.3.3, can be applied to this task. On the other hand, our procedures `add-terms` and `mul-terms` always access term lists sequentially from highest to lowest order. Thus, we will use some kind of ordered list representation.

**校订前**

最后，我们必须面对为项表实现良好表示的任务。项表实际上是一组以项的阶数为键的系数。因此，任何表示集合的方法，如 2.3.3 中所讨论的，都可以应用于此任务。另一方面，我们的过程 `add-terms` 和 `mul-terms` 总是从最高阶到最低阶顺序访问项表。因此，我们将使用某种有序表表示。

**校订后**

最后，我们必须面对为项表实现良好表示的任务。项表实际上是一组以项的次数为键的系数。因此，任何表示集合的方法，如 2.3.3 中所讨论的，都可以应用于此任务。另一方面，我们的过程 `add-terms` 和 `mul-terms` 总是从最高次到最低次顺序访问项表。因此，我们将使用某种有序表表示。

### 2_002e5:0073

**原文**

How should we structure the list that represents a term list? One consideration is the “density” of the polynomials we intend to manipulate. A polynomial is said to be dense if it has nonzero coefficients in terms of most orders. If it has many zero terms it is said to be sparse. For example, $A:x^(5)+2x^(4)+3x^(2)−2x−5$ is a dense polynomial, whereas $B:x^(100)+2x^(2)+1$ is sparse.

**校订前**

我们应该如何构造表示项表的表？一个考虑是我们打算操作的多项式的“密度”。如果一个多项式在大多数阶的项上都有非零系数，则称其为 稠密。如果它有许多零项，则称其为 稀疏。例如，$A:x^(5)+2x^(4)+3x^(2)−2x−5$ 是稠密多项式，而 $B:x^(100)+2x^(2)+1$ 是稀疏的。

**校订后**

我们应该如何构造表示项表的表？一个考虑是我们打算操作的多项式的“密度”。如果一个多项式在大多数次数的项上都有非零系数，则称其为 稠密。如果它有许多零项，则称其为 稀疏。例如，$A:x^(5)+2x^(4)+3x^(2)−2x−5$ 是稠密多项式，而 $B:x^(100)+2x^(2)+1$ 是稀疏的。

### 2_002e5:0074

**原文**

The term lists of dense polynomials are most efficiently represented as lists of the coefficients. For example, $A$ above would be nicely represented as `(1 2 0 3 -2 -5)`. The order of a term in this representation is the length of the sublist beginning with that term’s coefficient, decremented by 1.[注124] This would be a terrible representation for a sparse polynomial such as $B$: There would be a giant list of zeros punctuated by a few lonely nonzero terms. A more reasonable representation of the term list of a sparse polynomial is as a list of the nonzero terms, where each term is a list containing the order of the term and the coefficient for that order. In such a scheme, polynomial $B$ is efficiently represented as `((100 1) (2 2) (0 1))`. As most polynomial manipulations are performed on sparse polynomials, we will use this method. We will assume that term lists are represented as lists of terms, arranged from highest-order to lowest-order term. Once we have made this decision, implementing the selectors and constructors for terms and term lists is straightforward:[注125]

**校订前**

稠密多项式的项表最有效地表示为系数表。例如，上面的 $A$ 可以很好地表示为 `(1 2 0 3 -2 -5)`。在这种表示中，项的阶数是从该项系数开始的子表的长度减 1。[注124] 对于像 $B$ 这样的稀疏多项式，这将是一种糟糕的表示：会有一个巨大的零表，中间点缀着几个孤立的非零项。稀疏多项式的项表更合理的表示是非零项的表，其中每一项是一个包含该项的阶数和该阶数系数的表。在这种方案中，多项式 $B$ 被有效地表示为 `((100 1) (2 2) (0 1))`。由于大多数多项式操作是在稀疏多项式上进行的，我们将使用这种方法。我们将假设项表表示为项的表，从最高阶项到最低阶项排列。一旦我们做出这个决定，实现项和项表的选择函数和构造函数就很简单了：[注125]

**校订后**

稠密多项式的项表最有效地表示为系数表。例如，上面的 $A$ 可以很好地表示为 `(1 2 0 3 -2 -5)`。在这种表示中，项的次数是从该项系数开始的子表的长度减 1。[注124] 对于像 $B$ 这样的稀疏多项式，这将是一种糟糕的表示：会有一个巨大的零表，中间点缀着几个孤立的非零项。稀疏多项式的项表更合理的表示是非零项的表，其中每一项是一个包含该项的次数和该次数系数的表。在这种方案中，多项式 $B$ 被有效地表示为 `((100 1) (2 2) (0 1))`。由于大多数多项式操作是在稀疏多项式上进行的，我们将使用这种方法。我们将假设项表表示为项的表，从最高次项到最低次项排列。一旦我们做出这个决定，实现项和项表的选择函数和构造函数就很简单了：[注125]

### 2_002e5:0081

**原文**

Exercise 2.91: A univariate polynomial can be divided by another one to produce a polynomial quotient and a polynomial remainder. For example, $(x^(5)−1)/(x^(2)−1)=x^(3)+x,remainderx−1.$ Division can be performed via long division. That is, divide the highest-order term of the dividend by the highest-order term of the divisor. The result is the first term of the quotient. Next, multiply the result by the divisor, subtract that from the dividend, and produce the rest of the answer by recursively dividing the difference by the divisor. Stop when the order of the divisor exceeds the order of the dividend and declare the dividend to be the remainder. Also, if the dividend ever becomes zero, return zero as both quotient and remainder.

**校订前**

习题 2.91： 一个单变量多项式可以被另一个多项式除，产生一个多项式商和一个多项式余数。例如，$(x^(5)−1)/(x^(2)−1)=x^(3)+x,remainderx−1.$ 除法可以通过长除法进行。即，将被除式的最高阶项除以除式的最高阶项。结果是商的第一项。接下来，将结果乘以除式，从被除式中减去，并通过递归地将差除以除式来产生答案的其余部分。当除式的阶数超过被除式的阶数时停止，并声明被除式为余数。此外，如果被除式变为零，则返回零作为商和余数。

**校订后**

习题 2.91： 一个单变量多项式可以被另一个多项式除，产生一个多项式商和一个多项式余数。例如，$(x^(5)−1)/(x^(2)−1)=x^(3)+x,remainderx−1.$ 除法可以通过长除法进行。即，将被除式的最高次项除以除式的最高次项。结果是商的第一项。接下来，将结果乘以除式，从被除式中减去，并通过递归地将差除以除式来产生答案的其余部分。当除式的次数超过被除式的次数时停止，并声明被除式为余数。此外，如果被除式变为零，则返回零作为商和余数。

### 2_002e5:0100

**原文**

We can solve the problem exhibited in Exercise 2.95 if we use the following modification of the GCD algorithm (which really works only in the case of polynomials with integer coefficients). Before performing any polynomial division in the GCD computation, we multiply the dividend by an integer constant factor, chosen to guarantee that no fractions will arise during the division process. Our answer will thus differ from the actual GCD by an integer constant factor, but this does not matter in the case of reducing rational functions to lowest terms; the GCD will be used to divide both the numerator and denominator, so the integer constant factor will cancel out.

**校订前**

如果我们使用以下对 GCD 算法的修改（它实际上只适用于具有整数系数的多项式），就可以解决 习题 2.95 中展示的问题。在 GCD 计算中执行任何多项式除法之前，我们将被除数乘以一个整数常数因子，选择该因子以保证在除法过程中不会出现分数。因此，我们的答案将与实际的 GCD 相差一个整数常数因子，但在将有理函数化为最简形式时这无关紧要；GCD 将用于同时除分子和分母，因此整数常数因子会被约去。

**校订后**

如果我们使用以下对 GCD 算法的修改（它实际上只适用于具有整数系数的多项式），就可以解决 习题 2.95 中展示的问题。在 GCD 计算中执行任何多项式除法之前，我们将被除式乘以一个整数常数因子，选择该因子以保证在除法过程中不会出现分数。因此，我们的答案将与实际的 GCD 相差一个整数常数因子，但在将有理函数化为最简形式时这无关紧要；GCD 将用于同时除分子和分母，因此整数常数因子会被约去。

### 2_002e5:0101

**原文**

More precisely, if $P$ and $Q$ are polynomials, let $O_{1}$ be the order of $P$ (i.e., the order of the largest term of $P$) and let $O_{2}$ be the order of $Q$. Let $c$ be the leading coefficient of $Q$. Then it can be shown that, if we multiply $P$ by the integerizing factor $c^(1+O_{1}−O_{2})$, the resulting polynomial can be divided by $Q$ by using the `div-terms` algorithm without introducing any fractions. The operation of multiplying the dividend by this constant and then dividing is sometimes called the pseudodivision of $P$ by $Q$. The remainder of the division is called the pseudoremainder.

**校订前**

更准确地说，如果 $P$ 和 $Q$ 是多项式，令 $O_{1}$ 为 $P$ 的阶（即 $P$ 的最大项的阶），令 $O_{2}$ 为 $Q$ 的阶。令 $c$ 为 $Q$ 的首项系数。那么可以证明，如果我们将 $P$ 乘以 整数化因子 $c^(1+O_{1}−O_{2})$，所得多项式可以使用 `div-terms` 算法除以 $Q$ 而不引入任何分数。将被除数乘以这个常数然后进行除法的操作有时被称为 $P$ 除以 $Q$ 的 伪除法。除法的余数被称为 伪余数。

**校订后**

更准确地说，如果 $P$ 和 $Q$ 是多项式，令 $O_{1}$ 为 $P$ 的次数（即 $P$ 的最高次项的次数），令 $O_{2}$ 为 $Q$ 的次数。令 $c$ 为 $Q$ 的首项系数。那么可以证明，如果我们将 $P$ 乘以 整数化因子 $c^(1+O_{1}−O_{2})$，所得多项式可以使用 `div-terms` 算法除以 $Q$ 而不引入任何分数。将被除式乘以这个常数然后进行除法的操作有时被称为 $P$ 除以 $Q$ 的 伪除法。除法的余数被称为 伪余数。

### 2_002e5:0103

**原文**

Implement the procedure `pseudoremainder-terms`, which is just like `remainder-terms` except that it multiplies the dividend by the integerizing factor described above before calling `div-terms`. Modify `gcd-terms` to use `pseudoremainder-terms`, and verify that `greatest-common-divisor` now produces an answer with integer coefficients on the example in Exercise 2.95.

**校订前**

实现过程 `pseudoremainder-terms`，它就像 `remainder-terms` 一样，只是在调用 `div-terms` 之前将被除数乘以上述整数化因子。修改 `gcd-terms` 以使用 `pseudoremainder-terms`，并验证 `greatest-common-divisor` 现在在 习题 2.95 的例子中产生具有整数系数的答案。

**校订后**

实现过程 `pseudoremainder-terms`，它就像 `remainder-terms` 一样，只是在调用 `div-terms` 之前将被除式乘以上述整数化因子。修改 `gcd-terms` 以使用 `pseudoremainder-terms`，并验证 `greatest-common-divisor` 现在在 习题 2.95 的例子中产生具有整数系数的答案。

### 2_002e5:0107

**原文**

When you obtain the GCD, multiply both numerator and denominator by the same integerizing factor before dividing through by the GCD, so that division by the GCD will not introduce any noninteger coefficients. As the factor you can use the leading coefficient of the GCD raised to the power $1+O_{1}−O_{2}$, where $O_{2}$ is the order of the GCD and $O_{1}$ is the maximum of the orders of the numerator and denominator. This will ensure that dividing the numerator and denominator by the GCD will not introduce any fractions.

**校订前**

当你获得 GCD 后，在除以 GCD 之前，将分子和分母都乘以相同的整数化因子，这样除以 GCD 就不会引入任何非整数系数。作为因子，你可以使用 GCD 的首项系数的 $1+O_{1}−O_{2}$ 次幂，其中 $O_{2}$ 是 GCD 的阶，$O_{1}$ 是分子和分母的阶的最大值。这将确保将分子和分母除以 GCD 不会引入任何分数。

**校订后**

当你获得 GCD 后，在除以 GCD 之前，将分子和分母都乘以相同的整数化因子，这样除以 GCD 就不会引入任何非整数系数。作为因子，你可以使用 GCD 的首项系数的 $1+O_{1}−O_{2}$ 次幂，其中 $O_{2}$ 是 GCD 的次数，$O_{1}$ 是分子和分母的次数的最大值。这将确保将分子和分母除以 GCD 不会引入任何分数。

### 2_002e5:0110

**原文**

Implement this algorithm as a procedure `reduce-terms` that takes two term lists `n` and `d` as arguments and returns a list `nn`, `dd`, which are `n` and `d` reduced to lowest terms via the algorithm given above. Also write a procedure `reduce-poly`, analogous to `add-poly`, that checks to see if the two polys have the same variable. If so, `reduce-poly` strips off the variable and passes the problem to `reduce-terms`, then reattaches the variable to the two term lists supplied by `reduce-terms`.

**校订前**

将此算法实现为过程 `reduce-terms`，它接受两个项表 `n` 和 `d` 作为参数，并返回一个表 `nn`、`dd`，它们是通过上述算法化为最简形式的 `n` 和 `d`。还要编写一个过程 `reduce-poly`，类似于 `add-poly`，它检查两个多项式是否具有相同的变量。如果是，`reduce-poly` 剥离变量并将问题传递给 `reduce-terms`，然后将变量重新附加到由 `reduce-terms` 提供的两个项表上。

**校订后**

将此算法实现为过程 `reduce-terms`，它接受两个项表 `n` 和 `d` 作为参数，并返回由 `nn` 和 `dd` 组成的表，它们是通过上述算法化为最简形式的 `n` 和 `d`。还要编写一个过程 `reduce-poly`，类似于 `add-poly`，它检查两个多项式是否具有相同的变量。如果是，`reduce-poly` 剥离变量并将问题传递给 `reduce-terms`，然后将变量重新附加到由 `reduce-terms` 提供的两个项表上。

### 2_002e5:0123

**原文**

[注122] This operation is very much like the ordered `union-set` operation we developed in Exercise 2.62. In fact, if we think of the terms of the polynomial as a set ordered according to the power of the indeterminate, then the program that produces the term list for a sum is almost identical to `union-set`.

**校订前**

[注122] 这个操作非常像我们在习题2.62中开发的有序`union-set`操作。事实上，如果我们把多项式的项看作一个根据未知量的幂排序的集合，那么生成和的项表的程序几乎与`union-set`完全相同。

**校订后**

[注122] 这个操作非常像我们在习题2.62中开发的有序`union-set`操作。事实上，如果我们把多项式的项看作一个根据未定元的幂排序的集合，那么生成和的项表的程序几乎与`union-set`完全相同。

### 2_002e5:0126

**原文**

[注125] Although we are assuming that term lists are ordered, we have implemented `adjoin-term` to simply `cons` the new term onto the existing term list. We can get away with this so long as we guarantee that the procedures (such as `add-terms`) that use `adjoin-term` always call it with a higher-order term than appears in the list. If we did not want to make such a guarantee, we could have implemented `adjoin-term` to be similar to the `adjoin-set` constructor for the ordered-list representation of sets (Exercise 2.61).

**校订前**

[注125] 尽管我们假设项表是有序的，但我们实现的`adjoin-term`只是将新项`cons`到现有项表上。只要我们保证使用`adjoin-term`的过程（例如`add-terms`）总是以比表中出现的项更高阶的项来调用它，我们就可以这样做。如果我们不想做出这样的保证，我们可以将`adjoin-term`实现为类似于集合的有序表表示的`adjoin-set`构造过程（习题2.61）。

**校订后**

[注125] 尽管我们假设项表是有序的，但我们实现的`adjoin-term`只是将新项`cons`到现有项表上。只要我们保证使用`adjoin-term`的过程（例如`add-terms`）总是以比表中出现的项次数更高的项来调用它，我们就可以这样做。如果我们不想做出这样的保证，我们可以将`adjoin-term`实现为类似于集合的有序表表示的`adjoin-set`构造过程（习题2.61）。

### 2_002e5:0127

**原文**

[注126] The fact that Euclid’s Algorithm works for polynomials is formalized in algebra by saying that polynomials form a kind of algebraic domain called a Euclidean ring. A Euclidean ring is a domain that admits addition, subtraction, and commutative multiplication, together with a way of assigning to each element $x$ of the ring a positive integer “measure” $m(x)$ with the properties that $m(xy)≥m(x)$ for any nonzero $x$ and $y$ and that, given any $x$ and $y$, there exists a $q$ such that $y=qx+r$ and either $r=0$ or $m(r)<m(x)$. From an abstract point of view, this is what is needed to prove that Euclid’s Algorithm works. For the domain of integers, the measure $m$ of an integer is the absolute value of the integer itself. For the domain of polynomials, the measure of a polynomial is its degree.

**校订前**

[注126] 欧几里得算法适用于多项式这一事实，在代数中通过说多项式构成一种称为欧几里得环的代数域来形式化。欧几里得环是一个允许加法、减法和交换乘法的域，并且有一种为环中每个元素$x$分配一个正整数“度量”$m(x)$的方法，其性质是：对于任何非零的$x$和$y$，有$m(xy)≥m(x)$；并且，给定任何$x$和$y$，存在一个$q$使得$y=qx+r$，并且要么$r=0$，要么$m(r)<m(x)$。从抽象的角度来看，这就是证明欧几里得算法有效所需要的。对于整数域，整数$m$的度量是整数本身的绝对值。对于多项式域，多项式的度量是它的次数。

**校订后**

[注126] 欧几里得算法适用于多项式这一事实，在代数中通过说多项式构成一种称为欧几里得环的代数结构来形式化。欧几里得环是一个允许加法、减法和交换乘法的整环，并且有一种为环中每个元素$x$分配一个正整数“度量”$m(x)$的方法，其性质是：对于任何非零的$x$和$y$，有$m(xy)≥m(x)$；并且，给定任何$x$和$y$，存在一个$q$使得$y=qx+r$，并且要么$r=0$，要么$m(r)<m(x)$。从抽象的角度来看，这就是证明欧几里得算法有效所需要的。对于整数整环，整数的度量$m$是整数本身的绝对值。对于多项式整环，多项式的度量是它的次数。

### 3_002e1:0031

**原文**

The resulting account object should process a request only if it is accompanied by the password with which the account was created, and should otherwise return a complaint:

**校订前**

生成的账户对象应仅当请求附带有创建账户时所用的密码时才处理该请求，否则应返回一个抱怨：

**校订后**

生成的账户对象应仅当请求附带有创建账户时所用的密码时才处理该请求，否则应返回一条报错信息：

### 3_002e1:0032

**原文**

Exercise 3.4: Modify the `make-account` procedure of Exercise 3.3 by adding another local state variable so that, if an account is accessed more than seven consecutive times with an incorrect password, it invokes the procedure `call-the-cops`.

**校订前**

习题3.4：修改习题3.3的`make-account`过程，添加另一个局部状态变量，以便如果账户被连续访问超过七次且密码不正确，则调用过程`call-the-cops`。

**校订后**

习题3.4：修改习题3.3的`make-account`过程，添加另一个局部状态变量，以便如果连续超过七次使用错误密码访问账户，则调用过程`call-the-cops`。

### 3_002e1:0039

**原文**

The Monte Carlo method consists of choosing sample experiments at random from a large set and then making deductions on the basis of the probabilities estimated from tabulating the results of those experiments. For example, we can approximate $π$ using the fact that $6/π^(2)$ is the probability that two integers chosen at random will have no factors in common; that is, that their greatest common divisor will be 1.[注135] To obtain the approximation to $π$, we perform a large number of experiments. In each experiment we choose two integers at random and perform a test to see if their GCD is 1. The fraction of times that the test is passed gives us our estimate of $6/π^(2)$, and from this we obtain our approximation to $π$.

**校订前**

蒙特卡洛方法包括从大量集合中随机选择样本实验，然后根据对这些实验结果进行列表统计所估计出的概率作出推断。例如，我们可以利用 $6/π^(2)$ 是随机选取的两个整数没有公因子的概率，即它们的最大公约数为 1 的概率，来近似计算 $π$。[注135]为了得到 $π$ 的近似值，我们进行大量实验。在每次实验中，我们随机选取两个整数，并检验它们的 GCD 是否为 1。检验通过的比例给出了我们对 $6/π^(2)$ 的估计，由此我们得到对 $π$ 的近似值。

**校订后**

蒙特卡洛方法包括从一个大集合中随机选择样本实验，然后根据对这些实验结果进行列表统计所估计出的概率作出推断。例如，我们可以利用 $6/π^(2)$ 是随机选取的两个整数没有公因子的概率，即它们的最大公约数为 1 的概率，来近似计算 $π$。[注135]为了得到 $π$ 的近似值，我们进行大量实验。在每次实验中，我们随机选取两个整数，并检验它们的 GCD 是否为 1。检验通过的比例给出了我们对 $6/π^(2)$ 的估计，由此我们得到对 $π$ 的近似值。

### 3_002e1:0073

**原文**

As an example of how this issue arises in programming, consider the situation where Peter and Paul have a bank account with $100 in it. There is a substantial difference between modeling this as

**校订前**

作为这个问题在编程中如何出现的一个例子，考虑Peter和Paul有一个银行账户，其中有100美元。将其建模为

**校订后**

作为这个问题在编程中如何出现的一个例子，考虑Peter和Paul有一个银行账户，其中有100美元。以下两种建模方式有着实质性的区别，一种是

### 3_002e1:0074

**原文**

and modeling it as

**校订前**

和将其建模为

**校订后**

另一种是

### 3_002e1:0084

**原文**

will allow one to make transactions on `peter-acc` using the name `paul-acc` and the password `rosebud`. You may wish to modify your solution to Exercise 3.3 to accommodate this new feature.

**校订前**

将允许人们使用名称`peter-acc`和密码`paul-acc`在`rosebud`上进行交易。你可能希望修改你对习题3.3的解答，以适应这个新特性。

**校订后**

将允许人们使用名称`paul-acc`和密码`rosebud`在`peter-acc`上进行交易。你可能希望修改你对习题3.3的解答，以适应这个新特性。

### 3_002e1:0099

**原文**

[注139] In view of this, it is ironic that introductory programming is most often taught in a highly imperative style. This may be a vestige of a belief, common throughout the 1960s and 1970s, that programs that call procedures must inherently be less efficient than programs that perform assignments. (Steele 1977 debunks this argument.) Alternatively it may reflect a view that step-by-step assignment is easier for beginners to visualize than procedure call. Whatever the reason, it often saddles beginning programmers with “should I set this variable before or after that one” concerns that can complicate programming and obscure the important ideas.

**校订前**

[注139]有鉴于此，颇具讽刺意味的是，入门程序设计最常以高度命令式的风格来教授。这可能是二十世纪1960年代和1970年代普遍存在的一种信念的残余，即调用过程的程序必定比执行赋值的程序效率低。（Steele 1977驳斥了这一论点。）或者，它可能反映了一种观点，即逐步赋值对初学者来说比过程调用更容易想象。无论原因是什么，它常常使初学程序设计的人背上“我应该在这个变量之前还是之后设置那个变量”的负担，这会使程序设计复杂化并掩盖重要的思想。

**校订后**

[注139]有鉴于此，颇具讽刺意味的是，入门程序设计最常以高度命令式的风格来教授。这可能是1960年代和1970年代普遍存在的一种信念的残余，即调用过程的程序必定比执行赋值的程序效率低。（Steele 1977驳斥了这一论点。）或者，它可能反映了一种观点，即逐步赋值对初学者来说比过程调用更容易想象。无论原因是什么，它常常使初学程序设计的人背上“我应该在这个变量之前还是之后设置那个变量”的负担，这会使程序设计复杂化并掩盖重要的思想。

### 3_002e2:0081

**原文**

[注140] Assignment introduces a subtlety into step 1 of the evaluation rule. As shown in Exercise 3.8, the presence of assignment allows us to write expressions that will produce different values depending on the order in which the subexpressions in a combination are evaluated. Thus, to be precise, we should specify an evaluation order in step 1 (e.g., left to right or right to left). However, this order should always be considered to be an implementation detail, and one should never write programs that depend on some particular order. For instance, a sophisticated compiler might optimize a program by varying the order in which subexpressions are evaluated.

**校订前**

[注140]赋值给求值规则的第1步引入了一个微妙之处。如习题3.8所示，赋值的存在允许我们编写这样的表达式：其产生的值取决于组合式中子表达式的求值顺序。因此，为精确起见，我们应该在第1步中指定一个求值顺序（例如，从左到右或从右到左）。然而，这个顺序应始终被视为实现细节，人们绝不应该编写依赖于某种特定顺序的程序。例如，一个复杂的编译器可能通过改变子表达式的求值顺序来优化程序。

**校订后**

[注140]赋值给求值规则的第1步引入了一个微妙之处。如习题3.8所示，赋值的存在允许我们编写这样的表达式：其产生的值取决于组合式中子表达式的求值顺序。因此，为精确起见，我们应该在第1步中指定一个求值顺序（例如，从左到右或从右到左）。然而，这个顺序应始终被视为实现细节，人们绝不应该编写依赖于某种特定顺序的程序。例如，一个精巧的编译器可能通过改变子表达式的求值顺序来优化程序。

### 3_002e3:0004

**原文**

Chapter 2 dealt with compound data as a means for constructing computational objects that have several parts, in order to model real-world objects that have several aspects. In that chapter we introduced the discipline of data abstraction, according to which data structures are specified in terms of constructors, which create data objects, and selectors, which access the parts of compound data objects. But we now know that there is another aspect of data that chapter 2 did not address. The desire to model systems composed of objects that have changing state leads us to the need to modify compound data objects, as well as to construct and select from them. In order to model compound objects with changing state, we will design data abstractions to include, in addition to selectors and constructors, operations called mutators, which modify data objects. For instance, modeling a banking system requires us to change account balances. Thus, a data structure for representing bank accounts might admit an operation

**校订前**

第2章将复合数据作为构造具有若干部分的计算对象的手段，以便对具有若干方面的现实世界对象进行建模。在那一章中，我们介绍了数据抽象的准则，根据该准则，数据结构通过构造器（创建数据对象）和选择器（访问复合数据对象的部分）来指定。但我们现在知道，数据还有另一个方面，第2章没有涉及。对由具有变化状态的对象组成的系统进行建模的愿望，使我们不仅需要构造和选择复合数据对象，还需要修改它们。为了对具有变化状态的复合对象进行建模，我们将设计数据抽象，使其除了选择器和构造器之外，还包括称为 变异器的操作，这些操作修改数据对象。例如，对银行系统进行建模需要我们改变账户余额。因此，用于表示银行账户的数据结构可能允许一个操作

**校订后**

第2章将复合数据作为构造具有若干部分的计算对象的手段，以便对具有若干方面的现实世界对象进行建模。在那一章中，我们介绍了数据抽象的准则，根据该准则，数据结构通过构造函数（创建数据对象）和选择函数（访问复合数据对象的部分）来指定。但我们现在知道，数据还有另一个方面，第2章没有涉及。对由具有变化状态的对象组成的系统进行建模的愿望，使我们不仅需要构造和选择复合数据对象，还需要修改它们。为了对具有变化状态的复合对象进行建模，我们将设计数据抽象，使其除了选择函数和构造函数之外，还包括称为 修改器的操作，这些操作修改数据对象。例如，对银行系统进行建模需要我们改变账户余额。因此，用于表示银行账户的数据结构可能允许一个操作

### 3_002e3:0005

**原文**

that changes the balance of the designated account to the designated new value. Data objects for which mutators are defined are known as mutable data objects.

**校订前**

该操作将指定账户的余额改为指定的新值。为其定义了变异器的数据对象称为 可变数据对象。

**校订后**

该操作将指定账户的余额改为指定的新值。为其定义了修改器的数据对象称为 可变数据对象。

### 3_002e3:0006

**原文**

Chapter 2 introduced pairs as a general-purpose “glue” for synthesizing compound data. We begin this section by defining basic mutators for pairs, so that pairs can serve as building blocks for constructing mutable data objects. These mutators greatly enhance the representational power of pairs, enabling us to build data structures other than the sequences and trees that we worked with in 2.2. We also present some examples of simulations in which complex systems are modeled as collections of objects with local state.

**校订前**

第2章介绍了序对作为合成复合数据的通用“胶水”。我们本节首先定义序对的基本变异器，以便序对可以作为构造可变数据对象的构建块。这些变异器极大地增强了序对的表示能力，使我们能够构建除2.2中所使用的序列和树之外的数据结构。我们还给出了一些模拟示例，其中复杂系统被建模为具有局部状态的对象集合。

**校订后**

第2章介绍了序对作为合成复合数据的通用“胶水”。我们本节首先定义序对的基本修改器，以便序对可以作为构造可变数据对象的构建块。这些修改器极大地增强了序对的表示能力，使我们能够构建除2.2中所使用的序列和树之外的数据结构。我们还给出了一些模拟示例，其中复杂系统被建模为具有局部状态的对象集合。

### 3_002e3:0009

**原文**

The primitive mutators for pairs are `set-car!` and `set-cdr!`. `Set-car!` takes two arguments, the first of which must be a pair. It modifies this pair, replacing the `car` pointer by a pointer to the second argument of `set-car!`.[注144]

**校订前**

序对的基本变异器是`set-car!`和`set-cdr!`。`Set-car!`接受两个参数，第一个参数必须是序对。它修改这个序对，将`car`指针替换为指向`set-car!`的第二个参数的指针。[注144]

**校订后**

序对的基本修改器是`set-car!`和`set-cdr!`。`Set-car!`接受两个参数，第一个参数必须是序对。它修改这个序对，将`car`指针替换为指向`set-car!`的第二个参数的指针。[注144]

### 3_002e3:0017

**原文**

`Cons` builds new list structure by creating new pairs, while `set-car!` and `set-cdr!` modify existing pairs. Indeed, we could implement `cons` in terms of the two mutators, together with a procedure `get-new-pair`, which returns a new pair that is not part of any existing list structure. We obtain the new pair, set its `car` and `cdr` pointers to the designated objects, and return the new pair as the result of the `cons`.[注146]

**校订前**

`Cons`通过创建新序对来构建新的表结构，而`set-car!`和`set-cdr!`则修改已有的序对。实际上，我们可以用这两个变异器以及一个过程`get-new-pair`来实现`cons`，该过程返回一个不属于任何现有表结构的新序对。我们获得新序对，将其`car`和`cdr`指针设置为指定的对象，并返回新序对作为`cons`的结果。[注146]

**校订后**

`Cons`通过创建新序对来构建新的表结构，而`set-car!`和`set-cdr!`则修改已有的序对。实际上，我们可以用这两个修改器以及一个过程`get-new-pair`来实现`cons`，该过程返回一个不属于任何现有表结构的新序对。我们获得新序对，将其`car`和`cdr`指针设置为指定的对象，并返回新序对作为`cons`的结果。[注146]

### 3_002e3:0019

**原文**

`Append` forms a new list by successively `cons`ing the elements of `x` onto `y`. The procedure `append!` is similar to `append`, but it is a mutator rather than a constructor. It appends the lists by splicing them together, modifying the final pair of `x` so that its `cdr` is now `y`. (It is an error to call `append!` with an empty `x`.)

**校订前**

`Append`通过将`x`的元素依次`cons`到`y`上来形成新表。过程`append!`与`append`类似，但它是变异器而非构造器。它通过将表拼接在一起来连接它们，修改`x`的最后一个序对，使其`cdr`现在为`y`。（用空`x`调用`append!`是错误的。）

**校订后**

`Append`通过将`x`的元素依次`cons`到`y`上来形成新表。过程`append!`与`append`类似，但它是修改器而非构造函数。它通过将表拼接在一起来连接它们，修改`x`的最后一个序对，使其`cdr`现在为`y`。（用空`x`调用`append!`是错误的。）

### 3_002e3:0035

**原文**

When thought of as a list, `z1` and `z2` both represent “the same” list, `((a b) a b)`. In general, sharing is completely undetectable if we operate on lists using only `cons`, `car`, and `cdr`. However, if we allow mutators on list structure, sharing becomes significant. As an example of the difference that sharing can make, consider the following procedure, which modifies the `car` of the structure to which it is applied:

**校订前**

当作为表来考虑时，`z1`和`z2`都表示“同一个”表，`((a b) a b)`。一般来说，如果我们仅使用`cons`、`car`和`cdr`对表进行操作，共享是完全无法检测的。然而，如果我们允许对表结构进行变异，共享就变得重要了。作为共享可能造成的差异的一个例子，考虑以下过程，它修改所应用结构的`car`：

**校订后**

当作为表来考虑时，`z1`和`z2`都表示“同一个”表，`((a b) a b)`。一般来说，如果我们仅使用`cons`、`car`和`cdr`对表进行操作，共享是完全无法检测的。然而，如果我们允许对表结构进行修改，共享就变得重要了。作为共享可能造成的差异的一个例子，考虑以下过程，它修改所应用结构的`car`：

### 3_002e3:0038

**原文**

As will be seen in the following sections, we can exploit sharing to greatly extend the repertoire of data structures that can be represented by pairs. On the other hand, sharing can also be dangerous, since modifications made to structures will also affect other structures that happen to share the modified parts. The mutation operations `set-car!` and `set-cdr!` should be used with care; unless we have a good understanding of how our data objects are shared, mutation can have unanticipated results.[注148]

**校订前**

正如将在以下各节中看到的，我们可以利用共享来极大地扩展可用序对表示的数据结构的范围。另一方面，共享也可能是危险的，因为对结构所做的修改也会影响恰好共享被修改部分的其他结构。变异操作`set-car!`和`set-cdr!`应谨慎使用；除非我们很好地理解数据对象是如何共享的，否则变异可能会产生意想不到的结果。[注148]

**校订后**

正如将在以下各节中看到的，我们可以利用共享来极大地扩展可用序对表示的数据结构的范围。另一方面，共享也可能是危险的，因为对结构所做的修改也会影响恰好共享被修改部分的其他结构。修改操作`set-car!`和`set-cdr!`应谨慎使用；除非我们很好地理解数据对象是如何共享的，否则修改可能会产生意想不到的结果。[注148]

### 3_002e3:0045

**原文**

Mutation is just assignment

**校订前**

变异就是赋值

**校订后**

修改就是赋值

### 3_002e3:0052

**原文**

The mutators `set-car!` and `set-cdr!` enable us to use pairs to construct data structures that cannot be built with `cons`, `car`, and `cdr` alone. This section shows how to use pairs to represent a data structure called a queue. Section 3.3.3 will show how to represent data structures called tables.

**校订前**

变异器`set-car!`和`set-cdr!`使我们能够使用序对来构造仅用`cons`、`car`和`cdr`无法构建的数据结构。本节展示如何使用序对来表示一种称为队列的数据结构。第3.3.3节将展示如何表示称为表的数据结构。

**校订后**

修改器`set-car!`和`set-cdr!`使我们能够使用序对来构造仅用`cons`、`car`和`cdr`无法构建的数据结构。本节展示如何使用序对来表示一种称为队列的数据结构。第3.3.3节将展示如何表示称为表的数据结构。

### 3_002e3:0056

**原文**

a constructor: `(make-queue)` returns an empty queue (a queue containing no items).

**校订前**

一个构造器：`(make-queue)`返回一个空队列（一个不包含任何项的队列）。

**校订后**

一个构造函数：`(make-queue)`返回一个空队列（一个不包含任何项的队列）。

### 3_002e3:0057

**原文**

two selectors:

**校订前**

两个选择器：

**校订后**

两个选择函数：

### 3_002e3:0060

**原文**

two mutators:

**校订前**

两个变异器：

**校订后**

两个修改器：

### 3_002e3:0063

**原文**

Because a queue is a sequence of items, we could certainly represent it as an ordinary list; the front of the queue would be the `car` of the list, inserting an item in the queue would amount to appending a new element at the end of the list, and deleting an item from the queue would just be taking the `cdr` of the list. However, this representation is inefficient, because in order to insert an item we must scan the list until we reach the end. Since the only method we have for scanning a list is by successive `cdr` operations, this scanning requires $Θ(n)$ steps for a list of $n$ items. A simple modification to the list representation overcomes this disadvantage by allowing the queue operations to be implemented so that they require $Θ(1)$ steps; that is, so that the number of steps needed is independent of the length of the queue.

**校订前**

因为队列是项的序列，我们当然可以将其表示为普通的表；队列的前端将是表的`car`，在队列中插入项相当于在表的末尾追加一个新元素，而从队列中删除项只是取表的`cdr`。然而，这种表示效率低下，因为为了插入项，我们必须扫描表直到到达末尾。由于我们扫描表的唯一方法是连续进行`cdr`操作，对于有$n$个项的列表，这种扫描需要$Θ(n)$步。对表表示的一个简单修改克服了这个缺点，它允许队列操作的实现只需要$Θ(1)$步；也就是说，所需的步数与队列的长度无关。

**校订后**

因为队列是项的序列，我们当然可以将其表示为普通的表；队列的前端将是表的`car`，在队列中插入项相当于在表的末尾追加一个新元素，而从队列中删除项只是取表的`cdr`。然而，这种表示效率低下，因为为了插入项，我们必须扫描表直到到达末尾。由于我们扫描表的唯一方法是连续进行`cdr`操作，对于有$n$个项的表，这种扫描需要$Θ(n)$步。对表表示的一个简单修改克服了这个缺点，它允许队列操作的实现只需要$Θ(1)$步；也就是说，所需的步数与队列的长度无关。

### 3_002e3:0069

**原文**

The `make-queue` constructor returns, as an initially empty queue, a pair whose `car` and `cdr` are both the empty list:

**校订前**

`make-queue`构造器返回一个序对作为初始为空的队列，其`car`和`cdr`都是空表：

**校订后**

`make-queue`构造函数返回一个序对作为初始为空的队列，其`car`和`cdr`都是空表：

### 3_002e3:0079

**原文**

Exercise 3.23: A deque (“double-ended queue”) is a sequence in which items can be inserted and deleted at either the front or the rear. Operations on deques are the constructor `make-deque`, the predicate `empty-deque?`, selectors `front-deque` and `rear-deque`, and mutators `front-insert-deque!`, `rear-insert-deque!`, `front-delete-deque!`, `rear-delete-deque!`. Show how to represent deques using pairs, and give implementations of the operations.[注151] All operations should be accomplished in $Θ(1)$ steps.

**校订前**

习题 3.23： 一个 deque（“双端队列”）是一个序列，其中的项可以在前端或后端插入和删除。对 deque 的操作有构造器 `make-deque`、谓词 `empty-deque?`、选择器 `front-deque` 和 `rear-deque`，以及变异器 `front-insert-deque!`、`rear-insert-deque!`、`front-delete-deque!`、`rear-delete-deque!`。说明如何使用序对来表示 deque，并给出这些操作的实现。[注151] 所有操作都应在 $Θ(1)$ 步内完成。

**校订后**

习题 3.23： 一个 deque（“双端队列”）是一个序列，其中的项可以在前端或后端插入和删除。对 deque 的操作有构造函数 `make-deque`、谓词 `empty-deque?`、选择函数 `front-deque` 和 `rear-deque`，以及修改器 `front-insert-deque!`、`rear-insert-deque!`、`front-delete-deque!`、`rear-delete-deque!`。说明如何使用序对来表示 deque，并给出这些操作的实现。[注151] 所有操作都应在 $Θ(1)$ 步内完成。

### 3_002e3:0082

**原文**

We first consider a one-dimensional table, in which each value is stored under a single key. We implement the table as a list of records, each of which is implemented as a pair consisting of a key and the associated value. The records are glued together to form a list by pairs whose `car`s point to successive records. These gluing pairs are called the backbone of the table. In order to have a place that we can change when we add a new record to the table, we build the table as a headed list. A headed list has a special backbone pair at the beginning, which holds a dummy “record”—in this case the arbitrarily chosen symbol `*table*`. Figure 3.22 shows the box-and-pointer diagram for the table

**校订前**

我们首先考虑一维表，其中每个值存储在单个键下。我们将表实现为一个记录的表，每个记录实现为一个由键和关联值组成的序对。这些记录通过其 `car` 指向相继记录的序对粘合在一起形成表。这些粘合序对被称为表的 骨架。为了有一个在向表中添加新记录时可以更改的位置，我们将表构建为一个 有头表。有头表在开头有一个特殊的骨架序对，它持有一个哑“记录”——在这种情况下是任意选择的符号 `*table*`。图 3.22 显示了该表的箱指针图

**校订后**

我们首先考虑一维表，其中每个值存储在单个键下。我们将表实现为一个记录的表，每个记录实现为一个由键和关联值组成的序对。这些记录通过其 `car` 指向相继记录的序对粘合在一起形成表。这些粘合序对被称为表的 骨架。为了有一个在向表中添加新记录时可以更改的位置，我们将表构建为一个 带表头的表。带表头的表在开头有一个特殊的骨架序对，它持有一个哑“记录”——在这种情况下是任意选择的符号 `*table*`。图 3.22 显示了该表的盒指针图

### 3_002e3:0083

**原文**

Figure 3.22: A table represented as a headed list.

**校订前**

图 3.22： 一个表示为有头表的表。

**校订后**

图 3.22： 一个表示为带表头的表的表。

### 3_002e3:0084

**原文**

To extract information from a table we use the `lookup` procedure, which takes a key as argument and returns the associated value (or false if there is no value stored under that key). `Lookup` is defined in terms of the `assoc` operation, which expects a key and a list of records as arguments. Note that `assoc` never sees the dummy record. `Assoc` returns the record that has the given key as its `car`.[注152] `Lookup` then checks to see that the resulting record returned by `assoc` is not false, and returns the value (the `cdr`) of the record.

**校订前**

为了从表中提取信息，我们使用 `lookup` 过程，它接受一个键作为参数并返回关联的值（如果该键下没有存储值则返回假）。`Lookup` 是根据 `assoc` 操作定义的，该操作期望一个键和一个记录表作为参数。注意 `assoc` 从不会看到哑记录。`Assoc` 返回以给定键作为其 `car` 的记录。[注152] `Lookup` 然后检查由 `assoc` 返回的结果记录是否不为假，并返回该记录的值（即 `cdr`）。

**校订后**

为了从表中提取信息，我们使用 `lookup` 过程，它接受一个键作为参数并返回关联的值（如果该键下没有存储值则返回假）。`Lookup` 是根据 `assoc` 操作定义的，该操作期望一个键和一个记录表作为参数。注意 `assoc` 从不会看到占位记录。`Assoc` 返回以给定键作为其 `car` 的记录。[注152] `Lookup` 然后检查由 `assoc` 返回的结果记录是否不为假，并返回该记录的值（即 `cdr`）。

### 3_002e3:0085

**原文**

To insert a value in a table under a specified key, we first use `assoc` to see if there is already a record in the table with this key. If not, we form a new record by `cons`ing the key with the value, and insert this at the head of the table’s list of records, after the dummy record. If there already is a record with this key, we set the `cdr` of this record to the designated new value. The header of the table provides us with a fixed location to modify in order to insert the new record.[注153]

**校订前**

为了在表中指定的键下插入一个值，我们首先使用 `assoc` 查看表中是否已经存在具有该键的记录。如果没有，我们通过将键与值 `cons` 起来形成一个新记录，并将此记录插入到表的记录表的头部，即哑记录之后。如果已经存在具有该键的记录，我们将此记录的 `cdr` 设置为指定的新值。表的头部为我们提供了一个固定的位置，以便在插入新记录时进行修改。[注153]

**校订后**

为了在表中指定的键下插入一个值，我们首先使用 `assoc` 查看表中是否已经存在具有该键的记录。如果没有，我们通过将键与值 `cons` 起来形成一个新记录，并将此记录插入到表的记录表的头部，即占位记录之后。如果已经存在具有该键的记录，我们将此记录的 `cdr` 设置为指定的新值。表的头部为我们提供了一个固定的位置，以便在插入新记录时进行修改。[注153]

### 3_002e3:0088

**原文**

In a two-dimensional table, each value is indexed by two keys. We can construct such a table as a one-dimensional table in which each key identifies a subtable. Figure 3.23 shows the box-and-pointer diagram for the table

**校订前**

在二维表中，每个值由两个键索引。我们可以将这样的表构造为一个一维表，其中每个键标识一个子表。图 3.23 显示了该表的箱指针图

**校订后**

在二维表中，每个值由两个键索引。我们可以将这样的表构造为一个一维表，其中每个键标识一个子表。图 3.23 显示了该表的盒指针图

### 3_002e3:0097

**原文**

Exercise 3.24: In the table implementations above, the keys are tested for equality using `equal?` (called by `assoc`). This is not always the appropriate test. For instance, we might have a table with numeric keys in which we don’t need an exact match to the number we’re looking up, but only a number within some tolerance of it. Design a table constructor `make-table` that takes as an argument a `same-key?` procedure that will be used to test “equality” of keys. `Make-table` should return a `dispatch` procedure that can be used to access appropriate `lookup` and `insert!` procedures for a local table.

**校订前**

习题3.24：在上面的表实现中，键的相等性测试使用的是`equal?`（由`assoc`调用）。这并不总是合适的测试。例如，我们可能有一个带有数值键的表，其中我们不需要与所查找的数字精确匹配，而只需要在某个容差范围内的数字。设计一个表构造器`make-table`，它接受一个`same-key?`过程作为参数，该过程将用于测试键的“相等性”。`Make-table`应返回一个`dispatch`过程，该过程可用于访问局部表的相应`lookup`和`insert!`过程。

**校订后**

习题3.24：在上面的表实现中，键的相等性测试使用的是`equal?`（由`assoc`调用）。这并不总是合适的测试。例如，我们可能有一个带有数值键的表，其中我们不需要与所查找的数字精确匹配，而只需要在某个容差范围内的数字。设计一个表构造函数`make-table`，它接受一个`same-key?`过程作为参数，该过程将用于测试键的“相等性”。`Make-table`应返回一个`dispatch`过程，该过程可用于访问局部表的相应`lookup`和`insert!`过程。

### 3_002e3:0098

**原文**

Exercise 3.25: Generalizing one- and two-dimensional tables, show how to implement a table in which values are stored under an arbitrary number of keys and different values may be stored under different numbers of keys. The `lookup` and `insert!` procedures should take as input a list of keys used to access the table.

**校订前**

习题3.25：将一维和二维表推广，展示如何实现一个表，其中值存储在任意数量的键下，并且不同的值可以存储在不同数量的键下。`lookup`和`insert!`过程应接受一个用于访问表的键的列表作为输入。

**校订后**

习题3.25：将一维和二维表推广，展示如何实现一个表，其中值存储在任意数量的键下，并且不同的值可以存储在不同数量的键下。`lookup`和`insert!`过程应接受一个用于访问表的键的表作为输入。

### 3_002e3:0099

**原文**

Exercise 3.26: To search a table as implemented above, one needs to scan through the list of records. This is basically the unordered list representation of 2.3.3. For large tables, it may be more efficient to structure the table in a different manner. Describe a table implementation where the (key, value) records are organized using a binary tree, assuming that keys can be ordered in some way (e.g., numerically or alphabetically). (Compare Exercise 2.66 of Chapter 2.)

**校订前**

习题3.26：要搜索如上实现的表，需要扫描记录列表。这基本上就是2.3.3的无序列表表示。对于大型表，以不同的方式组织表可能更高效。描述一种表实现，其中（键，值）记录使用二叉树组织，假设键可以按某种方式排序（例如，按数值或字母顺序）。（比较第2章的习题2.66。）

**校订后**

习题3.26：要搜索如上实现的表，需要扫描记录表。这基本上就是2.3.3的无序表表示。对于大型表，以不同的方式组织表可能更高效。描述一种表实现，其中（键，值）记录使用二叉树组织，假设键可以按某种方式排序（例如，按数值或字母顺序）。（比较第2章的习题2.66。）

### 3_002e3:0108

**原文**

We can connect primitive functions together to construct more complex functions. To accomplish this we wire the outputs of some function boxes to the inputs of other function boxes. For example, the half-adder circuit shown in Figure 3.25 consists of an or-gate, two and-gates, and an inverter. It takes two input signals, A and B, and has two output signals, S and C. S will become 1 whenever precisely one of A and B is 1, and C will become 1 whenever A and B are both 1. We can see from the figure that, because of the delays involved, the outputs may be generated at different times. Many of the difficulties in the design of digital circuits arise from this fact.

**校订前**

我们可以将基本函数连接在一起以构造更复杂的函数。为此，我们将一些函数盒的输出连接到其他函数盒的输入。例如，图3.25中所示的半加器电路由一个或门、两个与门和一个反相器组成。它接受两个输入信号 A 和 B，并有两个输出信号 S 和 C。当 A 和 B 中恰好有一个为1时，S 将变为1；当 A 和 B 都为1时，C 将变为1。从图中可以看出，由于涉及的延迟，输出可能在不同时间产生。数字电路设计中的许多困难都源于这一事实。

**校订后**

我们可以将基本函数连接在一起以构造更复杂的函数。为此，我们将一些功能盒的输出连接到其他功能盒的输入。例如，图3.25中所示的半加器电路由一个或门、两个与门和一个反相器组成。它接受两个输入信号 A 和 B，并有两个输出信号 S 和 C。当 A 和 B 中恰好有一个为1时，S 将变为1；当 A 和 B 都为1时，C 将变为1。从图中可以看出，由于涉及的延迟，输出可能在不同时间产生。数字电路设计中的许多困难都源于这一事实。

### 3_002e3:0110

**原文**

We will now build a program for modeling the digital logic circuits we wish to study. The program will construct computational objects modeling the wires, which will “hold” the signals. Function boxes will be modeled by procedures that enforce the correct relationships among the signals.

**校订前**

我们现在将构建一个程序，用于对我们希望研究的数字逻辑电路进行建模。该程序将构造对导线进行建模的计算对象，这些导线将“持有”信号。函数盒将由强制信号之间正确关系的过程来建模。

**校订后**

我们现在将构建一个程序，用于对我们希望研究的数字逻辑电路进行建模。该程序将构造对导线进行建模的计算对象，这些导线将“持有”信号。功能盒将由强制信号之间正确关系的过程来建模。

### 3_002e3:0112

**原文**

We attach a function box to a set of wires by calling a procedure that constructs that kind of box. The arguments to the constructor procedure are the wires to be attached to the box. For example, given that we can construct and-gates, or-gates, and inverters, we can wire together the half-adder shown in Figure 3.25:

**校订前**

我们通过调用构造某种盒的过程，将一个函数盒连接到一组导线上。构造过程的参数是要连接到该盒的导线。例如，假设我们可以构造与门、或门和反相器，我们可以将图3.25中所示的半加器连接在一起：

**校订后**

我们通过调用构造某种盒的过程，将一个功能盒连接到一组导线上。构造过程的参数是要连接到该盒的导线。例如，假设我们可以构造与门、或门和反相器，我们可以将图3.25中所示的半加器连接在一起：

### 3_002e3:0117

**原文**

In essence, our simulator provides us with the tools to construct a language of circuits. If we adopt the general perspective on languages with which we approached the study of Lisp in 1.1, we can say that the primitive function boxes form the primitive elements of the language, that wiring boxes together provides a means of combination, and that specifying wiring patterns as procedures serves as a means of abstraction.

**校订前**

本质上，我们的模拟器为我们提供了构造电路语言的工具。如果我们采用在1.1中研究 Lisp 时所采用的关于语言的一般视角，我们可以说，基本函数盒构成了语言的基元元素，将盒连接在一起提供了一种组合手段，而将连接模式指定为过程则充当了一种抽象手段。

**校订后**

本质上，我们的模拟器为我们提供了构造电路语言的工具。如果我们采用在1.1中研究 Lisp 时所采用的关于语言的一般视角，我们可以说，基本功能盒构成了语言的基元元素，将盒连接在一起提供了一种组合手段，而将连接模式指定为过程则充当了一种抽象手段。

### 3_002e3:0118

**原文**

Primitive function boxes

**校订前**

基本函数盒

**校订后**

基本功能盒

### 3_002e3:0119

**原文**

The primitive function boxes implement the “forces” by which a change in the signal on one wire influences the signals on other wires. To build function boxes, we use the following operations on wires:

**校订前**

基本函数盒实现了“力”，通过这种力，一条导线上信号的变化会影响其他导线上的信号。为了构建函数盒，我们对导线使用以下操作：

**校订后**

基本功能盒实现了“力”，通过这种力，一条导线上信号的变化会影响其他导线上的信号。为了构建功能盒，我们对导线使用以下操作：

### 3_002e3:0126

**原文**

Exercise 3.28: Define an or-gate as a primitive function box. Your `or-gate` constructor should be similar to `and-gate`.

**校订前**

习题3.28：将或门定义为基本函数盒。你的`or-gate`构造过程应类似于`and-gate`。

**校订后**

习题3.28：将或门定义为基本功能盒。你的`or-gate`构造过程应类似于`and-gate`。

### 3_002e3:0128

**原文**

Exercise 3.30: Figure 3.27 shows a ripple-carry adder formed by stringing together $n$ full-adders. This is the simplest form of parallel adder for adding two $n$-bit binary numbers. The inputs $A_{1}$, $A_{2}$, $A_{3}$, …, $A_{n}$ and $B_{1}$, $B_{2}$, $B_{3}$, …, $B_{n}$ are the two binary numbers to be added (each $A_{k}$ and $B_{k}$ is a 0 or a 1). The circuit generates $S_{1}$, $S_{2}$, $S_{3}$, …, $S_{n}$, the $n$ bits of the sum, and $C$, the carry from the addition. Write a procedure `ripple-carry-adder` that generates this circuit. The procedure should take as arguments three lists of $n$ wires each—the $A_{k}$, the $B_{k}$, and the $S_{k}$—and also another wire $C$. The major drawback of the ripple-carry adder is the need to wait for the carry signals to propagate. What is the delay needed to obtain the complete output from an $n$-bit ripple-carry adder, expressed in terms of the delays for and-gates, or-gates, and inverters?

**校订前**

习题 3.30： 图 3.27展示了一个由 行波进位加法器，它通过将$n$个全加器串联而成。这是用于将两个$n$位二进制数相加的最简单的并行加法器形式。输入$A_{1}$、$A_{2}$、$A_{3}$、…、$A_{n}$和$B_{1}$、$B_{2}$、$B_{3}$、…、$B_{n}$是要相加的两个二进制数（每个$A_{k}$和$B_{k}$都是0或1）。该电路生成$S_{1}$、$S_{2}$、$S_{3}$、…、$S_{n}$，即和的$n$个位，以及$C$，即加法产生的进位。编写一个过程`ripple-carry-adder`来生成该电路。该过程应接受三个各含$n$条线的表作为参数——即$A_{k}$、$B_{k}$和$S_{k}$——以及另一条线$C$。行波进位加法器的主要缺点是必须等待进位信号传播。以与门、或门和非门的延迟来表示，从一个$n$位行波进位加法器获得完整输出需要多少延迟？

**校订后**

习题 3.30： 图 3.27展示了一个 行波进位加法器，它由$n$个全加器串联而成。这是用于将两个$n$位二进制数相加的最简单的并行加法器形式。输入$A_{1}$、$A_{2}$、$A_{3}$、…、$A_{n}$和$B_{1}$、$B_{2}$、$B_{3}$、…、$B_{n}$是要相加的两个二进制数（每个$A_{k}$和$B_{k}$都是0或1）。该电路生成$S_{1}$、$S_{2}$、$S_{3}$、…、$S_{n}$，即和的$n$个位，以及$C$，即加法产生的进位。编写一个过程`ripple-carry-adder`来生成该电路。该过程应接受三个各含$n$条线的表作为参数——即$A_{k}$、$B_{k}$和$S_{k}$——以及另一条线$C$。行波进位加法器的主要缺点是必须等待进位信号传播。以与门、或门和反相器的延迟来表示，从一个$n$位行波进位加法器获得完整输出需要多少延迟？

### 3_002e3:0132

**原文**

The local procedure `set-my-signal!` tests whether the new signal value changes the signal on the wire. If so, it runs each of the action procedures, using the following procedure `call-each`, which calls each of the items in a list of no-argument procedures:

**校订前**

局部过程 `set-my-signal!` 测试新的信号值是否改变了导线上的信号。如果是，它就运行每个动作过程，使用以下过程 `call-each`，该过程调用一个无参数过程列表中的每一项：

**校订后**

局部过程 `set-my-signal!` 测试新的信号值是否改变了导线上的信号。如果是，它就运行每个动作过程，使用以下过程 `call-each`，该过程调用一个无参数过程表中的每一项：

### 3_002e3:0133

**原文**

The local procedure `accept-action-procedure!` adds the given procedure to the list of procedures to be run, and then runs the new procedure once. (See Exercise 3.31.)

**校订前**

局部过程 `accept-action-procedure!` 将给定的过程添加到要运行的过程列表中，然后运行新过程一次。（见 习题 3.31。）

**校订后**

局部过程 `accept-action-procedure!` 将给定的过程添加到要运行的过程表中，然后运行新过程一次。（见 习题 3.31。）

### 3_002e3:0137

**原文**

The agenda

**校订前**

议程

**校订后**

日程表

### 3_002e3:0138

**原文**

The only thing needed to complete the simulator is `after-delay`. The idea here is that we maintain a data structure, called an agenda, that contains a schedule of things to do. The following operations are defined for agendas:

**校订前**

完成模拟器所需的唯一东西是 `after-delay`。这里的想法是我们维护一个称为 议程的数据结构，其中包含要做的事情的时间表。为议程定义了以下操作：

**校订后**

完成模拟器所需的唯一东西是 `after-delay`。这里的想法是我们维护一个称为 日程表的数据结构，其中包含要做的事情的时间表。为日程表定义了以下操作：

### 3_002e3:0139

**原文**

`(make-agenda)` returns a new empty agenda.

**校订前**

`(make-agenda)` 返回一个新的空议程。

**校订后**

`(make-agenda)` 返回一个新的空日程表。

### 3_002e3:0140

**原文**

`(empty-agenda? ⟨agenda⟩)` is true if the specified agenda is empty.

**校订前**

如果指定的议程为空，则 `(empty-agenda? ⟨agenda⟩)` 为真。

**校订后**

如果指定的日程表为空，则 `(empty-agenda? ⟨agenda⟩)` 为真。

### 3_002e3:0141

**原文**

`(first-agenda-item ⟨agenda⟩)` returns the first item on the agenda.

**校订前**

`(first-agenda-item ⟨agenda⟩)` 返回议程上的第一项。

**校订后**

`(first-agenda-item ⟨agenda⟩)` 返回日程表上的第一项。

### 3_002e3:0142

**原文**

`(remove-first-agenda-item! ⟨agenda⟩)` modifies the agenda by removing the first item.

**校订前**

`(remove-first-agenda-item! ⟨agenda⟩)` 通过移除第一项来修改议程。

**校订后**

`(remove-first-agenda-item! ⟨agenda⟩)` 通过移除第一项来修改日程表。

### 3_002e3:0143

**原文**

`(add-to-agenda! ⟨time⟩ ⟨action⟩ ⟨agenda⟩)` modifies the agenda by adding the given action procedure to be run at the specified time.

**校订前**

`(add-to-agenda! ⟨time⟩ ⟨action⟩ ⟨agenda⟩)` 通过添加给定的动作过程以在指定时间运行来修改议程。

**校订后**

`(add-to-agenda! ⟨time⟩ ⟨action⟩ ⟨agenda⟩)` 通过添加给定的动作过程以在指定时间运行来修改日程表。

### 3_002e3:0145

**原文**

The particular agenda that we use is denoted by `the-agenda`. The procedure `after-delay` adds new elements to `the-agenda`:

**校订前**

我们使用的特定议程由 `the-agenda` 表示。过程 `after-delay` 向 `the-agenda` 添加新元素：

**校订后**

我们使用的特定日程表由 `the-agenda` 表示。过程 `after-delay` 向 `the-agenda` 添加新元素：

### 3_002e3:0146

**原文**

The simulation is driven by the procedure `propagate`, which operates on `the-agenda`, executing each procedure on the agenda in sequence. In general, as the simulation runs, new items will be added to the agenda, and `propagate` will continue the simulation as long as there are items on the agenda:

**校订前**

模拟由过程 `propagate` 驱动，它作用于 `the-agenda`，按顺序执行议程上的每个过程。一般来说，随着模拟运行，新项将被添加到议程中，只要议程上还有项，`propagate` 就会继续模拟：

**校订后**

模拟由过程 `propagate` 驱动，它作用于 `the-agenda`，按顺序执行日程表上的每个过程。一般来说，随着模拟运行，新项将被添加到日程表中，只要日程表上还有项，`propagate` 就会继续模拟：

### 3_002e3:0149

**原文**

We begin by initializing the agenda and specifying delays for the primitive function boxes:

**校订前**

我们首先初始化议程并指定基本功能框的延迟：

**校订后**

我们首先初始化日程表并指定基本功能盒的延迟：

### 3_002e3:0154

**原文**

Exercise 3.31: The internal procedure `accept-action-procedure!` defined in `make-wire` specifies that when a new action procedure is added to a wire, the procedure is immediately run. Explain why this initialization is necessary. In particular, trace through the half-adder example in the paragraphs above and say how the system’s response would differ if we had defined `accept-action-procedure!` as

**校订前**

习题 3.31： `make-wire` 中定义的内部过程 `accept-action-procedure!` 规定，当新的动作过程被添加到导线时，该过程立即运行。解释为什么这种初始化是必要的。特别地，追踪上面段落中的半加器示例，并说明如果我们把 `accept-action-procedure!` 定义为

**校订后**

习题 3.31： `make-wire` 中定义的内部过程 `accept-action-procedure!` 规定，当新的动作过程被添加到导线时，该过程立即运行。解释为什么这种初始化是必要的。特别地，追踪上面段落中的半加器示例，并说明系统的响应会有何不同，如果我们把 `accept-action-procedure!` 定义为

### 3_002e3:0155

**原文**

Implementing the agenda

**校订前**

实现议程

**校订后**

实现日程表

### 3_002e3:0156

**原文**

Finally, we give details of the agenda data structure, which holds the procedures that are scheduled for future execution.

**校订前**

最后，我们给出议程数据结构的细节，它保存计划在未来执行的过程。

**校订后**

最后，我们给出日程表数据结构的细节，它保存计划在未来执行的过程。

### 3_002e3:0157

**原文**

The agenda is made up of time segments. Each time segment is a pair consisting of a number (the time) and a queue (see Exercise 3.32) that holds the procedures that are scheduled to be run during that time segment.

**校订前**

议程由 时间段组成。每个时间段是一个序对，由一个数字（时间）和一个队列（见 习题 3.32）组成，该队列保存计划在该时间段内运行的过程。

**校订后**

日程表由 时间段组成。每个时间段是一个序对，由一个数字（时间）和一个队列（见 习题 3.32）组成，该队列保存计划在该时间段内运行的过程。

### 3_002e3:0162

**原文**

The procedure that removes the first item from the agenda deletes the item at the front of the queue in the first time segment. If this deletion makes the time segment empty, we remove it from the list of segments:[注157]

**校订前**

从日程表中移除第一个项的过程会删除第一个时间段中队列前端的项。如果这次删除使得该时间段为空，我们就将它从时间段列表中移除：[注157]

**校订后**

从日程表中移除第一个项的过程会删除第一个时间段中队列前端的项。如果这次删除使得该时间段为空，我们就将它从时间段表中移除：[注157]

### 3_002e3:0163

**原文**

The first agenda item is found at the head of the queue in the first time segment. Whenever we extract an item, we also update the current time:[注158]

**校订前**

第一个议程项在第一个时间段中位于队列的头部。每当我们取出一个项时，我们也会更新当前时间：[注158]

**校订后**

第一个日程表项在第一个时间段中位于队列的头部。每当我们取出一个项时，我们也会更新当前时间：[注158]

### 3_002e3:0164

**原文**

Exercise 3.32: The procedures to be run during each time segment of the agenda are kept in a queue. Thus, the procedures for each segment are called in the order in which they were added to the agenda (first in, first out). Explain why this order must be used. In particular, trace the behavior of an and-gate whose inputs change from 0, 1 to 1, 0 in the same segment and say how the behavior would differ if we stored a segment’s procedures in an ordinary list, adding and removing procedures only at the front (last in, first out).

**校订前**

习题 3.32：议程的每个时间段中要运行的过程保存在一个队列中。因此，每个时间段的过程按照它们被添加到议程的顺序被调用（先进先出）。解释为什么必须使用这种顺序。特别地，追踪一个与门的行为，其输入在同一时间段内从 0、1 变为 1、0，并说明如果我们把某个时间段的过程存储在一个普通的表中，只在表的前端添加和移除过程（后进先出），行为会有什么不同。

**校订后**

习题 3.32：日程表的每个时间段中要运行的过程保存在一个队列中。因此，每个时间段的过程按照它们被添加到日程表的顺序被调用（先进先出）。解释为什么必须使用这种顺序。特别地，追踪一个与门的行为，其输入在同一时间段内从 0、1 变为 1、0，并说明如果我们把某个时间段的过程存储在一个普通的表中，只在表的前端添加和移除过程（后进先出），行为会有什么不同。

### 3_002e3:0172

**原文**

To use the constraint system to carry out the temperature computation outlined above, we first create two connectors, `C` and `F`, by calling the constructor `make-connector`, and link `C` and `F` in an appropriate network:

**校订前**

为了使用约束系统执行上面概述的温度计算，我们首先通过调用构造器 `make-connector` 创建两个连接器 `C` 和 `F`，并将 `C` 和 `F` 链接在一个适当的网络中：

**校订后**

为了使用约束系统执行上面概述的温度计算，我们首先通过调用构造函数 `make-connector` 创建两个连接器 `C` 和 `F`，并将 `C` 和 `F` 链接在一个适当的网络中：

### 3_002e3:0174

**原文**

This procedure creates the internal connectors `u`, `v`, `w`, `x`, and `y`, and links them as shown in Figure 3.28 using the primitive constraint constructors `adder`, `multiplier`, and `constant`. Just as with the digital-circuit simulator of 3.3.4, expressing these combinations of primitive elements in terms of procedures automatically provides our language with a means of abstraction for compound objects.

**校订前**

这个过程创建内部连接器 `u`、`v`、`w`、`x` 和 `y`，并使用基本约束构造器 `adder`、`multiplier` 和 `constant` 将它们如 图 3.28 所示链接起来。正如 3.3.4 的数字电路模拟器一样，用过程来表达这些基本元素的组合自动为我们的语言提供了一种对复合对象进行抽象的手段。

**校订后**

这个过程创建内部连接器 `u`、`v`、`w`、`x` 和 `y`，并使用基本约束构造函数 `adder`、`multiplier` 和 `constant` 将它们如 图 3.28 所示链接起来。正如 3.3.4 的数字电路模拟器一样，用过程来表达这些基本元素的组合自动为我们的语言提供了一种对复合对象进行抽象的手段。

### 3_002e3:0177

**原文**

The probe on `C` awakens and reports the value. `C` also propagates its value through the network as described above. This sets `F` to 77, which is reported by the probe on `F`.

**校订前**

`C`上的探测器被唤醒并报告该值。`C`也如上所述通过网络传播其值。这将`F`设置为77，由`F`上的探测器报告。

**校订后**

`C`上的探针被唤醒并报告该值。`C`也如上所述通过网络传播其值。这将`F`设置为77，由`F`上的探针报告。

### 3_002e3:0179

**原文**

The connector complains that it has sensed a contradiction: Its value is 77, and someone is trying to set it to 212. If we really want to reuse the network with new values, we can tell `C` to forget its old value:

**校订前**

连接器抱怨它感知到了矛盾：它的值是77，而有人试图将其设置为212。如果我们真的想用新值重用该网络，可以告诉`C`忘记它的旧值：

**校订后**

连接器报告检测到了矛盾：它的值是77，而有人试图将其设置为212。如果我们真的想用新值重用该网络，可以告诉`C`忘记它的旧值：

### 3_002e3:0180

**原文**

`C` finds that the `user`, who set its value originally, is now retracting that value, so `C` agrees to lose its value, as shown by the probe, and informs the rest of the network of this fact. This information eventually propagates to `F`, which now finds that it has no reason for continuing to believe that its own value is 77. Thus, `F` also gives up its value, as shown by the probe.

**校订前**

`C`发现最初设置其值的`user`现在正在撤回该值，因此`C`同意失去其值，如探测器所示，并将这一事实通知网络中的其余部分。这一信息最终传播到`F`，它现在发现自己没有理由继续相信自己的值是77。因此，`F`也放弃了它的值，如探测器所示。

**校订后**

`C`发现最初设置其值的`user`现在正在撤回该值，因此`C`同意失去其值，如探针所示，并将这一事实通知网络中的其余部分。这一信息最终传播到`F`，它现在发现自己没有理由继续相信自己的值是77。因此，`F`也放弃了它的值，如探针所示。

### 3_002e3:0182

**原文**

This new value, when propagated through the network, forces `C` to have a value of 100, and this is registered by the probe on `C`. Notice that the very same network is being used to compute `C` given `F` and to compute `F` given `C`. This nondirectionality of computation is the distinguishing feature of constraint-based systems.

**校订前**

这个新值在通过网络传播时，迫使`C`的值为100，这由`C`上的探测器记录。注意，同一个网络既被用来在给定`F`的情况下计算`C`，也被用来在给定`C`的情况下计算`F`。计算的这种无方向性是约束系统的显著特征。

**校订后**

这个新值在通过网络传播时，迫使`C`的值为100，这由`C`上的探针记录。注意，同一个网络既被用来在给定`F`的情况下计算`C`，也被用来在给定`C`的情况下计算`F`。计算的这种无方向性是约束系统的显著特征。

### 3_002e3:0193

**原文**

`Adder` connects the new adder to the designated connectors and returns it as its value. The procedure `me`, which represents the adder, acts as a dispatch to the local procedures. The following “syntax interfaces” (see Footnote 155 in 3.3.4) are used in conjunction with the dispatch:

**校订前**

`Adder`将新的加法器连接到指定的连接器，并将其作为值返回。表示加法器的过程`me`充当对局部过程的分派。以下“语法接口”（见脚注155在3.3.4中）与分派一起使用：

**校订后**

`Adder`将新的加法器连接到指定的连接器，并将其作为值返回。表示加法器的过程`me`充当对局部过程的分派。以下“语法接口”（见3.3.4中的脚注155）与分派一起使用：

### 3_002e3:0196

**原文**

A `constant` constructor simply sets the value of the designated connector. Any `I-have-a-value` or `I-lost-my-value` message sent to the constant box will produce an error.

**校订前**

`constant`构造器只是设置指定连接器的值。任何发送到常量框的`I-have-a-value`或`I-lost-my-value`消息都会产生错误。

**校订后**

`constant`构造函数只是设置指定连接器的值。任何发送到常量框的`I-have-a-value`或`I-lost-my-value`消息都会产生错误。

### 3_002e3:0197

**原文**

Finally, a probe prints a message about the setting or unsetting of the designated connector:

**校订前**

最后，探测器打印关于指定连接器设置或取消设置的消息：

**校订后**

最后，探针打印关于指定连接器设置或取消设置的消息：

### 3_002e3:0199

**原文**

A connector is represented as a procedural object with local state variables `value`, the current value of the connector; `informant`, the object that set the connector’s value; and `constraints`, a list of the constraints in which the connector participates.

**校订前**

连接器表示为一个带有局部状态变量的过程对象：`value`，连接器的当前值；`informant`，设置连接器值的对象；以及`constraints`，连接器参与的约束的列表。

**校订后**

连接器表示为一个带有局部状态变量的过程对象：`value`，连接器的当前值；`informant`，设置连接器值的对象；以及`constraints`，连接器参与的约束的表。

### 3_002e3:0207

**原文**

Exercise 3.35: Ben Bitdiddle tells Louis that one way to avoid the trouble in Exercise 3.34 is to define a squarer as a new primitive constraint. Fill in the missing portions in Ben’s outline for a procedure to implement such a constraint:

**校订前**

习题3.35：Ben Bitdiddle告诉Louis，避免习题3.34中麻烦的一种方法是将平方器定义为一个新的基本约束。填写Ben的提纲中缺失的部分，以实现这样一个约束的过程：

**校订后**

习题3.35：Ben Bitdiddle告诉Louis，避免习题3.34中麻烦的一种方法是将平方器定义为一个新的基本约束。补全Ben给出的过程框架，以实现这样一个约束：

### 3_002e3:0216

**原文**

[注145] We see from this that mutation operations on lists can create “garbage” that is not part of any accessible structure. We will see in 5.3.2 that Lisp memory-management systems include a garbage collector, which identifies and recycles the memory space used by unneeded pairs.

**校订前**

[注145]由此我们看到，对表进行变异操作可以产生不属于任何可访问结构的“垃圾”。我们将在5.3.2中看到，Lisp内存管理系统包含一个垃圾回收器，它识别并回收不再需要的序对所使用的内存空间。

**校订后**

[注145]由此我们看到，对表进行修改操作可以产生不属于任何可访问结构的“垃圾”。我们将在5.3.2中看到，Lisp内存管理系统包含一个垃圾回收器，它识别并回收不再需要的序对所使用的内存空间。

### 3_002e3:0218

**原文**

[注147] The two pairs are distinct because each call to `cons` returns a new pair. The symbols are shared; in Scheme there is a unique symbol with any given name. Since Scheme provides no way to mutate a symbol, this sharing is undetectable. Note also that the sharing is what enables us to compare symbols using `eq?`, which simply checks equality of pointers.

**校订前**

[注147]这两个序对是不同的，因为每次调用`cons`都返回一个新的序对。符号是共享的；在Scheme中，任何给定名称都有一个唯一的符号。由于Scheme没有提供变异符号的方法，这种共享是无法检测的。还要注意，正是这种共享使我们能够使用`eq?`来比较符号，它只是检查指针的相等性。

**校订后**

[注147]这两个序对是不同的，因为每次调用`cons`都返回一个新的序对。符号是共享的；在Scheme中，任何给定名称都有一个唯一的符号。由于Scheme没有提供修改符号的方法，这种共享是无法检测的。还要注意，正是这种共享使我们能够使用`eq?`来比较符号，它只是检查指针的相等性。

### 3_002e3:0220

**原文**

[注149] On the other hand, from the viewpoint of implementation, assignment requires us to modify the environment, which is itself a mutable data structure. Thus, assignment and mutation are equipotent: Each can be implemented in terms of the other.

**校订前**

[注149]另一方面，从实现的角度来看，赋值要求我们修改环境，而环境本身就是一个可变的数据结构。因此，赋值和变异是等势的：每一个都可以用另一个来实现。

**校订后**

[注149]另一方面，从实现的角度来看，赋值要求我们修改环境，而环境本身就是一个可变的数据结构。因此，赋值和修改是等势的：每一个都可以用另一个来实现。

### 3_002e3:0227

**原文**

[注156] The agenda is a headed list, like the tables in 3.3.3, but since the list is headed by the time, we do not need an additional dummy header (such as the `*table*` symbol used with tables).

**校订前**

[注156]议程是一个带表头的表，就像3.3.3中的表一样，但由于该表以时间作为表头，我们不需要额外的哑表头（例如与表一起使用的`*table*`符号）。

**校订后**

[注156]日程表是一个带表头的表，就像3.3.3中的表一样，但由于该表以时间作为表头，我们不需要额外的占位表头（例如与表一起使用的`*table*`符号）。

### 3_002e3:0229

**原文**

[注158] In this way, the current time will always be the time of the action most recently processed. Storing this time at the head of the agenda ensures that it will still be available even if the associated time segment has been deleted.

**校订前**

[注158]这样，当前时间将始终是最近处理的动作的时间。将此时间存储在议程的头部，确保即使关联的时间段已被删除，它仍然可用。

**校订后**

[注158]这样，当前时间将始终是最近处理的动作的时间。将此时间存储在日程表的头部，确保即使关联的时间段已被删除，它仍然可用。

### 3_002e4:0013

**原文**

This indeterminacy in the order of events can pose serious problems in the design of concurrent systems. For instance, suppose that the withdrawals made by Peter and Paul are implemented as two separate processes sharing a common variable `balance`, each process specified by the procedure given in 3.1.1:

**校订前**

事件顺序的这种不确定性可能会在并发系统的设计中造成严重问题。例如，假设 Peter 和 Paul 的取款被实现为两个共享公共变量 `balance` 的独立过程，每个过程由 3.1.1 中给出的过程指定：

**校订后**

事件顺序的这种不确定性可能会在并发系统的设计中造成严重问题。例如，假设 Peter 和 Paul 的取款被实现为两个共享公共变量 `balance` 的独立进程，每个进程由 3.1.1 中给出的过程指定：

### 3_002e4:0014

**原文**

If the two processes operate independently, then Peter might test the balance and attempt to withdraw a legitimate amount. However, Paul might withdraw some funds in between the time that Peter checks the balance and the time Peter completes the withdrawal, thus invalidating Peter’s test.

**校订前**

如果这两个过程独立运行，那么 Peter 可能会检查余额并尝试取出一个合法的金额。然而，Paul 可能会在 Peter 检查余额和 Peter 完成取款之间取出一些资金，从而使 Peter 的检查失效。

**校订后**

如果这两个进程独立运行，那么 Peter 可能会检查余额并尝试取出一个合法的金额。然而，Paul 可能会在 Peter 检查余额和 Peter 完成取款之间取出一些资金，从而使 Peter 的检查失效。

### 3_002e4:0017

**原文**

The timing diagram in Figure 3.29 depicts an order of events where `balance` starts at 100, Peter withdraws 10, Paul withdraws 25, and yet the final value of `balance` is 75. As shown in the diagram, the reason for this anomaly is that Paul’s assignment of 75 to `balance` is made under the assumption that the value of `balance` to be decremented is 100. That assumption, however, became invalid when Peter changed `balance` to 90. This is a catastrophic failure for the banking system, because the total amount of money in the system is not conserved. Before the transactions, the total amount of money was $100. Afterwards, Peter has $10, Paul has $25, and the bank has $75.[注164]

**校订前**

图3.29中的时序图描绘了一个事件顺序：`balance`从100开始，Peter取出10，Paul取出25，然而`balance`的最终值却是75。如图所示，这一异常现象的原因是，Paul将75赋值给`balance`时，假设要减去的`balance`的值是100。然而，当Peter将`balance`改为90时，这个假设就失效了。这对银行系统来说是一个灾难性的失败，因为系统中的总金额没有得到守恒。交易之前，总金额是$100。之后，Peter有$10，Paul有$25，银行有$75。[注164]

**校订后**

图3.29中的时序图描绘了一个事件顺序：`balance`从100开始，Peter取出10，Paul取出25，然而`balance`的最终值却是75。如图所示，这一异常现象的原因是，Paul将75赋值给`balance`时，假设将要减小的`balance`的值是100。然而，当Peter将`balance`改为90时，这个假设就失效了。这对银行系统来说是一个灾难性的失败，因为系统中的总金额没有得到守恒。交易之前，总金额是$100。之后，Peter有$10，Paul有$25，银行有$75。[注164]

### 3_002e4:0027

**原文**

List all the different possible values for `balance` after these three transactions have been completed, assuming that the banking system forces the three processes to run sequentially in some order.

**校订前**

列出这三个事务完成后 `balance` 所有不同的可能值，假设银行系统强制这三个进程按某种顺序顺序运行。

**校订后**

列出这三个事务完成后 `balance` 所有不同的可能值，假设银行系统强制这三个进程按某种次序依次运行。

### 3_002e4:0049

**原文**

Exercise 3.41: Ben Bitdiddle worries that it would be better to implement the bank account as follows (where the commented line has been changed):

**校订前**

习题 3.41： Ben Bitdiddle 担心，将银行账户实现如下会更好（其中注释行已被更改）：

**校订后**

习题 3.41： Ben Bitdiddle 担心，将银行账户实现如下会更好（其中带注释的那一行已被更改）：

### 3_002e4:0056

**原文**

This procedure works well when only a single process is trying to do the exchange. Suppose, however, that Peter and Paul both have access to accounts $a1$, $a2$, and $a3$, and that Peter exchanges $a1$ and $a2$ while Paul concurrently exchanges $a1$ and $a3$. Even with account deposits and withdrawals serialized for individual accounts (as in the `make-account` procedure shown above in this section), `exchange` can still produce incorrect results. For example, Peter might compute the difference in the balances for $a1$ and $a2$, but then Paul might change the balance in $a1$ before Peter is able to complete the exchange.[注170] For correct behavior, we must arrange for the `exchange` procedure to lock out any other concurrent accesses to the accounts during the entire time of the exchange.

**校订前**

当只有一个进程试图进行交换时，这个过程工作得很好。然而，假设 Peter 和 Paul 都能访问账户 $a1$、$a2$ 和 $a3$，并且 Peter 交换 $a1$ 和 $a2$，而 Paul 同时交换 $a1$ 和 $a3$。即使针对单个账户的存款和取款已经串行化（如本节前面展示的 `make-account` 过程那样），`exchange` 仍然可能产生不正确的结果。例如，Peter 可能计算了 $a1$ 和 $a2$ 的余额之差，但随后 Paul 可能在 Peter 能够完成交换之前改变了 $a1$ 中的余额。[注170] 为了行为正确，我们必须安排 `exchange` 过程在交换的整个期间锁定对账户的任何其他并发访问。

**校订后**

当只有一个进程试图进行交换时，这个过程工作得很好。然而，假设 Peter 和 Paul 都能访问账户 $a1$、$a2$ 和 $a3$，并且 Peter 交换 $a1$ 和 $a2$，而 Paul 同时交换 $a1$ 和 $a3$。即使针对单个账户的存款和取款已经串行化（如本节前面展示的 `make-account` 过程那样），`exchange` 仍然可能产生不正确的结果。例如，Peter 可能计算了 $a1$ 和 $a2$ 的余额之差，但随后 Paul 可能在 Peter 能够完成交换之前改变了 $a1$ 中的余额。[注170] 为了行为正确，我们必须安排 `exchange` 过程在交换的整个期间阻止对账户的任何其他并发访问。

### 3_002e4:0067

**原文**

We implement serializers in terms of a more primitive synchronization mechanism called a mutex. A mutex is an object that supports two operations—the mutex can be acquired, and the mutex can be released. Once a mutex has been acquired, no other acquire operations on that mutex may proceed until the mutex is released.[注172] In our implementation, each serializer has an associated mutex. Given a procedure `p`, the serializer returns a procedure that acquires the mutex, runs `p`, and then releases the mutex. This ensures that only one of the procedures produced by the serializer can be running at once, which is precisely the serialization property that we need to guarantee.

**校订前**

我们根据一种更原始的同步机制来实现串行化器，这种机制称为 互斥量。互斥量是一个支持两种操作的对象——互斥量可以被 获取，并且互斥量可以被 释放。一旦互斥量被获取，在该互斥量被释放之前，对该互斥量的任何其他获取操作都不能进行。[注172] 在我们的实现中，每个串行化器都有一个关联的互斥量。给定一个过程 `p`，串行化器返回一个过程，该过程获取互斥量，运行 `p`，然后释放互斥量。这确保了由该串行化器产生的过程中只有一个能同时运行，这正是我们需要保证的串行化性质。

**校订后**

我们根据一种更基本的同步机制来实现串行化器，这种机制称为 互斥量。互斥量是一个支持两种操作的对象——互斥量可以被 获取，并且互斥量可以被 释放。一旦互斥量被获取，在该互斥量被释放之前，对该互斥量的任何其他获取操作都不能进行。[注172] 在我们的实现中，每个串行化器都有一个关联的互斥量。给定一个过程 `p`，串行化器返回一个过程，该过程获取互斥量，运行 `p`，然后释放互斥量。这确保了由该串行化器产生的过程中只有一个能同时运行，这正是我们需要保证的串行化性质。

### 3_002e4:0071

**原文**

However, this implementation of `test-and-set!` does not suffice as it stands. There is a crucial subtlety here, which is the essential place where concurrency control enters the system: The `test-and-set!` operation must be performed atomically. That is, we must guarantee that, once a process has tested the cell and found it to be false, the cell contents will actually be set to true before any other process can test the cell. If we do not make this guarantee, then the mutex can fail in a way similar to the bank-account failure in Figure 3.29. (See Exercise 3.46.)

**校订前**

然而，这个`test-and-set!`的实现本身并不够用。这里有一个关键的微妙之处，这正是并发控制进入系统的关键所在：`test-and-set!`操作必须原子地执行。也就是说，我们必须保证，一旦某个进程测试了该单元并发现它为假，那么在任何其他进程能够测试该单元之前，该单元的内容实际上会被设置为真。如果我们不做出这个保证，那么互斥锁就可能以类似于图3.29中银行账户失败的方式失败。（参见习题3.46。）

**校订后**

然而，这个`test-and-set!`的实现本身并不够用。这里有一个关键的微妙之处，这正是并发控制进入系统的关键所在：`test-and-set!`操作必须原子地执行。也就是说，我们必须保证，一旦某个进程测试了该单元并发现它为假，那么在任何其他进程能够测试该单元之前，该单元的内容实际上会被设置为真。如果我们不做出这个保证，那么互斥量就可能以类似于图3.29中银行账户失败的方式失败。（参见习题3.46。）

### 3_002e4:0073

**原文**

Exercise 3.46: Suppose that we implement `test-and-set!` using an ordinary procedure as shown in the text, without attempting to make the operation atomic. Draw a timing diagram like the one in Figure 3.29 to demonstrate how the mutex implementation can fail by allowing two processes to acquire the mutex at the same time.

**校订前**

习题3.46：假设我们使用文本中所示的普通过程来实现`test-and-set!`，而不试图使该操作成为原子的。画一个类似于图3.29中的时序图，来演示互斥锁实现如何通过允许两个进程同时获取互斥锁而失败。

**校订后**

习题3.46：假设我们使用文本中所示的普通过程来实现`test-and-set!`，而不试图使该操作成为原子的。画一个类似于图3.29中的时序图，来演示互斥量实现如何通过允许两个进程同时获取互斥量而失败。

### 3_002e4:0074

**原文**

Exercise 3.47: A semaphore (of size $n$) is a generalization of a mutex. Like a mutex, a semaphore supports acquire and release operations, but it is more general in that up to $n$ processes can acquire it concurrently. Additional processes that attempt to acquire the semaphore must wait for release operations. Give implementations of semaphores

**校订前**

习题3.47：信号量（大小为$n$）是互斥锁的一种推广。与互斥锁一样，信号量支持获取和释放操作，但它更通用，因为最多可以有$n$个进程并发地获取它。试图获取信号量的额外进程必须等待释放操作。给出信号量的实现

**校订后**

习题3.47：信号量（大小为$n$）是互斥量的一种推广。与互斥量一样，信号量支持获取和释放操作，但它更通用，因为最多可以有$n$个进程并发地获取它。试图获取信号量的额外进程必须等待释放操作。给出信号量的实现

### 3_002e4:0075

**原文**

in terms of mutexes

**校订前**

基于互斥锁

**校订后**

基于互斥量

### 3_002e4:0098

**原文**

[注172] The term “mutex” is an abbreviation for mutual exclusion. The general problem of arranging a mechanism that permits concurrent processes to safely share resources is called the mutual exclusion problem. Our mutex is a simple variant of the semaphore mechanism (see Exercise 3.47), which was introduced in the “THE” Multiprogramming System developed at the Technological University of Eindhoven and named for the university’s initials in Dutch (Dijkstra 1968a). The acquire and release operations were originally called P and V, from the Dutch words passeren (to pass) and vrijgeven (to release), in reference to the semaphores used on railroad systems. Dijkstra’s classic exposition (1968b) was one of the first to clearly present the issues of concurrency control, and showed how to use semaphores to handle a variety of concurrency problems.

**校订前**

[注172]术语“mutex”是互斥的缩写。安排一种机制，使并发进程能够安全地共享资源，这个一般性问题称为互斥问题。我们的mutex是信号量机制的一个简单变体（见习题3.47），该机制是在埃因霍温技术大学开发的“THE”多道程序设计系统中引入的，并以该大学荷兰语名称的首字母命名（Dijkstra 1968a）。acquire和release操作最初被称为P和V，来自荷兰语单词passeren（通过）和vrijgeven（释放），指的是铁路系统中使用的信号量。Dijkstra的经典论述（1968b）是最早清晰阐述并发控制问题之一的著作，并展示了如何使用信号量来处理各种并发问题。

**校订后**

[注172]术语“mutex”是互斥的缩写。安排一种机制，使并发进程能够安全地共享资源，这个一般性问题称为互斥问题。我们的互斥量是信号量机制的一个简单变体（见习题3.47），该机制是在埃因霍温技术大学开发的“THE”多道程序设计系统中引入的，该系统以该大学荷兰语名称的首字母命名（Dijkstra 1968a）。获取和释放操作最初被称为P和V，来自荷兰语单词passeren（通过）和vrijgeven（释放），指的是铁路系统中使用的信号灯。Dijkstra的经典论述（1968b）是最早清晰阐述并发控制问题的著作之一，并展示了如何使用信号量来处理各种并发问题。

### 3_002e4:0099

**原文**

[注173] In most time-shared operating systems, processes that are blocked by a mutex do not waste time “busy-waiting” as above. Instead, the system schedules another process to run while the first is waiting, and the blocked process is awakened when the mutex becomes available.

**校订前**

[注173]在大多数分时操作系统中，被mutex阻塞的进程不会像上面那样浪费时间“忙等”。相反，系统会在第一个进程等待时调度另一个进程运行，当mutex变为可用时，被阻塞的进程会被唤醒。

**校订后**

[注173]在大多数分时操作系统中，被互斥量阻塞的进程不会像上面那样浪费时间“忙等”。相反，系统会在第一个进程等待时调度另一个进程运行，当互斥量变为可用时，被阻塞的进程会被唤醒。

### 3_002e4:0105

**原文**

[注178] This may seem like a strange point of view, but there are systems that work this way. International charges to credit-card accounts, for example, are normally cleared on a per-country basis, and the charges made in different countries are periodically reconciled. Thus the account balance may be different in different countries.

**校订前**

[注178]这看起来可能是一种奇怪的观点，但确实有系统是这样工作的。例如，信用卡账户的国际收费通常按国家分别结算，不同国家的收费会定期对账。因此，账户余额在不同国家可能不同。

**校订后**

[注178]这看起来可能是一种奇怪的观点，但确实有系统是这样工作的。例如，信用卡账户的跨国消费款项通常按国家分别结算，在不同国家发生的消费款项会定期对账。因此，账户余额在不同国家可能不同。

### 3_002e5:0006

**原文**

Is there another approach? Can we avoid identifying time in the computer with time in the modeled world? Must we make the model change with time in order to model phenomena in a changing world? Think about the issue in terms of mathematical functions. We can describe the time-varying behavior of a quantity $x$ as a function of time $x(t)$. If we concentrate on $x$ instant by instant, we think of it as a changing quantity. Yet if we concentrate on the entire time history of values, we do not emphasize change—the function itself does not change.[注180]

**校订前**

有没有另一种方法？我们能否避免将计算机中的时间与被建模世界中的时间等同起来？为了对变化世界中的现象建模，我们必须让模型随时间变化吗？从数学函数的角度来思考这个问题。我们可以将量$x$随时间变化的行为描述为时间$x(t)$的函数。如果我们一个瞬间一个瞬间地关注$x$，我们会把它看作一个变化的量。然而，如果我们关注值的整个时间历史，我们就不强调变化——函数本身并不改变。[注180]

**校订后**

有没有另一种方法？我们能否避免将计算机中的时间与被建模世界中的时间等同起来？为了对变化世界中的现象建模，我们必须让模型随时间变化吗？从数学函数的角度来思考这个问题。我们可以将量$x$随时间变化的行为描述为时间的函数$x(t)$。如果我们一个瞬间一个瞬间地关注$x$，我们会把它看作一个变化的量。然而，如果我们关注值的整个时间历史，我们就不强调变化——函数本身并不改变。[注180]

### 3_002e5:0018

**原文**

On the surface, streams are just lists with different names for the procedures that manipulate them. There is a constructor, `cons-stream`, and two selectors, `stream-car` and `stream-cdr`, which satisfy the constraints

**校订前**

从表面上看，流只不过是对操作它们的那些过程使用了不同名称的表。有一个构造器 `cons-stream`，以及两个选择器 `stream-car` 和 `stream-cdr`，它们满足以下约束

**校订后**

从表面上看，流只不过是对操作它们的那些过程使用了不同名称的表。有一个构造函数 `cons-stream`，以及两个选择函数 `stream-car` 和 `stream-cdr`，它们满足以下约束

### 3_002e5:0087

**原文**

Exercise 3.57: How many additions are performed when we compute the $n^(th)$ Fibonacci number using the definition of `fibs` based on the `add-streams` procedure? Show that the number of additions would be exponentially greater if we had implemented `(delay ⟨exp⟩)` simply as `(lambda () ⟨exp⟩)`, without using the optimization provided by the `memo-proc` procedure described in 3.5.1.[注192]

**校订前**

习题 3.57： 当我们使用基于 `add-streams` 过程的 `fibs` 定义来计算第 $n^(th)$ 个 Fibonacci 数时，会执行多少次加法？证明：如果我们把 `(delay ⟨exp⟩)` 简单地实现为 `(lambda () ⟨exp⟩)`，而不使用 3.5.1 中描述的 `memo-proc` 过程所提供的优化，那么加法的次数将呈指数级增长。[注192]

**校订后**

习题 3.57： 当我们使用基于 `add-streams` 过程的 `fibs` 定义来计算第 $n^(th)$ 个 斐波那契数时，会执行多少次加法？证明：如果我们把 `(delay ⟨exp⟩)` 简单地实现为 `(lambda () ⟨exp⟩)`，而不使用 3.5.1 中描述的 `memo-proc` 过程所提供的优化，那么加法的次数将呈指数级增长。[注192]

### 3_002e5:0090

**原文**

Exercise 3.59: In 2.5.3 we saw how to implement a polynomial arithmetic system representing polynomials as lists of terms. In a similar way, we can work with power series, such as $e^(x)=1+x+(1)/(2)x^(2)+(1)/(3⋅2)x^(3)+(1)/(4⋅3⋅2)x^(4)+…,cos⁡x=1−(1)/(2)x^(2)+(1)/(4⋅3⋅2)x^(4)−…,sin⁡x=x−(1)/(3⋅2)x^(3)+(1)/(5⋅4⋅3⋅2)x^(5)−…$ represented as infinite streams. We will represent the series $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ as the stream whose elements are the coefficients $a_{0}$, $a_{1}$, $a_{2}$, $a_{3}$, ….

**校订前**

习题 3.59： 在 2.5.3 中，我们看到了如何实现一个多项式算术系统，把多项式表示为项的列表。以类似的方式，我们可以处理 幂级数，例如 $e^(x)=1+x+(1)/(2)x^(2)+(1)/(3⋅2)x^(3)+(1)/(4⋅3⋅2)x^(4)+…,cos⁡x=1−(1)/(2)x^(2)+(1)/(4⋅3⋅2)x^(4)−…,sin⁡x=x−(1)/(3⋅2)x^(3)+(1)/(5⋅4⋅3⋅2)x^(5)−…$，把它们表示为无穷流。我们将把级数 $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ 表示为元素为系数 $a_{0}$、$a_{1}$、$a_{2}$、$a_{3}$、… 的流。

**校订后**

习题 3.59： 在 2.5.3 中，我们看到了如何实现一个多项式算术系统，把多项式表示为项的表。以类似的方式，我们可以处理 幂级数，例如 $e^(x)=1+x+(1)/(2)x^(2)+(1)/(3⋅2)x^(3)+(1)/(4⋅3⋅2)x^(4)+…,cos⁡x=1−(1)/(2)x^(2)+(1)/(4⋅3⋅2)x^(4)−…,sin⁡x=x−(1)/(3⋅2)x^(3)+(1)/(5⋅4⋅3⋅2)x^(5)−…$，把它们表示为无穷流。我们将把级数 $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ 表示为元素为系数 $a_{0}$、$a_{1}$、$a_{2}$、$a_{3}$、… 的流。

### 3_002e5:0091

**原文**

The integral of the series $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ is the series $c+a_{0}x+(1)/(2)a_{1}x^(2)+(1)/(3)a_{2}x^(3)+(1)/(4)a_{3}x^(4)+…,$ where $c$ is any constant. Define a procedure `integrate-series` that takes as input a stream $a_{0}$, $a_{1}$, $a_{2}$, … representing a power series and returns the stream $a_{0}$, $(1)/(2)a_{1}$, $(1)/(3)a_{2}$, … of coefficients of the non-constant terms of the integral of the series. (Since the result has no constant term, it doesn’t represent a power series; when we use `integrate-series`, we will `cons` on the appropriate constant.)

**校订前**

级数 $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ 的积分是级数 $c+a_{0}x+(1)/(2)a_{1}x^(2)+(1)/(3)a_{2}x^(3)+(1)/(4)a_{3}x^(4)+…,$，其中 $c$ 是任意常数。定义一个过程 `integrate-series`，它接受一个表示幂级数的流 $a_{0}$、$a_{1}$、$a_{2}$、… 作为输入，并返回该级数积分中非常数项的系数流 $a_{0}$、$(1)/(2)a_{1}$、$(1)/(3)a_{2}$、…。（由于结果没有常数项，它并不表示一个幂级数；当我们使用 `integrate-series` 时，我们将在适当的常数上使用 `cons`。）

**校订后**

级数 $a_{0}+a_{1}x+a_{2}x^(2)+a_{3}x^(3)+…$ 的积分是级数 $c+a_{0}x+(1)/(2)a_{1}x^(2)+(1)/(3)a_{2}x^(3)+(1)/(4)a_{3}x^(4)+…,$，其中 $c$ 是任意常数。定义一个过程 `integrate-series`，它接受一个表示幂级数的流 $a_{0}$、$a_{1}$、$a_{2}$、… 作为输入，并返回该级数积分中非常数项的系数流 $a_{0}$、$(1)/(2)a_{1}$、$(1)/(3)a_{2}$、…。（由于结果没有常数项，它并不表示一个幂级数；当我们使用 `integrate-series` 时，我们将使用 `cons` 把适当的常数添加到流的前端。）

### 3_002e5:0108

**原文**

One such accelerator, due to the eighteenth-century Swiss mathematician Leonhard Euler, works well with sequences that are partial sums of alternating series (series of terms with alternating signs). In Euler’s technique, if $S_{n}$ is the $n^(th)$ term of the original sum sequence, then the accelerated sequence has terms $S_{n+1}−((S_{n+1}−S_{n})^(2))/(S_{n−1}−2S_{n}+S_{n+1}).$ Thus, if the original sequence is represented as a stream of values, the transformed sequence is given by

**校订前**

其中一个这样的加速器，由十八世纪瑞士数学家 Leonhard Euler 提出，适用于交替级数（符号交替的项组成的级数）的部分和序列。在 Euler 的技术中，如果$S_{n}$是原始和序列的第$n^(th)$项，那么加速后的序列的项为$S_{n+1}−((S_{n+1}−S_{n})^(2))/(S_{n−1}−2S_{n}+S_{n+1}).$因此，如果原始序列表示为值的流，则变换后的序列由下式给出

**校订后**

其中一个这样的加速器，由十八世纪瑞士数学家 Leonhard Euler 提出，适用于交错级数（符号交替的项组成的级数）的部分和序列。在 Euler 的技术中，如果$S_{n}$是原始和序列的第$n^(th)$项，那么加速后的序列的项为$S_{n+1}−((S_{n+1}−S_{n})^(2))/(S_{n−1}−2S_{n}+S_{n+1}).$因此，如果原始序表示为值的流，则变换后的序列由下式给出

### 3_002e5:0119

**原文**

Infinite streams of pairs

**校订前**

无限的序对流

**校订后**

无穷序对流

### 3_002e5:0120

**原文**

In 2.2.3, we saw how the sequence paradigm handles traditional nested loops as processes defined on sequences of pairs. If we generalize this technique to infinite streams, then we can write programs that are not easily represented as loops, because the “looping” must range over an infinite set.

**校订前**

在2.2.3中，我们看到了序列范式如何将传统的嵌套循环处理为定义在序对序列上的计算过程。如果我们将这种技术推广到无限流，那么我们就可以编写那些不容易表示为循环的程序，因为“循环”必须在一个无限集上遍历。

**校订后**

在2.2.3中，我们看到了序列范式如何将传统的嵌套循环处理为定义在序对序列上的计算过程。如果我们将这种技术推广到无穷流，那么我们就可以编写那些不容易表示为循环的程序，因为“循环”必须在一个无限集上遍历。

### 3_002e5:0125

**原文**

In order to complete the procedure, we must choose some way to combine the two inner streams. One idea is to use the stream analog of the `append` procedure from 2.2.1:

**校订前**

为了完成这个过程，我们必须选择某种方式来组合两个内部流。一个想法是使用2.2.1中`append`过程的流模拟：

**校订后**

为了完成这个过程，我们必须选择某种方式来组合两个内部流。一个想法是使用2.2.1中`append`过程的流版本：

### 3_002e5:0126

**原文**

This is unsuitable for infinite streams, however, because it takes all the elements from the first stream before incorporating the second stream. In particular, if we try to generate all pairs of positive integers using

**校订前**

然而，这对于无限流是不合适的，因为它在合并第二个流之前取走了第一个流的所有元素。特别是，如果我们尝试使用以下方式生成所有正整数序对

**校订后**

然而，这对于无穷流是不合适的，因为它在合并第二个流之前取走了第一个流的所有元素。特别是，如果我们尝试使用以下方式生成所有正整数序对

### 3_002e5:0128

**原文**

To handle infinite streams, we need to devise an order of combination that ensures that every element will eventually be reached if we let our program run long enough. An elegant way to accomplish this is with the following `interleave` procedure:[注196]

**校订前**

为了处理无限流，我们需要设计一种组合顺序，确保如果我们让程序运行足够长的时间，每个元素最终都会被到达。实现这一点的一种优雅方式是使用以下`interleave`过程：[注196]

**校订后**

为了处理无穷流，我们需要设计一种组合顺序，确保如果我们让程序运行足够长的时间，每个元素最终都会被到达。实现这一点的一种优雅方式是使用以下`interleave`过程：[注196]

### 3_002e5:0152

**原文**

Exercise 3.75: Unfortunately, Alyssa’s zero-crossing detector in Exercise 3.74 proves to be insufficient, because the noisy signal from the sensor leads to spurious zero crossings. Lem E. Tweakit, a hardware specialist, suggests that Alyssa smooth the signal to filter out the noise before extracting the zero crossings. Alyssa takes his advice and decides to extract the zero crossings from the signal constructed by averaging each value of the sense data with the previous value. She explains the problem to her assistant, Louis Reasoner, who attempts to implement the idea, altering Alyssa’s program as follows:

**校订前**

习题3.75：不幸的是，习题3.74中Alyssa的过零检测器被证明是不够的，因为来自传感器的噪声信号导致虚假的过零点。硬件专家Lem E. Tweakit建议Alyssa在提取过零点之前平滑信号以滤除噪声。Alyssa接受了他的建议，决定从通过将每个感测数据值与前一个值平均而构造的信号中提取过零点。她向助手Louis Reasoner解释了这个问题，后者试图实现这个想法，将Alyssa的程序修改如下：

**校订后**

习题3.75：不幸的是，习题3.74中Alyssa的过零检测器被证明是不够的，因为来自传感器的含噪信号导致虚假的过零点。硬件专家Lem E. Tweakit建议Alyssa在提取过零点之前平滑信号以滤除噪声。Alyssa接受了他的建议，决定从通过将每个感测数据值与前一个值平均而构造的信号中提取过零点。她向助手Louis Reasoner解释了这个问题，后者试图实现这个想法，将Alyssa的程序修改如下：

### 3_002e5:0176

**原文**

The examples in this section illustrate how the explicit use of `delay` and `force` provides great programming flexibility, but the same examples also show how this can make our programs more complex. Our new `integral` procedure, for instance, gives us the power to model systems with loops, but we must now remember that `integral` should be called with a delayed integrand, and every procedure that uses `integral` must be aware of this. In effect, we have created two classes of procedures: ordinary procedures and procedures that take delayed arguments. In general, creating separate classes of procedures forces us to create separate classes of higher-order procedures as well.[注200]

**校订前**

本节中的例子说明了显式使用`delay`和`force`如何提供了极大的编程灵活性，但同样的例子也表明这如何使我们的程序更加复杂。例如，我们新的`integral`过程赋予我们建模带循环系统的能力，但我们现在必须记住`integral`应该用延迟的被积函数来调用，并且每个使用`integral`的过程都必须意识到这一点。实际上，我们创建了两类过程：普通过程和接受延迟参数的过程。一般来说，创建单独的过程类别迫使我们也要创建单独的高阶过程类别。[注200]

**校订后**

本节中的例子说明了显式使用`delay`和`force`如何提供了极大的编程灵活性，但同样的例子也表明这如何使我们的程序更加复杂。例如，我们新的`integral`过程赋予我们建模带回路的系统的能力，但我们现在必须记住`integral`应该用延迟的被积函数来调用，并且每个使用`integral`的过程都必须意识到这一点。实际上，我们创建了两类过程：普通过程和接受延迟参数的过程。一般来说，创建单独的过程类别迫使我们也要创建单独的高阶过程类别。[注200]

### 3_002e5:0177

**原文**

One way to avoid the need for two different classes of procedures is to make all procedures take delayed arguments. We could adopt a model of evaluation in which all arguments to procedures are automatically delayed and arguments are forced only when they are actually needed (for example, when they are required by a primitive operation). This would transform our language to use normal-order evaluation, which we first described when we introduced the substitution model for evaluation in 1.1.5. Converting to normal-order evaluation provides a uniform and elegant way to simplify the use of delayed evaluation, and this would be a natural strategy to adopt if we were concerned only with stream processing. In 4.2, after we have studied the evaluator, we will see how to transform our language in just this way. Unfortunately, including delays in procedure calls wreaks havoc with our ability to design programs that depend on the order of events, such as programs that use assignment, mutate data, or perform input or output. Even the single `delay` in `cons-stream` can cause great confusion, as illustrated by Exercise 3.51 and Exercise 3.52. As far as anyone knows, mutability and delayed evaluation do not mix well in programming languages, and devising ways to deal with both of these at once is an active area of research.

**校订前**

避免需要两类不同过程的一种方法是让所有过程都接受延迟参数。我们可以采用一种求值模型，其中过程的所有参数都自动延迟，只有在实际需要时才强制参数（例如，当基本操作需要它们时）。这会将我们的语言转变为使用正则序求值，我们在1.1.5中引入求值的代换模型时首次描述了它。转换为正则序求值提供了一种统一而优雅的方式来简化延迟求值的使用，如果我们只关心流处理，这将是一种自然采用的策略。在4.2中，在我们研究了求值器之后，我们将看到如何以这种方式转换我们的语言。不幸的是，在过程调用中包含延迟会严重破坏我们设计依赖于事件顺序的程序的能力，例如使用赋值、变异数据或执行输入或输出的程序。甚至`cons-stream`中的单个`delay`也会引起极大的混乱，如习题3.51和习题3.52所示。据大家所知，可变性和延迟求值在编程语言中不能很好地混合，设计同时处理这两者的方法是一个活跃的研究领域。

**校订后**

避免需要两类不同过程的一种方法是让所有过程都接受延迟参数。我们可以采用一种求值模型，其中过程的所有参数都自动延迟，只有在实际需要时才强制参数（例如，当基本操作需要它们时）。这会将我们的语言转变为使用正则序求值，我们在1.1.5中引入求值的代换模型时首次描述了它。转换为正则序求值提供了一种统一而优雅的方式来简化延迟求值的使用，如果我们只关心流处理，这将是一种自然采用的策略。在4.2中，在我们研究了求值器之后，我们将看到如何以这种方式转换我们的语言。不幸的是，在过程调用中包含延迟会严重破坏我们设计依赖于事件顺序的程序的能力，例如使用赋值、修改数据或执行输入或输出的程序。甚至`cons-stream`中的单个`delay`也会引起极大的混乱，如习题3.51和习题3.52所示。据大家所知，可变性和延迟求值在编程语言中不能很好地混合，设计同时处理这两者的方法是一个活跃的研究领域。

### 3_002e5:0186

**原文**

Exercise 3.82: Redo Exercise 3.5 on Monte Carlo integration in terms of streams. The stream version of `estimate-integral` will not have an argument telling how many trials to perform. Instead, it will produce a stream of estimates based on successively more trials.

**校订前**

习题3.82：用流重新做习题3.5中关于蒙特卡罗积分的内容。`estimate-integral`的流版本将不会有一个参数告诉要进行多少次试验。相反，它将基于越来越多的试验产生一个估计值的流。

**校订后**

习题3.82：用流重新做习题3.5中关于蒙特卡洛积分的内容。`estimate-integral`的流版本将不会有一个参数告诉要进行多少次试验。相反，它将基于越来越多的试验产生一个估计值的流。

### 3_002e5:0197

**原文**

On the other hand, if we look closely, we can see time-related problems creeping into functional models as well. One particularly troublesome area arises when we wish to design interactive systems, especially ones that model interactions between independent entities. For instance, consider once more the implementation of a banking system that permits joint bank accounts. In a conventional system using assignment and objects, we would model the fact that Peter and Paul share an account by having both Peter and Paul send their transaction requests to the same bank-account object, as we saw in 3.1.3. From the stream point of view, where there are no “objects” per se, we have already indicated that a bank account can be modeled as a process that operates on a stream of transaction requests to produce a stream of responses. Accordingly, we could model the fact that Peter and Paul have a joint bank account by merging Peter’s stream of transaction requests with Paul’s stream of requests and feeding the result to the bank-account stream process, as shown in Figure 3.38.

**校订前**

另一方面，如果我们仔细观察，我们可以看到与时间相关的问题也悄悄进入函数式模型。一个特别麻烦的领域出现在我们希望设计交互式系统时，特别是那些模拟独立实体之间交互的系统。例如，再次考虑允许联合银行账户的银行系统的实现。在使用赋值和对象的传统系统中，我们将通过让Peter和Paul将他们的交易请求发送到同一个银行账户对象来模拟Peter和Paul共享账户的事实，正如我们在3.1.3中看到的。从流的观点来看，没有“对象”本身，我们已经指出银行账户可以建模为对交易请求流进行操作以产生响应流的过程。因此，我们可以通过将Peter的交易请求流与Paul的请求流合并，并将结果馈送到银行账户流过程来模拟Peter和Paul拥有联合银行账户的事实，如图3.38所示。

**校订后**

另一方面，如果我们仔细观察，我们可以看到与时间相关的问题也悄悄进入函数式模型。一个特别麻烦的领域出现在我们希望设计交互式系统时，特别是那些模拟独立实体之间交互的系统。例如，再次考虑允许联名银行账户的银行系统的实现。在使用赋值和对象的传统系统中，我们将通过让Peter和Paul将他们的交易请求发送到同一个银行账户对象来模拟Peter和Paul共享账户的事实，正如我们在3.1.3中看到的。从流的观点来看，没有“对象”本身，我们已经指出银行账户可以建模为对交易请求流进行操作以产生响应流的过程。因此，我们可以通过将Peter的交易请求流与Paul的请求流合并，并将结果馈送到银行账户流过程来模拟Peter和Paul拥有联名银行账户的事实，如图3.38所示。

### 3_002e5:0198

**原文**

Figure 3.38: A joint bank account, modeled by merging two streams of transaction requests.

**校订前**

图3.38：通过合并两个交易请求流来建模的联合银行账户。

**校订后**

图3.38：通过合并两个交易请求流来建模的联名银行账户。

### 3_002e5:0199

**原文**

The trouble with this formulation is in the notion of merge. It will not do to merge the two streams by simply taking alternately one request from Peter and one request from Paul. Suppose Paul accesses the account only very rarely. We could hardly force Peter to wait for Paul to access the account before he could issue a second transaction. However such a merge is implemented, it must interleave the two transaction streams in some way that is constrained by “real time” as perceived by Peter and Paul, in the sense that, if Peter and Paul meet, they can agree that certain transactions were processed before the meeting, and other transactions were processed after the meeting.[注203] This is precisely the same constraint that we had to deal with in 3.4.1, where we found the need to introduce explicit synchronization to ensure a “correct” order of events in concurrent processing of objects with state. Thus, in an attempt to support the functional style, the need to merge inputs from different agents reintroduces the same problems that the functional style was meant to eliminate.

**校订前**

这种表述的问题在于合并的概念。通过简单地交替从Peter取一个请求和从Paul取一个请求来合并两个流是不行的。假设Paul极少访问账户。我们几乎不能强迫Peter等待Paul访问账户之后才能发出第二笔交易。无论这种合并如何实现，它都必须以某种方式交错两个交易流，这种方式受到Peter和Paul所感知的“实时”的约束，即如果Peter和Paul见面，他们可以同意某些交易在见面之前处理，其他交易在见面之后处理。[注203]这正是我们在3.4.1中必须处理的相同约束，在那里我们发现需要引入显式同步来确保具有状态的对象并发处理中事件的“正确”顺序。因此，在试图支持函数式风格时，合并来自不同代理的输入的需要重新引入了函数式风格本来要消除的相同问题。

**校订后**

这种表述的问题在于合并的概念。通过简单地交替从Peter取一个请求和从Paul取一个请求来合并两个流是不行的。假设Paul极少访问账户。我们几乎不能强迫Peter等待Paul访问账户之后才能发出第二笔交易。无论这种合并如何实现，它都必须以某种方式交错两个交易流，这种方式受到Peter和Paul所感知的“实际时间”的约束，即如果Peter和Paul见面，他们可以同意某些交易在见面之前处理，其他交易在见面之后处理。[注203]这正是我们在3.4.1中必须处理的相同约束，在那里我们发现需要引入显式同步来确保具有状态的对象并发处理中事件的“正确”顺序。因此，在试图支持函数式风格时，合并来自不同代理的输入的需要重新引入了函数式风格本来要消除的相同问题。

### 3_002e5:0200

**原文**

We began this chapter with the goal of building computational models whose structure matches our perception of the real world we are trying to model. We can model the world as a collection of separate, time-bound, interacting objects with state, or we can model the world as a single, timeless, stateless unity. Each view has powerful advantages, but neither view alone is completely satisfactory. A grand unification has yet to emerge.[注204]

**校订前**

我们以构建计算模型为目标开始了本章，这些模型的结构与我们试图建模的现实世界的感知相匹配。我们可以将世界建模为一组分离的、有时限的、具有状态的交互对象，或者我们可以将世界建模为一个单一的、无时限的、无状态的统一体。每种观点都有强大的优势，但单独任何一种观点都不完全令人满意。一个宏大的统一尚未出现。[注204]

**校订后**

我们以构建计算模型为目标开始了本章，这些模型的结构与我们试图建模的现实世界的感知相匹配。我们可以将世界建模为一组分离的、受时间约束的、具有状态的交互对象，或者我们可以将世界建模为一个单一的、无时间性的、无状态的统一体。每种观点都有强大的优势，但单独任何一种观点都不完全令人满意。一个宏大的统一尚未出现。[注204]

### 3_002e5:0210

**原文**

[注188] Eratosthenes, a third-century B.C. Alexandrian Greek philosopher, is famous for giving the first accurate estimate of the circumference of the Earth, which he computed by observing shadows cast at noon on the day of the summer solstice. Eratosthenes’s sieve method, although ancient, has formed the basis for special-purpose hardware “sieves” that, until recently, were the most powerful tools in existence for locating large primes. Since the 70s, however, these methods have been superseded by outgrowths of the probabilistic techniques discussed in 1.2.6.

**校订前**

[注188]埃拉托斯特尼，公元前三世纪的B.C.亚历山大希腊哲学家，以首次准确估计地球周长而闻名，他通过观察夏至日正午投下的阴影来计算。埃拉托斯特尼的筛法，尽管古老，却构成了专用硬件“筛”的基础，直到最近，这些硬件是定位大素数的最强大工具。然而，自70年代以来，这些方法已被1.2.6中讨论的概率技术的衍生物所取代。

**校订后**

[注188]埃拉托斯特尼，公元前三世纪亚历山大里亚的希腊哲学家，以首次准确估计地球周长而闻名，他通过观察夏至日正午投下的阴影来计算。埃拉托斯特尼的筛法，尽管古老，却构成了专用硬件“筛”的基础，直到最近，这些硬件是定位大素数的最强大工具。然而，自70年代以来，这些方法已被1.2.6中讨论的概率技术的衍生物所取代。

### 3_002e5:0220

**原文**

[注198] To quote from G. H. Hardy’s obituary of Ramanujan (Hardy 1921): “It was Mr. Littlewood (I believe) who remarked that ‘every positive integer was one of his friends.’ I remember once going to see him when he was lying ill at Putney. I had ridden in taxi-cab No. 1729, and remarked that the number seemed to me a rather dull one, and that I hoped it was not an unfavorable omen. ‘No,’ he replied, ‘it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways.’ ” The trick of using weighted pairs to generate the Ramanujan numbers was shown to us by Charles Leiserson.

**校订前**

[注198]引用G. H. Hardy为Ramanujan所写的讣告（Hardy 1921）中的话：“是Littlewood先生（我相信）评论说‘每个正整数都是他的朋友之一。’我记得有一次去看他，当时他病倒在Putney。我乘坐了1729号出租车，并评论说这个数字对我来说似乎相当乏味，我希望这不是一个不祥之兆。‘不，’他回答说，‘这是一个非常有趣的数字；它是可以用两种不同方式表示为两个立方数之和的最小数。’”使用加权序对来生成Ramanujan数的技巧是由Charles Leiserson展示给我们的。

**校订后**

[注198]引用G. H. Hardy为Ramanujan所写的讣告（Hardy 1921）中的话：“是Littlewood先生（我相信）评论说‘每个正整数都是他的朋友之一。’我记得有一次去看他，当时他病倒在Putney。我乘坐了1729号出租车，并评论说这个数字对我来说似乎相当乏味，我希望这不是一个不祥之兆。‘不，’他回答说，‘这是一个非常有趣的数字；它是可以用两种不同方式表示为两个立方数之和的最小数。’”使用加权序对来生成拉马努金数的技巧是由Charles Leiserson展示给我们的。

### 4_002e1:0021

**原文**

An `if` expression requires special processing of its parts, so as to evaluate the consequent if the predicate is true, and otherwise to evaluate the alternative.

**校订前**

`if` 表达式需要对其各部分进行特殊处理，以便在谓词为真时求值推论，否则求值替代。

**校订后**

`if` 表达式需要对其各部分进行特殊处理，以便在谓词为真时求值结果表达式，否则求值替代表达式。

### 4_002e1:0032

**原文**

When `eval` processes a procedure application, it uses `list-of-values` to produce the list of arguments to which the procedure is to be applied. `List-of-values` takes as an argument the operands of the combination. It evaluates each operand and returns a list of the corresponding values:[注209]

**校订前**

当`eval`处理一个过程应用时，它使用`list-of-values`来生成该过程将被应用到的参数表。`List-of-values`以一个组合式的操作数作为参数。它对每个操作数求值，并返回相应值的表：[注209]

**校订后**

当`eval`处理一个过程应用时，它使用`list-of-values`来生成该过程将被应用到的参数表。`List-of-values`以一个组合式的运算对象作为参数。它对每个运算对象求值，并返回相应值的表：[注209]

### 4_002e1:0034

**原文**

`Eval-if` evaluates the predicate part of an `if` expression in the given environment. If the result is true, `eval-if` evaluates the consequent, otherwise it evaluates the alternative:

**校订前**

`Eval-if`在给定环境中对一个`if`表达式的谓词部分求值。如果结果为真，`eval-if`对推论部分求值，否则它对替代部分求值：

**校订后**

`Eval-if`在给定环境中对一个`if`表达式的谓词部分求值。如果结果为真，`eval-if`对结果表达式求值，否则它对替代表达式求值：

### 4_002e1:0042

**原文**

Exercise 4.1: Notice that we cannot tell whether the metacircular evaluator evaluates operands from left to right or from right to left. Its evaluation order is inherited from the underlying Lisp: If the arguments to `cons` in `list-of-values` are evaluated from left to right, then `list-of-values` will evaluate operands from left to right; and if the arguments to `cons` are evaluated from right to left, then `list-of-values` will evaluate operands from right to left.

**校订前**

习题4.1：注意，我们无法判断元循环求值器是从左到右还是从右到左对操作数求值。它的求值顺序继承自底层 Lisp：如果`list-of-values`中`cons`的参数是从左到右求值的，那么`list-of-values`将从左到右对操作数求值；而如果`cons`的参数是从右到左求值的，那么`list-of-values`将从右到左对操作数求值。

**校订后**

习题4.1：注意，我们无法判断元循环求值器是从左到右还是从右到左对运算对象求值。它的求值顺序继承自底层 Lisp：如果`list-of-values`中`cons`的参数是从左到右求值的，那么`list-of-values`将从左到右对运算对象求值；而如果`cons`的参数是从右到左求值的，那么`list-of-values`将从右到左对运算对象求值。

### 4_002e1:0043

**原文**

Write a version of `list-of-values` that evaluates operands from left to right regardless of the order of evaluation in the underlying Lisp. Also write a version of `list-of-values` that evaluates operands from right to left.

**校订前**

编写一个`list-of-values`的版本，无论底层 Lisp 的求值顺序如何，都从左到右对操作数求值。再编写一个`list-of-values`的版本，从右到左对操作数求值。

**校订后**

编写一个`list-of-values`的版本，无论底层 Lisp 的求值顺序如何，都从左到右对运算对象求值。再编写一个`list-of-values`的版本，从右到左对运算对象求值。

### 4_002e1:0045

**原文**

The evaluator is reminiscent of the symbolic differentiation program discussed in 2.3.2. Both programs operate on symbolic expressions. In both programs, the result of operating on a compound expression is determined by operating recursively on the pieces of the expression and combining the results in a way that depends on the type of the expression. In both programs we used data abstraction to decouple the general rules of operation from the details of how expressions are represented. In the differentiation program this meant that the same differentiation procedure could deal with algebraic expressions in prefix form, in infix form, or in some other form. For the evaluator, this means that the syntax of the language being evaluated is determined solely by the procedures that classify and extract pieces of expressions.

**校订前**

这个求值器让人想起2.3.2中讨论的符号求导程序。两个程序都操作符号表达式。在两个程序中，对一个复合表达式操作的结果都是通过对表达式的各个部分递归地操作，并以一种取决于表达式类型的方式组合结果来确定的。在两个程序中，我们都使用了数据抽象，将操作的一般规则与表达式如何表示的细节解耦。在求导程序中，这意味着同一个求导过程可以处理前缀形式、中缀形式或某种其他形式的代数表达式。对于求值器，这意味着被求值语言的语法完全由对表达式各部分进行分类和提取的过程决定。

**校订后**

这个求值器让人想起2.3.2中讨论的符号求导程序。两个程序都运算符号表达式。在两个程序中，对一个复合表达式操作的结果都是通过对表达式的各个部分递归地操作，并以一种取决于表达式类型的方式组合结果来确定的。在两个程序中，我们都使用了数据抽象，将操作的一般规则与表达式如何表示的细节解耦。在求导程序中，这意味着同一个求导过程可以处理前缀形式、中缀形式或某种其他形式的代数表达式。对于求值器，这意味着被求值语言的语法完全由对表达式各部分进行分类和提取的过程决定。

### 4_002e1:0057

**原文**

We also provide a constructor for `lambda` expressions, which is used by `definition-value`, above:

**校订前**

我们还为`lambda`表达式提供了一个构造器，它被上面的`definition-value`使用：

**校订后**

我们还为`lambda`表达式提供了一个构造函数，它被上面的`definition-value`使用：

### 4_002e1:0058

**原文**

Conditionals begin with `if` and have a predicate, a consequent, and an (optional) alternative. If the expression has no alternative part, we provide `false` as the alternative.[注214]

**校订前**

条件式以`if`开头，并有一个谓词、一个推论部分和一个（可选的）替代部分。如果表达式没有替代部分，我们提供`false`作为替代部分。[注214]

**校订后**

条件式以`if`开头，并有一个谓词、一个结果表达式和一个（可选的）替代表达式。如果表达式没有替代表达式，我们提供`false`作为替代表达式。[注214]

### 4_002e1:0059

**原文**

We also provide a constructor for `if` expressions, to be used by `cond->if` to transform `cond` expressions into `if` expressions:

**校订前**

我们还为`if`表达式提供了一个构造器，供`cond->if`用来将`cond`表达式转换为`if`表达式：

**校订后**

我们还为`if`表达式提供了一个构造函数，供`cond->if`用来将`cond`表达式转换为`if`表达式：

### 4_002e1:0060

**原文**

`Begin` packages a sequence of expressions into a single expression. We include syntax operations on `begin` expressions to extract the actual sequence from the `begin` expression, as well as selectors that return the first expression and the rest of the expressions in the sequence.[注215]

**校订前**

`Begin`将表达式序列打包成单个表达式。我们包括对`begin`表达式的语法操作，以从`begin`表达式中提取实际的序列，以及返回序列中第一个表达式和其余表达式的选择器。[注215]

**校订后**

`Begin`将表达式序列打包成单个表达式。我们包括对`begin`表达式的语法操作，以从`begin`表达式中提取实际的序列，以及返回序列中第一个表达式和其余表达式的选择函数。[注215]

### 4_002e1:0061

**原文**

We also include a constructor `sequence->exp` (for use by `cond->if`) that transforms a sequence into a single expression, using `begin` if necessary:

**校订前**

我们还包括一个构造器`sequence->exp`（供`cond->if`使用），它在必要时使用`begin`将一个序列转换为单个表达式：

**校订后**

我们还包括一个构造函数`sequence->exp`（供`cond->if`使用），它在必要时使用`begin`将一个序列转换为单个表达式：

### 4_002e1:0062

**原文**

A procedure application is any compound expression that is not one of the above expression types. The `car` of the expression is the operator, and the `cdr` is the list of operands:

**校订前**

过程应用是任何不属于上述表达式类型的复合表达式。表达式的`car`是操作符，而`cdr`是操作数表：

**校订后**

过程应用是任何不属于上述表达式类型的复合表达式。表达式的`car`是运算符，而`cdr`是运算对象表：

### 4_002e1:0086

**原文**

The `⟨``bindings``⟩` and `⟨``body``⟩` are just as in ordinary `let`, except that `⟨``var``⟩` is bound within `⟨``body``⟩` to a procedure whose body is `⟨``body``⟩` and whose parameters are the variables in the `⟨``bindings``⟩`. Thus, one can repeatedly execute the `⟨``body``⟩` by invoking the procedure named `⟨``var``⟩`. For example, the iterative Fibonacci procedure (1.2.2) can be rewritten using named `let` as follows:

**校订前**

`⟨``bindings``⟩`和`⟨``body``⟩`与普通`let`中一样，不同之处在于`⟨``var``⟩`在`⟨``body``⟩`内被绑定到一个过程，该过程的主体是`⟨``body``⟩`，参数是`⟨``bindings``⟩`中的变量。因此，可以通过调用名为`⟨``var``⟩`的过程来重复执行`⟨``body``⟩`。例如，迭代 Fibonacci 过程（1.2.2）可以使用命名`let`重写如下：

**校订后**

`⟨``bindings``⟩`和`⟨``body``⟩`与普通`let`中一样，不同之处在于`⟨``var``⟩`在`⟨``body``⟩`内被绑定到一个过程，该过程的主体是`⟨``body``⟩`，参数是`⟨``bindings``⟩`中的变量。因此，可以通过调用名为`⟨``var``⟩`的过程来重复执行`⟨``body``⟩`。例如，迭代 斐波那契 过程（1.2.2）可以使用命名`let`重写如下：

### 4_002e1:0099

**原文**

Compound procedures are constructed from parameters, procedure bodies, and environments using the constructor `make-procedure`:

**校订前**

复合过程由参数、过程体和环境使用构造器 `make-procedure` 构造而成：

**校订后**

复合过程由形参、过程体和环境使用构造函数 `make-procedure` 构造而成：

### 4_002e1:0112

**原文**

The method described here is only one of many plausible ways to represent environments. Since we used data abstraction to isolate the rest of the evaluator from the detailed choice of representation, we could change the environment representation if we wanted to. (See Exercise 4.11.) In a production-quality Lisp system, the speed of the evaluator’s environment operations—especially that of variable lookup—has a major impact on the performance of the system. The representation described here, although conceptually simple, is not efficient and would not ordinarily be used in a production system.[注219]

**校订前**

这里描述的方法只是表示环境的许多可行方式之一。由于我们使用数据抽象将求值器的其余部分与表示的具体选择隔离开来，因此如果需要，我们可以更改环境的表示。（参见 习题 4.11。）在生产质量的 Lisp 系统中，求值器环境操作的速度——尤其是变量查找的速度——对系统的性能有重大影响。这里描述的表示虽然概念上简单，但效率不高，通常不会在生产系统中使用。[注219]

**校订后**

这里描述的方法只是表示环境的许多可行方式之一。由于我们使用数据抽象将求值器的其余部分与表示的具体选择隔离开来，因此如果需要，我们可以更改环境的表示。（参见 习题 4.11。）在达到实际应用质量要求的 Lisp 系统中，求值器环境操作的速度——尤其是变量查找的速度——对系统的性能有重大影响。这里描述的表示虽然概念上简单，但效率不高，通常不会在生产系统中使用。[注219]

### 4_002e1:0133

**原文**

From this perspective, our evaluator is seen to be a universal machine. It mimics other machines when these are described as Lisp programs.[注223] This is striking. Try to imagine an analogous evaluator for electrical circuits. This would be a circuit that takes as input a signal encoding the plans for some other circuit, such as a filter. Given this input, the circuit evaluator would then behave like a filter with the same description. Such a universal electrical circuit is almost unimaginably complex. It is remarkable that the program evaluator is a rather simple program.[注224]

**校订前**

从这个角度来看，我们的求值器被视为一台 通用机器。当其他机器被描述为 Lisp 程序时，它模拟这些机器。[注223] 这是惊人的。试着想象一个类似的电路求值器。这将是一个电路，它接受一个编码了某个其他电路（例如滤波器）的计划的信号作为输入。给定这个输入，电路求值器将表现得像一个具有相同描述的滤波器。这样一个通用的电路几乎难以想象地复杂。值得注意的是，程序求值器是一个相当简单的程序。[注224]

**校订后**

从这个角度来看，我们的求值器被视为一台 通用机器。当其他机器被描述为 Lisp 程序时，它模拟这些机器。[注223] 这是惊人的。试着想象一个类似的电路求值器。这将是一个电路，它接受一个编码了某个其他电路（例如滤波器）的设计方案的信号作为输入。给定这个输入，电路求值器将表现得像一个具有相同描述的滤波器。这样一个通用的电路几乎难以想象地复杂。值得注意的是，程序求值器是一个相当简单的程序。[注224]

### 4_002e1:0157

**原文**

Exercise 4.19: Ben Bitdiddle, Alyssa P. Hacker, and Eva Lu Ator are arguing about the desired result of evaluating the expression

**校订前**

习题4.19：Ben Bitdiddle、Alyssa P. Hacker和Eva Lu Ator正在争论求值表达式

**校订后**

习题4.19：Ben Bitdiddle、Alyssa P. Hacker和Eva Lu Ator正在争论以下表达式应有的求值结果

### 4_002e1:0165

**原文**

Check (by evaluating the expression) that this really does compute factorials. Devise an analogous expression for computing Fibonacci numbers.

**校订前**

通过求值该表达式来检查它确实计算了阶乘。设计一个类似的表达式来计算 Fibonacci 数。

**校订后**

通过求值该表达式来检查它确实计算了阶乘。设计一个类似的表达式来计算 斐波那契数。

### 4_002e1:0178

**原文**

For `if` expressions, we extract and analyze the predicate, consequent, and alternative at analysis time.

**校订前**

对于 `if` 表达式，我们在分析时提取并分析谓词、推论和替代。

**校订后**

对于 `if` 表达式，我们在分析时提取并分析谓词、结果表达式和替代表达式。

### 4_002e1:0196

**原文**

[注210] In this case, the language being implemented and the implementation language are the same. Contemplation of the meaning of `true?` here yields expansion of consciousness without the abuse of substance.

**校订前**

[注210] 在这种情况下，被实现的语言和实现语言是相同的。在此处思考 `true?` 的含义会带来意识的扩展，而不会滥用物质。

**校订后**

[注210] 在这种情况下，被实现的语言和实现语言是相同的。在此处思考 `true?` 的含义会带来意识的扩展，而无需滥用药物。

### 4_002e1:0200

**原文**

[注214] The value of an `if` expression when the predicate is false and there is no alternative is unspecified in Scheme; we have chosen here to make it false. We will support the use of the variables `true` and `false` in expressions to be evaluated by binding them in the global environment. See 4.1.4.

**校订前**

[注214] 当谓词为假且没有替代项时，`if` 表达式的值在 Scheme 中是未指定的；我们在这里选择使其为假。我们将通过在全局环境中绑定变量 `true` 和 `false` 来支持在待求值表达式中使用它们。参见 4.1.4。

**校订后**

[注214] 当谓词为假且没有替代表达式时，`if` 表达式的值在 Scheme 中是未指定的；我们在这里选择使其为假。我们将通过在全局环境中绑定变量 `true` 和 `false` 来支持在待求值表达式中使用它们。参见 4.1.4。

### 4_002e1:0201

**原文**

[注215] These selectors for a list of expressions—and the corresponding ones for a list of operands—are not intended as a data abstraction. They are introduced as mnemonic names for the basic list operations in order to make it easier to understand the explicit-control evaluator in 5.4.

**校订前**

[注215] 这些用于表达式表的选择器——以及用于操作数表的相应选择器——并非意在作为数据抽象。它们被引入作为基本表操作的助记名称，以便更容易理解 5.4 中的显式控制求值器。

**校订后**

[注215] 这些用于表达式表的选择函数——以及用于运算对象表的相应选择函数——并非意在作为数据抽象。它们被引入作为基本表操作的助记名称，以便更容易理解 5.4 中的显式控制求值器。

### 4_002e1:0210

**原文**

[注223] The fact that the machines are described in Lisp is inessential. If we give our evaluator a Lisp program that behaves as an evaluator for some other language, say C, the Lisp evaluator will emulate the C evaluator, which in turn can emulate any machine described as a C program. Similarly, writing a Lisp evaluator in C produces a C program that can execute any Lisp program. The deep idea here is that any evaluator can emulate any other. Thus, the notion of “what can in principle be computed” (ignoring practicalities of time and memory required) is independent of the language or the computer, and instead reflects an underlying notion of computability. This was first demonstrated in a clear way by Alan M. Turing (1912-1954), whose 1936 paper laid the foundations for theoretical computer science. In the paper, Turing presented a simple computational model—now known as a Turing machine—and argued that any “effective process” can be formulated as a program for such a machine. (This argument is known as the Church-Turing thesis.) Turing then implemented a universal machine, i.e., a Turing machine that behaves as an evaluator for Turing-machine programs. He used this framework to demonstrate that there are well-posed problems that cannot be computed by Turing machines (see Exercise 4.15), and so by implication cannot be formulated as “effective processes.” Turing went on to make fundamental contributions to practical computer science as well. For example, he invented the idea of structuring programs using general-purpose subroutines. See Hodges 1983 for a biography of Turing.

**校订前**

[注223]用 Lisp 描述这些机器并非关键。如果我们给我们的求值器一个 Lisp 程序，该程序充当另一种语言（比如 C）的求值器，那么这个 Lisp 求值器将模拟 C 求值器，而后者又能模拟任何用 C 程序描述的机器。类似地，用 C 编写一个 Lisp 求值器会产生一个能执行任何 Lisp 程序的 C 程序。这里的深刻思想是，任何求值器都能模拟任何其他求值器。因此，“原则上可以计算什么”这一概念（忽略所需时间和内存的实际限制）与语言或计算机无关，而是反映了底层的可计算性概念。Alan M. Turing（1912-1954）首次清晰地展示了这一点，他的1936年论文为理论计算机科学奠定了基础。在论文中，Turing 提出了一个简单的计算模型——现在称为图灵机——并论证任何“有效过程”都可以表述为这种机器上的程序。（这一论证被称为丘奇-图灵论题。）Turing 随后实现了一台通用机器，即一台充当图灵机程序求值器的图灵机。他利用这一框架证明了存在一些无法由图灵机计算的适定问题（见习题4.15），因此也就无法表述为“有效过程”。Turing 还对实用计算机科学做出了根本性贡献。例如，他发明了使用通用子程序来组织程序的思想。关于 Turing 的传记，见Hodges 1983。

**校订后**

[注223]用 Lisp 描述这些机器并非关键。如果我们给我们的求值器一个 Lisp 程序，该程序充当另一种语言（比如 C）的求值器，那么这个 Lisp 求值器将模拟 C 求值器，而后者又能模拟任何用 C 程序描述的机器。类似地，用 C 编写一个 Lisp 求值器会产生一个能执行任何 Lisp 程序的 C 程序。这里的深刻思想是，任何求值器都能模拟任何其他求值器。因此，“原则上可以计算什么”这一概念（忽略所需时间和内存的实际限制）与语言或计算机无关，而是反映了底层的可计算性概念。Alan M. Turing（1912-1954）首次清晰地展示了这一点，他的1936年论文为理论计算机科学奠定了基础。在论文中，Turing 提出了一个简单的计算模型——现在称为图灵机——并论证任何“可实际执行的计算过程”都可以表述为这种机器上的程序。（这一论证被称为丘奇-图灵论题。）Turing 随后实现了一台通用机器，即一台充当图灵机程序求值器的图灵机。他利用这一框架证明了存在一些无法由图灵机计算的适定问题（见习题4.15），因此也就无法表述为“可实际执行的计算过程”。Turing 还对实用计算机科学做出了根本性贡献。例如，他发明了使用通用子程序来组织程序的思想。关于 Turing 的传记，见Hodges 1983。

### 4_002e1:0215

**原文**

[注228] Wanting programs to not depend on this evaluation mechanism is the reason for the “management is not responsible” remark in Footnote 28 of Chapter 1. By insisting that internal definitions come first and do not use each other while the definitions are being evaluated, the IEEE standard for Scheme leaves implementors some choice in the mechanism used to evaluate these definitions. The choice of one evaluation rule rather than another here may seem like a small issue, affecting only the interpretation of “badly formed” programs. However, we will see in 5.5.6 that moving to a model of simultaneous scoping for internal definitions avoids some nasty difficulties that would otherwise arise in implementing a compiler.

**校订前**

[注228]希望程序不依赖于这种求值机制，正是第1章脚注28中“管理者不承担责任”这一说明的原因。通过坚持内部定义必须放在最前面，并且在求值这些定义时互不使用，Scheme 的IEEE标准给实现者在求值这些定义所用的机制上留下了一些选择。在这里选择一种求值规则而非另一种，可能看起来是个小问题，只影响“格式不良”程序的解释。然而，我们将在5.5.6中看到，转向内部定义的同步作用域模型可以避免在实现编译器时否则会出现的某些棘手困难。

**校订后**

[注228]希望程序不依赖于这种求值机制，正是第1章脚注28中“管理者不承担责任”这一说明的原因。通过坚持内部定义必须放在最前面，并且在求值这些定义时互不使用，Scheme 的IEEE标准给实现者在求值这些定义所用的机制上留下了一些选择。在这里选择一种求值规则而非另一种，可能看起来是个小问题，只影响“格式不良”程序的解释。然而，我们将在5.5.6中看到，转向内部定义的同时作用域模型可以避免在实现编译器时否则会出现的某些棘手困难。

### 4_002e1:0216

**原文**

[注229] The IEEE standard for Scheme allows for different implementation strategies by specifying that it is up to the programmer to obey this restriction, not up to the implementation to enforce it. Some Scheme implementations, including MIT Scheme, use the transformation shown above. Thus, some programs that don’t obey this restriction will in fact run in such implementations.

**校订前**

[注229]Scheme 的IEEE标准允许不同的实现策略，它规定遵守这一限制是程序员的责任，而不是实现的责任。一些 Scheme 实现，包括MIT Scheme，使用上面所示的变换。因此，一些不遵守这一限制的程序实际上会在这样的实现中运行。

**校订后**

[注229]Scheme 的IEEE标准允许不同的实现策略，它规定遵守这一限制是程序员的责任，而不是由实现来强制执行这一限制。一些 Scheme 实现，包括MIT Scheme，使用上面所示的变换。因此，一些不遵守这一限制的程序实际上会在这样的实现中运行。

### 4_002e2:0004

**原文**

Now that we have an evaluator expressed as a Lisp program, we can experiment with alternative choices in language design simply by modifying the evaluator. Indeed, new languages are often invented by first writing an evaluator that embeds the new language within an existing high-level language. For example, if we wish to discuss some aspect of a proposed modification to Lisp with another member of the Lisp community, we can supply an evaluator that embodies the change. The recipient can then experiment with the new evaluator and send back comments as further modifications. Not only does the high-level implementation base make it easier to test and debug the evaluator; in addition, the embedding enables the designer to snarf[注235] features from the underlying language, just as our embedded Lisp evaluator uses primitives and control structure from the underlying Lisp. Only later (if ever) need the designer go to the trouble of building a complete implementation in a low-level language or in hardware. In this section and the next we explore some variations on Scheme that provide significant additional expressive power.

**校订前**

既然我们有了一个用 Lisp 程序表达求值器，我们就可以仅仅通过修改求值器来试验语言设计中的替代选择。事实上，新语言常常是通过首先编写一个将新语言嵌入现有高级语言中的求值器而发明的。例如，如果我们希望与 Lisp 社区的另一位成员讨论对 Lisp 提议修改的某个方面，我们可以提供一个体现该修改的求值器。接收者随后可以用新的求值器进行实验，并作为进一步的修改发回评论。高级实现基础不仅使测试和调试求值器更容易；此外，这种嵌入使设计者能够从底层语言中攫取[注235]特性，正如我们嵌入的 Lisp 求值器使用底层 Lisp 的基本过程和控制结构一样。只有在后来（如果有的话），设计者才需要费心用低级语言或硬件构建完整的实现。在本节和下一节中，我们探讨 Scheme 的一些变体，它们提供了显著额外的表达能力。

**校订后**

既然我们有了一个用 Lisp 程序表达的求值器，我们就可以仅仅通过修改求值器来试验语言设计中的替代选择。事实上，新语言常常是通过首先编写一个将新语言嵌入现有高级语言中的求值器而发明的。例如，如果我们希望与 Lisp 社区的另一位成员讨论对 Lisp 提议修改的某个方面，我们可以提供一个体现该修改的求值器。接收者随后可以用新的求值器进行实验，并以进一步修改的形式反馈意见。高级实现基础不仅使测试和调试求值器更容易；此外，这种嵌入使设计者能够从底层语言中攫取[注235]特性，正如我们嵌入的 Lisp 求值器使用底层 Lisp 的基本过程和控制结构一样。只有在后来（如果有的话），设计者才需要费心用低级语言或硬件构建完整的实现。在本节和下一节中，我们探讨 Scheme 的一些变体，它们提供了显著额外的表达能力。

### 4_002e2:0012

**原文**

A striking example of a procedure that can usefully be made non-strict is `cons` (or, in general, almost any constructor for data structures). One can do useful computation, combining elements to form data structures and operating on the resulting data structures, even if the values of the elements are not known. It makes perfect sense, for instance, to compute the length of a list without knowing the values of the individual elements in the list. We will exploit this idea in 4.2.3 to implement the streams of Chapter 3 as lists formed of non-strict `cons` pairs.

**校订前**

一个可以有效地使其非严格的引人注目的例子是`cons`（或者，一般来说，几乎任何数据结构的构造器）。即使元素的值未知，也可以进行有用的计算，将元素组合成数据结构并对所得数据结构进行操作。例如，在不知道表中各个元素值的情况下计算表的长度是完全合理的。我们将在4.2.3中利用这一思想，将第3章的流实现为由非严格`cons`序对构成的表。

**校订后**

一个可以有效地使其非严格的引人注目的例子是`cons`（或者，一般来说，几乎任何数据结构的构造函数）。即使元素的值未知，也可以进行有用的计算，将元素组合成数据结构并对所得数据结构进行操作。例如，在不知道表中各个元素值的情况下计算表的长度是完全合理的。我们将在4.2.3中利用这一思想，将第3章的流实现为由非严格`cons`序对构成的表。

### 4_002e2:0023

**原文**

This is almost the same as the `application?` clause of `eval` in 4.1.1. For lazy evaluation, however, we call `apply` with the operand expressions, rather than the arguments produced by evaluating them. Since we will need the environment to construct thunks if the arguments are to be delayed, we must pass this as well. We still evaluate the operator, because `apply` needs the actual procedure to be applied in order to dispatch on its type (primitive versus compound) and apply it.

**校订前**

这与 4.1.1 中 `eval` 的 `application?` 子句几乎相同。然而，对于惰性求值，我们使用操作数表达式调用 `apply`，而不是使用对它们求值产生的参数。由于如果参数要被延迟，我们将需要环境来构造 thunk，因此我们也必须传递环境。我们仍然对运算符求值，因为 `apply` 需要实际要应用的过程，以便根据其类型（基本过程还是复合过程）进行分派并应用它。

**校订后**

这与 4.1.1 中 `eval` 的 `application?` 子句几乎相同。然而，对于惰性求值，我们使用运算对象表达式调用 `apply`，而不是使用对它们求值产生的参数。由于如果参数要被延迟，我们将需要环境来构造 thunk，因此我们也必须传递环境。我们仍然对运算符求值，因为 `apply` 需要实际要应用的过程，以便根据其类型（基本过程还是复合过程）进行分派并应用它。

### 4_002e2:0024

**原文**

Whenever we need the actual value of an expression, we use

**校订前**

每当我们需要的表达式的实际值时，我们使用

**校订后**

每当我们需要表达式的实际值时，我们使用

### 4_002e2:0026

**原文**

Our new version of `apply` is also almost the same as the version in 4.1.1. The difference is that `eval` has passed in unevaluated operand expressions: For primitive procedures (which are strict), we evaluate all the arguments before applying the primitive; for compound procedures (which are non-strict) we delay all the arguments before applying the procedure.

**校订前**

我们新版本的 `apply` 也与 4.1.1 中的版本几乎相同。区别在于 `eval` 传递的是未求值的操作数表达式：对于基本过程（它们是严格的），我们在应用基本过程之前对所有参数求值；对于复合过程（它们是非严格的），我们在应用过程之前延迟所有参数。

**校订后**

我们新版本的 `apply` 也与 4.1.1 中的版本几乎相同。区别在于 `eval` 传递的是未求值的运算对象表达式：对于基本过程（它们是严格的），我们在应用基本过程之前对所有参数求值；对于复合过程（它们是非严格的），我们在应用过程之前延迟所有参数。

### 4_002e2:0038

**原文**

Exercise 4.28: `Eval` uses `actual-value` rather than `eval` to evaluate the operator before passing it to `apply`, in order to force the value of the operator. Give an example that demonstrates the need for this forcing.

**校订前**

习题4.28：`Eval`使用`actual-value`而不是`eval`来在将操作符传递给`apply`之前对其求值，以强制求出操作符的值。给出一个例子，说明这种强制的必要性。

**校订后**

习题4.28：`Eval`使用`actual-value`而不是`eval`来在将运算符传递给`apply`之前对其求值，以强制求出运算符的值。给出一个例子，说明这种强制的必要性。

### 4_002e2:0041

**原文**

Exercise 4.30: Cy D. Fect, a reformed C programmer, is worried that some side effects may never take place, because the lazy evaluator doesn’t force the expressions in a sequence. Since the value of an expression in a sequence other than the last one is not used (the expression is there only for its effect, such as assigning to a variable or printing), there can be no subsequent use of this value (e.g., as an argument to a primitive procedure) that will cause it to be forced. Cy thus thinks that when evaluating sequences, we must force all expressions in the sequence except the final one. He proposes to modify `eval-sequence` from 4.1.1 to use `actual-value` rather than `eval`:

**校订前**

习题4.30：Cy D. Fect，一位改过自新的C程序员，担心某些副作用可能永远不会发生，因为惰性求值器不会强制求值序列中的表达式。由于序列中除最后一个表达式外的其他表达式的值不会被使用（这些表达式只是为了其效果而存在，例如给变量赋值或打印），因此后续不可能使用这个值（例如，作为基本过程的参数）来导致它被强制求值。因此Cy认为，在求值序列时，我们必须强制求值序列中除最后一个表达式外的所有表达式。他提议修改`eval-sequence`，从4.1.1改为使用`actual-value`而不是`eval`：

**校订后**

习题4.30：Cy D. Fect，一位改过自新的C程序员，担心某些副作用可能永远不会发生，因为惰性求值器不会强制求值序列中的表达式。由于序列中除最后一个表达式外的其他表达式的值不会被使用（这些表达式只是为了其效果而存在，例如给变量赋值或打印），因此后续不可能使用这个值（例如，作为基本过程的参数）来导致它被强制求值。因此Cy认为，在求值序列时，我们必须强制求值序列中除最后一个表达式外的所有表达式。他提议修改4.1.1中的`eval-sequence`，改为使用`actual-value`而不是`eval`：

### 4_002e2:0056

**原文**

Lazy pairs also help with the problem that arose with streams in 3.5.4, where we found that formulating stream models of systems with loops may require us to sprinkle our programs with explicit `delay` operations, beyond the ones supplied by `cons-stream`. With lazy evaluation, all arguments to procedures are delayed uniformly. For instance, we can implement procedures to integrate lists and solve differential equations as we originally intended in 3.5.4:

**校订前**

惰性序对还有助于解决在3.5.4中处理流时出现的问题，在那里我们发现，为带循环的系统建立流模型可能需要我们在程序中额外添加显式的`delay`操作，超出`cons-stream`所提供的那些。使用惰性求值，过程的所有参数都被统一延迟。例如，我们可以按照最初在3.5.4中的意图，实现用于对表进行积分和解微分方程的过程：

**校订后**

惰性序对还有助于解决在3.5.4中处理流时出现的问题，在那里我们发现，为带回路的系统建立流模型可能需要我们在程序中额外添加显式的`delay`操作，超出`cons-stream`所提供的那些。使用惰性求值，过程的所有参数都被统一延迟。例如，我们可以按照最初在3.5.4中的意图，实现用于对表进行积分和解微分方程的过程：

### 4_002e2:0072

**原文**

[注244] This is the procedural representation described in Exercise 2.4. Essentially any procedural representation (e.g., a message-passing implementation) would do as well. Notice that we can install these definitions in the lazy evaluator simply by typing them at the driver loop. If we had originally included `cons`, `car`, and `cdr` as primitives in the global environment, they will be redefined. (Also see Exercise 4.33 and Exercise 4.34.)

**校订前**

[注244] 这是习题2.4中描述的过程性表示。本质上，任何过程性表示（例如，消息传递实现）也同样可行。注意，我们只需在驱动程序循环中键入这些定义，就可以将它们安装到惰性求值器中。如果我们最初已将`cons`、`car`和`cdr`作为基本过程包含在全局环境中，它们将被重新定义。（另见习题4.33和习题4.34。）

**校订后**

[注244] 这是习题2.4中描述的过程性表示。本质上，任何过程性表示（例如，消息传递实现）也同样可行。注意，我们只需在驱动循环中键入这些定义，就可以将它们安装到惰性求值器中。如果我们最初已将`cons`、`car`和`cdr`作为基本过程包含在全局环境中，它们将被重新定义。（另见习题4.33和习题4.34。）

### 4_002e3:0005

**原文**

Nondeterministic computing, like stream processing, is useful for “generate and test” applications. Consider the task of starting with two lists of positive integers and finding a pair of integers—one from the first list and one from the second list—whose sum is prime. We saw how to handle this with finite sequence operations in 2.2.3 and with infinite streams in 3.5.3. Our approach was to generate the sequence of all possible pairs and filter these to select the pairs whose sum is prime. Whether we actually generate the entire sequence of pairs first as in Chapter 2, or interleave the generating and filtering as in Chapter 3, is immaterial to the essential image of how the computation is organized.

**校订前**

非确定性计算，像流处理一样，对于“生成并测试”应用很有用。考虑这样一个任务：从两个正整数表开始，找到一对整数——一个来自第一个表，一个来自第二个表——其和为素数。我们在2.2.3中看到了如何用有限序列操作处理这个问题，在3.5.3中用无限流处理。我们的方法是生成所有可能序对的序列，并过滤这些序对以选出和为素数的那些。无论我们像第2章中那样实际首先生成整个序对序列，还是像第3章中那样交错生成和过滤，对于计算如何组织的本质图景来说都无关紧要。

**校订后**

非确定性计算，像流处理一样，对于“生成并测试”应用很有用。考虑这样一个任务：从两个正整数表开始，找到一对整数——一个来自第一个表，一个来自第二个表——其和为素数。我们在2.2.3中看到了如何用有限序列操作处理这个问题，在3.5.3中用无穷流处理。我们的方法是生成所有可能序对的序列，并过滤这些序对以选出和为素数的那些。无论我们像第2章中那样实际首先生成整个序对序列，还是像第3章中那样交错生成和过滤，对于计算如何组织的本质图景来说都无关紧要。

### 4_002e3:0008

**原文**

The key idea here is that expressions in a nondeterministic language can have more than one possible value. For instance, `an-element-of` might return any element of the given list. Our nondeterministic program evaluator will work by automatically choosing a possible value and keeping track of the choice. If a subsequent requirement is not met, the evaluator will try a different choice, and it will keep trying new choices until the evaluation succeeds, or until we run out of choices. Just as the lazy evaluator freed the programmer from the details of how values are delayed and forced, the nondeterministic program evaluator will free the programmer from the details of how choices are made.

**校订前**

这里的关键思想是，非确定性语言中的表达式可以有多个可能的值。例如，`an-element-of`可能返回给定表中的任意元素。我们的非确定性程序求值器将通过自动选择一个可能的值并跟踪该选择来工作。如果后续要求未满足，求值器将尝试不同的选择，并不断尝试新的选择，直到求值成功，或者直到我们用尽所有选择。正如惰性求值器将程序员从值如何被延迟和强迫的细节中解放出来一样，非确定性程序求值器将程序员从选择如何做出的细节中解放出来。

**校订后**

这里的关键思想是，非确定性语言中的表达式可以有多个可能的值。例如，`an-element-of`可能返回给定表中的任意元素。我们的非确定性程序求值器将通过自动选择一个可能的值并跟踪该选择来工作。如果后续要求未满足，求值器将尝试不同的选择，并不断尝试新的选择，直到求值成功，或者直到我们用尽所有选择。正如惰性求值器将程序员从值如何被延迟和强制求值的细节中解放出来一样，非确定性程序求值器将程序员从选择如何做出的细节中解放出来。

### 4_002e3:0010

**原文**

The nondeterministic program evaluator implemented below is called the `amb` evaluator because it is based on a new special form called `amb`. We can type the above definition of `prime-sum-pair` at the `amb` evaluator driver loop (along with definitions of `prime?`, `an-element-of`, and `require`) and run the procedure as follows:

**校订前**

下面实现的非确定性程序求值器称为`amb`求值器，因为它基于一个称为`amb`的新特殊形式。我们可以在`amb`求值器驱动程序循环中键入上述`prime-sum-pair`的定义（以及`prime?`、`an-element-of`和`require`的定义），并按如下方式运行该过程：

**校订后**

下面实现的非确定性程序求值器称为`amb`求值器，因为它基于一个称为`amb`的新特殊形式。我们可以在`amb`求值器驱动循环中键入上述`prime-sum-pair`的定义（以及`prime?`、`an-element-of`和`require`的定义），并按如下方式运行该过程：

### 4_002e3:0040

**原文**

Exercise 4.40: In the multiple dwelling problem, how many sets of assignments are there of people to floors, both before and after the requirement that floor assignments be distinct? It is very inefficient to generate all possible assignments of people to floors and then leave it to backtracking to eliminate them. For example, most of the restrictions depend on only one or two of the person-floor variables, and can thus be imposed before floors have been selected for all the people. Write and demonstrate a much more efficient nondeterministic procedure that solves this problem based upon generating only those possibilities that are not already ruled out by previous restrictions. (Hint: This will require a nest of `let` expressions.)

**校订前**

习题 4.40：在多人居住问题中，在要求楼层分配互不相同之前和之后，人分配到楼层的赋值集合各有多少个？生成人分配到楼层的所有可能赋值，然后依靠回溯来排除它们，效率非常低。例如，大多数限制条件只依赖于一两个“人-楼层”变量，因此可以在为所有人选定楼层之前就施加这些限制。编写并演示一个效率高得多的非确定性过程，它基于只生成那些尚未被先前限制条件排除的可能性来求解此问题。（提示：这需要嵌套的 `let` 表达式。）

**校订后**

习题 4.40：在多人居住问题中，在要求楼层分配互不相同之前和之后，将各人分配到楼层的方案各有多少个？生成人分配到楼层的所有可能分配方案，然后依靠回溯来排除它们，效率非常低。例如，大多数限制条件只依赖于一两个“人-楼层”变量，因此可以在为所有人选定楼层之前就施加这些限制。编写并演示一个效率高得多的非确定性过程，它基于只生成那些尚未被先前限制条件排除的可能性来求解此问题。（提示：这需要嵌套的 `let` 表达式。）

### 4_002e3:0046

**原文**

Joan: “I was third, and poor old Ethel was bottom.”

**校订前**

Joan：“我得了第三名，可怜的老 Ethel 得了最后一名。”

**校订后**

Joan：“我得了第三名，可怜的 Ethel 得了最后一名。”

### 4_002e3:0073

**原文**

Exercise 4.46: The evaluators in 4.1 and 4.2 do not determine what order operands are evaluated in. We will see that the `amb` evaluator evaluates them from left to right. Explain why our parsing program wouldn’t work if the operands were evaluated in some other order.

**校订前**

习题 4.46： 4.1 和 4.2 中的求值器没有确定操作数的求值顺序。我们将看到 `amb` 求值器从左到右对它们求值。解释为什么如果操作数以某种其他顺序求值，我们的分析程序就不能工作。

**校订后**

习题 4.46： 4.1 和 4.2 中的求值器没有确定运算对象的求值顺序。我们将看到 `amb` 求值器从左到右对它们求值。解释为什么如果运算对象以某种其他顺序求值，我们的分析程序就不能工作。

### 4_002e3:0077

**原文**

Exercise 4.49: Alyssa P. Hacker is more interested in generating interesting sentences than in parsing them. She reasons that by simply changing the procedure `parse-word` so that it ignores the “input sentence” and instead always succeeds and generates an appropriate word, we can use the programs we had built for parsing to do generation instead. Implement Alyssa’s idea, and show the first half-dozen or so sentences generated.[注258]

**校订前**

习题 4.49： Alyssa P. Hacker 对生成有趣的句子比分析它们更感兴趣。她推理说，只要简单地改变过程 `parse-word`，使它忽略“输入句子”，而是总是成功并生成一个适当的词，我们就可以用为分析而构建的程序来进行生成。实现 Alyssa 的想法，并展示生成的前六七个句子。[注258]

**校订后**

习题 4.49： Alyssa P. Hacker 对生成有趣的句子比分析它们更感兴趣。她推理说，只要简单地改变过程 `parse-word`，使它忽略“输入句子”，而是总是成功并生成一个适当的词，我们就可以用为分析而构建的程序来进行生成。实现 Alyssa 的想法，并展示生成的前六个左右的句子。[注258]

### 4_002e3:0085

**原文**

A failure is triggered during evaluation (that is, a failure continuation is called) when a user program explicitly rejects the current line of attack (for example, a call to `require` may result in execution of `(amb)`, an expression that always fails—see 4.3.1). The failure continuation in hand at that point will cause the most recent choice point to choose another alternative. If there are no more alternatives to be considered at that choice point, a failure at an earlier choice point is triggered, and so on. Failure continuations are also invoked by the driver loop in response to a `try-again` request, to find another value of the expression.

**校订前**

当用户程序显式地拒绝当前攻击路线时（例如，对 `require` 的调用可能导致执行 `(amb)`，这是一个总是失败的表达式——见 4.3.1），在求值过程中就会触发一次失败（也就是说，调用一个失败继续过程）。此时手头的失败继续过程将导致最近的选择点选择另一个备选方案。如果该选择点没有更多备选方案可供考虑，就会触发更早的选择点上的失败，依此类推。驱动程序循环在响应 `try-again` 请求时也会调用失败继续过程，以寻找该表达式的另一个值。

**校订后**

当用户程序显式地拒绝当前的求解路径时（例如，对 `require` 的调用可能导致执行 `(amb)`，这是一个总是失败的表达式——见 4.3.1），在求值过程中就会触发一次失败（也就是说，调用一个失败继续过程）。此时手头的失败继续过程将导致最近的选择点选择另一个备选方案。如果该选择点没有更多备选方案可供考虑，就会触发更早的选择点上的失败，依此类推。驱动循环在响应 `try-again` 请求时也会调用失败继续过程，以寻找该表达式的另一个值。

### 4_002e3:0103

**原文**

will attempt to evaluate the given expression and will return either the expression’s value (if the evaluation succeeds) or the symbol `failed` (if the evaluation fails). The call to `ambeval` in the driver loop shown below uses much more complicated continuation procedures, which continue the loop and support the `try-again` request.

**校订前**

将尝试对给定表达式求值，并返回该表达式的值（如果求值成功）或符号 `failed`（如果求值失败）。下面显示的驱动程序循环中对 `ambeval` 的调用使用了复杂得多的继续过程，这些继续过程继续循环并支持 `try-again` 请求。

**校订后**

将尝试对给定表达式求值，并返回该表达式的值（如果求值成功）或符号 `failed`（如果求值失败）。下面显示的驱动循环中对 `ambeval` 的调用使用了复杂得多的继续过程，这些继续过程继续循环并支持 `try-again` 请求。

### 4_002e3:0109

**原文**

Conditionals are also handled in a similar way as in the ordinary evaluator. The execution procedure generated by `analyze-if` invokes the predicate execution procedure `pproc` with a success continuation that checks whether the predicate value is true and goes on to execute either the consequent or the alternative. If the execution of `pproc` fails, the original failure continuation for the `if` expression is called.

**校订前**

条件式的处理方式也与普通求值器类似。由 `analyze-if` 生成的执行过程调用谓词执行过程 `pproc`，并传入一个成功继续过程，该继续过程检查谓词值是否为真，并继续执行要么是推论要么是替代。如果 `pproc` 的执行失败，则调用 `if` 表达式原来的失败继续过程。

**校订后**

条件式的处理方式也与普通求值器类似。由 `analyze-if` 生成的执行过程调用谓词执行过程 `pproc`，并传入一个成功继续过程，该继续过程检查谓词值是否为真，并继续执行结果表达式或替代表达式。如果 `pproc` 的执行失败，则调用 `if` 表达式原来的失败继续过程。

### 4_002e3:0117

**原文**

The execution procedure for applications contains no new ideas except for the technical complexity of managing the continuations. This complexity arises in `analyze-application`, due to the need to keep track of the success and failure continuations as we evaluate the operands. We use a procedure `get-args` to evaluate the list of operands, rather than a simple `map` as in the ordinary evaluator.

**校订前**

应用的执行过程除了管理继续过程的技术复杂性之外，不包含任何新思想。这种复杂性出现在 `analyze-application` 中，因为在求值操作数时需要跟踪成功继续过程和失败继续过程。我们使用过程 `get-args` 来求值操作数表，而不是像普通求值器中那样使用简单的 `map`。

**校订后**

应用的执行过程除了管理继续过程的技术复杂性之外，不包含任何新思想。这种复杂性出现在 `analyze-application` 中，因为在求值运算对象时需要跟踪成功继续过程和失败继续过程。我们使用过程 `get-args` 来求值运算对象表，而不是像普通求值器中那样使用简单的 `map`。

### 4_002e3:0118

**原文**

In `get-args`, notice how `cdr`-ing down the list of `aproc` execution procedures and `cons`ing up the resulting list of `args` is accomplished by calling each `aproc` in the list with a success continuation that recursively calls `get-args`. Each of these recursive calls to `get-args` has a success continuation whose value is the `cons` of the newly obtained argument onto the list of accumulated arguments:

**校订前**

在 `get-args` 中，请注意，沿着 `aproc` 执行过程表向下 `cdr` 并向上 `cons` 得到的 `args` 表，是通过用成功继续过程调用表中的每个 `aproc` 来完成的，该成功继续过程递归地调用 `get-args`。这些对 `get-args` 的递归调用中的每一个都有一个成功继续过程，其值是将新获得的操作数 `cons` 到累积操作数表上：

**校订后**

在 `get-args` 中，请注意，沿着 `aproc` 执行过程表向下 `cdr` 并向上 `cons` 得到的 `args` 表，是通过用成功继续过程调用表中的每个 `aproc` 来完成的，该成功继续过程递归地调用 `get-args`。这些对 `get-args` 的递归调用中的每一个都有一个成功继续过程，其值是将新获得的实参 `cons` 到累积实参表上：

### 4_002e3:0126

**原文**

The initial call to `internal-loop` uses a `try-again` procedure that complains that there is no current problem and restarts the driver loop. This is the behavior that will happen if the user types `try-again` when there is no evaluation in progress.

**校订前**

对 `internal-loop` 的初始调用使用一个 `try-again` 过程，它抱怨没有当前问题并重新启动驱动循环。如果用户在没有进行中的求值时键入 `try-again`，就会发生这种行为。

**校订后**

对 `internal-loop` 的初始调用使用一个 `try-again` 过程，它报告当前没有待求解的问题并重新启动驱动循环。如果用户在没有进行中的求值时键入 `try-again`，就会发生这种行为。

### 4_002e3:0139

**原文**

[注249] One might object that this is a hopelessly inefficient mechanism. It might require millions of processors to solve some easily stated problem this way, and most of the time most of those processors would be idle. This objection should be taken in the context of history. Memory used to be considered just such an expensive commodity. In 1964 a megabyte of RAM cost about $400,000. Now every personal computer has many megabytes of RAM, and most of the time most of that RAM is unused. It is hard to underestimate the cost of mass-produced electronics.

**校订前**

[注249]有人可能会反对说，这是一种无可救药的低效机制。以这种方式解决某个容易陈述的问题可能需要数百万个处理器，而且大多数时候这些处理器中的大多数都会空闲。这种反对意见应该放在历史的背景下来看。内存曾经也被认为是这样一种昂贵的商品。在1964年，一兆字节的RAM大约花费400,000美元。现在每台个人计算机都有许多兆字节的RAM，而且大多数时候这些RAM中的大部分都未被使用。很难低估大规模生产的电子产品的成本。

**校订后**

[注249]有人可能会反对说，这是一种无可救药的低效机制。以这种方式解决某个容易陈述的问题可能需要数百万个处理器，而且大多数时候这些处理器中的大多数都会空闲。这种反对意见应该放在历史的背景下来看。内存曾经也被认为是这样一种昂贵的商品。在1964年，一兆字节的RAM大约花费400,000美元。现在每台个人计算机都有许多兆字节的RAM，而且大多数时候这些RAM中的大部分都未被使用。大规模生产的电子产品成本之低，几乎怎么估计都不为过。

### 4_002e4:0007

**原文**

This approach, when it works, can be a very powerful way to write programs. Part of the power comes from the fact that a single “what is” fact can be used to solve a number of different problems that would have different “how to” components. As an example, consider the `append` operation, which takes two lists as arguments and combines their elements to form a single list. In a procedural language such as Lisp, we could define `append` in terms of the basic list constructor `cons`, as we did in 2.2.1:

**校订前**

这种方法在有效时，可以是一种非常强大的编写程序的方式。其部分力量来自于这样一个事实：一个单一的“是什么”事实可以用来解决许多具有不同“如何做”组件的不同问题。作为一个例子，考虑 `append` 操作，它接受两个表作为参数，并将它们的元素组合成一个单一的表。在像 Lisp 这样的过程式语言中，我们可以用基本表构造器 `cons` 来定义 `append`，正如我们在 2.2.1 中所做的那样：

**校订后**

这种方法在有效时，可以是一种非常强大的编写程序的方式。其部分力量来自于这样一个事实：一个单一的“是什么”事实可以用来解决许多具有不同“如何做”组件的不同问题。作为一个例子，考虑 `append` 操作，它接受两个表作为参数，并将它们的元素组合成一个单一的表。在像 Lisp 这样的过程式语言中，我们可以用基本表构造函数 `cons` 来定义 `append`，正如我们在 2.2.1 中所做的那样：

### 4_002e4:0017

**原文**

Contemporary logic programming languages (including the one we implement here) have substantial deficiencies, in that their general “how to” methods can lead them into spurious infinite loops or other undesirable behavior. Logic programming is an active field of research in computer science.[注265]

**校订前**

当代逻辑程序设计语言（包括我们在此实现的那种）存在重大缺陷，因为它们的一般“如何做”方法可能导致它们陷入虚假的无限循环或其他不良行为。逻辑程序设计是计算机科学中一个活跃的研究领域。[注265]

**校订后**

当代逻辑程序设计语言（包括我们在此实现的那种）存在重大缺陷，因为它们的一般“如何做”方法可能导致它们陷入不必要的无限循环或其他不良行为。逻辑程序设计是计算机科学中一个活跃的研究领域。[注265]

### 4_002e4:0089

**原文**

says that a staff person is outranked by a boss in the organization if the boss is the person’s supervisor or (recursively) if the person’s supervisor is outranked by the boss.

**校订前**

表示：如果老板是某人的主管，或者（递归地）某人的主管被老板所超越，那么该员工在组织中被老板所超越。

**校订后**

表示：如果老板是某人的主管，或者（递归地）某人的主管在职级上低于老板，那么该员工在组织中的职级低于老板。

### 4_002e4:0118

**原文**

Formulate rules such as “If $S$ is the son of $f$, and $f$ is the son of $G$, then $S$ is the grandson of $G$” and “If $W$ is the wife of $M$, and $S$ is the son of $W$, then $S$ is the son of $M$” (which was supposedly more true in biblical times than today) that will enable the query system to find the grandson of Cain; the sons of Lamech; the grandsons of Methushael. (See Exercise 4.69 for some rules to deduce more complicated relationships.)

**校订前**

制定诸如“如果$S$是$f$的儿子，且$f$是$G$的儿子，那么$S$是$G$的孙子”和“如果$W$是$M$的妻子，且$S$是$W$的儿子，那么$S$是$M$的儿子”（据说这在圣经时代比今天更符合事实）这样的规则，使查询系统能够找到该隐的孙子；拉麦的儿子们；玛土撒利的孙子们。（关于推导更复杂关系的一些规则，见习题4.69。）

**校订后**

制定诸如“如果$S$是$f$的儿子，且$f$是$G$的儿子，那么$S$是$G$的孙子”和“如果$W$是$M$的妻子，且$S$是$W$的儿子，那么$S$是$M$的儿子”（据说这在圣经时代比今天更符合事实）这样的规则，使查询系统能够找到该隐的孙子；拉麦的儿子们；Methushael的孙子们。（关于推导更复杂关系的一些规则，见习题4.69。）

### 4_002e4:0135

**原文**

The real elegance of the stream-of-frames implementation is evident when we deal with compound queries. The processing of compound queries makes use of the ability of our matcher to demand that a match be consistent with a specified frame. For example, to handle the `and` of two queries, such as

**校订前**

当我们处理复合查询时，基于帧流的实现的真正优雅之处就显现出来了。复合查询的处理利用了我们的匹配器要求匹配与指定帧一致的能力。例如，为了处理两个查询的`and`，比如

**校订后**

当我们处理复合查询时，基于框架流的实现的真正优雅之处就显现出来了。复合查询的处理利用了我们的匹配器要求匹配与指定框架一致的能力。例如，为了处理两个查询的`and`，比如

### 4_002e4:0137

**原文**

This produces a stream of frames, each of which contains a binding for `?x`. Then for each frame in the stream we find all entries that match

**校订前**

这产生一个帧流，每个帧都包含一个对`?x`的绑定。然后对于流中的每个帧，我们找出所有匹配以下模式的条目

**校订后**

这产生一个框架流，每个框架都包含一个对`?x`的绑定。然后对于流中的每个框架，我们找出所有匹配以下模式的条目

### 4_002e4:0138

**原文**

in a way that is consistent with the given binding for `?x`. Each such match will produce a frame containing bindings for `?x` and `?person`. The `and` of two queries can be viewed as a series combination of the two component queries, as shown in Figure 4.5. The frames that pass through the first query filter are filtered and further extended by the second query.

**校订前**

并且与给定的`?x`绑定一致。每个这样的匹配将产生一个包含对`?x`和`?person`绑定的帧。两个查询的`and`可以看作两个组件查询的串联组合，如图4.5所示。通过第一个查询过滤器的帧被第二个查询过滤并进一步扩展。

**校订后**

并且与给定的`?x`绑定一致。每个这样的匹配将产生一个包含对`?x`和`?person`绑定的框架。两个查询的`and`可以看作两个组件查询的串联组合，如图4.5所示。通过第一个查询过滤器的框架被第二个查询过滤并进一步扩展。

### 4_002e4:0139

**原文**

Figure 4.5: The `and` combination of two queries is produced by operating on the stream of frames in series.

**校订前**

图4.5：两个查询的`and`组合是通过串联操作帧流产生的。

**校订后**

图4.5：两个查询的`and`组合是通过串联操作框架流产生的。

### 4_002e4:0140

**原文**

Figure 4.6 shows the analogous method for computing the `or` of two queries as a parallel combination of the two component queries. The input stream of frames is extended separately by each query. The two resulting streams are then merged to produce the final output stream.

**校订前**

图4.6展示了计算两个查询的`or`的类似方法，即两个组件查询的并联组合。输入帧流被每个查询分别扩展。然后合并两个结果流以产生最终输出流。

**校订后**

图4.6展示了计算两个查询的`or`的类似方法，即两个组件查询的并联组合。输入框架流被每个查询分别扩展。然后合并两个结果流以产生最终输出流。

### 4_002e4:0141

**原文**

Figure 4.6: The `or` combination of two queries is produced by operating on the stream of frames in parallel and merging the results.

**校订前**

图4.6：两个查询的`or`组合是通过并联操作帧流并合并结果产生的。

**校订后**

图4.6：两个查询的`or`组合是通过并联操作框架流并合并结果产生的。

### 4_002e4:0142

**原文**

Even from this high-level description, it is apparent that the processing of compound queries can be slow. For example, since a query may produce more than one output frame for each input frame, and each query in an `and` gets its input frames from the previous query, an `and` query could, in the worst case, have to perform a number of matches that is exponential in the number of queries (see Exercise 4.76).[注272] Though systems for handling only simple queries are quite practical, dealing with complex queries is extremely difficult.[注273]

**校订前**

即使从这个高层描述来看，复合查询的处理也可能很慢。例如，由于一个查询可能为每个输入帧产生多个输出帧，并且`and`中的每个查询从前一个查询获取输入帧，在最坏情况下，一个`and`查询可能必须执行与查询数量成指数关系的匹配次数（见习题4.76）。[注272]尽管仅处理简单查询的系统相当实用，但处理复杂查询极其困难。[注273]

**校订后**

即使从这个高层描述来看，复合查询的处理也可能很慢。例如，由于一个查询可能为每个输入框架产生多个输出框架，并且`and`中的每个查询从前一个查询获取输入框架，在最坏情况下，一个`and`查询可能必须执行与查询数量成指数关系的匹配次数（见习题4.76）。[注272]尽管仅处理简单查询的系统相当实用，但处理复杂查询极其困难。[注273]

### 4_002e4:0143

**原文**

From the stream-of-frames viewpoint, the `not` of some query acts as a filter that removes all frames for which the query can be satisfied. For instance, given the pattern

**校订前**

从帧流的观点来看，某个查询的`not`充当一个过滤器，移除所有使该查询能够被满足的帧。例如，给定模式

**校订后**

从框架流的观点来看，某个查询的`not`充当一个过滤器，移除所有使该查询能够被满足的框架。例如，给定模式

### 4_002e4:0144

**原文**

we attempt, for each frame in the input stream, to produce extension frames that satisfy `(job ?x (computer programmer))`. We remove from the input stream all frames for which such extensions exist. The result is a stream consisting of only those frames in which the binding for `?x` does not satisfy `(job ?x (computer programmer))`. For example, in processing the query

**校订前**

对于输入流中的每个帧，我们尝试产生满足`(job ?x (computer programmer))`的扩展帧。我们从输入流中移除所有存在此类扩展的帧。结果是一个仅由那些对`?x`的绑定不满足`(job ?x (computer programmer))`的帧组成的流。例如，在处理查询

**校订后**

对于输入流中的每个框架，我们尝试产生满足`(job ?x (computer programmer))`的扩展框架。我们从输入流中移除所有存在此类扩展的框架。结果是一个仅由那些对`?x`的绑定不满足`(job ?x (computer programmer))`的框架组成的流。例如，在处理查询

### 4_002e4:0145

**原文**

the first clause will generate frames with bindings for `?x` and `?y`. The `not` clause will then filter these by removing all frames in which the binding for `?x` satisfies the restriction that `?x` is a computer programmer.[注274]

**校订前**

时，第一个子句将生成带有对`?x`和`?y`绑定的帧。然后`not`子句将通过移除所有对`?x`的绑定满足`?x`是计算机程序员这一限制的帧来过滤这些帧。[注274]

**校订后**

时，第一个子句将生成带有对`?x`和`?y`绑定的框架。然后`not`子句将通过移除所有对`?x`的绑定满足`?x`是计算机程序员这一限制的框架来过滤这些框架。[注274]

### 4_002e4:0146

**原文**

The `lisp-value` special form is implemented as a similar filter on frame streams. We use each frame in the stream to instantiate any variables in the pattern, then apply the Lisp predicate. We remove from the input stream all frames for which the predicate fails.

**校订前**

`lisp-value`特殊形式实现为对帧流的类似过滤器。我们使用流中的每个帧来实例化模式中的任何变量，然后应用 Lisp 谓词。我们从输入流中移除所有谓词失败的帧。

**校订后**

`lisp-value`特殊形式实现为对框架流的类似过滤器。我们使用流中的每个框架来实例化模式中的任何变量，然后应用 Lisp 谓词。我们从输入流中移除所有谓词失败的框架。

### 4_002e4:0149

**原文**

A unifier takes two patterns, each containing constants and variables, and determines whether it is possible to assign values to the variables that will make the two patterns equal. If so, it returns a frame containing these bindings. For example, unifying `(?x a ?y)` and `(?y ?z a)` will specify a frame in which `?x`, `?y`, and `?z` must all be bound to `a`. On the other hand, unifying `(?x ?y a)` and `(?x b ?y)` will fail, because there is no value for `?y` that can make the two patterns equal. (For the second elements of the patterns to be equal, `?y` would have to be `b`; however, for the third elements to be equal, `?y` would have to be `a`.) The unifier used in the query system, like the pattern matcher, takes a frame as input and performs unifications that are consistent with this frame.

**校订前**

合一器接受两个模式，每个模式包含常量和变量，并确定是否可以为变量赋值以使两个模式相等。如果可以，它返回一个包含这些绑定的帧。例如，合一`(?x a ?y)`和`(?y ?z a)`将指定一个帧，其中`?x`、`?y`和`?z`都必须绑定到`a`。另一方面，合一`(?x ?y a)`和`(?x b ?y)`将失败，因为不存在能使两个模式相等的`?y`值。（为了使模式的第二个元素相等，`?y`必须为`b`；然而，为了使第三个元素相等，`?y`必须为`a`。）查询系统中使用的合一器，像模式匹配器一样，接受一个帧作为输入，并执行与该帧一致的合一。

**校订后**

合一器接受两个模式，每个模式包含常量和变量，并确定是否可以为变量赋值以使两个模式相等。如果可以，它返回一个包含这些绑定的框架。例如，合一`(?x a ?y)`和`(?y ?z a)`将指定一个框架，其中`?x`、`?y`和`?z`都必须绑定到`a`。另一方面，合一`(?x ?y a)`和`(?x b ?y)`将失败，因为不存在能使两个模式相等的`?y`值。（为了使模式的第二个元素相等，`?y`必须为`b`；然而，为了使第三个元素相等，`?y`必须为`a`。）查询系统中使用的合一器，像模式匹配器一样，接受一个框架作为输入，并执行与该框架一致的合一。

### 4_002e4:0150

**原文**

The unification algorithm is the most technically difficult part of the query system. With complex patterns, performing unification may seem to require deduction. To unify `(?x ?x)` and `((a ?y c) (a b ?z))`, for example, the algorithm must infer that `?x` should be `(a b c)`, `?y` should be `b`, and `?z` should be `c`. We may think of this process as solving a set of equations among the pattern components. In general, these are simultaneous equations, which may require substantial manipulation to solve.[注275] For example, unifying `(?x ?x)` and `((a ?y c) (a b ?z))` may be thought of as specifying the simultaneous equations

**校订前**

合一算法是查询系统中最技术困难的部分。对于复杂模式，执行合一似乎需要推理。例如，为了合一`(?x ?x)`和`((a ?y c) (a b ?z))`，算法必须推断出`?x`应为`(a b c)`，`?y`应为`b`，以及`?z`应为`c`。我们可以将此过程视为求解模式组件之间的一组方程。一般来说，这些是联立方程，可能需要大量操作才能求解。[注275]例如，合一`(?x ?x)`和`((a ?y c) (a b ?z))`可以被视为指定联立方程

**校订后**

合一算法是查询系统中技术难度最高的部分。对于复杂模式，执行合一似乎需要推理。例如，为了合一`(?x ?x)`和`((a ?y c) (a b ?z))`，算法必须推断出`?x`应为`(a b c)`，`?y`应为`b`，以及`?z`应为`c`。我们可以将此过程视为求解模式组件之间的一组方程。一般来说，这些是联立方程，可能需要大量操作才能求解。[注275]例如，合一`(?x ?x)`和`((a ?y c) (a b ?z))`可以被视为指定联立方程

### 4_002e4:0159

**原文**

resulting in a frame specifying that `?person-2` is bound to `(Hacker Alyssa P)` and that `?x` should be bound to (have the same value as) `?person-1`. Now, relative to this frame, we evaluate the compound query given by the body of the rule. Successful matches will extend this frame by providing a binding for `?person-1`, and consequently a value for `?x`, which we can use to instantiate the original query pattern.

**校订前**

结果得到一个框架，其中指定`?person-2`绑定到`(Hacker Alyssa P)`，并且`?x`应绑定到（具有与`?person-1`相同的值）。现在，相对于这个框架，我们求值由规则体给出的复合查询。成功的匹配将通过提供`?person-1`的绑定来扩展这个框架，并因此提供`?x`的值，我们可以用它来实例化原始查询模式。

**校订后**

结果得到一个框架，其中指定`?person-2`绑定到`(Hacker Alyssa P)`，并且`?x`应绑定到`?person-1`（即具有相同的值）。现在，相对于这个框架，我们求值由规则体给出的复合查询。成功的匹配将通过提供`?person-1`的绑定来扩展这个框架，并因此提供`?x`的值，我们可以用它来实例化原始查询模式。

### 4_002e4:0178

**原文**

The means of combination used in the query language may at first seem identical to the operations `and`, `or`, and `not` of mathematical logic, and the application of query-language rules is in fact accomplished through a legitimate method of inference.[注279] This identification of the query language with mathematical logic is not really valid, though, because the query language provides a control structure that interprets the logical statements procedurally. We can often take advantage of this control structure. For example, to find all of the supervisors of programmers we could formulate a query in either of two logically equivalent forms:

**校订前**

查询语言中使用的组合手段初看起来可能与数学逻辑中的运算`and`、`or`和`not`完全相同，而查询语言规则的应用实际上是通过一种合法的推理方法完成的。[注279]然而，将查询语言等同于数学逻辑并不真正成立，因为查询语言提供了一种控制结构，它以过程性的方式解释逻辑陈述。我们常常可以利用这种控制结构。例如，要找出所有程序员的 supervisor，我们可以用两种逻辑上等价的形式之一来构造查询：

**校订后**

查询语言中使用的组合手段初看起来可能与数学逻辑中的运算`and`、`or`和`not`完全相同，而查询语言规则的应用实际上是通过一种合法的推理方法完成的。[注279]然而，将查询语言等同于数学逻辑并不真正成立，因为查询语言提供了一种控制结构，它以过程性的方式解释逻辑陈述。我们常常可以利用这种控制结构。例如，要找出所有程序员的 主管，我们可以用两种逻辑上等价的形式之一来构造查询：

### 4_002e4:0180

**原文**

If a company has many more supervisors than programmers (the usual case), it is better to use the first form rather than the second because the data base must be scanned for each intermediate result (frame) produced by the first clause of the `and`.

**校订前**

如果一家公司的 supervisor 比程序员多得多（这是常见情况），那么使用第一种形式比第二种形式更好，因为对于`and`的第一个子句产生的每个中间结果（框架），都必须扫描数据库。

**校订后**

如果一家公司的 主管 比程序员多得多（这是常见情况），那么使用第一种形式比第二种形式更好，因为对于`and`的第一个子句产生的每个中间结果（框架），都必须扫描数据库。

### 4_002e4:0201

**原文**

Exercise 4.65: Cy D. Fect, looking forward to the day when he will rise in the organization, gives a query to find all the wheels (using the `wheel` rule of 4.4.1):

**校订前**

习题 4.65：Cy D. Fect 期盼着有朝一日能在组织中晋升，他发出一个查询来找出所有的轮子（使用 4.4.1 的 `wheel` 规则）：

**校订后**

习题 4.65：Cy D. Fect 期盼着有朝一日能在组织中晋升，他发出一个查询来找出所有的大人物（使用 4.4.1 的 `wheel` 规则）：

### 4_002e4:0215

**原文**

Here, as in the other evaluators in this chapter, we use an abstract syntax for the expressions of the query language. The implementation of the expression syntax, including the predicate `assertion-to-be-added?` and the selector `add-assertion-body`, is given in 4.4.4.7. `Add-rule-or-assertion!` is defined in 4.4.4.5.

**校订前**

这里，如同本章中的其他求值器一样，我们对查询语言的表达式使用抽象语法。表达式语法的实现，包括谓词 `assertion-to-be-added?` 和选择器 `add-assertion-body`，在 4.4.4.7 中给出。`Add-rule-or-assertion!` 定义在 4.4.4.5 中。

**校订后**

这里，如同本章中的其他求值器一样，我们对查询语言的表达式使用抽象语法。表达式语法的实现，包括谓词 `assertion-to-be-added?` 和选择函数 `add-assertion-body`，在 4.4.4.7 中给出。`Add-rule-or-assertion!` 定义在 4.4.4.5 中。

### 4_002e4:0230

**原文**

The predicates and selectors for the syntax of conjuncts and disjuncts are given in 4.4.4.7.

**校订前**

合取项和析取项语法的谓词和选择器在4.4.4.7中给出。

**校订后**

合取项和析取项语法的谓词和选择函数在4.4.4.7中给出。

### 4_002e4:0235

**原文**

The `always-true` special form provides for a query that is always satisfied. It ignores its contents (normally empty) and simply passes through all the frames in the input stream. `Always-true` is used by the `rule-body` selector (4.4.4.7) to provide bodies for rules that were defined without bodies (that is, rules whose conclusions are always satisfied).

**校订前**

`always-true`特殊形式提供了一种总是被满足的查询。它忽略其内容（通常为空），并简单地传递输入流中的所有框架。`Always-true`被`rule-body`选择器（4.4.4.7）用于为没有定义体的规则（即结论总是被满足的规则）提供体。

**校订后**

`always-true`特殊形式提供了一种总是被满足的查询。它忽略其内容（通常为空），并简单地传递输入流中的所有框架。`Always-true`被`rule-body`选择函数（4.4.4.7）用于为没有定义体的规则（即结论总是被满足的规则）提供体。

### 4_002e4:0236

**原文**

The selectors that define the syntax of `not` and `lisp-value` are given in 4.4.4.7.

**校订前**

定义`not`和`lisp-value`语法的选择器在4.4.4.7中给出。

**校订后**

定义`not`和`lisp-value`语法的选择函数在4.4.4.7中给出。

### 4_002e4:0245

**原文**

If a pattern contains a dot followed by a pattern variable, the pattern variable matches the rest of the data list (rather than the next element of the data list), just as one would expect with the dotted-tail notation described in Exercise 2.20. Although the pattern matcher we have just implemented doesn’t look for dots, it does behave as we want. This is because the Lisp `read` primitive, which is used by `query-driver-loop` to read the query and represent it as a list structure, treats dots in a special way.

**校订前**

如果一个模式包含一个点后跟一个模式变量，该模式变量匹配数据列表的剩余部分（而不是数据列表的下一个元素），正如在 习题 2.20 中描述的点尾表示法所预期的那样。尽管我们刚刚实现的模式匹配器不查找点，但它的行为符合我们的期望。这是因为 Lisp 的 `read` 基本过程，被 `query-driver-loop` 用来读取查询并将其表示为列表结构，对点进行了特殊处理。

**校订后**

如果一个模式包含一个点后跟一个模式变量，该模式变量匹配数据表的剩余部分（而不是数据表的下一个元素），正如在 习题 2.20 中描述的点尾表示法所预期的那样。尽管我们刚刚实现的模式匹配器不查找点，但它的行为符合我们的期望。这是因为 Lisp 的 `read` 基本过程，被 `query-driver-loop` 用来读取查询并将其表示为表结构，对点进行了特殊处理。

### 4_002e4:0246

**原文**

When `read` sees a dot, instead of making the next item be the next element of a list (the `car` of a `cons` whose `cdr` will be the rest of the list) it makes the next item be the `cdr` of the list structure. For example, the list structure produced by `read` for the pattern `(computer ?type)` could be constructed by evaluating the expression `(cons 'computer (cons '?type '()))`, and that for `(computer . ?type)` could be constructed by evaluating the expression `(cons 'computer '?type)`.

**校订前**

当 `read` 看到点时，它不会让下一个项成为列表的下一个元素（即 `cons` 的 `car`，其 `cdr` 将是列表的剩余部分），而是让下一个项成为列表结构的 `cdr`。例如，`read` 为模式 `(computer ?type)` 产生的列表结构可以通过求值表达式 `(cons 'computer (cons '?type '()))` 来构造，而为 `(computer . ?type)` 产生的列表结构可以通过求值表达式 `(cons 'computer '?type)` 来构造。

**校订后**

当 `read` 看到点时，它不会让下一个项成为表的下一个元素（即 `cons` 的 `car`，其 `cdr` 将是表的剩余部分），而是让下一个项成为表结构的 `cdr`。例如，`read` 为模式 `(computer ?type)` 产生的表结构可以通过求值表达式 `(cons 'computer (cons '?type '()))` 来构造，而为 `(computer . ?type)` 产生的表结构可以通过求值表达式 `(cons 'computer '?type)` 来构造。

### 4_002e4:0247

**原文**

Thus, as `pattern-match` recursively compares `car`s and `cdr`s of a data list and a pattern that had a dot, it eventually matches the variable after the dot (which is a `cdr` of the pattern) against a sublist of the data list, binding the variable to that list. For example, matching the pattern `(computer . ?type)` against `(computer programmer trainee)` will match `?type` against the list `(programmer trainee)`.

**校订前**

因此，当 `pattern-match` 递归地比较数据列表和带点的模式的 `car` 和 `cdr` 时，它最终将点后的变量（即模式的 `cdr`）与数据列表的子列表进行匹配，将变量绑定到该列表。例如，将模式 `(computer . ?type)` 与 `(computer programmer trainee)` 匹配将把 `?type` 与列表 `(programmer trainee)` 匹配。

**校订后**

因此，当 `pattern-match` 递归地比较数据表和带点的模式的 `car` 和 `cdr` 时，它最终将点后的变量（即模式的 `cdr`）与数据表的子表进行匹配，将变量绑定到该表。例如，将模式 `(computer . ?type)` 与 `(computer programmer trainee)` 匹配将把 `?type` 与表 `(programmer trainee)` 匹配。

### 4_002e4:0252

**原文**

The selectors `rule-body` and `conclusion` that extract parts of a rule are defined in 4.4.4.7.

**校订前**

提取规则部分的选取函数 `rule-body` 和 `conclusion` 定义在 4.4.4.7 中。

**校订后**

提取规则部分的选择函数 `rule-body` 和 `conclusion` 定义在 4.4.4.7 中。

### 4_002e4:0257

**原文**

`Depends-on?` is a predicate that tests whether an expression proposed to be the value of a pattern variable depends on the variable. This must be done relative to the current frame because the expression may contain occurrences of a variable that already has a value that depends on our test variable. The structure of `depends-on?` is a simple recursive tree walk in which we substitute for the values of variables whenever necessary.

**校订前**

`Depends-on?`是一个谓词，用于测试一个被提议作为模式变量值的表达式是否依赖于该变量。这必须相对于当前框架进行，因为该表达式可能包含某个变量的出现，而该变量已经有一个依赖于我们测试变量的值。`depends-on?`的结构是一个简单的递归树遍历，在必要时替换变量的值。

**校订后**

`Depends-on?`是一个谓词，用于测试一个被提议作为模式变量值的表达式是否依赖于该变量。这必须相对于当前框架进行，因为该表达式可能包含某个变量的出现，而该变量已经有一个依赖于我们测试变量的值。`depends-on?`的结构是一个简单的递归树遍历，在必要时用变量的值替换变量。

### 4_002e4:0259

**原文**

One important problem in designing logic programming languages is that of arranging things so that as few irrelevant data-base entries as possible will be examined in checking a given pattern. In our system, in addition to storing all assertions in one big stream, we store all assertions whose `car`s are constant symbols in separate streams, in a table indexed by the symbol. To fetch an assertion that may match a pattern, we first check to see if the `car` of the pattern is a constant symbol. If so, we return (to be tested using the matcher) all the stored assertions that have the same `car`. If the pattern’s `car` is not a constant symbol, we return all the stored assertions. Cleverer methods could also take advantage of information in the frame, or try also to optimize the case where the `car` of the pattern is not a constant symbol. We avoid building our criteria for indexing (using the `car`, handling only the case of constant symbols) into the program; instead we call on predicates and selectors that embody our criteria.

**校订前**

设计逻辑编程语言的一个重要问题是，安排事情使得在检查给定模式时尽可能少地检查不相关的数据库条目。在我们的系统中，除了将所有断言存储在一个大流中之外，我们还将所有`car`为常量符号的断言存储在单独的流中，放在一个以该符号为索引的表中。为了获取可能匹配模式的断言，我们首先检查模式的`car`是否为常量符号。如果是，我们返回（用匹配器测试）所有具有相同`car`的已存储断言。如果模式的`car`不是常量符号，我们返回所有已存储的断言。更聪明的方法还可以利用框架中的信息，或者尝试优化模式的`car`不是常量符号的情况。我们避免将索引标准（使用`car`，仅处理常量符号的情况）构建到程序中；相反，我们调用体现我们标准的谓词和选择器。

**校订后**

设计逻辑编程语言的一个重要问题是，安排事情使得在检查给定模式时尽可能少地检查不相关的数据库条目。在我们的系统中，除了将所有断言存储在一个大流中之外，我们还将所有`car`为常量符号的断言存储在单独的流中，放在一个以该符号为索引的表中。为了获取可能匹配模式的断言，我们首先检查模式的`car`是否为常量符号。如果是，我们返回（用匹配器测试）所有具有相同`car`的已存储断言。如果模式的`car`不是常量符号，我们返回所有已存储的断言。更聪明的方法还可以利用框架中的信息，或者尝试优化模式的`car`不是常量符号的情况。我们避免将索引标准（使用`car`，仅处理常量符号的情况）构建到程序中；相反，我们调用体现我们标准的谓词和选择函数。

### 4_002e4:0271

**原文**

`Stream-flatmap`, which is used throughout the query evaluator to map a procedure over a stream of frames and combine the resulting streams of frames, is the stream analog of the `flatmap` procedure introduced for ordinary lists in 2.2.3. Unlike ordinary `flatmap`, however, we accumulate the streams with an interleaving process, rather than simply appending them (see Exercise 4.72 and Exercise 4.73).

**校订前**

`Stream-flatmap`在整个查询求值器中用于将一个过程映射到一个框架流上，并组合得到的框架流，它是2.2.3中为普通表引入的`flatmap`过程的流模拟。然而，与普通的`flatmap`不同，我们使用交错过程来累积流，而不是简单地追加它们（见习题4.72和习题4.73）。

**校订后**

`Stream-flatmap`在整个查询求值器中用于将一个过程映射到一个框架流上，并组合得到的框架流，它是2.2.3中为普通表引入的`flatmap`过程的流版本。然而，与普通的`flatmap`不同，我们使用交错过程来累积流，而不是简单地追加它们（见习题4.72和习题4.73）。

### 4_002e4:0293

**原文**

since Ben is the only computer wizard, and

**校订前**

因为 Ben 是唯一的计算机巫师，而

**校订后**

因为 Ben 是唯一的计算机奇才，而

### 4_002e4:0300

**原文**

Exercise 4.76: Our implementation of `and` as a series combination of queries (Figure 4.5) is elegant, but it is inefficient because in processing the second query of the `and` we must scan the data base for each frame produced by the first query. If the data base has $n$ elements, and a typical query produces a number of output frames proportional to $n$ (say $n/k$), then scanning the data base for each frame produced by the first query will require $n^(2)/k$ calls to the pattern matcher. Another approach would be to process the two clauses of the `and` separately, then look for all pairs of output frames that are compatible. If each query produces $n/k$ output frames, then this means that we must perform $n^(2)/k^(2)$ compatibility checks—a factor of $k$ fewer than the number of matches required in our current method.

**校订前**

习题 4.76：我们将 `and` 实现为查询的串行组合（图 4.5）很优雅，但效率低下，因为在处理 `and` 的第二个查询时，我们必须为第一个查询产生的每个框架扫描数据库。如果数据库有 $n$ 个元素，而一个典型查询产生的输出框架数量与 $n$ 成正比（比如 $n/k$），那么为第一个查询产生的每个框架扫描数据库将需要 $n^(2)/k$ 次模式匹配器调用。另一种方法是分别处理 `and` 的两个子句，然后寻找所有兼容的输出框架对。如果每个查询产生 $n/k$ 个输出框架，那么这意味着我们必须执行 $n^(2)/k^(2)$ 次兼容性检查——比我们当前方法所需的匹配次数少一个因子 $k$。

**校订后**

习题 4.76：我们将 `and` 实现为查询的串行组合（图 4.5）很优雅，但效率低下，因为在处理 `and` 的第二个查询时，我们必须为第一个查询产生的每个框架扫描数据库。如果数据库有 $n$ 个元素，而一个典型查询产生的输出框架数量与 $n$ 成正比（比如 $n/k$），那么为第一个查询产生的每个框架扫描数据库将需要 $n^(2)/k$ 次模式匹配器调用。另一种方法是分别处理 `and` 的两个子句，然后寻找所有兼容的输出框架对。如果每个查询产生 $n/k$ 个输出框架，那么这意味着我们必须执行 $n^(2)/k^(2)$ 次兼容性检查——是我们当前方法所需匹配次数的 $k$ 分之一。

### 4_002e4:0322

**原文**

[注276] Another way to think of unification is that it generates the most general pattern that is a specialization of the two input patterns. That is, the unification of `(?x a)` and `((b ?y) ?z)` is `((b ?y) a)`, and the unification of `(?x a ?y)` and `(?y ?z a)`, discussed above, is `(a a a)`. For our implementation, it is more convenient to think of the result of unification as a frame rather than a pattern.

**校订前**

[注276]思考统一的另一种方式是，它生成最一般的模式，该模式是两个输入模式的特殊化。也就是说，`(?x a)`和`((b ?y) ?z)`的统一是`((b ?y) a)`，而上面讨论的`(?x a ?y)`和`(?y ?z a)`的统一是`(a a a)`。对于我们的实现，将统一的结果视为框架而不是模式更为方便。

**校订后**

[注276]思考合一的另一种方式是，它生成最一般的模式，该模式是两个输入模式的特殊化。也就是说，`(?x a)`和`((b ?y) ?z)`的合一是`((b ?y) a)`，而上面讨论的`(?x a ?y)`和`(?y ?z a)`的合一是`(a a a)`。对于我们的实现，将合一的结果视为框架而不是模式更为方便。

### 4_002e4:0323

**原文**

[注277] Since unification is a generalization of matching, we could simplify the system by using the unifier to produce both streams. Treating the easy case with the simple matcher, however, illustrates how matching (as opposed to full-blown unification) can be useful in its own right.

**校订前**

[注277]由于统一是匹配的推广，我们可以通过使用统一器来产生两个流，从而简化系统。然而，用简单匹配器处理简单情况说明了匹配（与完全统一相对）本身如何有用。

**校订后**

[注277]由于合一是匹配的推广，我们可以通过使用合一器来产生两个流，从而简化系统。然而，用简单匹配器处理简单情况说明了匹配（与完全合一相对）本身如何有用。

### 4_002e4:0330

**原文**

[注284] In general, unifying `?y` with an expression involving `?y` would require our being able to find a fixed point of the equation `?y` = `⟨``expression involving ?y``⟩`. It is sometimes possible to syntactically form an expression that appears to be the solution. For example, `?y` = `(f ?y)` seems to have the fixed point `(f (f (f … )))`, which we can produce by beginning with the expression `(f ?y)` and repeatedly substituting `(f ?y)` for `?y`. Unfortunately, not every such equation has a meaningful fixed point. The issues that arise here are similar to the issues of manipulating infinite series in mathematics. For example, we know that 2 is the solution to the equation $y=1+y/2$. Beginning with the expression $1+y/2$ and repeatedly substituting $1+y/2$ for $y$ gives $2=y=1+(y)/(2)=1+(1)/(2)(1+(y)/(2))=1+(1)/(2)+(y)/(4)=…,$ which leads to $2=1+(1)/(2)+(1)/(4)+(1)/(8)+….$ However, if we try the same manipulation beginning with the observation that $−1$ is the solution to the equation $y=1+2y$, we obtain $−1=y=1+2y=1+2(1+2y)=1+2+4y=…,$ which leads to $−1=1+2+4+8+….$ Although the formal manipulations used in deriving these two equations are identical, the first result is a valid assertion about infinite series but the second is not. Similarly, for our unification results, reasoning with an arbitrary syntactically constructed expression may lead to errors.

**校订前**

[注284] 一般来说，将 `?y` 与一个涉及 `?y` 的表达式统一，需要我们能够找到方程 `?y` = `⟨``expression involving ?y``⟩` 的不动点。有时可以语法上构造出一个看似是解的表达式。例如，`?y` = `(f ?y)` 似乎有不动点 `(f (f (f … )))`，我们可以从表达式 `(f ?y)` 开始，反复用 `(f ?y)` 代换 `?y` 来产生它。不幸的是，并非每个这样的方程都有有意义的不动点。这里出现的问题类似于数学中处理无穷级数的问题。例如，我们知道 2 是方程 $y=1+y/2$ 的解。从表达式 $1+y/2$ 开始，反复用 $1+y/2$ 代换 $y$ 得到 $2=y=1+(y)/(2)=1+(1)/(2)(1+(y)/(2))=1+(1)/(2)+(y)/(4)=…,$，这导致 $2=1+(1)/(2)+(1)/(4)+(1)/(8)+….$。然而，如果我们从观察 $−1$ 是方程 $y=1+2y$ 的解开始尝试同样的操作，我们得到 $−1=y=1+2y=1+2(1+2y)=1+2+4y=…,$，这导致 $−1=1+2+4+8+….$。尽管在推导这两个方程时所用的形式操作是相同的，但第一个结果是对无穷级数的有效断言，而第二个则不是。类似地，对于我们的统一结果，用任意语法构造的表达式进行推理可能会导致错误。

**校订后**

[注284] 一般来说，将 `?y` 与一个涉及 `?y` 的表达式合一，需要我们能够找到方程 `?y` = `⟨``expression involving ?y``⟩` 的不动点。有时可以语法上构造出一个看似是解的表达式。例如，`?y` = `(f ?y)` 似乎有不动点 `(f (f (f … )))`，我们可以从表达式 `(f ?y)` 开始，反复用 `(f ?y)` 代换 `?y` 来产生它。不幸的是，并非每个这样的方程都有有意义的不动点。这里出现的问题类似于数学中处理无穷级数的问题。例如，我们知道 2 是方程 $y=1+y/2$ 的解。从表达式 $1+y/2$ 开始，反复用 $1+y/2$ 代换 $y$ 得到 $2=y=1+(y)/(2)=1+(1)/(2)(1+(y)/(2))=1+(1)/(2)+(y)/(4)=…,$，这导致 $2=1+(1)/(2)+(1)/(4)+(1)/(8)+….$。然而，如果我们从观察 $−1$ 是方程 $y=1+2y$ 的解开始尝试同样的操作，我们得到 $−1=y=1+2y=1+2(1+2y)=1+2+4y=…,$，这导致 $−1=1+2+4+8+….$。尽管在推导这两个方程时所用的形式操作是相同的，但第一个结果是对无穷级数的有效断言，而第二个则不是。类似地，对于我们的合一结果，用任意语法构造的表达式进行推理可能会导致错误。

### 5_002e1:0062

**原文**

Nevertheless, we can implement the factorial process as a register machine if we can arrange to use the same components for each nested instance of the machine. Specifically, the machine that computes $n!$ should use the same components to work on the subproblem of computing $(n−1)!$, on the subproblem for $(n−2)!$, and so on. This is plausible because, although the factorial process dictates that an unbounded number of copies of the same machine are needed to perform a computation, only one of these copies needs to be active at any given time. When the machine encounters a recursive subproblem, it can suspend work on the main problem, reuse the same physical parts to work on the subproblem, then continue the suspended computation.

**校订前**

尽管如此，如果我们能够安排对机器的每个嵌套实例使用相同的组件，我们就可以将阶乘计算过程实现为寄存器机器。具体来说，计算 $n!$ 的机器应该使用相同的组件来处理计算 $(n−1)!$ 的子问题、计算 $(n−2)!$ 的子问题，等等。这是合理的，因为尽管阶乘计算过程要求使用无限多份相同机器的副本来执行计算，但在任何给定时刻只需要其中一份处于活动状态。当机器遇到递归子问题时，它可以暂停主问题上的工作，重用相同的物理部件来处理子问题，然后继续被暂停的计算。

**校订后**

尽管如此，如果我们能够安排对机器的每个嵌套实例使用相同的组件，我们就可以将阶乘计算过程实现为寄存器机器。具体来说，计算 $n!$ 的机器应该使用相同的组件来处理计算 $(n−1)!$ 的子问题、计算 $(n−2)!$ 的子问题，等等。这是合理的，因为尽管阶乘计算过程要求使用数量没有上限的相同机器副本来执行计算，但在任何给定时刻只需要其中一份处于活动状态。当机器遇到递归子问题时，它可以暂停主问题上的工作，重用相同的物理部件来处理子问题，然后继续被暂停的计算。

### 5_002e1:0065

**原文**

With the aid of the stack, we can reuse a single copy of the factorial machine’s data paths for each factorial subproblem. There is a similar design issue in reusing the controller sequence that operates the data paths. To reexecute the factorial computation, the controller cannot simply loop back to the beginning, as with an iterative process, because after solving the $(n−1)!$ subproblem the machine must still multiply the result by $n$. The controller must suspend its computation of $n!$, solve the $(n−1)!$ subproblem, then continue its computation of $n!$. This view of the factorial computation suggests the use of the subroutine mechanism described in 5.1.3, which has the controller use a `continue` register to transfer to the part of the sequence that solves a subproblem and then continue where it left off on the main problem. We can thus make a factorial subroutine that returns to the entry point stored in the `continue` register. Around each subroutine call, we save and restore `continue` just as we do the `n` register, since each “level” of the factorial computation will use the same `continue` register. That is, the factorial subroutine must put a new value in `continue` when it calls itself for a subproblem, but it will need the old value in order to return to the place that called it to solve a subproblem.

**校订前**

借助栈，我们可以为每个阶乘子问题重用阶乘机器数据路径的单一副本。在重用操作数据路径的控制器序列时也存在类似的设计问题。为了重新执行阶乘计算，控制器不能像迭代过程那样简单地循环回开头，因为在求解$(n−1)!$子问题之后，机器仍然必须将结果乘以$n$。控制器必须暂停其对$n!$的计算，求解$(n−1)!$子问题，然后继续其对$n!$的计算。这种对阶乘计算的看法表明应使用5.1.3中描述的子程序机制，该机制让控制器使用`continue`寄存器转移到序列中求解子问题的部分，然后在主问题上从离开的地方继续。因此，我们可以制作一个阶乘子程序，返回到存储在`continue`寄存器中的入口点。在每次子程序调用前后，我们保存和恢复`continue`，就像我们对`n`寄存器所做的那样，因为阶乘计算的每个“层级”都将使用相同的`continue`寄存器。也就是说，阶乘子程序在为一个子问题调用自身时必须将新值放入`continue`，但它将需要旧值以便返回到调用它求解子问题的位置。

**校订后**

借助栈，我们可以为每个阶乘子问题重用阶乘机器数据通路的单一副本。在重用操作数据通路的控制器序列时也存在类似的设计问题。为了重新执行阶乘计算，控制器不能像迭代计算过程那样简单地循环回开头，因为在求解$(n−1)!$子问题之后，机器仍然必须将结果乘以$n$。控制器必须暂停其对$n!$的计算，求解$(n−1)!$子问题，然后继续其对$n!$的计算。这种对阶乘计算的看法表明应使用5.1.3中描述的子程序机制，该机制让控制器使用`continue`寄存器转移到序列中求解子问题的部分，然后在主问题上从离开的地方继续。因此，我们可以制作一个阶乘子程序，返回到存储在`continue`寄存器中的入口点。在每次子程序调用前后，我们保存和恢复`continue`，就像我们对`n`寄存器所做的那样，因为阶乘计算的每个“层级”都将使用相同的`continue`寄存器。也就是说，阶乘子程序在为一个子问题调用自身时必须将新值放入`continue`，但它将需要旧值以便返回到调用它求解子问题的位置。

### 5_002e1:0066

**原文**

Figure 5.11 shows the data paths and controller for a machine that implements the recursive `factorial` procedure. The machine has a stack and three registers, called `n`, `val`, and `continue`. To simplify the data-path diagram, we have not named the register-assignment buttons, only the stack-operation buttons (`sc` and `sn` to save registers, `rc` and `rn` to restore registers). To operate the machine, we put in register `n` the number whose factorial we wish to compute and start the machine. When the machine reaches `fact-done`, the computation is finished and the answer will be found in the `val` register. In the controller sequence, `n` and `continue` are saved before each recursive call and restored upon return from the call. Returning from a call is accomplished by branching to the location stored in `continue`. `Continue` is initialized when the machine starts so that the last return will go to `fact-done`. The `val` register, which holds the result of the factorial computation, is not saved before the recursive call, because the old contents of `val` is not useful after the subroutine returns. Only the new value, which is the value produced by the subcomputation, is needed.

**校订前**

图5.11展示了实现递归`factorial`过程的机器的数据路径和控制器。该机器有一个栈和三个寄存器，分别称为`n`、`val`和`continue`。为了简化数据路径图，我们没有命名寄存器赋值按钮，只命名了栈操作按钮（`sc`和`sn`用于保存寄存器，`rc`和`rn`用于恢复寄存器）。要操作该机器，我们将希望计算其阶乘的数放入寄存器`n`并启动机器。当机器到达`fact-done`时，计算完成，答案将在`val`寄存器中找到。在控制器序列中，`n`和`continue`在每次递归调用之前被保存，并在调用返回时恢复。从调用返回是通过分支到存储在`continue`中的位置来完成的。`Continue`在机器启动时初始化，以便最后一次返回将转到`fact-done`。保存阶乘计算结果的`val`寄存器在递归调用之前不被保存，因为`val`的旧内容在子程序返回后没有用处。只需要新值，即子计算产生的值。

**校订后**

图5.11展示了实现递归`factorial`过程的机器的数据通路和控制器。该机器有一个栈和三个寄存器，分别称为`n`、`val`和`continue`。为了简化数据通路图，我们没有命名寄存器赋值按钮，只命名了栈操作按钮（`sc`和`sn`用于保存寄存器，`rc`和`rn`用于恢复寄存器）。要操作该机器，我们将希望计算其阶乘的数放入寄存器`n`并启动机器。当机器到达`fact-done`时，计算完成，答案将在`val`寄存器中找到。在控制器序列中，`n`和`continue`在每次递归调用之前被保存，并在调用返回时恢复。从调用返回是通过分支到存储在`continue`中的位置来完成的。`Continue`在机器启动时初始化，以便最后一次返回将转到`fact-done`。保存阶乘计算结果的`val`寄存器在递归调用之前不被保存，因为`val`的旧内容在子程序返回后没有用处。只需要新值，即子计算产生的值。

### 5_002e1:0070

**原文**

Let us examine a more complex recursive process, the tree-recursive computation of the Fibonacci numbers, which we introduced in 1.2.2:

**校订前**

让我们考察一个更复杂的递归过程，即斐波那契数的树递归计算，我们在1.2.2中介绍过它：

**校订后**

让我们考察一个更复杂的递归计算过程，即斐波那契数的树形递归计算，我们在1.2.2中介绍过它：

### 5_002e1:0073

**原文**

Exercise 5.4: Specify register machines that implement each of the following procedures. For each machine, write a controller instruction sequence and draw a diagram showing the data paths.

**校订前**

习题5.4： 指定实现以下每个过程的寄存器机器。对于每台机器，编写控制器指令序列并绘制显示数据路径的图。

**校订后**

习题5.4： 指定实现以下每个过程的寄存器机器。对于每台机器，编写控制器指令序列并绘制显示数据通路的图。

### 5_002e1:0076

**原文**

Exercise 5.5: Hand-simulate the factorial and Fibonacci machines, using some nontrivial input (requiring execution of at least one recursive call). Show the contents of the stack at each significant point in the execution.

**校订前**

习题 5.5： 使用某个非平凡输入（要求至少执行一次递归调用）手工模拟阶乘机器和 Fibonacci 机器。展示执行过程中每个重要时刻栈的内容。

**校订后**

习题 5.5： 使用某个非平凡输入（要求至少执行一次递归调用）手工模拟阶乘机器和 斐波那契 机器。展示执行过程中每个重要时刻栈的内容。

### 5_002e1:0077

**原文**

Exercise 5.6: Ben Bitdiddle observes that the Fibonacci machine’s controller sequence has an extra `save` and an extra `restore`, which can be removed to make a faster machine. Where are these instructions?

**校订前**

习题 5.6： Ben Bitdiddle 观察到 Fibonacci 机器的控制器序列中多了一条 `save` 和一条 `restore`，去掉它们可以使机器更快。这些指令在哪里？

**校订后**

习题 5.6： Ben Bitdiddle 观察到 斐波那契 机器的控制器序列中多了一条 `save` 和一条 `restore`，去掉它们可以使机器更快。这些指令在哪里？

### 5_002e2:0037

**原文**

`Extract-labels` takes as arguments a list `text` (the sequence of controller instruction expressions) and a `receive` procedure. `Receive` will be called with two values: (1) a list `insts` of instruction data structures, each containing an instruction from `text`; and (2) a table called `labels`, which associates each label from `text` with the position in the list `insts` that the label designates.

**校订前**

`Extract-labels` 以表 `text`（控制器指令表达式的序列）和 `receive` 过程为参数。`Receive` 将被调用，并带有两个值：(1) 一个指令数据结构表 `insts`，其中每个数据结构包含来自 `text` 的一条指令；以及 (2) 一个称为 `labels` 的表，它将来自 `text` 的每个标签与表 `insts` 中该标签所指定的位置关联起来。

**校订后**

`Extract-labels` 以表 `text`（控制器指令表达式的序列）和 `receive` 过程为参数。`Receive` 将被调用，并带有两个值：(1) 一个指令数据结构表 `insts`，其中每个数据结构包含来自 `text` 的一条指令；以及 (2) 一个称为 `labels` 的表，它将来自 `text` 的每个标号与表 `insts` 中该标号所指定的位置关联起来。

### 5_002e2:0051

**原文**

`Make-assign` extracts the target register name (the second element of the instruction) and the value expression (the rest of the list that forms the instruction) from the `assign` instruction using the selectors

**校订前**

`Make-assign` 使用选择器从 `assign` 指令中提取目标寄存器名（指令的第二个元素）和值表达式（构成指令的表的其余部分）

**校订后**

`Make-assign` 使用选择函数从 `assign` 指令中提取目标寄存器名（指令的第二个元素）和值表达式（构成指令的表的其余部分）

### 5_002e2:0060

**原文**

The stack instructions `save` and `restore` simply use the stack with the designated register and advance the `pc`:

**校订前**

栈指令 `save` 和 `restore` 只是用指定的寄存器使用栈，并推进 `pc`：

**校订后**

栈指令 `save` 和 `restore` 只是针对指定的寄存器执行栈操作，并推进 `pc`：

### 5_002e2:0065

**原文**

`Assign`, `perform`, and `test` instructions may include the application of a machine operation (specified by an `op` expression) to some operands (specified by `reg` and `const` expressions). The following procedure produces an execution procedure for an “operation expression”—a list containing the operation and operand expressions from the instruction:

**校订前**

`Assign`、`perform` 和 `test` 指令可以包括把一个机器运算（由 `op` 表达式指定）应用于某些操作数（由 `reg` 和 `const` 表达式指定）。下面的过程为一个“运算表达式”——一个包含指令中的运算和操作数表达式的表——产生一个执行过程：

**校订后**

`Assign`、`perform` 和 `test` 指令可以包括把一个机器运算（由 `op` 表达式指定）应用于某些运算对象（由 `reg` 和 `const` 表达式指定）。下面的过程为一个“运算表达式”——一个包含指令中的运算和运算对象表达式的表——产生一个执行过程：

### 5_002e2:0067

**原文**

Observe that the treatment of operation expressions is very much like the treatment of procedure applications by the `analyze-application` procedure in the evaluator of 4.1.7 in that we generate an execution procedure for each operand. At simulation time, we call the operand procedures and apply the Scheme procedure that simulates the operation to the resulting values. The simulation procedure is found by looking up the operation name in the operation table for the machine:

**校订前**

注意，对运算表达式的处理非常类似于4.1.7的求值器中`analyze-application`过程对过程应用的处理，因为我们为每个操作数生成一个执行过程。在模拟时，我们调用操作数过程，并将模拟该运算的 Scheme 过程应用于结果值。模拟过程是通过在机器的操作表中查找运算名称而找到的：

**校订后**

注意，对运算表达式的处理非常类似于4.1.7的求值器中`analyze-application`过程对过程应用的处理，因为我们为每个运算对象生成一个执行过程。在模拟时，我们调用运算对象过程，并将模拟该运算的 Scheme 过程应用于结果值。模拟过程是通过在机器的运算表中查找运算名称而找到的：

### 5_002e2:0068

**原文**

Exercise 5.9: The treatment of machine operations above permits them to operate on labels as well as on constants and the contents of registers. Modify the expression-processing procedures to enforce the condition that operations can be used only with registers and constants.

**校订前**

习题 5.9： 上述对机器运算的处理允许它们对标签以及常量和寄存器的内容进行操作。修改表达式处理过程，以强制实施运算只能用于寄存器和常量的条件。

**校订后**

习题 5.9： 上述对机器运算的处理允许它们对标号以及常量和寄存器的内容进行操作。修改表达式处理过程，以强制实施运算只能用于寄存器和常量的条件。

### 5_002e2:0072

**原文**

`(restore y)` puts into `y` the last value saved on the stack, regardless of what register that value came from. This is the way our simulator behaves. Show how to take advantage of this behavior to eliminate one instruction from the Fibonacci machine of 5.1.4 (Figure 5.12).

**校订前**

`(restore y)`将栈上最后保存的值放入`y`，无论该值来自哪个寄存器。这就是我们的模拟器的行为方式。展示如何利用这种行为从5.1.4的 Fibonacci 机器（图 5.12）中消除一条指令。

**校订后**

`(restore y)`将栈上最后保存的值放入`y`，无论该值来自哪个寄存器。这就是我们的模拟器的行为方式。展示如何利用这种行为从5.1.4的 斐波那契 机器（图 5.12）中消除一条指令。

### 5_002e2:0076

**原文**

a list of all instructions, with duplicates removed, sorted by instruction type (`assign`, `goto`, and so on);

**校订前**

所有指令的列表，去除重复项，按指令类型排序（`assign`、`goto`等）；

**校订后**

所有指令的表，去除重复项，按指令类型排序（`assign`、`goto`等）；

### 5_002e2:0077

**原文**

a list (without duplicates) of the registers used to hold entry points (these are the registers referenced by `goto` instructions);

**校订前**

用于保存入口点的寄存器的列表（无重复项）（这些是`goto`指令引用的寄存器）；

**校订后**

用于保存入口点的寄存器的表（无重复项）（这些是`goto`指令引用的寄存器）；

### 5_002e2:0078

**原文**

a list (without duplicates) of the registers that are `save`d or `restore`d;

**校订前**

被`save`或`restore`的寄存器的列表（无重复项）；

**校订后**

被`save`或`restore`的寄存器的表（无重复项）；

### 5_002e2:0079

**原文**

for each register, a list (without duplicates) of the sources from which it is assigned (for example, the sources for register `val` in the factorial machine of Figure 5.11 are `(const 1)` and `((op *) (reg n) (reg val))`).

**校订前**

对于每个寄存器，一个从其赋值的来源的列表（无重复项）（例如，图 5.11的阶乘机器中寄存器`val`的来源是`(const 1)`和`((op *) (reg n) (reg val))`）。

**校订后**

对于每个寄存器，一个列出赋给它的值的来源的表（无重复项）（例如，图 5.11的阶乘机器中寄存器`val`的来源是`(const 1)`和`((op *) (reg n) (reg val))`）。

### 5_002e2:0080

**原文**

Extend the message-passing interface to the machine to provide access to this new information. To test your analyzer, define the Fibonacci machine from Figure 5.12 and examine the lists you constructed.

**校订前**

扩展机器的消息传递接口以提供对这些新信息的访问。为了测试你的分析器，定义图 5.12中的 Fibonacci 机器，并检查你构造的列表。

**校订后**

扩展机器的消息传递接口以提供对这些新信息的访问。为了测试你的分析器，定义图 5.12中的 斐波那契 机器，并检查你构造的表。

### 5_002e2:0081

**原文**

Exercise 5.13: Modify the simulator so that it uses the controller sequence to determine what registers the machine has rather than requiring a list of registers as an argument to `make-machine`. Instead of pre-allocating the registers in `make-machine`, you can allocate them one at a time when they are first seen during assembly of the instructions.

**校订前**

习题 5.13： 修改模拟器，使其使用控制器序列来确定机器具有哪些寄存器，而不是要求将寄存器列表作为`make-machine`的参数。与其在`make-machine`中预先分配寄存器，你可以在指令汇编期间首次见到它们时逐个分配。

**校订后**

习题 5.13： 修改模拟器，使其使用控制器序列来确定机器具有哪些寄存器，而不是要求将寄存器表作为`make-machine`的参数。与其在`make-machine`中预先分配寄存器，你可以在指令汇编期间首次见到它们时逐个分配。

### 5_002e2:0089

**原文**

Exercise 5.17: Extend the instruction tracing of Exercise 5.16 so that before printing an instruction, the simulator prints any labels that immediately precede that instruction in the controller sequence. Be careful to do this in a way that does not interfere with instruction counting (Exercise 5.15). You will have to make the simulator retain the necessary label information.

**校订前**

习题 5.17： 扩展习题 5.16的指令跟踪，使得在打印一条指令之前，模拟器打印在控制器序列中紧接在该指令之前的任何标签。注意要以不干扰指令计数的方式做到这一点（习题 5.15）。你必须让模拟器保留必要的标签信息。

**校订后**

习题 5.17： 扩展习题 5.16的指令跟踪，使得在打印一条指令之前，模拟器打印在控制器序列中紧接在该指令之前的任何标号。注意要以不干扰指令计数的方式做到这一点（习题 5.15）。你必须让模拟器保留必要的标号信息。

### 5_002e2:0092

**原文**

that sets a breakpoint just before the $n^(th)$ instruction after the given label. For example,

**校订前**

它在给定标签之后的第$n^(th)$条指令之前设置一个断点。例如，

**校订后**

它在给定标号之后的第$n^(th)$条指令之前设置一个断点。例如，

### 5_002e2:0093

**原文**

installs a breakpoint in `gcd-machine` just before the assignment to register `a`. When the simulator reaches the breakpoint it should print the label and the offset of the breakpoint and stop executing instructions. Alyssa can then use `get-register-contents` and `set-register-contents!` to manipulate the state of the simulated machine. She should then be able to continue execution by saying

**校订前**

在`gcd-machine`中，就在对寄存器`a`的赋值之前安装一个断点。当模拟器到达断点时，它应打印断点的标签和偏移量，并停止执行指令。然后 Alyssa 可以使用`get-register-contents`和`set-register-contents!`来操作被模拟机器的状态。然后她应该能够通过说以下内容来继续执行

**校订后**

在`gcd-machine`中，就在对寄存器`a`的赋值之前安装一个断点。当模拟器到达断点时，它应打印断点的标号和偏移量，并停止执行指令。然后 Alyssa 可以使用`get-register-contents`和`set-register-contents!`来操作被模拟机器的状态。然后她应该能够通过执行以下表达式来继续执行

### 5_002e2:0099

**原文**

You can consider our use of `receive` as demonstrating an elegant way to return multiple values, or simply an excuse to show off a programming trick. An argument like `receive` that is the next procedure to be invoked is called a “continuation.” Recall that we also used continuations to implement the backtracking control structure in the `amb` evaluator in 4.3.3.

**校订前**

你可以认为我们对`receive`的使用展示了一种返回多个值的优雅方式，或者仅仅是一个炫耀编程技巧的借口。像`receive`这样作为下一个被调用过程的自变量被称为“继续过程”。回想一下，我们还在4.3.3的`amb`求值器中使用了继续过程来实现回溯控制结构。

**校订后**

你可以认为我们对`receive`的使用展示了一种返回多个值的优雅方式，或者仅仅是一个炫耀编程技巧的借口。像`receive`这样作为下一个被调用过程的参数被称为“继续过程”。回想一下，我们还在4.3.3的`amb`求值器中使用了继续过程来实现回溯控制结构。

### 5_002e3:0004

**原文**

In section 5.4, we will show how to implement a Scheme evaluator as a register machine. In order to simplify the discussion, we will assume that our register machines can be equipped with a list-structured memory, in which the basic operations for manipulating list-structured data are primitive. Postulating the existence of such a memory is a useful abstraction when one is focusing on the mechanisms of control in a Scheme interpreter, but this does not reflect a realistic view of the actual primitive data operations of contemporary computers. To obtain a more complete picture of how a Lisp system operates, we must investigate how list structure can be represented in a way that is compatible with conventional computer memories.

**校订前**

在5.4节中，我们将展示如何将 Scheme 求值器实现为寄存器机器。为了简化讨论，我们将假设我们的寄存器机器可以配备一个表结构内存，其中用于操作表结构数据的基本操作是基本的。当人们关注 Scheme 解释器中的控制机制时，假设这种内存的存在是一种有用的抽象，但这并不反映当代计算机实际基本数据操作的真实情况。为了更完整地了解 Lisp 系统如何运作，我们必须研究如何以与传统计算机内存兼容的方式表示表结构。

**校订后**

在5.4节中，我们将展示如何将 Scheme 求值器实现为寄存器机器。为了简化讨论，我们将假设我们的寄存器机器可以配备一个表结构内存，其中操作表结构数据所需的基本操作都是机器的基本操作。当人们关注 Scheme 解释器中的控制机制时，假设这种内存的存在是一种有用的抽象，但这并不反映当代计算机实际基本数据操作的真实情况。为了更完整地了解 Lisp 系统如何运作，我们必须研究如何以与传统计算机内存兼容的方式表示表结构。

### 5_002e3:0005

**原文**

There are two considerations in implementing list structure. The first is purely an issue of representation: how to represent the “box-and-pointer” structure of Lisp pairs, using only the storage and addressing capabilities of typical computer memories. The second issue concerns the management of memory as a computation proceeds. The operation of a Lisp system depends crucially on the ability to continually create new data objects. These include objects that are explicitly created by the Lisp procedures being interpreted as well as structures created by the interpreter itself, such as environments and argument lists. Although the constant creation of new data objects would pose no problem on a computer with an infinite amount of rapidly addressable memory, computer memories are available only in finite sizes (more’s the pity). Lisp systems thus provide an automatic storage allocation facility to support the illusion of an infinite memory. When a data object is no longer needed, the memory allocated to it is automatically recycled and used to construct new data objects. There are various techniques for providing such automatic storage allocation. The method we shall discuss in this section is called garbage collection.

**校订前**

实现表结构时有两个考虑因素。第一个纯粹是表示问题：如何仅使用典型计算机内存的存储和寻址能力来表示 Lisp 序对的“盒子和指针”结构。第二个问题涉及计算进行时的内存管理。Lisp 系统的运行关键取决于持续创建新数据对象的能力。这些对象包括被解释的 Lisp 过程显式创建的对象，以及解释器自身创建的结构，例如环境和参数表。尽管在具有无限快速可寻址内存的计算机上，不断创建新数据对象不会造成问题，但计算机内存只有有限的大小（更遗憾的是）。因此，Lisp 系统提供自动存储分配设施来支持无限内存的假象。当一个数据对象不再需要时，分配给它的内存会自动回收并用于构造新的数据对象。有多种技术可以提供这种自动存储分配。我们将在本节讨论的方法称为垃圾回收。

**校订后**

实现表结构时有两个考虑因素。第一个纯粹是表示问题：如何仅使用典型计算机内存的存储和寻址能力来表示 Lisp 序对的“盒指针”结构。第二个问题涉及计算进行时的内存管理。Lisp 系统的运行关键取决于持续创建新数据对象的能力。这些对象包括被解释的 Lisp 过程显式创建的对象，以及解释器自身创建的结构，例如环境和参数表。尽管在具有容量无限且可快速寻址的内存的计算机上，不断创建新数据对象不会造成问题，但计算机内存只有有限的大小（真是遗憾）。因此，Lisp 系统提供自动存储分配设施来支持无限内存的假象。当一个数据对象不再需要时，分配给它的内存会自动回收并用于构造新的数据对象。有多种技术可以提供这种自动存储分配。我们将在本节讨论的方法称为垃圾回收。

### 5_002e3:0013

**原文**

We can use vectors to implement the basic pair structures required for a list-structured memory. Let us imagine that computer memory is divided into two vectors: `the-cars` and `the-cdrs`. We will represent list structure as follows: A pointer to a pair is an index into the two vectors. The `car` of the pair is the entry in `the-cars` with the designated index, and the `cdr` of the pair is the entry in `the-cdrs` with the designated index. We also need a representation for objects other than pairs (such as numbers and symbols) and a way to distinguish one kind of data from another. There are many methods of accomplishing this, but they all reduce to using typed pointers, that is, to extending the notion of “pointer” to include information on data type.[注292] The data type enables the system to distinguish a pointer to a pair (which consists of the “pair” data type and an index into the memory vectors) from pointers to other kinds of data (which consist of some other data type and whatever is being used to represent data of that type). Two data objects are considered to be the same (`eq?`) if their pointers are identical.[注293] Figure 5.14 illustrates the use of this method to represent the list `((1 2) 3 4)`, whose box-and-pointer diagram is also shown. We use letter prefixes to denote the data-type information. Thus, a pointer to the pair with index 5 is denoted `p5`, the empty list is denoted by the pointer `e0`, and a pointer to the number 4 is denoted `n4`. In the box-and-pointer diagram, we have indicated at the lower left of each pair the vector index that specifies where the `car` and `cdr` of the pair are stored. The blank locations in `the-cars` and `the-cdrs` may contain parts of other list structures (not of interest here).

**校订前**

我们可以使用向量来实现表结构内存所需的基本序对结构。让我们设想计算机内存被分成两个向量：`the-cars`和`the-cdrs`。我们将按如下方式表示表结构：指向一个序对的指针是这两个向量中的一个索引。序对的`car`是指定索引在`the-cars`中的条目，而序对的`cdr`是指定索引在`the-cdrs`中的条目。我们还需要一种表示序对以外的对象（例如数字和符号）的方式，以及一种区分不同种类数据的方式。实现这一点有许多方法，但它们都归结为使用带类型的指针，也就是说，把“指针”的概念扩展到包含数据类型信息。[注292]数据类型使系统能够区分指向序对的指针（由“序对”数据类型和一个内存向量索引组成）与指向其他种类数据的指针（由某种其他数据类型以及用于表示该类型数据的任何东西组成）。如果两个数据对象的指针完全相同，则认为它们是相同的（`eq?`）。[注293]图5.14说明了使用这种方法来表示表`((1 2) 3 4)`，其盒指针图也一并给出。我们使用字母前缀来表示数据类型信息。因此，指向索引为5的序对的指针记为`p5`，空表记为指针`e0`，而指向数字4的指针记为`n4`。在盒指针图中，我们在每个序对的左下方标出了指定该序对的`car`和`cdr`存放在何处的向量索引。`the-cars`和`the-cdrs`中的空白位置可能包含其他表结构的部分（此处不关心）。

**校订后**

我们可以使用向量来实现表结构内存所需的基本序对结构。让我们设想计算机内存被分成两个向量：`the-cars`和`the-cdrs`。我们将按如下方式表示表结构：指向一个序对的指针是这两个向量中的一个索引。序对的`car`是指定索引在`the-cars`中的条目，而序对的`cdr`是指定索引在`the-cdrs`中的条目。我们还需要一种表示序对以外的对象（例如数和符号）的方式，以及一种区分不同种类数据的方式。实现这一点有许多方法，但它们都归结为使用带类型的指针，也就是说，把“指针”的概念扩展到包含数据类型信息。[注292]数据类型使系统能够区分指向序对的指针（由“序对”数据类型和一个内存向量索引组成）与指向其他种类数据的指针（由某种其他数据类型以及用于表示该类型数据的任何东西组成）。如果两个数据对象的指针完全相同，则认为它们是相同的（`eq?`）。[注293]图5.14说明了使用这种方法来表示表`((1 2) 3 4)`，其盒指针图也一并给出。我们使用字母前缀来表示数据类型信息。因此，指向索引为5的序对的指针记为`p5`，空表记为指针`e0`，而指向数4的指针记为`n4`。在盒指针图中，我们在每个序对的左下方标出了指定该序对的`car`和`cdr`存放在何处的向量索引。`the-cars`和`the-cdrs`中的空白位置可能包含其他表结构的部分（此处不关心）。

### 5_002e3:0015

**原文**

A pointer to a number, such as `n4`, might consist of a type indicating numeric data together with the actual representation of the number 4.[注294] To deal with numbers that are too large to be represented in the fixed amount of space allocated for a single pointer, we could use a distinct bignum data type, for which the pointer designates a list in which the parts of the number are stored.[注295]

**校订前**

指向数字的指针，例如`n4`，可能由一个表示数值数据的类型以及数字4的实际表示组成。[注294]为了处理大到无法在分配给单个指针的固定空间中表示的数字，我们可以使用一种独特的大数数据类型，其指针指定一个表，数字的各个部分就存放在这个表中。[注295]

**校订后**

指向数的指针，例如`n4`，可能由一个表示数值数据的类型以及数4的实际表示组成。[注294]为了处理大到无法在分配给单个指针的固定空间中表示的数，我们可以使用一种独特的大数数据类型，其指针指定一个表，数的各个部分就存放在这个表中。[注295]

### 5_002e3:0016

**原文**

A symbol might be represented as a typed pointer that designates a sequence of the characters that form the symbol’s printed representation. This sequence is constructed by the Lisp reader when the character string is initially encountered in input. Since we want two instances of a symbol to be recognized as the “same” symbol by `eq?` and we want `eq?` to be a simple test for equality of pointers, we must ensure that if the reader sees the same character string twice, it will use the same pointer (to the same sequence of characters) to represent both occurrences. To accomplish this, the reader maintains a table, traditionally called the obarray, of all the symbols it has ever encountered. When the reader encounters a character string and is about to construct a symbol, it checks the obarray to see if it has ever before seen the same character string. If it has not, it uses the characters to construct a new symbol (a typed pointer to a new character sequence) and enters this pointer in the obarray. If the reader has seen the string before, it returns the symbol pointer stored in the obarray. This process of replacing character strings by unique pointers is called interning symbols.

**校订前**

符号可以表示为一个带类型的指针，它指定构成该符号打印表示的字符序列。当字符字符串最初在输入中出现时，这个序列由 Lisp 读取器构造。由于我们希望符号的两个实例被`eq?`识别为“同一个”符号，并且我们希望`eq?`是对指针相等性的简单测试，因此必须确保如果读取器两次看到相同的字符字符串，它将使用同一个指针（指向同一个字符序列）来表示这两次出现。为了实现这一点，读取器维护一个表，传统上称为obarray，其中包含它曾经遇到过的所有符号。当读取器遇到一个字符字符串并准备构造一个符号时，它会检查 obarray，看以前是否见过相同的字符字符串。如果没有见过，它就使用这些字符构造一个新符号（指向新字符序列的带类型指针），并将这个指针加入 obarray。如果读取器以前见过这个字符串，它就返回存储在 obarray 中的符号指针。这种用唯一指针替换字符字符串的过程称为符号驻留。

**校订后**

符号可以表示为一个带类型的指针，它指定构成该符号打印表示的字符序列。当字符串最初在输入中出现时，这个序列由 Lisp 读取器构造。由于我们希望符号的两个实例被`eq?`识别为“同一个”符号，并且我们希望`eq?`是对指针相等性的简单测试，因此必须确保如果读取器两次看到相同的字符串，它将使用同一个指针（指向同一个字符序列）来表示这两次出现。为了实现这一点，读取器维护一个表，传统上称为obarray，其中包含它曾经遇到过的所有符号。当读取器遇到一个字符串并准备构造一个符号时，它会检查 obarray，看以前是否见过相同的字符串。如果没有见过，它就使用这些字符构造一个新符号（指向新字符序列的带类型指针），并将这个指针加入 obarray。如果读取器以前见过这个字符串，它就返回存储在 obarray 中的符号指针。这种用唯一指针替换字符串的过程称为符号驻留。

### 5_002e3:0047

**原文**

The state of the garbage-collection process is controlled by maintaining two pointers: `free` and `scan`. These are initialized to point to the beginning of the new memory. The algorithm begins by relocating the pair pointed at by `root` to the beginning of the new memory. The pair is copied, the `root` pointer is adjusted to point to the new location, and the `free` pointer is incremented. In addition, the old location of the pair is marked to show that its contents have been moved. This marking is done as follows: In the `car` position, we place a special tag that signals that this is an already-moved object. (Such an object is traditionally called a broken heart.)[注302] In the `cdr` position we place a forwarding address that points at the location to which the object has been moved.

**校订前**

垃圾回收过程的状态通过维护两个指针来控制：`free` 和 `scan`。它们被初始化为指向新内存的开头。算法首先将 `root` 指向的序对重新安置到新内存的开头。该序对被复制，`root` 指针被调整为指向新位置，并且 `free` 指针递增。此外，该序对的旧位置被标记，以表明其内容已被移动。这种标记如下进行：在 `car` 位置，我们放置一个特殊标记，表明这是一个已被移动的对象。（这样的对象传统上称为 broken heart。）[注302] 在 `cdr` 位置，我们放置一个 forwarding address，它指向该对象已被移动到的位置。

**校订后**

垃圾回收过程的状态通过维护两个指针来控制：`free` 和 `scan`。它们被初始化为指向新内存的开头。算法首先将 `root` 指向的序对重定位到新内存的开头。该序对被复制，`root` 指针被调整为指向新位置，并且 `free` 指针递增。此外，该序对的旧位置被标记，以表明其内容已被移动。这种标记如下进行：在 `car` 位置，我们放置一个特殊标记，表明这是一个已被移动的对象。（这样的对象传统上称为 断心。）[注302] 在 `cdr` 位置，我们放置一个 转发地址，它指向该对象已被移动到的位置。

### 5_002e3:0048

**原文**

After relocating the root, the garbage collector enters its basic cycle. At each step in the algorithm, the `scan` pointer (initially pointing at the relocated root) points at a pair that has been moved to the new memory but whose `car` and `cdr` pointers still refer to objects in the old memory. These objects are each relocated, and the `scan` pointer is incremented. To relocate an object (for example, the object indicated by the `car` pointer of the pair we are scanning) we check to see if the object has already been moved (as indicated by the presence of a broken-heart tag in the `car` position of the object). If the object has not already been moved, we copy it to the place indicated by `free`, update `free`, set up a broken heart at the object’s old location, and update the pointer to the object (in this example, the `car` pointer of the pair we are scanning) to point to the new location. If the object has already been moved, its forwarding address (found in the `cdr` position of the broken heart) is substituted for the pointer in the pair being scanned. Eventually, all accessible objects will have been moved and scanned, at which point the `scan` pointer will overtake the `free` pointer and the process will terminate.

**校订前**

在重新安置根之后，垃圾收集器进入其基本循环。在算法的每一步中，`scan` 指针（最初指向已重新安置的根）指向一个已被移动到新内存但其 `car` 和 `cdr` 指针仍指向旧内存中对象的序对。这些对象各自被重新安置，并且 `scan` 指针递增。要重新安置一个对象（例如，我们正在扫描的序对的 `car` 指针所指示的对象），我们检查该对象是否已经被移动（如该对象的 `car` 位置中存在 broken-heart 标记所指示的那样）。如果该对象尚未被移动，我们将其复制到 `free` 指示的位置，更新 `free`，在该对象的旧位置设置一个 broken heart，并更新指向该对象的指针（在此例中，即我们正在扫描的序对的 `car` 指针）以指向新位置。如果该对象已经被移动，则将其转发地址（在 broken heart 的 `cdr` 位置中找到）替换正在扫描的序对中的指针。最终，所有可访问的对象都将被移动和扫描，此时 `scan` 指针将超过 `free` 指针，过程将终止。

**校订后**

在重定位根之后，垃圾回收器进入其基本循环。在算法的每一步中，`scan` 指针（最初指向已重定位的根）指向一个已被移动到新内存但其 `car` 和 `cdr` 指针仍指向旧内存中对象的序对。这些对象各自被重定位，并且 `scan` 指针递增。要重定位一个对象（例如，我们正在扫描的序对的 `car` 指针所指示的对象），我们检查该对象是否已经被移动（如该对象的 `car` 位置中存在 断心 标记所指示的那样）。如果该对象尚未被移动，我们将其复制到 `free` 指示的位置，更新 `free`，在该对象的旧位置设置一个 断心，并更新指向该对象的指针（在此例中，即我们正在扫描的序对的 `car` 指针）以指向新位置。如果该对象已经被移动，则用其转发地址（在 断心 的 `cdr` 位置中找到）替换正在扫描的序对中的指针。最终，所有可访问的对象都将被移动和扫描，此时 `scan` 指针将超过 `free` 指针，过程将终止。

### 5_002e3:0049

**原文**

We can specify the stop-and-copy algorithm as a sequence of instructions for a register machine. The basic step of relocating an object is accomplished by a subroutine called `relocate-old-result-in-new`. This subroutine gets its argument, a pointer to the object to be relocated, from a register named `old`. It relocates the designated object (incrementing `free` in the process), puts a pointer to the relocated object into a register called `new`, and returns by branching to the entry point stored in the register `relocate-continue`. To begin garbage collection, we invoke this subroutine to relocate the `root` pointer, after initializing `free` and `scan`. When the relocation of `root` has been accomplished, we install the new pointer as the new `root` and enter the main loop of the garbage collector.

**校订前**

我们可以将停止并复制算法指定为寄存器机器的一系列指令。重新安置一个对象的基本步骤由一个称为 `relocate-old-result-in-new` 的子例程完成。这个子例程从名为 `old` 的寄存器中获取其参数，即指向要重新安置的对象的指针。它重新安置指定的对象（在此过程中递增 `free`），将指向已重新安置对象的指针放入称为 `new` 的寄存器中，并通过分支到存储在寄存器 `relocate-continue` 中的入口点来返回。为了开始垃圾回收，我们在初始化 `free` 和 `scan` 之后，调用这个子例程来重新安置 `root` 指针。当 `root` 的重新安置完成后，我们将新指针安装为新的 `root`，并进入垃圾收集器的主循环。

**校订后**

我们可以将停止并复制算法指定为寄存器机器的一系列指令。重定位一个对象的基本步骤由一个称为 `relocate-old-result-in-new` 的子例程完成。这个子例程从名为 `old` 的寄存器中获取其参数，即指向要重定位的对象的指针。它重定位指定的对象（在此过程中递增 `free`），将指向已重定位对象的指针放入称为 `new` 的寄存器中，并通过分支到存储在寄存器 `relocate-continue` 中的入口点来返回。为了开始垃圾回收，我们在初始化 `free` 和 `scan` 之后，调用这个子例程来重定位 `root` 指针。当 `root` 的重定位完成后，我们将新指针安装为新的 `root`，并进入垃圾回收器的主循环。

### 5_002e3:0050

**原文**

In the main loop of the garbage collector we must determine whether there are any more objects to be scanned. We do this by testing whether the `scan` pointer is coincident with the `free` pointer. If the pointers are equal, then all accessible objects have been relocated, and we branch to `gc-flip`, which cleans things up so that we can continue the interrupted computation. If there are still pairs to be scanned, we call the relocate subroutine to relocate the `car` of the next pair (by placing the `car` pointer in `old`). The `relocate-continue` register is set up so that the subroutine will return to update the `car` pointer.

**校订前**

在垃圾收集器的主循环中，我们必须确定是否还有更多对象需要扫描。我们通过测试 `scan` 指针是否与 `free` 指针重合来做到这一点。如果指针相等，那么所有可访问的对象都已被重新安置，我们分支到 `gc-flip`，它会清理现场，以便我们可以继续被中断的计算。如果仍有需要扫描的序对，我们调用 relocate 子例程来重新安置下一个序对的 `car`（通过将 `car` 指针放入 `old`）。`relocate-continue` 寄存器被设置好，以便子例程将返回以更新 `car` 指针。

**校订后**

在垃圾回收器的主循环中，我们必须确定是否还有更多对象需要扫描。我们通过测试 `scan` 指针是否与 `free` 指针重合来做到这一点。如果指针相等，那么所有可访问的对象都已被重定位，我们分支到 `gc-flip`，它会清理现场，以便我们可以继续被中断的计算。如果仍有需要扫描的序对，我们调用 relocate 子例程来重定位下一个序对的 `car`（通过将 `car` 指针放入 `old`）。`relocate-continue` 寄存器被设置好，以便子例程将返回以更新 `car` 指针。

### 5_002e3:0051

**原文**

At `update-car`, we modify the `car` pointer of the pair being scanned, then proceed to relocate the `cdr` of the pair. We return to `update-cdr` when that relocation has been accomplished. After relocating and updating the `cdr`, we are finished scanning that pair, so we continue with the main loop.

**校订前**

在 `update-car` 处，我们修改正在扫描的序对的 `car` 指针，然后继续重新安置该序对的 `cdr`。当该重新安置完成后，我们返回到 `update-cdr`。在重新安置并更新 `cdr` 之后，我们完成了对该序对的扫描，因此我们继续主循环。

**校订后**

在 `update-car` 处，我们修改正在扫描的序对的 `car` 指针，然后继续重定位该序对的 `cdr`。当该重定位完成后，我们返回到 `update-cdr`。在重定位并更新 `cdr` 之后，我们完成了对该序对的扫描，因此我们继续主循环。

### 5_002e3:0052

**原文**

The subroutine `relocate-old-result-in-new` relocates objects as follows: If the object to be relocated (pointed at by `old`) is not a pair, then we return the same pointer to the object unchanged (in `new`). (For example, we may be scanning a pair whose `car` is the number 4. If we represent the `car` by `n4`, as described in 5.3.1, then we want the “relocated” `car` pointer to still be `n4`.) Otherwise, we must perform the relocation. If the `car` position of the pair to be relocated contains a broken-heart tag, then the pair has in fact already been moved, so we retrieve the forwarding address (from the `cdr` position of the broken heart) and return this in `new`. If the pointer in `old` points at a yet-unmoved pair, then we move the pair to the first free cell in new memory (pointed at by `free`) and set up the broken heart by storing a broken-heart tag and forwarding address at the old location. `Relocate-old-result-in-new` uses a register `oldcr` to hold the `car` or the `cdr` of the object pointed at by `old`.[注303]

**校订前**

子例程 `relocate-old-result-in-new` 按如下方式重定位对象：如果要重定位的对象（由 `old` 指向）不是序对，那么我们就返回指向该对象的同一个指针，保持不变（在 `new` 中）。（例如，我们可能正在扫描一个序对，其 `car` 是数字 4。如果我们按照 5.3.1 中所述用 `n4` 表示 `car`，那么我们希望“重定位”后的 `car` 指针仍然是 `n4`。）否则，我们必须执行重定位。如果要重定位的序对的 `car` 位置包含一个断心标签，那么该序对实际上已经被移动过了，因此我们检索转发地址（从断心的 `cdr` 位置）并在 `new` 中返回它。如果 `old` 中的指针指向一个尚未移动的序对，那么我们将该序对移动到新内存中的第一个空闲单元（由 `free` 指向），并通过在旧位置存储一个断心标签和转发地址来设置断心。`Relocate-old-result-in-new` 使用寄存器 `oldcr` 来保存由 `old` 指向的对象的 `car` 或 `cdr`。[注303]

**校订后**

子例程 `relocate-old-result-in-new` 按如下方式重定位对象：如果要重定位的对象（由 `old` 指向）不是序对，那么我们就返回指向该对象的同一个指针，保持不变（在 `new` 中）。（例如，我们可能正在扫描一个序对，其 `car` 是数 4。如果我们按照 5.3.1 中所述用 `n4` 表示 `car`，那么我们希望“重定位”后的 `car` 指针仍然是 `n4`。）否则，我们必须执行重定位。如果要重定位的序对的 `car` 位置包含一个断心标签，那么该序对实际上已经被移动过了，因此我们检索转发地址（从断心的 `cdr` 位置）并在 `new` 中返回它。如果 `old` 中的指针指向一个尚未移动的序对，那么我们将该序对移动到新内存中的第一个空闲单元（由 `free` 指向），并通过在旧位置存储一个断心标签和转发地址来设置断心。`Relocate-old-result-in-new` 使用寄存器 `oldcr` 来保存由 `old` 指向的对象的 `car` 或 `cdr`。[注303]

### 5_002e3:0055

**原文**

[注290] We could represent memory as lists of items. However, the access time would then not be independent of the index, since accessing the $n^(th)$ element of a list requires $n−1$ `cdr` operations.

**校订前**

[注290] 我们可以将内存表示为项的列表。然而，访问时间将不再与索引无关，因为访问列表的第 $n^(th)$ 个元素需要 $n−1$ 次 `cdr` 操作。

**校订后**

[注290] 我们可以将内存表示为项的表。然而，访问时间将不再与索引无关，因为访问表的第 $n^(th)$ 个元素需要 $n−1$ 次 `cdr` 操作。

### 5_002e3:0057

**原文**

[注292] This is precisely the same “tagged data” idea we introduced in Chapter 2 for dealing with generic operations. Here, however, the data types are included at the primitive machine level rather than constructed through the use of lists.

**校订前**

[注292] 这正是我们在 第 2 章 中为处理通用操作而引入的同一个“带标签数据”思想。然而，在这里，数据类型是在基本机器层面包含的，而不是通过使用列表构造的。

**校订后**

[注292] 这正是我们在 第 2 章 中为处理通用操作而引入的同一个“带标签数据”思想。然而，在这里，数据类型是在基本机器层面包含的，而不是通过使用表构造的。

### 5_002e3:0059

**原文**

[注294] This decision on the representation of numbers determines whether `eq?`, which tests equality of pointers, can be used to test for equality of numbers. If the pointer contains the number itself, then equal numbers will have the same pointer. But if the pointer contains the index of a location where the number is stored, equal numbers will be guaranteed to have equal pointers only if we are careful never to store the same number in more than one location.

**校订前**

[注294] 这个关于数字表示的决定决定了 `eq?`（它测试指针的相等性）是否可用于测试数字的相等性。如果指针包含数字本身，那么相等的数字将具有相同的指针。但如果指针包含存储数字的位置的索引，那么只有当我们小心地从不将同一个数字存储在多于一个位置时，才能保证相等的数字具有相等的指针。

**校订后**

[注294] 这个关于数表示的决定决定了 `eq?`（它测试指针的相等性）是否可用于测试数的相等性。如果指针包含数本身，那么相等的数将具有相同的指针。但如果指针包含存储数的位置的索引，那么只有当我们小心地从不将同一个数存储在多于一个位置时，才能保证相等的数具有相等的指针。

### 5_002e3:0060

**原文**

[注295] This is just like writing a number as a sequence of digits, except that each “digit” is a number between 0 and the largest number that can be stored in a single pointer.

**校订前**

[注295] 这就像把一个数字写成数字序列一样，只不过每个“数字”是一个介于 0 和单个指针中能存储的最大数字之间的数。

**校订后**

[注295] 这就像把一个数写成数码序列一样，只不过每个“数码”是一个介于 0 和单个指针中能存储的最大数之间的数。

### 5_002e3:0064

**原文**

[注299] We assume here that the stack is represented as a list as described in 5.3.1, so that items on the stack are accessible via the pointer in the stack register.

**校订前**

[注299] 我们在此假设栈按照 5.3.1 中所述表示为列表，因此栈上的项可以通过栈寄存器中的指针访问。

**校订后**

[注299] 我们在此假设栈按照 5.3.1 中所述表示为表，因此栈上的项可以通过栈寄存器中的指针访问。

### 5_002e3:0067

**原文**

The Minsky-Fenichel-Yochelson algorithm is the dominant algorithm in use for large-memory systems because it examines only the useful part of memory. This is in contrast to mark-sweep, in which the sweep phase must check all of memory. A second advantage of stop-and-copy is that it is a compacting garbage collector. That is, at the end of the garbage-collection phase the useful data will have been moved to consecutive memory locations, with all garbage pairs compressed out. This can be an extremely important performance consideration in machines with virtual memory, in which accesses to widely separated memory addresses may require extra paging operations.

**校订前**

Minsky-Fenichel-Yochelson算法是用于大内存系统的主导算法，因为它只检查内存中有用的部分。这与标记-清除形成对比，在标记-清除中，清除阶段必须检查整个内存。停止-复制的第二个优点是它是一种压缩垃圾回收器。也就是说，在垃圾回收阶段结束时，有用数据将被移动到连续的内存位置，所有垃圾序对都被压缩掉。在具有虚拟内存的机器中，这可能是一个极其重要的性能考虑因素，因为访问相隔很远的内存地址可能需要额外的分页操作。

**校订后**

Minsky-Fenichel-Yochelson算法是用于大内存系统的主导算法，因为它只检查内存中有用的部分。这与标记-清除形成对比，在标记-清除中，清除阶段必须检查整个内存。停止并复制的第二个优点是它是一种压缩垃圾回收器。也就是说，在垃圾回收阶段结束时，有用数据将被移动到连续的内存位置，所有垃圾序对都被压缩掉。在具有虚拟内存的机器中，这可能是一个极其重要的性能考虑因素，因为访问相隔很远的内存地址可能需要额外的分页操作。

### 5_002e3:0068

**原文**

[注301] This list of registers does not include the registers used by the storage-allocation system—`root`, `the-cars`, `the-cdrs`, and the other registers that will be introduced in this section.

**校订前**

[注301]这个寄存器列表不包括存储分配系统使用的寄存器——`root`、`the-cars`、`the-cdrs`，以及本节将介绍的其他寄存器。

**校订后**

[注301]这个寄存器表不包括存储分配系统使用的寄存器——`root`、`the-cars`、`the-cdrs`，以及本节将介绍的其他寄存器。

### 5_002e3:0069

**原文**

[注302] The term broken heart was coined by David Cressey, who wrote a garbage collector for MDL, a dialect of Lisp developed at MIT during the early 1970s.

**校订前**

[注302]术语心碎是由David Cressey创造的，他为MDL编写了一个垃圾回收器，MDL是MIT在1970年代早期开发的一种Lisp方言。

**校订后**

[注302]术语断心是由David Cressey创造的，他为MDL编写了一个垃圾回收器，MDL是MIT在1970年代早期开发的一种Lisp方言。

### 5_002e3:0070

**原文**

[注303] The garbage collector uses the low-level predicate `pointer-to-pair?` instead of the list-structure `pair?` operation because in a real system there might be various things that are treated as pairs for garbage-collection purposes. For example, in a Scheme system that conforms to the IEEE standard a procedure object may be implemented as a special kind of “pair” that doesn’t satisfy the `pair?` predicate. For simulation purposes, `pointer-to-pair?` can be implemented as `pair?`.

**校订前**

[注303]垃圾回收器使用低级谓词`pointer-to-pair?`而不是表结构操作`pair?`，因为在真实系统中可能有各种事物在垃圾回收目的上被视为序对。例如，在符合IEEE标准的Scheme系统中，过程对象可能被实现为一种不满足`pair?`谓词的特殊“序对”。出于模拟目的，`pointer-to-pair?`可以实现为`pair?`。

**校订后**

[注303]垃圾回收器使用低级谓词`pointer-to-pair?`而不是表结构操作`pair?`，因为在真实系统中可能有各种事物在垃圾回收时被视为序对。例如，在符合IEEE标准的Scheme系统中，过程对象可能被实现为一种不满足`pair?`谓词的特殊“序对”。出于模拟目的，`pointer-to-pair?`可以实现为`pair?`。

### 5_002e4:0013

**原文**

Numbers and strings (which are self-evaluating), variables, quotations, and `lambda` expressions have no subexpressions to be evaluated. For these, the evaluator simply places the correct value in the `val` register and continues execution at the entry point specified by `continue`. Evaluation of simple expressions is performed by the following controller code:

**校订前**

数字和字符串（它们是自求值的）、变量、引用和`lambda`表达式没有需要求值的子表达式。对于这些，求值器只需将正确的值放入`val`寄存器，并在由`continue`指定的入口点继续执行。简单表达式的求值由以下控制器代码执行：

**校订后**

数和字符串（它们是自求值的）、变量、引用和`lambda`表达式没有需要求值的子表达式。对于这些，求值器只需将正确的值放入`val`寄存器，并在由`continue`指定的入口点继续执行。简单表达式的求值由以下控制器代码执行：

### 5_002e4:0016

**原文**

A procedure application is specified by a combination containing an operator and operands. The operator is a subexpression whose value is a procedure, and the operands are subexpressions whose values are the arguments to which the procedure should be applied. The metacircular `eval` handles applications by calling itself recursively to evaluate each element of the combination, and then passing the results to `apply`, which performs the actual procedure application. The explicit-control evaluator does the same thing; these recursive calls are implemented by `goto` instructions, together with use of the stack to save registers that will be restored after the recursive call returns. Before each call we will be careful to identify which registers must be saved (because their values will be needed later).[注306]

**校订前**

过程应用由包含运算符和操作数的组合式指定。运算符是一个子表达式，其值是一个过程，而操作数是子表达式，其值是过程应被应用到的参数。元循环`eval`通过递归调用自身来求值组合式的每个元素，然后将结果传递给`apply`，后者执行实际的过程应用，从而处理应用。显式控制求值器做同样的事情；这些递归调用由`goto`指令实现，同时使用栈来保存将在递归调用返回后恢复的寄存器。在每次调用之前，我们将小心地确定哪些寄存器必须保存（因为它们的值稍后将被需要）。[注306]

**校订后**

过程应用由包含运算符和运算对象的组合式指定。运算符是一个子表达式，其值是一个过程，而运算对象是子表达式，其值是过程应被应用到的参数。元循环`eval`通过递归调用自身来求值组合式的每个元素，然后将结果传递给`apply`，后者执行实际的过程应用，从而处理应用。显式控制求值器做同样的事情；这些递归调用由`goto`指令实现，同时使用栈来保存将在递归调用返回后恢复的寄存器。在每次调用之前，我们将小心地确定哪些寄存器必须保存（因为它们的值稍后将被需要）。[注306]

### 5_002e4:0017

**原文**

We begin the evaluation of an application by evaluating the operator to produce a procedure, which will later be applied to the evaluated operands. To evaluate the operator, we move it to the `exp` register and go to `eval-dispatch`. The environment in the `env` register is already the correct one in which to evaluate the operator. However, we save `env` because we will need it later to evaluate the operands. We also extract the operands into `unev` and save this on the stack. We set up `continue` so that `eval-dispatch` will resume at `ev-appl-did-operator` after the operator has been evaluated. First, however, we save the old value of `continue`, which tells the controller where to continue after the application.

**校订前**

我们通过求值运算符以产生一个过程来开始应用求值，该过程稍后将应用于已求值的操作数。为了求值运算符，我们将其移动到`exp`寄存器并转到`eval-dispatch`。`env`寄存器中的环境已经是求值运算符的正确环境。然而，我们保存`env`，因为稍后求值操作数时需要它。我们还将操作数提取到`unev`中并将此保存在栈上。我们设置`continue`，以便在运算符求值后，`eval-dispatch`将在`ev-appl-did-operator`处恢复。然而，首先我们保存`continue`的旧值，它告诉控制器在应用之后继续的位置。

**校订后**

我们通过求值运算符以产生一个过程来开始应用求值，该过程稍后将应用于已求值的运算对象。为了求值运算符，我们将其移动到`exp`寄存器并转到`eval-dispatch`。`env`寄存器中的环境已经是求值运算符的正确环境。然而，我们保存`env`，因为稍后求值运算对象时需要它。我们还将运算对象提取到`unev`中并将此保存在栈上。我们设置`continue`，以便在运算符求值后，`eval-dispatch`将在`ev-appl-did-operator`处恢复。然而，首先我们保存`continue`的旧值，它告诉控制器在应用之后继续的位置。

### 5_002e4:0018

**原文**

Upon returning from evaluating the operator subexpression, we proceed to evaluate the operands of the combination and to accumulate the resulting arguments in a list, held in `argl`. First we restore the unevaluated operands and the environment. We initialize `argl` to an empty list. Then we assign to the `proc` register the procedure that was produced by evaluating the operator. If there are no operands, we go directly to `apply-dispatch`. Otherwise we save `proc` on the stack and start the argument-evaluation loop:[注307]

**校订前**

从求值运算符子表达式返回后，我们继续求值组合式的操作数，并将结果参数累积在一个表中，该表保存在`argl`中。首先我们恢复未求值的操作数和环境。我们将`argl`初始化为空表。然后我们将通过求值运算符产生的过程赋值给`proc`寄存器。如果没有操作数，我们直接转到`apply-dispatch`。否则我们将`proc`保存在栈上并开始参数求值循环：[注307]

**校订后**

从求值运算符子表达式返回后，我们继续求值组合式的运算对象，并将结果参数累积在一个表中，该表保存在`argl`中。首先我们恢复未求值的运算对象和环境。我们将`argl`初始化为空表。然后我们将通过求值运算符产生的过程赋值给`proc`寄存器。如果没有运算对象，我们直接转到`apply-dispatch`。否则我们将`proc`保存在栈上并开始参数求值循环：[注307]

### 5_002e4:0019

**原文**

Each cycle of the argument-evaluation loop evaluates an operand from the list in `unev` and accumulates the result into `argl`. To evaluate an operand, we place it in the `exp` register and go to `eval-dispatch`, after setting `continue` so that execution will resume with the argument-accumulation phase. But first we save the arguments accumulated so far (held in `argl`), the environment (held in `env`), and the remaining operands to be evaluated (held in `unev`). A special case is made for the evaluation of the last operand, which is handled at `ev-appl-last-arg`.

**校订前**

参数求值循环的每个周期从`unev`中的表求值一个操作数，并将结果累积到`argl`中。为了求值一个操作数，我们将其放入`exp`寄存器并转到`eval-dispatch`，在设置`continue`以便执行将在参数累积阶段恢复之后。但首先我们保存到目前为止累积的参数（保存在`argl`中）、环境（保存在`env`中）以及剩余要计算的操作数（保存在`unev`中）。对最后一个操作数的求值做了特殊处理，在`ev-appl-last-arg`处处理。

**校订后**

参数求值循环的每个周期从`unev`中的表求值一个运算对象，并将结果累积到`argl`中。为了求值一个运算对象，我们将其放入`exp`寄存器并转到`eval-dispatch`，在设置`continue`以便执行将在参数累积阶段恢复之后。但首先我们保存到目前为止累积的参数（保存在`argl`中）、环境（保存在`env`中）以及剩余要计算的运算对象（保存在`unev`中）。对最后一个运算对象的求值做了特殊处理，在`ev-appl-last-arg`处处理。

### 5_002e4:0020

**原文**

When an operand has been evaluated, the value is accumulated into the list held in `argl`. The operand is then removed from the list of unevaluated operands in `unev`, and the argument-evaluation continues.

**校订前**

当一个操作数被求值后，该值被累积到`argl`中保存的表里。然后该操作数从`unev`中的未求值操作数表中移除，参数求值继续。

**校订后**

当一个运算对象被求值后，该值被累积到`argl`中保存的表里。然后该运算对象从`unev`中的未求值运算对象表中移除，参数求值继续。

### 5_002e4:0021

**原文**

Evaluation of the last argument is handled differently. There is no need to save the environment or the list of unevaluated operands before going to `eval-dispatch`, since they will not be required after the last operand is evaluated. Thus, we return from the evaluation to a special entry point `ev-appl-accum-last-arg`, which restores the argument list, accumulates the new argument, restores the saved procedure, and goes off to perform the application.[注308]

**校订前**

最后一个参数的求值处理方式不同。在转到`eval-dispatch`之前不需要保存环境或未求值操作数表，因为在最后一个操作数求值后它们将不再需要。因此，我们从求值返回到一个特殊入口点`ev-appl-accum-last-arg`，它恢复参数表，累积新参数，恢复保存的过程，并转去执行应用。[注308]

**校订后**

最后一个参数的求值处理方式不同。在转到`eval-dispatch`之前不需要保存环境或未求值运算对象表，因为在最后一个运算对象求值后它们将不再需要。因此，我们从求值返回到一个特殊入口点`ev-appl-accum-last-arg`，它恢复参数表，累积新参数，恢复保存的过程，并转去执行应用。[注308]

### 5_002e4:0022

**原文**

The details of the argument-evaluation loop determine the order in which the interpreter evaluates the operands of a combination (e.g., left to right or right to left—see Exercise 3.8). This order is not determined by the metacircular evaluator, which inherits its control structure from the underlying Scheme in which it is implemented.[注309] Because the `first-operand` selector (used in `ev-appl-operand-loop` to extract successive operands from `unev`) is implemented as `car` and the `rest-operands` selector is implemented as `cdr`, the explicit-control evaluator will evaluate the operands of a combination in left-to-right order.

**校订前**

参数求值循环的细节决定了解释器求值组合式操作数的顺序（例如，从左到右或从右到左——参见习题3.8）。这个顺序不是由元循环求值器决定的，元循环求值器从其实现所基于的Scheme继承控制结构。[注309]因为`first-operand`选择器（在`ev-appl-operand-loop`中用于从`unev`中提取连续的操作数）实现为`car`，而`rest-operands`选择器实现为`cdr`，所以显式控制求值器将按从左到右的顺序求值组合式的操作数。

**校订后**

参数求值循环的细节决定了解释器求值组合式运算对象的顺序（例如，从左到右或从右到左——参见习题3.8）。这个顺序不是由元循环求值器决定的，元循环求值器从其实现所基于的Scheme继承控制结构。[注309]因为`first-operand`选择函数（在`ev-appl-operand-loop`中用于从`unev`中提取连续的运算对象）实现为`car`，而`rest-operands`选择函数实现为`cdr`，所以显式控制求值器将按从左到右的顺序求值组合式的运算对象。

### 5_002e4:0026

**原文**

To apply a compound procedure, we proceed just as with the metacircular evaluator. We construct a frame that binds the procedure’s parameters to the arguments, use this frame to extend the environment carried by the procedure, and evaluate in this extended environment the sequence of expressions that forms the body of the procedure. `Ev-sequence`, described below in 5.4.2, handles the evaluation of the sequence.

**校订前**

要应用复合过程，我们就像元循环求值器那样进行。我们构造一个框架，将过程的参数绑定到参数上，使用这个框架来扩展过程所携带的环境，并在这个扩展环境中求值构成过程体的表达式序列。`Ev-sequence`，下面在 5.4.2 中描述，处理序列的求值。

**校订后**

要应用复合过程，我们就像元循环求值器那样进行。我们构造一个框架，将过程的形参绑定到实参上，使用这个框架来扩展过程所携带的环境，并在这个扩展环境中求值构成过程体的表达式序列。`Ev-sequence`，下面在 5.4.2 中描述，处理序列的求值。

### 5_002e4:0032

**原文**

The entries at `ev-sequence` and `ev-sequence-continue` form a loop that successively evaluates each expression in a sequence. The list of unevaluated expressions is kept in `unev`. Before evaluating each expression, we check to see if there are additional expressions to be evaluated in the sequence. If so, we save the rest of the unevaluated expressions (held in `unev`) and the environment in which these must be evaluated (held in `env`) and call `eval-dispatch` to evaluate the expression. The two saved registers are restored upon the return from this evaluation, at `ev-sequence-continue`.

**校订前**

`ev-sequence` 和 `ev-sequence-continue` 处的条目形成一个循环，依次求值序列中的每个表达式。未求值表达式的表保存在 `unev` 中。在求值每个表达式之前，我们检查序列中是否还有要额外求值的表达式。如果有，我们保存剩余的未求值表达式（保存在 `unev` 中）以及必须求值这些表达式的环境（保存在 `env` 中），并调用 `eval-dispatch` 来求值该表达式。这两个保存的寄存器在从这次求值返回时，在 `ev-sequence-continue` 处恢复。

**校订后**

`ev-sequence` 和 `ev-sequence-continue` 处的入口形成一个循环，依次求值序列中的每个表达式。未求值表达式的表保存在 `unev` 中。在求值每个表达式之前，我们检查序列中是否还有要额外求值的表达式。如果有，我们保存剩余的未求值表达式（保存在 `unev` 中）以及必须求值这些表达式的环境（保存在 `env` 中），并调用 `eval-dispatch` 来求值该表达式。这两个保存的寄存器在从这次求值返回时，在 `ev-sequence-continue` 处恢复。

### 5_002e4:0042

**原文**

As with the metacircular evaluator, special forms are handled by selectively evaluating fragments of the expression. For an `if` expression, we must evaluate the predicate and decide, based on the value of predicate, whether to evaluate the consequent or the alternative.

**校订前**

与元循环求值器一样，特殊形式通过选择性地求值表达式的片段来处理。对于`if`表达式，我们必须求值谓词，并根据谓词的值决定是求值推论还是求值替代。

**校订后**

与元循环求值器一样，特殊形式通过选择性地求值表达式的片段来处理。对于`if`表达式，我们必须求值谓词，并根据谓词的值决定是求值结果表达式还是求值替代表达式。

### 5_002e4:0043

**原文**

Before evaluating the predicate, we save the `if` expression itself so that we can later extract the consequent or alternative. We also save the environment, which we will need later in order to evaluate the consequent or the alternative, and we save `continue`, which we will need later in order to return to the evaluation of the expression that is waiting for the value of the `if`.

**校订前**

在求值谓词之前，我们保存`if`表达式本身，以便稍后能提取推论或替代。我们还保存环境，稍后求值推论或替代时需要它，并且我们保存`continue`，稍后返回等待`if`值的表达式的求值过程时需要它。

**校订后**

在求值谓词之前，我们保存`if`表达式本身，以便稍后能提取结果表达式或替代表达式。我们还保存环境，稍后求值结果表达式或替代表达式时需要它，并且我们保存`continue`，稍后返回等待`if`值的表达式的求值过程时需要它。

### 5_002e4:0044

**原文**

When we return from evaluating the predicate, we test whether it was true or false and, depending on the result, place either the consequent or the alternative in `exp` before going to `eval-dispatch`. Notice that restoring `env` and `continue` here sets up `eval-dispatch` to have the correct environment and to continue at the right place to receive the value of the `if` expression.

**校订前**

当我们从求值谓词返回时，我们测试它是真还是假，并根据结果，在转到`eval-dispatch`之前将推论或替代放入`exp`。注意，这里恢复`env`和`continue`使得`eval-dispatch`具有正确的环境，并在正确的位置继续以接收`if`表达式的值。

**校订后**

当我们从求值谓词返回时，我们测试它是真还是假，并根据结果，在转到`eval-dispatch`之前将结果表达式或替代表达式放入`exp`。注意，这里恢复`env`和`continue`使得`eval-dispatch`具有正确的环境，并在正确的位置继续以接收`if`表达式的值。

### 5_002e4:0071

**原文**

Exercise 5.29: Monitor the stack operations in the tree-recursive Fibonacci computation:

**校订前**

习题 5.29： 监控树递归 Fibonacci 计算中的栈操作：

**校订后**

习题 5.29： 监控树形递归斐波那契 计算中的栈操作：

### 5_002e4:0072

**原文**

Give a formula in terms of $n$ for the maximum depth of the stack required to compute $Fib(n)$ for $n≥2$. Hint: In 1.2.2 we argued that the space used by this process grows linearly with $n$.

**校订前**

给出一个以 $n$ 表示的公式，用于计算对 $n≥2$ 计算 $Fib(n)$ 所需的最大栈深度。提示：在 1.2.2 中我们论证了此过程使用的空间随 $n$ 线性增长。

**校订后**

给出一个以 $n$ 表示的公式，用于计算对 $n≥2$ 计算 $Fib(n)$ 所需的最大栈深度。提示：在 1.2.2 中我们论证了此计算过程使用的空间随 $n$ 线性增长。

### 5_002e4:0076

**原文**

Much worse is the problem of handling errors that are signaled by applying primitive procedures, such as an attempt to divide by zero or an attempt to extract the `car` of a symbol. In a professionally written high-quality system, each primitive application is checked for safety as part of the primitive. For example, every call to `car` could first check that the argument is a pair. If the argument is not a pair, the application would return a distinguished condition code to the evaluator, which would then report the failure. We could arrange for this in our register-machine simulator by making each primitive procedure check for applicability and returning an appropriate distinguished condition code on failure. Then the `primitive-apply` code in the evaluator can check for the condition code and go to `signal-error` if necessary. Build this structure and make it work. This is a major project.

**校订前**

更糟糕的是处理由应用基本过程所引发的错误，例如试图除以零或试图提取符号的`car`。在专业编写的高质量系统中，每个基本应用都作为基本过程的一部分进行安全检查。例如，每次调用`car`都可以首先检查参数是否为序对。如果参数不是序对，应用将向求值器返回一个特殊的条件码，求值器随后报告失败。我们可以在寄存器机器模拟器中安排这一点，让每个基本过程检查适用性，并在失败时返回适当的特殊条件码。然后求值器中的`primitive-apply`代码可以检查条件码，并在必要时转到`signal-error`。构建这个结构并使其工作。这是一个大项目。

**校订后**

更糟糕的是处理由应用基本过程所引发的错误，例如试图除以零或试图提取符号的`car`。在专业编写的高质量系统中，每次基本过程应用都作为基本过程的一部分进行安全检查。例如，每次调用`car`都可以首先检查参数是否为序对。如果参数不是序对，应用将向求值器返回一个特殊的条件码，求值器随后报告失败。我们可以在寄存器机器模拟器中安排这一点，让每个基本过程检查适用性，并在失败时返回适当的特殊条件码。然后求值器中的`primitive-apply`代码可以检查条件码，并在必要时转到`signal-error`。构建这个结构并使其工作。这是一个大项目。

### 5_002e4:0082

**原文**

We also use an additional syntax procedure to test for the last operand in a combination:

**校订前**

我们还使用一个额外的语法过程来测试组合式中的最后一个操作数：

**校订后**

我们还使用一个额外的语法过程来测试组合式中的最后一个运算对象：

### 5_002e4:0083

**原文**

[注308] The optimization of treating the last operand specially is known as evlis tail recursion (see Wand 1980). We could be somewhat more efficient in the argument evaluation loop if we made evaluation of the first operand a special case too. This would permit us to postpone initializing `argl` until after evaluating the first operand, so as to avoid saving `argl` in this case. The compiler in 5.5 performs this optimization. (Compare the `construct-arglist` procedure of 5.5.3.)

**校订前**

[注308] 将最后一个操作数特殊处理的优化被称为 evlis 尾递归（参见Wand 1980）。如果我们把第一个操作数的求值也作为特殊情况处理，参数求值循环可以更高效一些。这将允许我们将`argl`的初始化推迟到求值第一个操作数之后，从而在这种情况下避免保存`argl`。5.5中的编译器执行了这种优化。（比较5.5.3中的`construct-arglist`过程。）

**校订后**

[注308] 将最后一个运算对象特殊处理的优化被称为 evlis 尾递归（参见Wand 1980）。如果我们把第一个运算对象的求值也作为特殊情况处理，参数求值循环可以更高效一些。这将允许我们将`argl`的初始化推迟到求值第一个运算对象之后，从而在这种情况下避免保存`argl`。5.5中的编译器执行了这种优化。（比较5.5.3中的`construct-arglist`过程。）

### 5_002e4:0084

**原文**

[注309] The order of operand evaluation in the metacircular evaluator is determined by the order of evaluation of the arguments to `cons` in the procedure `list-of-values` of 4.1.1 (see Exercise 4.1).

**校订前**

[注309] 元循环求值器中操作数的求值顺序由4.1.1中过程`list-of-values`里`cons`的参数的求值顺序决定（参见习题4.1）。

**校订后**

[注309] 元循环求值器中运算对象的求值顺序由4.1.1中过程`list-of-values`里`cons`的参数的求值顺序决定（参见习题4.1）。

### 5_002e4:0093

**原文**

[注317] Regrettably, this is the normal state of affairs in conventional compiler-based language systems such as C. In UNIX(tm) the system “dumps core,” and in DOS/Windows(tm) it becomes catatonic. The Macintosh(tm) displays a picture of an exploding bomb and offers you the opportunity to reboot the computer—if you’re lucky.

**校订前**

[注317] 遗憾的是，在诸如 C 这样的传统基于编译器的语言系统中，这是正常情况。在UNIX(tm)中，系统会“转储核心”，而在DOS/Windows(tm)中，它会变得僵死。Macintosh(tm)会显示一张炸弹爆炸的图片，并给你机会重启计算机——如果你运气好的话。

**校订后**

[注317] 遗憾的是，在诸如 C 这样的传统基于编译器的语言系统中，这是正常情况。在UNIX(tm)中，系统会“生成内存转储”，而在DOS/Windows(tm)中，它会变得僵死。Macintosh(tm)会显示一张炸弹爆炸的图片，并给你机会重启计算机——如果你运气好的话。

### 5_002e5:0002

**原文**

Next: References, Prev: 5.4, Up: Chapter 5 [Contents]

**校订前**

下一节： References, 上一节： 5.4, 上一级： 第5章 [目录]

**校订后**

下一节： 参考文献, 上一节： 5.4, 上一级： 第5章 [目录]

### 5_002e5:0005

**原文**

The explicit-control evaluator machine is universal—it can carry out any computational process that can be described in Scheme. The evaluator’s controller orchestrates the use of its data paths to perform the desired computation. Thus, the evaluator’s data paths are universal: They are sufficient to perform any computation we desire, given an appropriate controller.[注318]

**校订前**

显式控制求值器机器是通用的——它能执行任何可以用 Scheme 描述的计算过程。求值器的控制器协调其数据路径的使用，以执行所需的计算。因此，求值器的数据路径是通用的：给定适当的控制器，它们足以执行我们想要的任何计算。[注318]

**校订后**

显式控制求值器机器是通用的——它能执行任何可以用 Scheme 描述的计算过程。求值器的控制器协调其数据通路的使用，以执行所需的计算。因此，求值器的数据通路是通用的：给定适当的控制器，它们足以执行我们想要的任何计算。[注318]

### 5_002e5:0006

**原文**

Commercial general-purpose computers are register machines organized around a collection of registers and operations that constitute an efficient and convenient universal set of data paths. The controller for a general-purpose machine is an interpreter for a register-machine language like the one we have been using. This language is called the native language of the machine, or simply machine language. Programs written in machine language are sequences of instructions that use the machine’s data paths. For example, the explicit-control evaluator’s instruction sequence can be thought of as a machine-language program for a general-purpose computer rather than as the controller for a specialized interpreter machine.

**校订前**

商用通用计算机是围绕一组寄存器和操作组织起来的寄存器机器，这些寄存器和操作构成了一组高效且方便的通用数据路径。通用机器的控制器是用于寄存器机器语言的解释器，就像我们一直在使用的那种。这种语言被称为机器的本机语言，或简称为机器语言。用机器语言编写的程序是使用机器数据路径的指令序列。例如，显式控制求值器的指令序列可以被视为通用计算机的机器语言程序，而不是专用解释器机器的控制器。

**校订后**

商用通用计算机是围绕一组寄存器和操作组织起来的寄存器机器，这些寄存器和操作构成了一组高效且方便的通用数据通路。通用机器的控制器是用于寄存器机器语言的解释器，就像我们一直在使用的那种。这种语言被称为机器的本机语言，或简称为机器语言。用机器语言编写的程序是使用机器数据通路的指令序列。例如，显式控制求值器的指令序列可以被视为通用计算机的机器语言程序，而不是专用解释器机器的控制器。

### 5_002e5:0008

**原文**

In this section, we explore the alternative strategy of compilation. A compiler for a given source language and machine translates a source program into an equivalent program (called the object program) written in the machine’s native language. The compiler that we implement in this section translates programs written in Scheme into sequences of instructions to be executed using the explicit-control evaluator machine’s data paths.[注319]

**校订前**

在本节中，我们探讨另一种策略：编译。针对给定源语言和机器的编译器将源程序翻译成用机器本机语言编写的等价程序（称为目标程序）。我们在本节中实现的编译器将用 Scheme 编写的程序翻译成使用显式控制求值器机器的数据路径执行的指令序列。[注319]

**校订后**

在本节中，我们探讨另一种策略：编译。针对给定源语言和机器的编译器将源程序翻译成用机器本机语言编写的等价程序（称为目标程序）。我们在本节中实现的编译器将用 Scheme 编写的程序翻译成使用显式控制求值器机器的数据通路执行的指令序列。[注319]

### 5_002e5:0010

**原文**

In view of the complementary advantages of compilation and interpretation, modern program-development environments pursue a mixed strategy. Lisp interpreters are generally organized so that interpreted procedures and compiled procedures can call each other. This enables a programmer to compile those parts of a program that are assumed to be debugged, thus gaining the efficiency advantage of compilation, while retaining the interpretive mode of execution for those parts of the program that are in the flux of interactive development and debugging. In 5.5.7, after we have implemented the compiler, we will show how to interface it with our interpreter to produce an integrated interpreter-compiler development system.

**校订前**

鉴于编译和解释的互补优势，现代程序开发环境采用混合策略。Lisp 解释器通常被组织成使被解释的过程和被编译的过程可以相互调用。这使程序员能够编译程序中假定已调试的部分，从而获得编译的效率优势，同时为程序中处于交互式开发和调试变动中的部分保留解释执行模式。在5.5.7中，在我们实现编译器之后，我们将展示如何将其与我们的解释器接口，以产生一个集成的解释器-编译器开发系统。

**校订后**

鉴于编译和解释的互补优势，现代程序开发环境采用混合策略。Lisp 解释器通常被组织成使被解释的过程和被编译的过程可以相互调用。这使程序员能够编译程序中假定已调试的部分，从而获得编译的效率优势，同时为程序中处于交互式开发和调试变动中的部分保留解释执行模式。在5.5.7中，在我们实现编译器之后，我们将展示如何将其与我们的解释器衔接，以产生一个集成的解释器-编译器开发系统。

### 5_002e5:0012

**原文**

Our compiler is much like our interpreter, both in its structure and in the function it performs. Accordingly, the mechanisms used by the compiler for analyzing expressions will be similar to those used by the interpreter. Moreover, to make it easy to interface compiled and interpreted code, we will design the compiler to generate code that obeys the same conventions of register usage as the interpreter: The environment will be kept in the `env` register, argument lists will be accumulated in `argl`, a procedure to be applied will be in `proc`, procedures will return their answers in `val`, and the location to which a procedure should return will be kept in `continue`. In general, the compiler translates a source program into an object program that performs essentially the same register operations as would the interpreter in evaluating the same source program.

**校订前**

我们的编译器在结构和所执行的功能上都很像我们的解释器。因此，编译器用于分析表达式的机制将类似于解释器所使用的机制。此外，为了便于接口编译代码和解释代码，我们将设计编译器生成遵循与解释器相同的寄存器使用约定的代码：环境将保存在`env`寄存器中，参数列表将累积在`argl`中，要应用的过程将位于`proc`中，过程将在`val`中返回它们的答案，过程应返回的位置将保存在`continue`中。一般来说，编译器将源程序翻译成目标程序，该目标程序执行与解释器在求值同一源程序时基本相同的寄存器操作。

**校订后**

我们的编译器在结构和所执行的功能上都很像我们的解释器。因此，编译器用于分析表达式的机制将类似于解释器所使用的机制。此外，为了便于让编译代码与解释代码相互调用，我们将设计编译器生成遵循与解释器相同的寄存器使用约定的代码：环境将保存在`env`寄存器中，参数表将累积在`argl`中，要应用的过程将位于`proc`中，过程将在`val`中返回它们的答案，过程应返回的位置将保存在`continue`中。一般来说，编译器将源程序翻译成目标程序，该目标程序执行与解释器在求值同一源程序时基本相同的寄存器操作。

### 5_002e5:0013

**原文**

This description suggests a strategy for implementing a rudimentary compiler: We traverse the expression in the same way the interpreter does. When we encounter a register instruction that the interpreter would perform in evaluating the expression, we do not execute the instruction but instead accumulate it into a sequence. The resulting sequence of instructions will be the object code. Observe the efficiency advantage of compilation over interpretation. Each time the interpreter evaluates an expression—for example, `(f 84 96)`—it performs the work of classifying the expression (discovering that this is a procedure application) and testing for the end of the operand list (discovering that there are two operands). With a compiler, the expression is analyzed only once, when the instruction sequence is generated at compile time. The object code produced by the compiler contains only the instructions that evaluate the operator and the two operands, assemble the argument list, and apply the procedure (in `proc`) to the arguments (in `argl`).

**校订前**

这一描述提出了实现一个基本编译器的策略：我们以与解释器相同的方式遍历表达式。当我们遇到解释器在求值表达式时会执行的寄存器指令时，我们不执行该指令，而是将其累积到一个序列中。得到的指令序列就是目标代码。观察编译相对于解释的效率优势。每次解释器求值一个表达式——例如`(f 84 96)`——它都要执行分类表达式的工作（发现这是一个过程应用）并测试操作数列表的末尾（发现有两个操作数）。使用编译器时，表达式只在编译时生成指令序列时被分析一次。编译器产生的目标代码只包含求值运算符和两个操作数、组装参数列表、并将过程（在`proc`中）应用于参数（在`argl`中）的指令。

**校订后**

这一描述提出了实现一个基本编译器的策略：我们以与解释器相同的方式遍历表达式。当我们遇到解释器在求值表达式时会执行的寄存器指令时，我们不执行该指令，而是将其累积到一个序列中。得到的指令序列就是目标代码。观察编译相对于解释的效率优势。每次解释器求值一个表达式——例如`(f 84 96)`——它都要执行分类表达式的工作（发现这是一个过程应用）并测试运算对象表的末尾（发现有两个运算对象）。使用编译器时，表达式只在编译时生成指令序列时被分析一次。编译器产生的目标代码只包含求值运算符和两个运算对象、组装参数表、并将过程（在`proc`中）应用于参数（在`argl`中）的指令。

### 5_002e5:0015

**原文**

As a case in point, consider the combination `(f 84 96)`. Before the interpreter evaluates the operator of the combination, it prepares for this evaluation by saving the registers containing the operands and the environment, whose values will be needed later. The interpreter then evaluates the operator to obtain the result in `val`, restores the saved registers, and finally moves the result from `val` to `proc`. However, in the particular expression we are dealing with, the operator is the symbol `f`, whose evaluation is accomplished by the machine operation `lookup-variable-value`, which does not alter any registers. The compiler that we implement in this section will take advantage of this fact and generate code that evaluates the operator using the instruction

**校订前**

作为一个例子，考虑组合式`(f 84 96)`。在解释器求值组合式的运算符之前，它通过保存包含操作数和环境的寄存器来为这次求值做准备，这些值以后会需要。然后解释器求值运算符以在`val`中获得结果，恢复保存的寄存器，最后将结果从`val`移到`proc`。然而，在我们处理的这个特定表达式中，运算符是符号`f`，它的求值由机器操作`lookup-variable-value`完成，该操作不改变任何寄存器。我们在本节实现的编译器将利用这一事实，生成使用指令求值运算符的代码

**校订后**

作为一个例子，考虑组合式`(f 84 96)`。在解释器求值组合式的运算符之前，它通过保存包含运算对象和环境的寄存器来为这次求值做准备，这些值以后会需要。然后解释器求值运算符以在`val`中获得结果，恢复保存的寄存器，最后将结果从`val`移到`proc`。然而，在我们处理的这个特定表达式中，运算符是符号`f`，它的求值由机器操作`lookup-variable-value`完成，该操作不改变任何寄存器。我们在本节实现的编译器将利用这一事实，生成使用指令求值运算符的代码

### 5_002e5:0020

**原文**

The procedure `compile` is the top-level dispatch in the compiler. It corresponds to the `eval` procedure of 4.1.1, the `analyze` procedure of 4.1.7, and the `eval-dispatch` entry point of the explicit-control-evaluator in 5.4.1. The compiler, like the interpreters, uses the expression-syntax procedures defined in 4.1.2.[注320] `Compile` performs a case analysis on the syntactic type of the expression to be compiled. For each type of expression, it dispatches to a specialized code generator:

**校订前**

过程`compile`是编译器中的顶层分派。它对应于4.1.1的`eval`过程、4.1.7的`analyze`过程，以及5.4.1中显式控制求值器的`eval-dispatch`入口点。编译器与解释器一样，使用4.1.2中定义的表达式语法过程。[注320] `Compile`对待编译表达式的语法类型进行案例分析。对于每种表达式类型，它分派到一个专门的 代码生成器：

**校订后**

过程`compile`是编译器中的顶层分派。它对应于4.1.1的`eval`过程、4.1.7的`analyze`过程，以及5.4.1中显式控制求值器的`eval-dispatch`入口点。编译器与解释器一样，使用4.1.2中定义的表达式语法过程。[注320] `Compile`对待编译表达式的语法类型进行分情况分析。对于每种表达式类型，它分派到一个专门的 代码生成器：

### 5_002e5:0025

**原文**

jump to a named entry point (this is specified by using the designated label as the linkage descriptor).

**校订前**

跳转到一个命名的入口点（这通过使用指定的标签作为链接描述符来指定）。

**校订后**

跳转到一个命名的入口点（这通过使用指定的标号作为链接描述符来指定）。

### 5_002e5:0026

**原文**

For example, compiling the expression `5` (which is self-evaluating) with a target of the `val` register and a linkage of `next` should produce the instruction

**校订前**

例如，编译表达式`5`（它是自求值的），目标为`val`寄存器，连接为`next`，应该产生指令

**校订后**

例如，编译表达式`5`（它是自求值的），目标为`val`寄存器，链接为`next`，应该产生指令

### 5_002e5:0027

**原文**

Compiling the same expression with a linkage of `return` should produce the instructions

**校订前**

用连接`return`编译同一个表达式应该产生指令

**校订后**

用链接`return`编译同一个表达式应该产生指令

### 5_002e5:0030

**原文**

Each code generator returns an instruction sequence containing the object code it has generated for the expression. Code generation for a compound expression is accomplished by combining the output from simpler code generators for component expressions, just as evaluation of a compound expression is accomplished by evaluating the component expressions.

**校订前**

每个代码生成器返回一个指令序列，其中包含它为表达式生成的目标代码。复合表达式的代码生成是通过组合来自组件表达式的更简单代码生成器的输出来完成的，就像复合表达式的求值是通过求值组件表达式来完成的一样。

**校订后**

每个代码生成器返回一个指令序列，其中包含它为表达式生成的目标代码。复合表达式的代码生成是通过组合来自组成部分的表达式的更简单代码生成器的输出来完成的，就像复合表达式的求值是通过求值组成部分的表达式来完成的一样。

### 5_002e5:0044

**原文**

Exercise 5.31: In evaluating a procedure application, the explicit-control evaluator always saves and restores the `env` register around the evaluation of the operator, saves and restores `env` around the evaluation of each operand (except the final one), saves and restores `argl` around the evaluation of each operand, and saves and restores `proc` around the evaluation of the operand sequence. For each of the following combinations, say which of these `save` and `restore` operations are superfluous and thus could be eliminated by the compiler’s `preserving` mechanism:

**校订前**

习题5.31：在求值过程应用时，显式控制求值器总是在求值运算符时保存和恢复`env`寄存器，在求值每个操作数（除了最后一个）时保存和恢复`env`，在求值每个操作数时保存和恢复`argl`，并在求值操作数序列时保存和恢复`proc`。对于以下每个组合，说明这些`save`和`restore`操作中哪些是多余的，因此可以被编译器的`preserving`机制消除：

**校订后**

习题5.31：在求值过程应用时，显式控制求值器总是在求值运算符时保存和恢复`env`寄存器，在求值每个运算对象（除了最后一个）时保存和恢复`env`，在求值每个运算对象时保存和恢复`argl`，并在求值运算对象序列时保存和恢复`proc`。对于以下每个组合式，说明这些`save`和`restore`操作中哪些是多余的，因此可以被编译器的`preserving`机制消除：

### 5_002e5:0045

**原文**

Exercise 5.32: Using the `preserving` mechanism, the compiler will avoid saving and restoring `env` around the evaluation of the operator of a combination in the case where the operator is a symbol. We could also build such optimizations into the evaluator. Indeed, the explicit-control evaluator of 5.4 already performs a similar optimization, by treating combinations with no operands as a special case.

**校订前**

习题5.32：使用`preserving`机制，编译器将在运算符是符号的情况下，避免在求值组合的运算符时保存和恢复`env`。我们也可以将这样的优化构建到求值器中。事实上，5.4的显式控制求值器已经执行了类似的优化，通过将没有操作数的组合作为特殊情况处理。

**校订后**

习题5.32：使用`preserving`机制，编译器将在运算符是符号的情况下，避免在求值组合式的运算符时保存和恢复`env`。我们也可以将这样的优化构建到求值器中。事实上，5.4的显式控制求值器已经执行了类似的优化，通过将没有运算对象的组合式作为特殊情况处理。

### 5_002e5:0050

**原文**

Compiling linkage code

**校订前**

编译连接代码

**校订后**

编译链接代码

### 5_002e5:0051

**原文**

In general, the output of each code generator will end with instructions—generated by the procedure `compile-linkage`—that implement the required linkage. If the linkage is `return` then we must generate the instruction `(goto (reg continue))`. This needs the `continue` register and does not modify any registers. If the linkage is `next`, then we needn’t include any additional instructions. Otherwise, the linkage is a label, and we generate a `goto` to that label, an instruction that does not need or modify any registers.[注321]

**校订前**

一般来说，每个代码生成器的输出都会以由过程 `compile-linkage` 生成的指令结尾，这些指令实现所需的连接。如果连接是 `return`，那么我们必须生成指令 `(goto (reg continue))`。这需要 `continue` 寄存器，并且不修改任何寄存器。如果连接是 `next`，那么我们无需包含任何额外指令。否则，连接是一个标签，我们生成一条到该标签的 `goto`，这条指令不需要也不修改任何寄存器。[注321]

**校订后**

一般来说，每个代码生成器的输出都会以由过程 `compile-linkage` 生成的指令结尾，这些指令实现所需的链接。如果链接是 `return`，那么我们必须生成指令 `(goto (reg continue))`。这需要 `continue` 寄存器，并且不修改任何寄存器。如果链接是 `next`，那么我们无需包含任何额外指令。否则，链接是一个标号，我们生成一条到该标号的 `goto`，这条指令不需要也不修改任何寄存器。[注321]

### 5_002e5:0052

**原文**

The linkage code is appended to an instruction sequence by `preserving` the `continue` register, since a `return` linkage will require the `continue` register: If the given instruction sequence modifies `continue` and the linkage code needs it, `continue` will be saved and restored.

**校订前**

连接代码通过 `preserving` `continue` 寄存器追加到指令序列上，因为 `return` 连接将需要 `continue` 寄存器：如果给定的指令序列修改了 `continue` 而连接代码需要它，`continue` 将被保存和恢复。

**校订后**

链接代码通过 `preserving` `continue` 寄存器追加到指令序列上，因为 `return` 链接将需要 `continue` 寄存器：如果给定的指令序列修改了 `continue` 而链接代码需要它，`continue` 将被保存和恢复。

### 5_002e5:0054

**原文**

The code generators for self-evaluating expressions, quotations, and variables construct instruction sequences that assign the required value to the target register and then proceed as specified by the linkage descriptor.

**校订前**

用于自求值表达式、引用和变量的代码生成器构造指令序列，这些指令序列将所需的值赋给目标寄存器，然后按照连接描述符的指定继续执行。

**校订后**

用于自求值表达式、引用和变量的代码生成器构造指令序列，这些指令序列将所需的值赋给目标寄存器，然后按照链接描述符的指定继续执行。

### 5_002e5:0056

**原文**

Assignments and definitions are handled much as they are in the interpreter. We recursively generate code that computes the value to be assigned to the variable, and append to it a two-instruction sequence that actually sets or defines the variable and assigns the value of the whole expression (the symbol `ok`) to the target register. The recursive compilation has target `val` and linkage `next` so that the code will put its result into `val` and continue with the code that is appended after it. The appending is done preserving `env`, since the environment is needed for setting or defining the variable and the code for the variable value could be the compilation of a complex expression that might modify the registers in arbitrary ways.

**校订前**

赋值和定义的处理方式与解释器中大致相同。我们递归地生成计算要赋给变量的值的代码，并在其后追加一个两条指令的序列，该序列实际设置或定义变量，并将整个表达式的值（符号 `ok`）赋给目标寄存器。递归编译的目标为 `val`，连接为 `next`，这样代码会将其结果放入 `val`，并继续执行追加在其后的代码。追加操作在保留 `env` 的情况下进行，因为设置或定义变量需要环境，而变量值的代码可能是对复杂表达式的编译，该表达式可能以任意方式修改寄存器。

**校订后**

赋值和定义的处理方式与解释器中大致相同。我们递归地生成计算要赋给变量的值的代码，并在其后追加一个两条指令的序列，该序列实际设置或定义变量，并将整个表达式的值（符号 `ok`）赋给目标寄存器。递归编译的目标为 `val`，链接为 `next`，这样代码会将其结果放入 `val`，并继续执行追加在其后的代码。追加操作在保留 `env` 的情况下进行，因为设置或定义变量需要环境，而变量值的代码可能是对复杂表达式的编译，该表达式可能以任意方式修改寄存器。

### 5_002e5:0059

**原文**

The code for an `if` expression compiled with a given target and linkage has the form

**校订前**

用给定目标和连接编译的 `if` 表达式的代码具有以下形式

**校订后**

用给定目标和链接编译的 `if` 表达式的代码具有以下形式

### 5_002e5:0060

**原文**

To generate this code, we compile the predicate, consequent, and alternative, and combine the resulting code with instructions to test the predicate result and with newly generated labels to mark the true and false branches and the end of the conditional.[注322] In this arrangement of code, we must branch around the true branch if the test is false. The only slight complication is in how the linkage for the true branch should be handled. If the linkage for the conditional is `return` or a label, then the true and false branches will both use this same linkage. If the linkage is `next`, the true branch ends with a jump around the code for the false branch to the label at the end of the conditional.

**校订前**

为了生成这段代码，我们编译谓词、推论和替代，并将生成的代码与测试谓词结果的指令以及新生成的标签组合起来，以标记真分支、假分支和条件表达式的结尾。[注322] 在这种代码安排中，如果测试为假，我们必须绕过真分支。唯一稍微复杂的地方在于如何处理真分支的连接。如果条件表达式的连接是 `return` 或一个标签，那么真分支和假分支都将使用相同的连接。如果连接是 `next`，真分支以跳过假分支代码并跳转到条件表达式末尾标签的跳转结束。

**校订后**

为了生成这段代码，我们编译谓词、结果表达式和替代表达式，并将生成的代码与测试谓词结果的指令以及新生成的标号组合起来，以标记真分支、假分支和条件表达式的结尾。[注322] 在这种代码安排中，如果测试为假，我们必须绕过真分支。唯一稍微复杂的地方在于如何处理真分支的链接。如果条件表达式的链接是 `return` 或一个标号，那么真分支和假分支都将使用相同的链接。如果链接是 `next`，真分支以跳过假分支代码并跳转到条件表达式末尾标号的跳转结束。

### 5_002e5:0061

**原文**

`Env` is preserved around the predicate code because it could be needed by the true and false branches, and `continue` is preserved because it could be needed by the linkage code in those branches. The code for the true and false branches (which are not executed sequentially) is appended using a special combiner `parallel-instruction-sequences` described in 5.5.4.

**校订前**

`Env` 在谓词代码周围被保留，因为真分支和假分支可能需要它；`continue` 被保留，因为这些分支中的连接代码可能需要它。真分支和假分支的代码（它们不是顺序执行的）使用 5.5.4 中描述的特殊组合器 `parallel-instruction-sequences` 追加。

**校订后**

`Env` 在谓词代码周围被保留，因为真分支和假分支可能需要它；`continue` 被保留，因为这些分支中的链接代码可能需要它。真分支和假分支的代码（它们不是顺序执行的）使用 5.5.4 中描述的特殊组合器 `parallel-instruction-sequences` 追加。

### 5_002e5:0064

**原文**

The compilation of sequences (from procedure bodies or explicit `begin` expressions) parallels their evaluation. Each expression of the sequence is compiled—the last expression with the linkage specified for the sequence, and the other expressions with linkage `next` (to execute the rest of the sequence). The instruction sequences for the individual expressions are appended to form a single instruction sequence, such that `env` (needed for the rest of the sequence) and `continue` (possibly needed for the linkage at the end of the sequence) are preserved.

**校订前**

序列的编译（来自过程体或显式 `begin` 表达式）与其求值类似。序列中的每个表达式都被编译——最后一个表达式使用为序列指定的连接，其他表达式使用连接 `next`（以执行序列的其余部分）。各个表达式的指令序列被追加形成单个指令序列，使得 `env`（序列其余部分所需）和 `continue`（序列末尾的连接可能所需）被保留。

**校订后**

序列的编译（来自过程体或显式 `begin` 表达式）与其求值类似。序列中的每个表达式都被编译——最后一个表达式使用为序列指定的链接，其他表达式使用链接 `next`（以执行序列的其余部分）。各个表达式的指令序列被追加形成单个指令序列，使得 `env`（序列其余部分所需）和 `continue`（序列末尾的链接可能所需）被保留。

### 5_002e5:0067

**原文**

When we compile the `lambda` expression, we also generate the code for the procedure body. Although the body won’t be executed at the time of procedure construction, it is convenient to insert it into the object code right after the code for the `lambda`. If the linkage for the `lambda` expression is a label or `return`, this is fine. But if the linkage is `next`, we will need to skip around the code for the procedure body by using a linkage that jumps to a label that is inserted after the body. The object code thus has the form

**校订前**

当我们编译 `lambda` 表达式时，我们还生成过程体的代码。尽管过程体在过程构造时不会被执行，但将其插入到 `lambda` 的代码之后的目标代码中很方便。如果 `lambda` 表达式的连接是一个标签或 `return`，这没问题。但如果连接是 `next`，我们将需要使用一个跳转到插入在过程体之后的标签的连接来跳过过程体的代码。因此目标代码具有以下形式

**校订后**

当我们编译 `lambda` 表达式时，我们还生成过程体的代码。尽管过程体在过程构造时不会被执行，但将其插入到 `lambda` 的代码之后的目标代码中很方便。如果 `lambda` 表达式的链接是一个标号或 `return`，这没问题。但如果链接是 `next`，我们将需要使用一个跳转到插入在过程体之后的标号的链接来跳过过程体的代码。因此目标代码具有以下形式

### 5_002e5:0068

**原文**

`Compile-lambda` generates the code for constructing the procedure object followed by the code for the procedure body. The procedure object will be constructed at run time by combining the current environment (the environment at the point of definition) with the entry point to the compiled procedure body (a newly generated label).[注323]

**校订前**

`Compile-lambda` 生成用于构造过程对象的代码，随后是过程体的代码。过程对象将在运行时通过将当前环境（定义点处的环境）与已编译过程体的入口点（一个新生成的标签）组合起来而构造。[注323]

**校订后**

`Compile-lambda` 生成用于构造过程对象的代码，随后是过程体的代码。过程对象将在运行时通过将当前环境（定义点处的环境）与已编译过程体的入口点（一个新生成的标号）组合起来而构造。[注323]

### 5_002e5:0069

**原文**

`Compile-lambda` uses the special combiner `tack-on-instruction-sequence` rather than `append-instruction-sequences` (5.5.4) to append the procedure body to the `lambda` expression code, because the body is not part of the sequence of instructions that will be executed when the combined sequence is entered; rather, it is in the sequence only because that was a convenient place to put it.

**校订前**

`Compile-lambda` 使用特殊组合子 `tack-on-instruction-sequence` 而不是 `append-instruction-sequences`（5.5.4）来将过程体附加到 `lambda` 表达式代码上，因为过程体不是当组合后的序列被进入时将执行的指令序列的一部分；它出现在该序列中仅仅是因为那是一个方便放置它的地方。

**校订后**

`Compile-lambda` 使用特殊组合器 `tack-on-instruction-sequence` 而不是 `append-instruction-sequences`（5.5.4）来将过程体附加到 `lambda` 表达式代码上，因为过程体不是当组合后的序列被进入时将执行的指令序列的一部分；它出现在该序列中仅仅是因为那是一个方便放置它的地方。

### 5_002e5:0070

**原文**

`Compile-lambda-body` constructs the code for the body of the procedure. This code begins with a label for the entry point. Next come instructions that will cause the run-time evaluation environment to switch to the correct environment for evaluating the procedure body—namely, the definition environment of the procedure, extended to include the bindings of the formal parameters to the arguments with which the procedure is called. After this comes the code for the sequence of expressions that makes up the procedure body. The sequence is compiled with linkage `return` and target `val` so that it will end by returning from the procedure with the procedure result in `val`.

**校订前**

`Compile-lambda-body` 构造过程体的代码。这段代码以一个入口点标签开始。接下来是使运行时求值环境切换到用于求值过程体的正确环境的指令——即过程定义环境，并扩展以包含形式参数到调用过程时所用实参的绑定。在这之后是构成过程体的表达式序列的代码。该序列以连接 `return` 和目标 `val` 进行编译，以便它最终从过程返回，过程结果在 `val` 中。

**校订后**

`Compile-lambda-body` 构造过程体的代码。这段代码以一个入口点标号开始。接下来是使运行时求值环境切换到用于求值过程体的正确环境的指令——即过程定义环境，并扩展以包含形式参数到调用过程时所用实参的绑定。在这之后是构成过程体的表达式序列的代码。该序列以链接 `return` 和目标 `val` 进行编译，以便它最终从过程返回，过程结果在 `val` 中。

### 5_002e5:0072

**原文**

The essence of the compilation process is the compilation of procedure applications. The code for a combination compiled with a given target and linkage has the form

**校订前**

编译过程的本质是过程应用的编译。以给定目标和连接编译的组合式的代码具有如下形式

**校订后**

编译过程的本质是过程应用的编译。以给定目标和链接编译的组合式的代码具有如下形式

### 5_002e5:0074

**原文**

The required code is generated by `compile-application`. This recursively compiles the operator, to produce code that puts the procedure to be applied into `proc`, and compiles the operands, to produce code that evaluates the individual operands of the application. The instruction sequences for the operands are combined (by `construct-arglist`) with code that constructs the list of arguments in `argl`, and the resulting argument-list code is combined with the procedure code and the code that performs the procedure call (produced by `compile-procedure-call`). In appending the code sequences, the `env` register must be preserved around the evaluation of the operator (since evaluating the operator might modify `env`, which will be needed to evaluate the operands), and the `proc` register must be preserved around the construction of the argument list (since evaluating the operands might modify `proc`, which will be needed for the actual procedure application). `Continue` must also be preserved throughout, since it is needed for the linkage in the procedure call.

**校订前**

所需的代码由 `compile-application` 生成。它递归地编译运算符，以产生将待应用的过程放入 `proc` 的代码，并编译运算对象，以产生求值应用的各个运算对象的代码。运算对象的指令序列（由 `construct-arglist`）与在 `argl` 中构造实参表的代码组合，得到的实参表代码与过程代码以及执行过程调用的代码（由 `compile-procedure-call` 产生）组合。在附加代码序列时，`env` 寄存器必须在求值运算符前后被保留（因为求值运算符可能修改 `env`，而求值运算对象将需要它），并且 `proc` 寄存器必须在构造实参表前后被保留（因为求值运算对象可能修改 `proc`，而实际的过程应用将需要它）。`Continue` 也必须始终被保留，因为过程调用中的连接需要它。

**校订后**

所需的代码由 `compile-application` 生成。它递归地编译运算符，以产生将待应用的过程放入 `proc` 的代码，并编译运算对象，以产生求值应用的各个运算对象的代码。运算对象的指令序列（由 `construct-arglist`）与在 `argl` 中构造实参表的代码组合，得到的实参表代码与过程代码以及执行过程调用的代码（由 `compile-procedure-call` 产生）组合。在附加代码序列时，`env` 寄存器必须在求值运算符前后被保留（因为求值运算符可能修改 `env`，而求值运算对象将需要它），并且 `proc` 寄存器必须在构造实参表前后被保留（因为求值运算对象可能修改 `proc`，而实际的过程应用将需要它）。`Continue` 也必须始终被保留，因为过程调用中的链接需要它。

### 5_002e5:0081

**原文**

Observe that the compiled branch must skip around the primitive branch. Therefore, if the linkage for the original procedure call was `next`, the compound branch must use a linkage that jumps to a label that is inserted after the primitive branch. (This is similar to the linkage used for the true branch in `compile-if`.)

**校订前**

注意，已编译分支必须跳过基本过程分支。因此，如果原始过程调用的连接是 `next`，则复合分支必须使用跳转到插入在基本过程分支之后的标签的连接。（这类似于 `compile-if` 中真分支所使用的连接。）

**校订后**

注意，已编译分支必须跳过基本过程分支。因此，如果原始过程调用的链接是 `next`，则复合分支必须使用跳转到插入在基本过程分支之后的标号的链接。（这类似于 `compile-if` 中真分支所使用的链接。）

### 5_002e5:0084

**原文**

The code that handles procedure application is the most subtle part of the compiler, even though the instruction sequences it generates are very short. A compiled procedure (as constructed by `compile-lambda`) has an entry point, which is a label that designates where the code for the procedure starts. The code at this entry point computes a result in `val` and returns by executing the instruction `(goto (reg continue))`. Thus, we might expect the code for a compiled-procedure application (to be generated by `compile-proc-appl`) with a given target and linkage to look like this if the linkage is a label

**校订前**

处理过程应用的代码是编译器中最微妙的部分，尽管它生成的指令序列非常短。一个编译后的过程（由`compile-lambda`构造）有一个入口点，即一个标号，指定过程代码开始的位置。这个入口点处的代码在`val`中计算出一个结果，并通过执行指令`(goto (reg continue))`返回。因此，对于给定目标寄存器和连接方式的编译过程应用（将由`compile-proc-appl`生成），如果连接方式是一个标号，我们可能期望代码看起来像这样：

**校订后**

处理过程应用的代码是编译器中最微妙的部分，尽管它生成的指令序列非常短。一个编译后的过程（由`compile-lambda`构造）有一个入口点，即一个标号，指定过程代码开始的位置。这个入口点处的代码在`val`中计算出一个结果，并通过执行指令`(goto (reg continue))`返回。因此，对于给定目标寄存器和链接方式的编译过程应用（将由`compile-proc-appl`生成），如果链接方式是一个标号，我们可能期望代码看起来像这样：

### 5_002e5:0085

**原文**

or like this if the linkage is `return`.

**校订前**

或者如果连接方式是`return`，则像这样。

**校订后**

或者如果链接方式是`return`，则像这样。

### 5_002e5:0086

**原文**

This code sets up `continue` so that the procedure will return to a label `proc-return` and jumps to the procedure’s entry point. The code at `proc-return` transfers the procedure’s result from `val` to the target register (if necessary) and then jumps to the location specified by the linkage. (The linkage is always `return` or a label, because `compile-procedure-call` replaces a `next` linkage for the compound-procedure branch by an `after-call` label.)

**校订前**

这段代码设置`continue`，使得过程将返回到标号`proc-return`，并跳转到过程的入口点。`proc-return`处的代码将过程的结果从`val`传送到目标寄存器（如果需要），然后跳转到连接方式指定的位置。（连接方式总是`return`或一个标号，因为`compile-procedure-call`将复合过程分支的`next`连接方式替换为`after-call`标号。）

**校订后**

这段代码设置`continue`，使得过程将返回到标号`proc-return`，并跳转到过程的入口点。`proc-return`处的代码将过程的结果从`val`传送到目标寄存器（如果需要），然后跳转到链接方式指定的位置。（链接方式总是`return`或一个标号，因为`compile-procedure-call`将复合过程分支的`next`链接方式替换为`after-call`标号。）

### 5_002e5:0087

**原文**

In fact, if the target is not `val`, that is exactly the code our compiler will generate.[注324] Usually, however, the target is `val` (the only time the compiler specifies a different register is when targeting the evaluation of an operator to `proc`), so the procedure result is put directly into the target register and there is no need to return to a special location that copies it. Instead, we simplify the code by setting up `continue` so that the procedure will “return” directly to the place specified by the caller’s linkage:

**校订前**

事实上，如果目标不是`val`，那正是我们的编译器将生成的代码。[注324]然而，通常目标是`val`（编译器指定不同寄存器的唯一情况是当针对运算符求值而指向`proc`时），因此过程结果直接放入目标寄存器，无需返回到一个特殊位置来复制它。相反，我们通过设置`continue`来简化代码，使得过程将直接“返回”到调用者的连接方式所指定的位置：

**校订后**

事实上，如果目标不是`val`，那正是我们的编译器将生成的代码。[注324]然而，通常目标是`val`（编译器指定不同寄存器的唯一情况是当针对运算符求值而指向`proc`时），因此过程结果直接放入目标寄存器，无需返回到一个特殊位置来复制它。相反，我们通过设置`continue`来简化代码，使得过程将直接“返回”到调用者的链接方式所指定的位置：

### 5_002e5:0088

**原文**

If the linkage is a label, we set up `continue` so that the procedure will return to that label. (That is, the `(goto (reg continue))` the procedure ends with becomes equivalent to the `(goto (label ⟨linkage⟩))` at `proc-return` above.)

**校订前**

如果连接方式是一个标号，我们设置`continue`，使得过程将返回到该标号。（也就是说，过程结尾的`(goto (reg continue))`变得等价于上面`proc-return`处的`(goto (label ⟨linkage⟩))`。）

**校订后**

如果链接方式是一个标号，我们设置`continue`，使得过程将返回到该标号。（也就是说，过程结尾的`(goto (reg continue))`变得等价于上面`proc-return`处的`(goto (label ⟨linkage⟩))`。）

### 5_002e5:0089

**原文**

If the linkage is `return`, we don’t need to set up `continue` at all: It already holds the desired location. (That is, the `(goto (reg continue))` the procedure ends with goes directly to the place where the `(goto (reg continue))` at `proc-return` would have gone.)

**校订前**

如果连接方式是`return`，我们根本不需要设置`continue`：它已经保存了所需的位置。（也就是说，过程结尾的`(goto (reg continue))`直接转到`proc-return`处的`(goto (reg continue))`本来会去的地方。）

**校订后**

如果链接方式是`return`，我们根本不需要设置`continue`：它已经保存了所需的位置。（也就是说，过程结尾的`(goto (reg continue))`直接转到`proc-return`处的`(goto (reg continue))`本来会去的地方。）

### 5_002e5:0090

**原文**

With this implementation of the `return` linkage, the compiler generates tail-recursive code. Calling a procedure as the final step in a procedure body does a direct transfer, without saving any information on the stack.

**校订前**

通过这种`return`连接方式的实现，编译器生成尾递归代码。在过程体的最后一步调用过程会进行直接转移，而不在栈上保存任何信息。

**校订后**

通过这种`return`链接方式的实现，编译器生成尾递归代码。在过程体的最后一步调用过程会进行直接转移，而不在栈上保存任何信息。

### 5_002e5:0091

**原文**

Suppose instead that we had handled the case of a procedure call with a linkage of `return` and a target of `val` as shown above for a non-`val` target. This would destroy tail recursion. Our system would still give the same value for any expression. But each time we called a procedure, we would save `continue` and return after the call to undo the (useless) save. These extra saves would accumulate during a nest of procedure calls.[注325]

**校订前**

假设相反，我们像上面针对非`val`目标所示的那样，处理了连接方式为`return`且目标为`val`的过程调用情况。这会破坏尾递归。我们的系统对于任何表达式仍然会给出相同的值。但每次调用过程时，我们会保存`continue`，并在调用返回后撤销（无用的）保存。这些额外的保存在嵌套的过程调用中会累积。[注325]

**校订后**

假设相反，我们像上面针对非`val`目标所示的那样，处理了链接方式为`return`且目标为`val`的过程调用情况。这会破坏尾递归。我们的系统对于任何表达式仍然会给出相同的值。但每次调用过程时，我们会保存`continue`，并在调用返回后撤销（无用的）保存。这些额外的保存在嵌套的过程调用中会累积。[注325]

### 5_002e5:0092

**原文**

`Compile-proc-appl` generates the above procedure-application code by considering four cases, depending on whether the target for the call is `val` and whether the linkage is `return`. Observe that the instruction sequences are declared to modify all the registers, since executing the procedure body can change the registers in arbitrary ways.[注326] Also note that the code sequence for the case with target `val` and linkage `return` is declared to need `continue`: Even though `continue` is not explicitly used in the two-instruction sequence, we must be sure that `continue` will have the correct value when we enter the compiled procedure.

**校订前**

`Compile-proc-appl`通过考虑四种情况来生成上述过程应用代码，取决于调用的目标是`val`以及连接方式是否为`return`。注意，这些指令序列被声明为修改所有寄存器，因为执行过程体可以以任意方式改变寄存器。[注326]还要注意，目标为`val`且连接方式为`return`的情况的代码序列被声明为需要`continue`：即使在两条指令的序列中没有显式使用`continue`，我们也必须确保在进入编译后的过程时`continue`具有正确的值。

**校订后**

`Compile-proc-appl`通过考虑四种情况来生成上述过程应用代码，取决于调用的目标是否为`val`以及链接方式是否为`return`。注意，这些指令序列被声明为修改所有寄存器，因为执行过程体可以以任意方式改变寄存器。[注326]还要注意，目标为`val`且链接方式为`return`的情况的代码序列被声明为需要`continue`：即使在两条指令的序列中没有显式使用`continue`，我们也必须确保在进入编译后的过程时`continue`具有正确的值。

### 5_002e5:0094

**原文**

This section describes the details on how instruction sequences are represented and combined. Recall from 5.5.1 that an instruction sequence is represented as a list of the registers needed, the registers modified, and the actual instructions. We will also consider a label (symbol) to be a degenerate case of an instruction sequence, which doesn’t need or modify any registers. So to determine the registers needed and modified by instruction sequences we use the selectors

**校订前**

本节详细描述指令序列如何表示和组合。回忆5.5.1，指令序列表示为一个表，包含所需的寄存器、修改的寄存器以及实际的指令。我们还将标号（符号）视为指令序列的退化情况，它不需要也不修改任何寄存器。因此，为了确定指令序列所需和修改的寄存器，我们使用选择器

**校订后**

本节详细描述指令序列如何表示和组合。回忆5.5.1，指令序列表示为一个表，包含所需的寄存器、修改的寄存器以及实际的指令。我们还将标号（符号）视为指令序列的退化情况，它不需要也不修改任何寄存器。因此，为了确定指令序列所需和修改的寄存器，我们使用选择函数

### 5_002e5:0096

**原文**

In terms of these predicates and selectors, we can implement the various instruction sequence combiners used throughout the compiler.

**校订前**

根据这些谓词和选择器，我们可以实现整个编译器中使用的各种指令序列组合器。

**校订后**

根据这些谓词和选择函数，我们可以实现整个编译器中使用的各种指令序列组合器。

### 5_002e5:0100

**原文**

`Preserving`, the second major instruction sequence combiner, takes a list of registers `regs` and two instruction sequences `seq1` and `seq2` that are to be executed sequentially. It returns an instruction sequence whose statements are the statements of `seq1` followed by the statements of `seq2`, with appropriate `save` and `restore` instructions around `seq1` to protect the registers in `regs` that are modified by `seq1` but needed by `seq2`. To accomplish this, `preserving` first creates a sequence that has the required `save`s followed by the statements of `seq1` followed by the required `restore`s. This sequence needs the registers being saved and restored in addition to the registers needed by `seq1`, and modifies the registers modified by `seq1` except for the ones being saved and restored. This augmented sequence and `seq2` are then appended in the usual way. The following procedure implements this strategy recursively, walking down the list of registers to be preserved:[注327]

**校订前**

`Preserving`，第二个主要的指令序列组合子，接受一个寄存器表`regs`以及两个要顺序执行的指令序列`seq1`和`seq2`。它返回一个指令序列，其语句是`seq1`的语句后接`seq2`的语句，并在`seq1`周围加上适当的`save`和`restore`指令，以保护`regs`中那些被`seq1`修改但`seq2`需要的寄存器。为实现这一点，`preserving`首先创建一个序列，其中包含所需的`save`，后接`seq1`的语句，再接所需的`restore`。这个序列除了需要`seq1`所需的寄存器外，还需要那些被保存和恢复的寄存器，并且会修改`seq1`所修改的寄存器，但被保存和恢复的那些寄存器除外。然后，这个扩充后的序列和`seq2`按通常方式被追加在一起。下面的过程递归地实现这一策略，沿着要保留的寄存器表向下遍历：[注327]

**校订后**

`Preserving`，第二个主要的指令序列组合器，接受一个寄存器表`regs`以及两个要顺序执行的指令序列`seq1`和`seq2`。它返回一个指令序列，其语句是`seq1`的语句后接`seq2`的语句，并在`seq1`周围加上适当的`save`和`restore`指令，以保护`regs`中那些被`seq1`修改但`seq2`需要的寄存器。为实现这一点，`preserving`首先创建一个序列，其中包含所需的`save`，后接`seq1`的语句，再接所需的`restore`。这个序列除了需要`seq1`所需的寄存器外，还需要那些被保存和恢复的寄存器，并且会修改`seq1`所修改的寄存器，但被保存和恢复的那些寄存器除外。然后，这个扩充后的序列和`seq2`按通常方式被追加在一起。下面的过程递归地实现这一策略，沿着要保留的寄存器表向下遍历：[注327]

### 5_002e5:0101

**原文**

Another sequence combiner, `tack-on-instruction-sequence`, is used by `compile-lambda` to append a procedure body to another sequence. Because the procedure body is not “in line” to be executed as part of the combined sequence, its register use has no impact on the register use of the sequence in which it is embedded. We thus ignore the procedure body’s sets of needed and modified registers when we tack it onto the other sequence.

**校订前**

另一个序列组合子`tack-on-instruction-sequence`被`compile-lambda`用来将一个过程体追加到另一个序列上。由于过程体并不是“按行”作为组合序列的一部分来执行的，它的寄存器使用不会影响它所嵌入的那个序列的寄存器使用。因此，当我们将过程体附加到另一个序列上时，我们忽略该过程体所需的和所修改的寄存器集合。

**校订后**

另一个序列组合器`tack-on-instruction-sequence`被`compile-lambda`用来将一个过程体追加到另一个序列上。由于过程体并不是“顺序地”作为组合序列的一部分来执行的，它的寄存器使用不会影响它所嵌入的那个序列的寄存器使用。因此，当我们将过程体附加到另一个序列上时，我们忽略该过程体所需的和所修改的寄存器集合。

### 5_002e5:0102

**原文**

`Compile-if` and `compile-procedure-call` use a special combiner called `parallel-instruction-sequences` to append the two alternative branches that follow a test. The two branches will never be executed sequentially; for any particular evaluation of the test, one branch or the other will be entered. Because of this, the registers needed by the second branch are still needed by the combined sequence, even if these are modified by the first branch.

**校订前**

`Compile-if`和`compile-procedure-call`使用一个称为`parallel-instruction-sequences`的特殊组合子来追加测试之后的两个备选分支。这两个分支永远不会顺序执行；对于测试的任何一次特定求值，都会进入其中一个分支或另一个分支。因此，第二个分支所需的寄存器对于组合后的序列仍然是需要的，即使这些寄存器被第一个分支修改了。

**校订后**

`Compile-if`和`compile-procedure-call`使用一个称为`parallel-instruction-sequences`的特殊组合器来追加测试之后的两个备选分支。这两个分支永远不会顺序执行；对于测试的任何一次特定求值，都会进入其中一个分支或另一个分支。因此，第二个分支所需的寄存器对于组合后的序列仍然是需要的，即使这些寄存器被第一个分支修改了。

### 5_002e5:0105

**原文**

We have specified that the value of the `define` expression should be placed in the `val` register. We don’t care what the compiled code does after executing the `define`, so our choice of `next` as the linkage descriptor is arbitrary.

**校订前**

我们已经指定`define`表达式的值应放在`val`寄存器中。我们不关心编译后的代码在执行完`define`之后做什么，因此选择`next`作为连接描述符是任意的。

**校订后**

我们已经指定`define`表达式的值应放在`val`寄存器中。我们不关心编译后的代码在执行完`define`之后做什么，因此选择`next`作为链接描述符是任意的。

### 5_002e5:0106

**原文**

`Compile` determines that the expression is a definition, so it calls `compile-definition` to compile code to compute the value to be assigned (targeted to `val`), followed by code to install the definition, followed by code to put the value of the `define` (which is the symbol `ok`) into the target register, followed finally by the linkage code. `Env` is preserved around the computation of the value, because it is needed in order to install the definition. Because the linkage is `next`, there is no linkage code in this case. The skeleton of the compiled code is thus

**校订前**

`Compile`判定该表达式是一个定义，因此它调用`compile-definition`来编译计算待赋值之值的代码（目标为`val`），接着是安装该定义的代码，接着是将`define`的值（即符号`ok`）放入目标寄存器的代码，最后是连接代码。`Env`在计算该值的过程中被保留，因为安装该定义需要它。由于连接是`next`，这种情况下没有连接代码。因此，编译后代码的骨架是

**校订后**

`Compile`判定该表达式是一个定义，因此它调用`compile-definition`来编译计算待赋值之值的代码（目标为`val`），接着是安装该定义的代码，接着是将`define`的值（即符号`ok`）放入目标寄存器的代码，最后是链接代码。`Env`在计算该值的过程中被保留，因为安装该定义需要它。由于链接是`next`，这种情况下没有链接代码。因此，编译后代码的骨架是

### 5_002e5:0107

**原文**

The expression that is to be compiled to produce the value for the variable `factorial` is a `lambda` expression whose value is the procedure that computes factorials. `Compile` handles this by calling `compile-lambda`, which compiles the procedure body, labels it as a new entry point, and generates the instruction that will combine the procedure body at the new entry point with the run-time environment and assign the result to `val`. The sequence then skips around the compiled procedure code, which is inserted at this point. The procedure code itself begins by extending the procedure’s definition environment by a frame that binds the formal parameter `n` to the procedure argument. Then comes the actual procedure body. Since this code for the value of the variable doesn’t modify the `env` register, the optional `save` and `restore` shown above aren’t generated. (The procedure code at `entry2` isn’t executed at this point, so its use of `env` is irrelevant.) Therefore, the skeleton for the compiled code becomes

**校订前**

为产生变量`factorial`的值而编译的表达式是一个`lambda`表达式，其值是计算阶乘的过程。`Compile`通过调用`compile-lambda`来处理这一点，后者编译过程体，将其标记为一个新的入口点，并生成指令，将新入口点处的过程体与运行时环境组合起来，并将结果赋给`val`。然后该序列跳过编译后的过程代码，后者被插入在此处。过程代码本身首先通过一个框架来扩展过程的定义环境，该框架将形式参数`n`绑定到过程参数。接着是实际的过程体。由于这段用于变量值的代码不修改`env`寄存器，上面显示的可选的`save`和`restore`不会被生成。（`entry2`处的过程代码此时不会被执行，因此它对`env`的使用无关紧要。）因此，编译后代码的骨架变为

**校订后**

为产生变量`factorial`的值而编译的表达式是一个`lambda`表达式，其值是计算阶乘的过程。`Compile`通过调用`compile-lambda`来处理这一点，后者编译过程体，将其标记为一个新的入口点，并生成指令，将新入口点处的过程体与运行时环境组合起来，并将结果赋给`val`。然后该序列跳过编译后的过程代码，后者被插入在此处。过程代码本身首先通过一个框架来扩展过程的定义环境，该框架将形式参数`n`绑定到过程实参。接着是实际的过程体。由于这段用于变量值的代码不修改`env`寄存器，上面显示的可选的`save`和`restore`不会被生成。（`entry2`处的过程代码此时不会被执行，因此它对`env`的使用无关紧要。）因此，编译后代码的骨架变为

### 5_002e5:0108

**原文**

A procedure body is always compiled (by `compile-lambda-body`) as a sequence with target `val` and linkage `return`. The sequence in this case consists of a single `if` expression:

**校订前**

过程体总是（由`compile-lambda-body`）编译为一个目标为`val`、连接为`return`的序列。本例中的序列由一个`if`表达式组成：

**校订后**

过程体总是（由`compile-lambda-body`）编译为一个目标为`val`、链接为`return`的序列。本例中的序列由一个`if`表达式组成：

### 5_002e5:0109

**原文**

`Compile-if` generates code that first computes the predicate (targeted to `val`), then checks the result and branches around the true branch if the predicate is false. `Env` and `continue` are preserved around the predicate code, since they may be needed for the rest of the `if` expression. Since the `if` expression is the final expression (and only expression) in the sequence making up the procedure body, its target is `val` and its linkage is `return`, so the true and false branches are both compiled with target `val` and linkage `return`. (That is, the value of the conditional, which is the value computed by either of its branches, is the value of the procedure.)

**校订前**

`Compile-if`生成代码，首先计算谓词（目标为`val`），然后检查结果，如果谓词为假则绕过真分支进行分支。`Env`和`continue`在谓词代码周围被保留，因为它们可能对`if`表达式的其余部分需要。由于`if`表达式是构成过程体的序列中的最终表达式（也是唯一的表达式），其目标是`val`，其连接是`return`，因此真分支和假分支都以目标`val`和连接`return`来编译。（也就是说，条件表达式的值，即由其任一分支计算出的值，就是该过程的值。）

**校订后**

`Compile-if`生成代码，首先计算谓词（目标为`val`），然后检查结果，如果谓词为假则绕过真分支进行分支。`Env`和`continue`在谓词代码周围被保留，因为它们可能对`if`表达式的其余部分需要。由于`if`表达式是构成过程体的序列中的最终表达式（也是唯一的表达式），其目标是`val`，其链接是`return`，因此真分支和假分支都以目标`val`和链接`return`来编译。（也就是说，条件表达式的值，即由其任一分支计算出的值，就是该过程的值。）

### 5_002e5:0110

**原文**

The predicate `(= n 1)` is a procedure call. This looks up the operator (the symbol `=`) and places this value in `proc`. It then assembles the arguments `1` and the value of `n` into `argl`. Then it tests whether `proc` contains a primitive or a compound procedure, and dispatches to a primitive branch or a compound branch accordingly. Both branches resume at the `after-call` label. The requirements to preserve registers around the evaluation of the operator and operands don’t result in any saving of registers, because in this case those evaluations don’t modify the registers in question.

**校订前**

谓词`(= n 1)`是一个过程调用。它查找运算符（符号`=`）并将该值放入`proc`。然后它将参数`1`和`n`的值组装到`argl`中。接着它测试`proc`中包含的是基本过程还是复合过程，并相应地分派到基本分支或复合分支。两个分支都在`after-call`标签处继续。在求值运算符和操作数周围保留寄存器的要求不会导致任何寄存器的保存，因为在这种情况下，那些求值不会修改所涉及的寄存器。

**校订后**

谓词`(= n 1)`是一个过程调用。它查找运算符（符号`=`）并将该值放入`proc`。然后它将参数`1`和`n`的值组装到`argl`中。接着它测试`proc`中包含的是基本过程还是复合过程，并相应地分派到基本分支或复合分支。两个分支都在`after-call`标号处继续。在求值运算符和运算对象周围保留寄存器的要求不会导致任何寄存器的保存，因为在这种情况下，那些求值不会修改所涉及的寄存器。

### 5_002e5:0111

**原文**

The true branch, which is the constant 1, compiles (with target `val` and linkage `return`) to

**校订前**

真分支，即常量1，编译（目标为`val`、连接为`return`）为

**校订后**

真分支，即常量1，编译（目标为`val`、链接为`return`）为

### 5_002e5:0120

**原文**

Exercise 5.36: What order of evaluation does our compiler produce for operands of a combination? Is it left-to-right, right-to-left, or some other order? Where in the compiler is this order determined? Modify the compiler so that it produces some other order of evaluation. (See the discussion of order of evaluation for the explicit-control evaluator in 5.4.1.) How does changing the order of operand evaluation affect the efficiency of the code that constructs the argument list?

**校订前**

习题 5.36： 我们的编译器为组合式的操作数产生什么样的求值顺序？是从左到右、从右到左，还是某种其他顺序？这个顺序在编译器中的什么地方确定？修改编译器，使其产生某种其他求值顺序。（参见 5.4.1 中对显式控制求值器求值顺序的讨论。）改变操作数求值顺序如何影响构造参数表的代码的效率？

**校订后**

习题 5.36： 我们的编译器为组合式的运算对象产生什么样的求值顺序？是从左到右、从右到左，还是某种其他顺序？这个顺序在编译器中的什么地方确定？修改编译器，使其产生某种其他求值顺序。（参见 5.4.1 中对显式控制求值器求值顺序的讨论。）改变运算对象求值顺序如何影响构造参数表的代码的效率？

### 5_002e5:0122

**原文**

Exercise 5.38: Our compiler is clever about avoiding unnecessary stack operations, but it is not clever at all when it comes to compiling calls to the primitive procedures of the language in terms of the primitive operations supplied by the machine. For example, consider how much code is compiled to compute `(+ a 1)`: The code sets up an argument list in `argl`, puts the primitive addition procedure (which it finds by looking up the symbol `+` in the environment) into `proc`, and tests whether the procedure is primitive or compound. The compiler always generates code to perform the test, as well as code for primitive and compound branches (only one of which will be executed). We have not shown the part of the controller that implements primitives, but we presume that these instructions make use of primitive arithmetic operations in the machine’s data paths. Consider how much less code would be generated if the compiler could open-code primitives—that is, if it could generate code to directly use these primitive machine operations. The expression `(+ a 1)` might be compiled into something as simple as[注328]

**校订前**

习题 5.38： 我们的编译器在避免不必要的栈操作方面很聪明，但在根据机器提供的基本操作来编译对语言基本过程的调用方面，它一点也不聪明。例如，考虑计算 `(+ a 1)` 编译了多少代码：代码在 `argl` 中设置参数表，将基本加法过程（它通过在环境中查找符号 `+` 找到）放入 `proc`，并测试该过程是基本的还是复合的。编译器总是生成执行该测试的代码，以及基本分支和复合分支的代码（其中只有一个会被执行）。我们没有展示控制器中实现基本过程的部分，但我们假定这些指令利用了机器数据通路中的基本算术操作。考虑一下，如果编译器能够 开放编码 基本过程——也就是说，如果它能够生成直接使用这些基本机器操作的代码——会少生成多少代码。表达式 `(+ a 1)` 可能被编译成像[注328]这样简单的东西

**校订后**

习题 5.38： 我们的编译器在避免不必要的栈操作方面很聪明，但在根据机器提供的基本操作来编译对语言基本过程的调用方面，它一点也不聪明。例如，考虑计算 `(+ a 1)` 编译了多少代码：代码在 `argl` 中设置参数表，将基本加法过程（它通过在环境中查找符号 `+` 找到）放入 `proc`，并测试该过程是基本的还是复合的。编译器总是生成执行该测试的代码，以及基本分支和复合分支的代码（其中只有一个会被执行）。我们没有展示控制器中实现基本过程的部分，但我们假定这些指令利用了机器数据通路中的基本算术操作。考虑一下，如果编译器能够 开放编码 基本过程——也就是说，如果它能够生成直接使用这些基本机器操作的代码——会少生成多少代码。表达式 `(+ a 1)` 可能被编译成如下这样简单的代码：[注328]

### 5_002e5:0125

**原文**

The open-coded primitives, unlike the special forms, all need their operands evaluated. Write a code generator `spread-arguments` for use by all the open-coding code generators. `Spread-arguments` should take an operand list and compile the given operands targeted to successive argument registers. Note that an operand may contain a call to an open-coded primitive, so argument registers will have to be preserved during operand evaluation.

**校订前**

与特殊形式不同，开放编码的基本过程都需要对其操作数求值。编写一个代码生成器 `spread-arguments`，供所有开放编码代码生成器使用。`Spread-arguments` 应该接受一个操作数表，并将给定的操作数编译到连续的目标参数寄存器。注意，一个操作数可能包含对开放编码基本过程的调用，因此在操作数求值期间必须保留参数寄存器。

**校订后**

与特殊形式不同，开放编码的基本过程都需要对其运算对象求值。编写一个代码生成器 `spread-arguments`，供所有开放编码代码生成器使用。`Spread-arguments` 应该接受一个运算对象表，并将给定的运算对象编译到连续的目标参数寄存器。注意，一个运算对象可能包含对开放编码基本过程的调用，因此在运算对象求值期间必须保留参数寄存器。

### 5_002e5:0126

**原文**

For each of the primitive procedures `=`, `*`, `-`, and `+`, write a code generator that takes a combination with that operator, together with a target and a linkage descriptor, and produces code to spread the arguments into the registers and then perform the operation targeted to the given target with the given linkage. You need only handle expressions with two operands. Make `compile` dispatch to these code generators.

**校订前**

对于基本过程 `=`、`*`、`-` 和 `+` 中的每一个，编写一个代码生成器，它接受以该运算符构成的组合式，以及一个目标和链接描述符，并生成代码将参数散布到寄存器中，然后执行以给定目标为目标、以给定链接为链接的操作。你只需要处理有两个操作数的表达式。让 `compile` 分派到这些代码生成器。

**校订后**

对于基本过程 `=`、`*`、`-` 和 `+` 中的每一个，编写一个代码生成器，它接受以该运算符构成的组合式，以及一个目标和链接描述符，并生成代码将参数散布到寄存器中，然后执行以给定目标为目标、以给定链接为链接的操作。你只需要处理有两个运算对象的表达式。让 `compile` 分派到这些代码生成器。

### 5_002e5:0128

**原文**

Extend your code generators for `+` and `*` so that they can handle expressions with arbitrary numbers of operands. An expression with more than two operands will have to be compiled into a sequence of operations, each with only two inputs.

**校订前**

扩展你为`+`和`*`编写的代码生成器，使它们能够处理具有任意数量操作数的表达式。具有多于两个操作数的表达式必须被编译成一系列操作，每个操作只有两个输入。

**校订后**

扩展你为`+`和`*`编写的代码生成器，使它们能够处理具有任意数量运算对象的表达式。具有多于两个运算对象的表达式必须被编译成一系列操作，每个操作只有两个输入。

### 5_002e5:0130

**原文**

One of the most common optimizations performed by compilers is the optimization of variable lookup. Our compiler, as we have implemented it so far, generates code that uses the `lookup-variable-value` operation of the evaluator machine. This searches for a variable by comparing it with each variable that is currently bound, working frame by frame outward through the run-time environment. This search can be expensive if the frames are deeply nested or if there are many variables. For example, consider the problem of looking up the value of `x` while evaluating the expression `(* x y z)` in an application of the procedure that is returned by

**校订前**

编译器执行的最常见优化之一是变量查找的优化。到目前为止，我们所实现的编译器生成的代码使用了求值器机器的`lookup-variable-value`操作。该操作通过将变量与当前绑定的每个变量进行比较来搜索变量，在运行时环境中逐帧向外进行。如果框架嵌套很深或者变量很多，这种搜索可能会很昂贵。例如，考虑在应用由以下过程返回的过程时，求值表达式`(* x y z)`的过程中查找`x`的值的问题

**校订后**

编译器执行的最常见优化之一是变量查找的优化。到目前为止，我们所实现的编译器生成的代码使用了求值器机器的`lookup-variable-value`操作。该操作通过将变量与当前绑定的每个变量进行比较来搜索变量，在运行时环境中逐个框架向外进行。如果框架嵌套很深或者变量很多，这种搜索可能会很昂贵。例如，考虑在应用由以下表达式返回的过程时，求值表达式`(* x y z)`的过程中查找`x`的值的问题

### 5_002e5:0132

**原文**

Each time `lookup-variable-value` searches for `x`, it must determine that the symbol `x` is not `eq?` to `y` or `z` (in the first frame), nor to `a`, `b`, `c`, `d`, or `e` (in the second frame). We will assume, for the moment, that our programs do not use `define`—that variables are bound only with `lambda`. Because our language is lexically scoped, the run-time environment for any expression will have a structure that parallels the lexical structure of the program in which the expression appears.[注330] Thus, the compiler can know, when it analyzes the above expression, that each time the procedure is applied the variable `x` in `(* x y z)` will be found two frames out from the current frame and will be the first variable in that frame.

**校订前**

每次`lookup-variable-value`搜索`x`时，它必须确定符号`x`不是`eq?`到`y`或`z`（在第一个框架中），也不是`a`、`b`、`c`、`d`或`e`（在第二个框架中）。我们暂时假设我们的程序不使用`define`——变量仅用`lambda`绑定。由于我们的语言是词法作用域的，任何表达式的运行时环境都将具有与出现该表达式的程序的词法结构平行的结构。[注330]因此，编译器在分析上述表达式时就可以知道，每次应用该过程时，`(* x y z)`中的变量`x`将在当前框架向外两帧处找到，并且将是该框架中的第一个变量。

**校订后**

每次`lookup-variable-value`搜索`x`时，它必须确定符号`x`既不与`y`或`z`（在第一个框架中）满足`eq?`关系，也不与`a`、`b`、`c`、`d`或`e`（在第二个框架中）满足这一关系。我们暂时假设我们的程序不使用`define`——变量仅用`lambda`绑定。由于我们的语言是词法作用域的，任何表达式的运行时环境都将具有与出现该表达式的程序的词法结构平行的结构。[注330]因此，编译器在分析上述表达式时就可以知道，每次应用该过程时，`(* x y z)`中的变量`x`将在当前框架向外两个框架处找到，并且将是该框架中的第一个变量。

### 5_002e5:0134

**原文**

In order to generate such code, the compiler must be able to determine the lexical address of a variable it is about to compile a reference to. The lexical address of a variable in a program depends on where one is in the code. For example, in the following program, the address of `x` in expression `⟨``e1``⟩` is (2, 0)—two frames back and the first variable in the frame. At that point `y` is at address (0, 0) and `c` is at address (1, 2). In expression `⟨``e2``⟩`, `x` is at (1, 0), `y` is at (1, 1), and `c` is at (0, 2).

**校订前**

为了生成这样的代码，编译器必须能够确定它即将编译引用的变量的词法地址。程序中变量的词法地址取决于代码中的位置。例如，在以下程序中，表达式`⟨``e1``⟩`中`x`的地址是（2，0）——向后两帧，并且是该帧中的第一个变量。在该点，`y`的地址是（0，0），`c`的地址是（1，2）。在表达式`⟨``e2``⟩`中，`x`的地址是（1，0），`y`的地址是（1，1），`c`的地址是（0，2）。

**校订后**

为了生成这样的代码，编译器必须能够确定它即将编译引用的变量的词法地址。程序中变量的词法地址取决于代码中的位置。例如，在以下程序中，表达式`⟨``e1``⟩`中`x`的地址是（2，0）——向外两个框架，并且是该框架中的第一个变量。在该点，`y`的地址是（0，0），`c`的地址是（1，2）。在表达式`⟨``e2``⟩`中，`x`的地址是（1，0），`y`的地址是（1，1），`c`的地址是（0，2）。

### 5_002e5:0135

**原文**

One way for the compiler to produce code that uses lexical addressing is to maintain a data structure called a compile-time environment. This keeps track of which variables will be at which positions in which frames in the run-time environment when a particular variable-access operation is executed. The compile-time environment is a list of frames, each containing a list of variables. (There will of course be no values bound to the variables, since values are not computed at compile time.) The compile-time environment becomes an additional argument to `compile` and is passed along to each code generator. The top-level call to `compile` uses an empty compile-time environment. When a `lambda` body is compiled, `compile-lambda-body` extends the compile-time environment by a frame containing the procedure’s parameters, so that the sequence making up the body is compiled with that extended environment. At each point in the compilation, `compile-variable` and `compile-assignment` use the compile-time environment in order to generate the appropriate lexical addresses.

**校订前**

编译器生成使用词法寻址的代码的一种方法是维护一个称为编译时环境的数据结构。它跟踪在执行特定变量访问操作时，哪些变量将位于运行时环境中的哪些框架中的哪些位置。编译时环境是一个框架的列表，每个框架包含一个变量列表。（当然，不会有值绑定到这些变量，因为值不是在编译时计算的。）编译时环境成为`compile`的附加参数，并传递给每个代码生成器。对`compile`的顶层调用使用空的编译时环境。当编译`lambda`体时，`compile-lambda-body`通过一个包含该过程参数的框架来扩展编译时环境，以便组成体的序列在该扩展环境中编译。在编译的每个点，`compile-variable`和`compile-assignment`使用编译时环境来生成适当的词法地址。

**校订后**

编译器生成使用词法寻址的代码的一种方法是维护一个称为编译时环境的数据结构。它跟踪在执行特定变量访问操作时，哪些变量将位于运行时环境中的哪些框架中的哪些位置。编译时环境是一个框架的表，每个框架包含一个变量表。（当然，不会有值绑定到这些变量，因为值不是在编译时计算的。）编译时环境成为`compile`的附加参数，并传递给每个代码生成器。对`compile`的顶层调用使用空的编译时环境。当编译`lambda`体时，`compile-lambda-body`通过一个包含该过程参数的框架来扩展编译时环境，以便组成体的序列在该扩展环境中编译。在编译的每个点，`compile-variable`和`compile-assignment`使用编译时环境来生成适当的词法地址。

### 5_002e5:0150

**原文**

Now we can use the following procedure to compile a procedure definition, execute the compiled code, and run the read-eval-print loop so we can try the procedure. Because we want the compiled code to return to the location in `continue` with its result in `val`, we compile the expression with a target of `val` and a linkage of `return`. In order to transform the object code produced by the compiler into executable instructions for the evaluator register machine, we use the procedure `assemble` from the register-machine simulator (5.2.2). We then initialize the `val` register to point to the list of instructions, set the `flag` so that the evaluator will go to `external-entry`, and start the evaluator.

**校订前**

现在我们可以使用以下过程来编译过程定义、执行编译代码并运行读-求值-打印循环，以便我们可以尝试该过程。因为我们希望编译代码返回到`continue`中的位置，其结果在`val`中，所以我们编译表达式时目标为`val`，链接为`return`。为了将编译器生成的目标代码转换为求值器寄存器机器的可执行指令，我们使用寄存器机器模拟器中的过程`assemble`（5.2.2）。然后我们将`val`寄存器初始化为指向指令列表，设置`flag`以便求值器转到`external-entry`，并启动求值器。

**校订后**

现在我们可以使用以下过程来编译过程定义、执行编译代码并运行读-求值-打印循环，以便我们可以尝试该过程。因为我们希望编译代码返回到`continue`中的位置，其结果在`val`中，所以我们编译表达式时目标为`val`，链接为`return`。为了将编译器生成的目标代码转换为求值器寄存器机器的可执行指令，我们使用寄存器机器模拟器中的过程`assemble`（5.2.2）。然后我们将`val`寄存器初始化为指向指令表，设置`flag`以便求值器转到`external-entry`，并启动求值器。

### 5_002e5:0157

**原文**

Exercise 5.27 asked you to determine, as a function of $n$, the number of pushes and the maximum stack depth needed by the evaluator to compute $n!$ using the recursive factorial procedure given above. Exercise 5.14 asked you to do the same measurements for the special-purpose factorial machine shown in Figure 5.11. Now perform the same analysis using the compiled `factorial` procedure.

**校订前**

习题 5.27要求你确定，作为$n$的函数，求值器使用上面给出的递归 factorial 过程计算$n!$所需的压栈次数和最大栈深度。习题 5.14要求你对图 5.11中所示的专用 factorial 机器做同样的测量。现在使用编译后的`factorial`过程进行同样的分析。

**校订后**

习题 5.27要求你确定，作为$n$的函数，求值器使用上面给出的递归 阶乘 过程计算$n!$所需的压栈次数和最大栈深度。习题 5.14要求你对图 5.11中所示的专用 阶乘 机器做同样的测量。现在使用编译后的`factorial`过程进行同样的分析。

### 5_002e5:0161

**原文**

Exercise 5.46: Carry out an analysis like the one in Exercise 5.45 to determine the effectiveness of compiling the tree-recursive Fibonacci procedure

**校订前**

习题 5.46：进行类似于习题 5.45中的分析，以确定编译树递归 Fibonacci 过程的有效性

**校订后**

习题 5.46：进行类似于习题 5.45中的分析，以确定编译树形递归 斐波那契 过程的有效性

### 5_002e5:0162

**原文**

compared to the effectiveness of using the special-purpose Fibonacci machine of Figure 5.12. (For measurement of the interpreted performance, see Exercise 5.29.) For Fibonacci, the time resource used is not linear in $n;$ hence the ratios of stack operations will not approach a limiting value that is independent of $n$.

**校订前**

与使用图 5.12中的专用 Fibonacci 机器的有效性进行比较。（关于被解释性能的测量，见习题 5.29。）对于 Fibonacci，所使用的时间资源与$n;$不成线性关系，因此栈操作的比值不会趋近于一个独立于$n$的极限值。

**校订后**

与使用图 5.12中的专用 斐波那契 机器的有效性进行比较。（关于被解释性能的测量，见习题 5.29。）对于 斐波那契，所使用的时间资源与$n;$不成线性关系，因此栈操作的比值不会趋近于一个独立于$n$的极限值。

### 5_002e5:0163

**原文**

Exercise 5.47: This section described how to modify the explicit-control evaluator so that interpreted code can call compiled procedures. Show how to modify the compiler so that compiled procedures can call not only primitive procedures and compiled procedures, but interpreted procedures as well. This requires modifying `compile-procedure-call` to handle the case of compound (interpreted) procedures. Be sure to handle all the same `target` and `linkage` combinations as in `compile-proc-appl`. To do the actual procedure application, the code needs to jump to the evaluator’s `compound-apply` entry point. This label cannot be directly referenced in object code (since the assembler requires that all labels referenced by the code it is assembling be defined there), so we will add a register called `compapp` to the evaluator machine to hold this entry point, and add an instruction to initialize it:

**校订前**

习题 5.47：本节描述了如何修改显式控制求值器，使被解释代码可以调用编译过程。说明如何修改编译器，使编译过程不仅可以调用基本过程和编译过程，还可以调用被解释过程。这需要修改`compile-procedure-call`以处理复合（被解释）过程的情况。确保处理与`compile-proc-appl`中相同的所有`target`和`linkage`组合。为了进行实际的过程应用，代码需要跳转到求值器的`compound-apply`入口点。这个标签不能在目标代码中直接引用（因为汇编器要求它所汇编的代码引用的所有标签都在那里定义），因此我们将在求值器机器中添加一个名为`compapp`的寄存器来保存这个入口点，并添加一条指令来初始化它：

**校订后**

习题 5.47：本节描述了如何修改显式控制求值器，使被解释代码可以调用编译过程。说明如何修改编译器，使编译过程不仅可以调用基本过程和编译过程，还可以调用被解释过程。这需要修改`compile-procedure-call`以处理复合（被解释）过程的情况。确保处理与`compile-proc-appl`中相同的所有`target`和`linkage`组合。为了进行实际的过程应用，代码需要跳转到求值器的`compound-apply`入口点。这个标号不能在目标代码中直接引用（因为汇编器要求它所汇编的代码引用的所有标号都在那里定义），因此我们将在求值器机器中添加一个名为`compapp`的寄存器来保存这个入口点，并添加一条指令来初始化它：

### 5_002e5:0179

**原文**

[注322] We can’t just use the labels `true-branch`, `false-branch`, and `after-if` as shown above, because there might be more than one `if` in the program. The compiler uses the procedure `make-label` to generate labels. `Make-label` takes a symbol as argument and returns a new symbol that begins with the given symbol. For example, successive calls to `(make-label 'a)` would return `a1`, `a2`, and so on. `Make-label` can be implemented similarly to the generation of unique variable names in the query language, as follows:

**校订前**

[注322] 我们不能像上面所示那样直接使用标签 `true-branch`、`false-branch` 和 `after-if`，因为程序中可能有多个 `if`。编译器使用过程 `make-label` 来生成标签。`Make-label` 接受一个符号作为参数，并返回一个以给定符号开头的新符号。例如，连续调用 `(make-label 'a)` 将返回 `a1`、`a2`，依此类推。`Make-label` 可以类似于查询语言中唯一变量名的生成方式来实现，如下所示：

**校订后**

[注322] 我们不能像上面所示那样直接使用标号 `true-branch`、`false-branch` 和 `after-if`，因为程序中可能有多个 `if`。编译器使用过程 `make-label` 来生成标号。`Make-label` 接受一个符号作为参数，并返回一个以给定符号开头的新符号。例如，连续调用 `(make-label 'a)` 将返回 `a1`、`a2`，依此类推。`Make-label` 可以类似于查询语言中唯一变量名的生成方式来实现，如下所示：

### 5_002e5:0181

**原文**

[注324] Actually, we signal an error when the target is not `val` and the linkage is `return`, since the only place we request `return` linkages is in compiling procedures, and our convention is that procedures return their values in `val`.

**校订前**

[注324] 实际上，当目标不是 `val` 且连接是 `return` 时，我们会发出错误信号，因为我们请求 `return` 连接的唯一地方是在编译过程时，而我们的约定是过程在 `val` 中返回它们的值。

**校订后**

[注324] 实际上，当目标不是 `val` 且链接是 `return` 时，我们会发出错误信号，因为我们请求 `return` 链接的唯一地方是在编译过程时，而我们的约定是过程在 `val` 中返回它们的值。

### 5_002e5:0196

**原文**

[注338] Of course, with either the interpretation or the compilation strategy we must also implement for the new machine storage allocation, input and output, and all the various operations that we took as “primitive” in our discussion of the evaluator and compiler. One strategy for minimizing work here is to write as many of these operations as possible in Lisp and then compile them for the new machine. Ultimately, everything reduces to a small kernel (such as garbage collection and the mechanism for applying actual machine primitives) that is hand-coded for the new machine.

**校订前**

[注338]当然，无论是采用解释策略还是编译策略，我们都必须为新机器实现存储分配、输入输出，以及我们在讨论求值器和编译器时视为“基本”的所有各种操作。在这里最小化工作的一种策略是，尽可能多地用 Lisp 编写这些操作，然后为新机器编译它们。最终，一切都归结为一个小的内核（例如垃圾回收和应用实际机器基本过程的机制），这个内核是为新机器手工编写的。

**校订后**

[注338]当然，无论是采用解释策略还是编译策略，我们都必须为新机器实现存储分配、输入输出，以及我们在讨论求值器和编译器时视为“基本”的所有各种操作。在这里最小化工作的一种策略是，尽可能多地用 Lisp 编写这些操作，然后为新机器编译它们。最终，一切都归结为一个小的内核（例如垃圾回收和应用实际机器基本操作的机制），这个内核是为新机器手工编写的。

### 5_002e5:0198

**原文**

Next: References, Prev: 5.4, Up: 5.5 [Contents]

**校订前**

下一节： References, 上一节： 5.4, 上一级： 5.5 [目录]

**校订后**

下一节： 参考文献, 上一节： 5.4, 上一级： 5.5 [目录]

### Acknowledgments:0002

**原文**

Next: Chapter 1, Prev: Preface 1e, Up: Top [Contents]

**校订前**

下一节： 第1章, 上一节： Preface 1e, 上一级： Top [目录]

**校订后**

下一节： 第1章, 上一节： 第1版前言, 上一级： 首页 [目录]

### Acknowledgments:0004

**原文**

We would like to thank the many people who have helped us develop this book and this curriculum.

**校订前**

我们要感谢许多帮助我们开发这本书和这门课程的人。

**校订后**

我们要感谢许多帮助我们编写本书和开发这门课程的人。

### Acknowledgments:0005

**原文**

Our subject is a clear intellectual descendant of “6.231,” a wonderful subject on programming linguistics and the λ-calculus taught at MIT in the late 1960s by Jack Wozencraft and Arthur Evans, Jr.

**校订前**

我们的主题是“6.231”的明确知识后裔，这是一门关于编程语言学和 λ 演算的精彩课程，由 Jack Wozencraft 和 Arthur Evans, Jr. 于 1960 年代末在 MIT 讲授。

**校订后**

我们的课程在思想上显然承袭了“6.231”，这是一门关于编程语言学和 λ 演算的精彩课程，由 Jack Wozencraft 和 Arthur Evans, Jr. 于 1960 年代末在 MIT 讲授。

### Acknowledgments:0009

**原文**

Marvin Minsky and Seymour Papert formed many of our attitudes about programming and its place in our intellectual lives. To them we owe the understanding that computation provides a means of expression for exploring ideas that would otherwise be too complex to deal with precisely. They emphasize that a student’s ability to write and modify programs provides a powerful medium in which exploring becomes a natural activity.

**校订前**

Marvin Minsky 和 Seymour Papert 形成了我们关于编程及其在我们智力生活中的地位的许多态度。我们归功于他们这样的理解：计算提供了一种表达手段，用于探索那些否则会过于复杂而无法精确处理的想法。他们强调，学生编写和修改程序的能力提供了一种强大的媒介，在其中探索成为一种自然的活动。

**校订后**

Marvin Minsky 和 Seymour Papert 塑造了我们对编程及其在我们智力生活中的地位的许多看法。正是他们让我们认识到：计算提供了一种表达手段，用于探索那些否则会过于复杂而无法精确处理的想法。他们强调，学生编写和修改程序的能力提供了一种强大的媒介，在其中探索成为一种自然的活动。

### Acknowledgments:0010

**原文**

We also strongly agree with Alan Perlis that programming is lots of fun and we had better be careful to support the joy of programming. Part of this joy derives from observing great masters at work. We are fortunate to have been apprentice programmers at the feet of Bill Gosper and Richard Greenblatt.

**校订前**

我们也强烈同意 Alan Perlis 的观点：编程非常有趣，我们最好小心地支持编程的乐趣。这种乐趣的一部分来自于观察大师们的工作。我们很幸运能成为 Bill Gosper 和 Richard Greenblatt 门下的学徒程序员。

**校订后**

我们也强烈同意 Alan Perlis 的观点：编程非常有趣，我们最好用心维护编程的乐趣。这种乐趣的一部分来自于观察大师们的工作。我们很幸运能成为 Bill Gosper 和 Richard Greenblatt 门下的学徒程序员。

### Acknowledgments:0012

**原文**

Many people have put in significant effort presenting this material at other universities. Some of the people we have worked closely with are Jacob Katzenelson at the Technion, Hardy Mayer at the University of California at Irvine, Joe Stoy at Oxford, Elisha Sacks at Purdue, and Jan Komorowski at the Norwegian University of Science and Technology. We are exceptionally proud of our colleagues who have received major teaching awards for their adaptations of this subject at other universities, including Kenneth Yip at Yale, Brian Harvey at the University of California at Berkeley, and Dan Huttenlocher at Cornell.

**校订前**

许多人在其他大学展示了这些材料，付出了巨大的努力。我们密切合作过的一些人包括 Technion 的 Jacob Katzenelson、加州大学欧文分校的 Hardy Mayer、牛津大学的 Joe Stoy、普渡大学的 Elisha Sacks 和挪威科技大学 的 Jan Komorowski。我们特别自豪的是，我们的同事因在其他大学改编这门课程而获得了重要的教学奖项，包括耶鲁大学的 Kenneth Yip、加州大学伯克利分校的 Brian Harvey 和康奈尔大学的 Dan Huttenlocher。

**校订后**

许多人在其他大学讲授这些内容，付出了巨大的努力。我们密切合作过的一些人包括 Technion 的 Jacob Katzenelson、加州大学欧文分校的 Hardy Mayer、牛津大学的 Joe Stoy、普渡大学的 Elisha Sacks 和挪威科技大学 的 Jan Komorowski。我们特别自豪的是，我们的同事因在其他大学改编这门课程而获得了重要的教学奖项，包括耶鲁大学的 Kenneth Yip、加州大学伯克利分校的 Brian Harvey 和康奈尔大学的 Dan Huttenlocher。

### Acknowledgments:0014

**原文**

Many educators in other countries have put in significant work translating the first edition. Michel Briand, Pierre Chamard, and André Pic produced a French edition; Susanne Daniels-Herold produced a German edition; and Fumio Motoyoshi produced a Japanese edition. We do not know who produced the Chinese edition, but we consider it an honor to have been selected as the subject of an “unauthorized” translation.

**校订前**

其他国家的许多教育工作者为翻译第一版付出了巨大的努力。Michel Briand、Pierre Chamard 和 André Pic 制作了法文版；Susanne Daniels-Herold 制作了德文版；Fumio Motoyoshi 制作了日文版。我们不知道是谁制作了中文版，但我们认为被选为“未经授权”翻译的主题是一种荣誉。

**校订后**

其他国家的许多教育工作者为翻译第一版付出了巨大的努力。Michel Briand、Pierre Chamard 和 André Pic 制作了法文版；Susanne Daniels-Herold 制作了德文版；Fumio Motoyoshi 制作了日文版。我们不知道是谁制作了中文版，但我们认为被选为“未经授权”翻译的对象是一种荣誉。

### Acknowledgments:0020

**原文**

Next: Chapter 1, Prev: Preface 1e, Up: Top [Contents]

**校订前**

下一节： 第1章, 上一节： Preface 1e, 上一级： Top [目录]

**校订后**

下一节： 第1章, 上一节： 第1版前言, 上一级： 首页 [目录]

### Chapter-1:0002

**原文**

Next: 1.1, Prev: Acknowledgments, Up: Top [Contents]

**校订前**

下一节： 1.1, 上一节： Acknowledgments, 上一级： Top [目录]

**校订后**

下一节： 1.1, 上一节： 致谢, 上一级： 首页 [目录]

### Chapter-1:0004

**原文**

The acts of the mind, wherein it exerts its power over simple ideas, are chiefly these three: 1. Combining several simple ideas into one compound one, and thus all complex ideas are made. 2. The second is bringing two ideas, whether simple or complex, together, and setting them by one another so as to take a view of them at once, without uniting them into one, by which it gets all its ideas of relations. 3. The third is separating them from all other ideas that accompany them in their real existence: this is called abstraction, and thus all its general ideas are made.

**校订前**

心灵在施展其力量于简单观念时的活动，主要有这三种：1. 组合 将若干简单观念结合成一个复合观念，一切复杂观念由此形成。2. 第二种 是将两个观念，无论简单还是复杂，放在一起，并相互对照，以便同时审视它们，而不将它们合而为一，由此获得一切关系观念。3. 第三种 是将它们与在现实存在中伴随它们的所有其他观念分离：这称为抽象，一切一般观念由此形成。

**校订后**

心灵在施展其力量于简单观念时的活动，主要有这三种：1. 将若干简单观念组合成一个复合观念，一切复杂观念由此形成。2. 第二种 是将两个观念，无论简单还是复杂，放在一起，并相互对照，以便同时审视它们，而不将它们合而为一，由此获得一切关系观念。3. 第三种 是将它们与在现实存在中伴随它们的所有其他观念分离：这称为抽象，一切一般观念由此形成。

### Chapter-1:0006

**原文**

We are about to study the idea of a computational process. Computational processes are abstract beings that inhabit computers. As they evolve, processes manipulate other abstract things called data. The evolution of a process is directed by a pattern of rules called a program. People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells.

**校订前**

我们即将研究 计算过程 这一概念。计算过程是栖居于计算机中的抽象存在。在它们演进的过程中，过程操纵其他称为 数据 的抽象事物。过程的演进由称为 程序 的规则模式所指导。人们创建程序来指导过程。实际上，我们用咒语召唤计算机的精灵。

**校订后**

我们即将研究 计算过程 这一概念。计算过程是栖居于计算机中的抽象存在。在它们演进的过程中，它们操纵其他称为 数据 的抽象事物。计算过程的演进由称为 程序 的规则模式所指导。人们创建程序来指导计算过程。实际上，我们用咒语召唤计算机的精灵。

### Chapter-1:0007

**原文**

A computational process is indeed much like a sorcerer’s idea of a spirit. It cannot be seen or touched. It is not composed of matter at all. However, it is very real. It can perform intellectual work. It can answer questions. It can affect the world by disbursing money at a bank or by controlling a robot arm in a factory. The programs we use to conjure processes are like a sorcerer’s spells. They are carefully composed from symbolic expressions in arcane and esoteric programming languages that prescribe the tasks we want our processes to perform.

**校订前**

计算过程确实很像巫师对精灵的设想。它不能被看见或触摸。它根本不由物质构成。然而，它非常真实。它能执行智力工作。它能回答问题。它能通过在银行支付金钱或在工厂控制机械臂来影响世界。我们用来召唤过程的程序就像巫师的咒语。它们由神秘而深奥的 编程语言 中的符号表达式精心组成，这些表达式规定了我们希望过程执行的任务。

**校订后**

计算过程确实很像巫师对精灵的设想。它不能被看见或触摸。它根本不由物质构成。然而，它非常真实。它能执行智力工作。它能回答问题。它能通过在银行支付金钱或在工厂控制机械臂来影响世界。我们用来召唤计算过程的程序就像巫师的咒语。它们由神秘而深奥的 编程语言 中的符号表达式精心组成，这些表达式规定了我们希望计算过程执行的任务。

### Chapter-1:0009

**原文**

Fortunately, learning to program is considerably less dangerous than learning sorcery, because the spirits we deal with are conveniently contained in a secure way. Real-world programming, however, requires care, expertise, and wisdom. A small bug in a computer-aided design program, for example, can lead to the catastrophic collapse of an airplane or a dam or the self-destruction of an industrial robot.

**校订前**

幸运的是，学习编程比学习巫术危险小得多，因为我们打交道的精灵都被妥善地限制在安全的范围内。然而，现实世界中的编程需要谨慎、专业知识和智慧。例如，计算机辅助设计程序中的一个小错误，就可能导致飞机或大坝的灾难性崩塌，或工业机器人的自我毁坏。

**校订后**

幸运的是，学习编程比学习巫术危险小得多，因为我们打交道的精灵都被妥善地限制在安全的范围内。然而，现实世界中的编程需要谨慎、专业知识和智慧。例如，计算机辅助设计程序中的一个小错误，就可能导致飞机的灾难性解体或大坝的灾难性坍塌，或工业机器人的自我毁坏。

### Chapter-1:0010

**原文**

Master software engineers have the ability to organize programs so that they can be reasonably sure that the resulting processes will perform the tasks intended. They can visualize the behavior of their systems in advance. They know how to structure programs so that unanticipated problems do not lead to catastrophic consequences, and when problems do arise, they can debug their programs. Well-designed computational systems, like well-designed automobiles or nuclear reactors, are designed in a modular manner, so that the parts can be constructed, replaced, and debugged separately.

**校订前**

大师级软件工程师有能力组织程序，使他们能够相当确信所得到的过程将执行预期的任务。他们能够预先想象其系统的行为。他们知道如何构造程序，使意想不到的问题不会导致灾难性后果，而当问题确实出现时，他们能够 调试 他们的程序。设计良好的计算系统，就像设计良好的汽车或核反应堆一样，是以模块化方式设计的，因此各个部分可以分别构造、替换和调试。

**校订后**

大师级软件工程师有能力组织程序，使他们能够相当确信所得到的计算过程将执行预期的任务。他们能够预先想象其系统的行为。他们知道如何构造程序，使意想不到的问题不会导致灾难性后果，而当问题确实出现时，他们能够 调试 他们的程序。设计良好的计算系统，就像设计良好的汽车或核反应堆一样，是以模块化方式设计的，因此各个部分可以分别构造、替换和调试。

### Chapter-1:0021

**原文**

Next: 1.1, Prev: Acknowledgments, Up: Top [Contents]

**校订前**

下一节： 1.1, 上一节： Acknowledgments, 上一级： Top [目录]

**校订后**

下一节： 1.1, 上一节： 致谢, 上一级： 首页 [目录]

### Chapter-2:0002

**原文**

Next: 2.1, Prev: 1.3, Up: Top [Contents]

**校订前**

下一节： 2.1, 上一节： 1.3, 上一级： Top [目录]

**校订后**

下一节： 2.1, 上一节： 1.3, 上一级： 首页 [目录]

### Chapter-2:0006

**原文**

We concentrated in Chapter 1 on computational processes and on the role of procedures in program design. We saw how to use primitive data (numbers) and primitive operations (arithmetic operations), how to combine procedures to form compound procedures through composition, conditionals, and the use of parameters, and how to abstract procedures by using `define`. We saw that a procedure can be regarded as a pattern for the local evolution of a process, and we classified, reasoned about, and performed simple algorithmic analyses of some common patterns for processes as embodied in procedures. We also saw that higher-order procedures enhance the power of our language by enabling us to manipulate, and thereby to reason in terms of, general methods of computation. This is much of the essence of programming.

**校订前**

我们在第1章中集中讨论了计算过程和过程在程序设计中的作用。我们看到了如何使用基本数据（数字）和基本操作（算术运算），如何通过组合、条件和使用参数将过程组合成复合过程，以及如何通过使用`define`来抽象过程。我们看到过程可以被视为计算过程局部演化的模式，并且我们对体现在过程中的一些常见计算过程模式进行了分类、推理和简单的算法分析。我们还看到，高阶过程通过使我们能够操作并因此根据一般计算方法进行推理，增强了我们语言的能力。这就是编程的许多精髓。

**校订后**

我们在第1章中集中讨论了计算过程和过程在程序设计中的作用。我们看到了如何使用基本数据（数）和基本操作（算术运算），如何通过组合、条件和使用参数将过程组合成复合过程，以及如何通过使用`define`来抽象过程。我们看到过程可以被视为计算过程局部演化的模式，并且我们对体现在过程中的一些常见计算过程模式进行了分类、推理和简单的算法分析。我们还看到，高阶过程通过使我们能够操作并因此根据一般计算方法进行推理，增强了我们语言的能力。这就是编程的许多精髓。

### Chapter-2:0015

**原文**

We will see that the key to forming compound data is that a programming language should provide some kind of “glue” so that data objects can be combined to form more complex data objects. There are many possible kinds of glue. Indeed, we will discover how to form compound data using no special “data” operations at all, only procedures. This will further blur the distinction between “procedure” and “data,” which was already becoming tenuous toward the end of chapter 1. We will also explore some conventional techniques for representing sequences and trees. One key idea in dealing with compound data is the notion of closure—that the glue we use for combining data objects should allow us to combine not only primitive data objects, but compound data objects as well. Another key idea is that compound data objects can serve as conventional interfaces for combining program modules in mix-and-match ways. We illustrate some of these ideas by presenting a simple graphics language that exploits closure.

**校订前**

我们将看到，形成复合数据的关键在于编程语言应提供某种“粘合剂”，以便数据对象可以组合成更复杂的数据对象。有许多可能的粘合剂。事实上，我们将发现如何完全不使用特殊的“数据”操作，而仅使用过程来形成复合数据。这将进一步模糊“过程”和“数据”之间的区别，这种区别在第1章末尾已经变得很微弱了。我们还将探索一些表示序列和树的常规技术。处理复合数据的一个关键思想是闭包的概念——我们用来组合数据对象的粘合剂应允许我们不仅组合基本数据对象，还能组合复合数据对象。另一个关键思想是，复合数据对象可以作为常规接口，以混搭的方式组合程序模块。我们通过展示一个利用闭包的简单图形语言来说明其中一些思想。

**校订后**

我们将看到，形成复合数据的关键在于编程语言应提供某种“粘合剂”，以便数据对象可以组合成更复杂的数据对象。有许多可能的粘合剂。事实上，我们将发现如何完全不使用特殊的“数据”操作，而仅使用过程来形成复合数据。这将进一步模糊“过程”和“数据”之间的区别，这种区别在第1章末尾已经变得很微弱了。我们还将探索一些表示序列和树的常规技术。处理复合数据的一个关键思想是闭合性的概念——我们用来组合数据对象的粘合剂应允许我们不仅组合基本数据对象，还能组合复合数据对象。另一个关键思想是，复合数据对象可以作为约定接口，以混搭的方式组合程序模块。我们通过展示一个利用闭合性的简单图形语言来说明其中一些思想。

### Chapter-2:0016

**原文**

We will then augment the representational power of our language by introducing symbolic expressions—data whose elementary parts can be arbitrary symbols rather than only numbers. We explore various alternatives for representing sets of objects. We will find that, just as a given numerical function can be computed by many different computational processes, there are many ways in which a given data structure can be represented in terms of simpler objects, and the choice of representation can have significant impact on the time and space requirements of processes that manipulate the data. We will investigate these ideas in the context of symbolic differentiation, the representation of sets, and the encoding of information.

**校订前**

然后，我们将通过引入符号表达式——其基本部分可以是任意符号而不仅仅是数字的数据——来增强我们语言的表示能力。我们探索表示对象集合的各种替代方案。我们将发现，正如一个给定的数值函数可以由许多不同的计算过程来计算一样，一个给定的数据结构也可以有许多方式用更简单的对象来表示，而表示方式的选择可能对操作这些数据的过程的时间和空间需求产生重大影响。我们将在符号求导、集合的表示和信息编码的背景下研究这些思想。

**校订后**

然后，我们将通过引入符号表达式——其基本部分可以是任意符号而不仅仅是数的数据——来增强我们语言的表示能力。我们探索表示对象集合的各种替代方案。我们将发现，正如一个给定的数值函数可以由许多不同的计算过程来计算一样，一个给定的数据结构也可以有许多方式用更简单的对象来表示，而表示方式的选择可能对操作这些数据的计算过程的时间和空间需求产生重大影响。我们将在符号求导、集合的表示和信息编码的背景下研究这些思想。

### Chapter-2:0020

**原文**

Next: 2.1, Prev: 1.3, Up: Top [Contents]

**校订前**

下一节： 2.1, 上一节： 1.3, 上一级： Top [目录]

**校订后**

下一节： 2.1, 上一节： 1.3, 上一级： 首页 [目录]

### Chapter-3:0002

**原文**

Next: 3.1, Prev: 2.5, Up: Top [Contents]

**校订前**

下一节： 3.1, 上一节： 2.5, 上一级： Top [目录]

**校订后**

下一节： 3.1, 上一节： 2.5, 上一级： 首页 [目录]

### Chapter-3:0007

**原文**

One powerful design strategy, which is particularly appropriate to the construction of programs for modeling physical systems, is to base the structure of our programs on the structure of the system being modeled. For each object in the system, we construct a corresponding computational object. For each system action, we define a symbolic operation in our computational model. Our hope in using this strategy is that extending the model to accommodate new objects or new actions will require no strategic changes to the program, only the addition of the new symbolic analogs of those objects or actions. If we have been successful in our system organization, then to add a new feature or debug an old one we will have to work on only a localized part of the system.

**校订前**

一种强大的设计策略，特别适用于构造用于建模物理系统的程序，是将我们程序的结构建立在被建模系统的结构之上。对于系统中的每个对象，我们构造一个对应的计算对象。对于每个系统动作，我们在计算模型中定义一个符号操作。使用这种策略的希望在于，扩展模型以容纳新对象或新动作将不需要对程序进行策略性更改，只需添加这些对象或动作的新符号类似物。如果我们在系统组织方面做得成功，那么要添加新功能或调试旧功能，我们将只需处理系统的一个局部部分。

**校订后**

一种强大的设计策略，特别适用于构造用于建模物理系统的程序，是将我们程序的结构建立在被建模系统的结构之上。对于系统中的每个对象，我们构造一个对应的计算对象。对于每个系统动作，我们在计算模型中定义一个符号操作。使用这种策略的希望在于，扩展模型以容纳新对象或新动作将不需要对程序进行策略性更改，只需添加这些对象或动作的新的符号对应物。如果我们在系统组织方面做得成功，那么要添加新功能或调试旧功能，我们将只需处理系统的一个局部部分。

### Chapter-3:0010

**原文**

Next: 3.1, Prev: 2.5, Up: Top [Contents]

**校订前**

下一节： 3.1, 上一节： 2.5, 上一级： Top [目录]

**校订后**

下一节： 3.1, 上一节： 2.5, 上一级： 首页 [目录]

### Chapter-4:0002

**原文**

Next: 4.1, Prev: 3.5, Up: Top [Contents]

**校订前**

下一节： 4.1, 上一节： 3.5, 上一级： Top [目录]

**校订后**

下一节： 4.1, 上一节： 3.5, 上一级： 首页 [目录]

### Chapter-4:0005

**原文**

… And those words are made from the letters of our alphabet: a couple-dozen squiggles we can draw with the pen. This is the key! And the treasure, too, if we can only get our hands on it! It’s as if—as if the key to the treasure is the treasure!

**校订前**

……而这些词语是由我们字母表中的字母构成的：二十几个我们可以用笔画的弯弯曲曲的线条。这就是关键！也是宝藏，只要我们能把它拿到手！就好像——就好像通往宝藏的钥匙就是宝藏！

**校订后**

……而这些词语是由我们字母表中的字母构成的：二十几个我们可以用笔画的弯弯曲曲的线条。这就是钥匙！也是宝藏，只要我们能把它拿到手！就好像——就好像通往宝藏的钥匙就是宝藏！

### Chapter-4:0007

**原文**

In our study of program design, we have seen that expert programmers control the complexity of their designs with the same general techniques used by designers of all complex systems. They combine primitive elements to form compound objects, they abstract compound objects to form higher-level building blocks, and they preserve modularity by adopting appropriate large-scale views of system structure. In illustrating these techniques, we have used Lisp as a language for describing processes and for constructing computational data objects and processes to model complex phenomena in the real world. However, as we confront increasingly complex problems, we will find that Lisp, or indeed any fixed programming language, is not sufficient for our needs. We must constantly turn to new languages in order to express our ideas more effectively. Establishing new languages is a powerful strategy for controlling complexity in engineering design; we can often enhance our ability to deal with a complex problem by adopting a new language that enables us to describe (and hence to think about) the problem in a different way, using primitives, means of combination, and means of abstraction that are particularly well suited to the problem at hand.[注205]

**校订前**

在我们对程序设计的研究中，我们已经看到，专家程序员使用与所有复杂系统的设计者相同的一般技术来控制其设计的复杂性。他们将基本元素组合成复合对象，他们将复合对象抽象成更高层次的构建块，他们通过采用适当的系统结构大规模视图来保持模块性。在说明这些技术时，我们使用 Lisp 作为描述计算过程以及构造计算数据对象和计算过程以模拟现实世界中复杂现象的语言。然而，当我们面对越来越复杂的问题时，我们会发现 Lisp，或者实际上任何固定的编程语言，都不足以满足我们的需求。我们必须不断转向新的语言，以便更有效地表达我们的思想。建立新语言是工程设计控制复杂性的一种强大策略；我们通常可以通过采用一种新语言来增强处理复杂问题的能力，这种语言使我们能够以不同的方式描述（并因此思考）问题，使用特别适合手头问题的基本元素、组合手段和抽象手段。[注205]

**校订后**

在我们对程序设计的研究中，我们已经看到，专家程序员使用与所有复杂系统的设计者相同的一般技术来控制其设计的复杂性。他们将基本元素组合成复合对象，他们将复合对象抽象成更高层次的构建块，他们通过采用适当的系统结构整体视角来保持模块性。在说明这些技术时，我们使用 Lisp 作为描述计算过程以及构造计算数据对象和计算过程以模拟现实世界中复杂现象的语言。然而，当我们面对越来越复杂的问题时，我们会发现 Lisp，或者实际上任何固定的编程语言，都不足以满足我们的需求。我们必须不断转向新的语言，以便更有效地表达我们的思想。建立新语言是工程设计控制复杂性的一种强大策略；我们通常可以通过采用一种新语言来增强处理复杂问题的能力，这种语言使我们能够以不同的方式描述（并因此思考）问题，使用特别适合手头问题的基本元素、组合手段和抽象手段。[注205]

### Chapter-4:0008

**原文**

Programming is endowed with a multitude of languages. There are physical languages, such as the machine languages for particular computers. These languages are concerned with the representation of data and control in terms of individual bits of storage and primitive machine instructions. The machine-language programmer is concerned with using the given hardware to erect systems and utilities for the efficient implementation of resource-limited computations. High-level languages, erected on a machine-language substrate, hide concerns about the representation of data as collections of bits and the representation of programs as sequences of primitive instructions. These languages have means of combination and abstraction, such as procedure definition, that are appropriate to the larger-scale organization of systems.

**校订前**

编程被赋予了众多的语言。有物理语言，例如特定计算机的机器语言。这些语言关注的是以单个存储位和基本机器指令来表示数据和控制。机器语言程序员关注的是使用给定的硬件来构建系统和实用程序，以高效实现资源受限的计算。建立在机器语言基础之上的高级语言，隐藏了将数据表示为位的集合以及将程序表示为基本指令序列的关注。这些语言具有组合和抽象的手段，例如过程定义，适合系统更大规模的组织。

**校订后**

编程被赋予了众多的语言。有物理语言，例如特定计算机的机器语言。这些语言关注的是以单个存储位和基本机器指令来表示数据和控制。机器语言程序员关注的是使用给定的硬件来构建系统和实用程序，以高效实现资源受限的计算。建立在机器语言基础之上的高级语言，使我们不必关注如何将数据表示为位的集合，以及如何将程序表示为基本指令序列。这些语言具有组合和抽象的手段，例如过程定义，适合系统更大规模的组织。

### Chapter-4:0013

**原文**

In fact, we can regard almost any program as the evaluator for some language. For instance, the polynomial manipulation system of 2.5.3 embodies the rules of polynomial arithmetic and implements them in terms of operations on list-structured data. If we augment this system with procedures to read and print polynomial expressions, we have the core of a special-purpose language for dealing with problems in symbolic mathematics. The digital-logic simulator of 3.3.4 and the constraint propagator of 3.3.5 are legitimate languages in their own right, each with its own primitives, means of combination, and means of abstraction. Seen from this perspective, the technology for coping with large-scale computer systems merges with the technology for building new computer languages, and computer science itself becomes no more (and no less) than the discipline of constructing appropriate descriptive languages.

**校订前**

事实上，我们几乎可以把任何程序都看作某种语言的求值器。例如，2.5.3中的多项式操作体系体现了多项式算术的规则，并用对表结构数据的操作来实现这些规则。如果我们为这个系统增加读取和打印多项式表达式的过程，就得到了一个用于处理符号数学问题的专用语言的核心。3.3.4中的数字逻辑模拟器和3.3.5中的约束传播器本身就是合法的语言，各自有自己的基本元素、组合方式和抽象方式。从这个角度看，处理大规模计算机系统的技术与构造新计算机语言的技术融合在一起，而计算机科学本身也就变成了（不多也不少）构造合适的描述性语言的学科。

**校订后**

事实上，我们几乎可以把任何程序都看作某种语言的求值器。例如，2.5.3中的多项式操作体系体现了多项式算术的规则，并用对表结构数据的操作来实现这些规则。如果我们为这个系统增加读取和打印多项式表达式的过程，就得到了一个用于处理符号数学问题的专用语言的核心。3.3.4中的数字逻辑模拟器和3.3.5中的约束传播器本身就是名副其实的语言，各自有自己的基本元素、组合方式和抽象方式。从这个角度看，处理大规模计算机系统的技术与构造新计算机语言的技术融合在一起，而计算机科学本身也就变成了（不多也不少）构造合适的描述性语言的学科。

### Chapter-4:0014

**原文**

We now embark on a tour of the technology by which languages are established in terms of other languages. In this chapter we shall use Lisp as a base, implementing evaluators as Lisp procedures. Lisp is particularly well suited to this task, because of its ability to represent and manipulate symbolic expressions. We will take the first step in understanding how languages are implemented by building an evaluator for Lisp itself. The language implemented by our evaluator will be a subset of the Scheme dialect of Lisp that we use in this book. Although the evaluator described in this chapter is written for a particular dialect of Lisp, it contains the essential structure of an evaluator for any expression-oriented language designed for writing programs for a sequential machine. (In fact, most language processors contain, deep within them, a little “Lisp” evaluator.) The evaluator has been simplified for the purposes of illustration and discussion, and some features have been left out that would be important to include in a production-quality Lisp system. Nevertheless, this simple evaluator is adequate to execute most of the programs in this book.[注206]

**校订前**

我们现在开始巡览以其他语言为基础建立语言的技术。在本章中，我们将以 Lisp 为基础，把求值器实现为 Lisp 过程。Lisp 特别适合这项任务，因为它能够表示和操作符号表达式。我们将通过为 Lisp 本身构造一个求值器，迈出理解语言如何实现的第一步。我们的求值器所实现的语言将是本书中使用的 Lisp 的 Scheme 方言的一个子集。尽管本章描述的求值器是为 Lisp 的一个特定方言编写的，但它包含了为顺序机器编写程序的任何面向表达式的语言的求值器的基本结构。（事实上，大多数语言处理器深处都包含一个小小的“Lisp”求值器。）为了便于说明和讨论，这个求值器已经做了简化，并且省略了一些对于生产质量的 Lisp 系统来说很重要的特性。尽管如此，这个简单的求值器足以执行本书中的大部分程序。[注206]

**校订后**

我们现在开始巡览以其他语言为基础建立语言的技术。在本章中，我们将以 Lisp 为基础，把求值器实现为 Lisp 过程。Lisp 特别适合这项任务，因为它能够表示和操作符号表达式。我们将通过为 Lisp 本身构造一个求值器，迈出理解语言如何实现的第一步。我们的求值器所实现的语言将是本书中使用的 Lisp 的 Scheme 方言的一个子集。尽管本章描述的求值器是为 Lisp 的一个特定方言编写的，但它包含了为顺序机器编写程序的任何面向表达式的语言的求值器的基本结构。（事实上，大多数语言处理器深处都包含一个小小的“Lisp”求值器。）为了便于说明和讨论，这个求值器已经做了简化，并且省略了一些对于达到实际应用质量要求的 Lisp 系统来说很重要的特性。尽管如此，这个简单的求值器足以执行本书中的大部分程序。[注206]

### Chapter-4:0019

**原文**

[注205] The same idea is pervasive throughout all of engineering. For example, electrical engineers use many different languages for describing circuits. Two of these are the language of electrical networks and the language of electrical systems. The network language emphasizes the physical modeling of devices in terms of discrete electrical elements. The primitive objects of the network language are primitive electrical components such as resistors, capacitors, inductors, and transistors, which are characterized in terms of physical variables called voltage and current. When describing circuits in the network language, the engineer is concerned with the physical characteristics of a design. In contrast, the primitive objects of the system language are signal-processing modules such as filters and amplifiers. Only the functional behavior of the modules is relevant, and signals are manipulated without concern for their physical realization as voltages and currents. The system language is erected on the network language, in the sense that the elements of signal-processing systems are constructed from electrical networks. Here, however, the concerns are with the large-scale organization of electrical devices to solve a given application problem; the physical feasibility of the parts is assumed. This layered collection of languages is another example of the stratified design technique illustrated by the picture language of 2.2.4.

**校订前**

[注205]同样的思想贯穿于整个工程领域。例如，电气工程师使用许多不同的语言来描述电路。其中两种是电 网络的语言和电 系统的语言。网络语言强调用离散电气元件对器件进行物理建模。网络语言的基本对象是基本电气元件，如电阻、电容、电感和晶体管，它们用称为电压和电流的物理变量来表征。当用网络语言描述电路时，工程师关心的是设计的物理特性。相比之下，系统语言的基本对象是信号处理模块，如滤波器和放大器。只有模块的功能行为是相关的，信号的操纵不关心其作为电压和电流的物理实现。系统语言建立在网络语言之上，其意义在于，信号处理系统的元件是由电气网络构造的。然而，这里关心的是电气设备的大规模组织以解决给定的应用问题；部件的物理可行性是假定的。这种分层语言集合是2.2.4的图片语言所说明的分层设计技术的另一个例子。

**校订后**

[注205]同样的思想贯穿于整个工程领域。例如，电气工程师使用许多不同的语言来描述电路。其中两种是电 网络的语言和电 系统的语言。网络语言强调用离散电气元件对器件进行物理建模。网络语言的基本对象是基本电气元件，如电阻、电容、电感和晶体管，它们用称为电压和电流的物理变量来表征。当用网络语言描述电路时，工程师关心的是设计的物理特性。相比之下，系统语言的基本对象是信号处理模块，如滤波器和放大器。只有模块的功能行为是相关的，信号的操纵不关心其作为电压和电流的物理实现。系统语言建立在网络语言之上，其意义在于，信号处理系统的元件是由电气网络构造的。然而，这里关心的是电气设备的大规模组织以解决给定的应用问题；部件的物理可行性是假定的。这种分层语言集合是2.2.4的图画语言所说明的分层设计技术的另一个例子。

### Chapter-4:0021

**原文**

Next: 4.1, Prev: 3.5, Up: Top [Contents]

**校订前**

下一节： 4.1, 上一节： 3.5, 上一级： Top [目录]

**校订后**

下一节： 4.1, 上一节： 3.5, 上一级： 首页 [目录]

### Chapter-5:0002

**原文**

Next: 5.1, Prev: 4.4, Up: Top [Contents]

**校订前**

下一节： 5.1, 上一节： 4.4, 上一级： Top [目录]

**校订后**

下一节： 5.1, 上一节： 4.4, 上一级： 首页 [目录]

### Chapter-5:0004

**原文**

My aim is to show that the heavenly machine is not a kind of divine, live being, but a kind of clockwork (and he who believes that a clock has soul attributes the maker’s glory to the work), insofar as nearly all the manifold motions are caused by a most simple and material force, just as all motions of the clock are caused by a single weight.

**校订前**

我的目的是表明，天体机器并非某种神圣的、活的存在，而是一种钟表装置（而相信钟表有灵魂的人，是把造物主的荣耀归给了作品），因为几乎所有这些多样的运动都是由一种最简单、最物质的力量引起的，正如钟表的所有运动都是由一个单一的重量引起的一样。

**校订后**

我的目的是表明，天体机器并非某种神圣的、活的存在，而是一种钟表装置（而相信钟表有灵魂的人，是把造物主的荣耀归给了作品），因为几乎所有这些多样的运动都是由一种最简单、最物质的力量引起的，正如钟表的所有运动都是由一个重锤引起的一样。

### Chapter-5:0008

**原文**

Most of the primitive operations of our register machines are very simple. For example, an operation might add the numbers fetched from two registers, producing a result to be stored into a third register. Such an operation can be performed by easily described hardware. In order to deal with list structure, however, we will also use the memory operations `car`, `cdr`, and `cons`, which require an elaborate storage-allocation mechanism. In 5.3 we study their implementation in terms of more elementary operations.

**校订前**

我们的寄存器机器的大多数基本操作都非常简单。例如，一个操作可以将从两个寄存器中取出的数字相加，产生一个结果存储到第三个寄存器中。这样的操作可以由容易描述的硬件来执行。然而，为了处理表结构，我们还将使用内存操作`car`、`cdr`和`cons`，这些操作需要精细的存储分配机制。在5.3中，我们根据更基本的操作来研究它们的实现。

**校订后**

我们的寄存器机器的大多数基本操作都非常简单。例如，一个操作可以将从两个寄存器中取出的数相加，产生一个结果存储到第三个寄存器中。这样的操作可以由容易描述的硬件来执行。然而，为了处理表结构，我们还将使用内存操作`car`、`cdr`和`cons`，这些操作需要精细的存储分配机制。在5.3中，我们根据更基本的操作来研究它们的实现。

### Chapter-5:0010

**原文**

Next: 5.1, Prev: 4.4, Up: Top [Contents]

**校订前**

下一节： 5.1, 上一节： 4.4, 上一级： Top [目录]

**校订后**

下一节： 5.1, 上一节： 4.4, 上一级： 首页 [目录]

### Colophon:0002

**原文**

Prev: Term Index, Up: Top [Contents]

**校订前**

上一节： Term 索引, 上一级： Top [目录]

**校订后**

上一节： 术语索引, 上一级： 首页 [目录]

### Colophon:0007

**原文**

Prev: Term Index, Up: Top [Contents]

**校订前**

上一节： Term 索引, 上一级： Top [目录]

**校订后**

上一节： 术语索引, 上一级： 首页 [目录]

### Dedication:0002

**原文**

Next: Foreword, Prev: UTF, Up: Top [Contents]

**校订前**

下一节： Foreword, 上一节： UTF, 上一级： Top [目录]

**校订后**

下一节： 序言, 上一节： UTF, 上一级： 首页 [目录]

### Dedication:0004

**原文**

This book is dedicated, in respect and admiration, to the spirit that lives in the computer.

**校订前**

本书谨以尊敬与钦佩之情，献给活在计算机中的精神。

**校订后**

本书谨以尊敬与钦佩之情，献给栖居于计算机中的精灵。

### Dedication:0005

**原文**

“I think that it’s extraordinarily important that we in computer science keep fun in computing. When it started out, it was an awful lot of fun. Of course, the paying customers got shafted every now and then, and after a while we began to take their complaints seriously. We began to feel as if we really were responsible for the successful, error-free perfect use of these machines. I don’t think we are. I think we’re responsible for stretching them, setting them off in new directions, and keeping fun in the house. I hope the field of computer science never loses its sense of fun. Above all, I hope we don’t become missionaries. Don’t feel as if you’re Bible salesmen. The world has too many of those already. What you know about computing other people will learn. Don’t feel as if the key to successful computing is only in your hands. What’s in your hands, I think and hope, is intelligence: the ability to see the machine as more than when you were first led up to it, that you can make it more.”

**校订前**

“我认为，我们计算机科学界在计算中保持乐趣，这一点极其重要。当初它刚起步时，乐趣无穷。当然，付钱的客户时不时会吃亏，过了一阵子，我们开始认真对待他们的抱怨。我们开始觉得，仿佛我们真的要为这些机器成功、无错、完美地使用负责。我认为并非如此。我认为我们负责的是拓展它们，把它们引向新的方向，并把乐趣留在这门学问里。我希望计算机科学领域永远不要失去乐趣感。最重要的是，我希望我们不要变成传教士。不要觉得自己是圣经推销员。世上已经有太多那样的人了。你所知道的关于计算的东西，别人也会学到。不要觉得成功计算的关键只掌握在你手中。我认为并希望，掌握在你手中的是智慧：一种能力，能看出机器比你最初被引向它时更多，能看出你可以让它变得更多。”

**校订后**

“我认为，我们计算机科学界在计算中保持乐趣，这一点极其重要。当初它刚起步时，乐趣无穷。当然，付钱的客户时不时会吃亏，过了一阵子，我们开始认真对待他们的抱怨。我们开始觉得，仿佛我们真的要为这些机器成功、无错、完美地使用负责。我认为并非如此。我认为我们负责的是拓展它们，把它们引向新的方向，并把乐趣留在这门学问里。我希望计算机科学领域永远不要失去乐趣感。最重要的是，我希望我们不要变成传教士。不要觉得自己是圣经推销员。世上已经有太多那样的人了。你所知道的关于计算的东西，别人也会学到。不要觉得成功计算的关键只掌握在你手中。我认为并希望，掌握在你手中的是智慧：一种能力，能看出机器的潜能超出你初识它时的认识，并且你能使它拥有更多能力。”

### Dedication:0007

**原文**

Next: Foreword, Prev: UTF, Up: Top [Contents]

**校订前**

下一节： Foreword, 上一节： UTF, 上一级： Top [目录]

**校订后**

下一节： 序言, 上一节： UTF, 上一级： 首页 [目录]

### Exercises:0002

**原文**

Next: Figures, Prev: References, Up: Top [Contents]

**校订前**

下一节： Figures, 上一节： References, 上一级： Top [目录]

**校订后**

下一节： 插图, 上一节： 参考文献, 上一级： 首页 [目录]

### Exercises:0009

**原文**

Next: Figures, Prev: References, Up: Top [Contents]

**校订前**

下一节： Figures, 上一节： References, 上一级： Top [目录]

**校订后**

下一节： 插图, 上一节： 参考文献, 上一级： 首页 [目录]

### Figures:0002

**原文**

Next: Term Index, Prev: Exercises, Up: Top [Contents]

**校订前**

下一节： Term 索引, 上一节： Exercises, 上一级： Top [目录]

**校订后**

下一节： 术语索引, 上一节： 习题, 上一级： 首页 [目录]

### Figures:0009

**原文**

Next: Term Index, Prev: Exercises, Up: Top [Contents]

**校订前**

下一节： Term 索引, 上一节： Exercises, 上一级： Top [目录]

**校订后**

下一节： 术语索引, 上一节： 习题, 上一级： 首页 [目录]

### Foreword:0002

**原文**

Next: Preface, Prev: Dedication, Up: Top [Contents]

**校订前**

下一节： Preface, 上一节： Dedication, 上一级： Top [目录]

**校订后**

下一节： 前言, 上一节： 献词, 上一级： 首页 [目录]

### Foreword:0004

**原文**

Educators, generals, dieticians, psychologists, and parents program. Armies, students, and some societies are programmed. An assault on large problems employs a succession of programs, most of which spring into existence en route. These programs are rife with issues that appear to be particular to the problem at hand. To appreciate programming as an intellectual activity in its own right you must turn to computer programming; you must read and write computer programs—many of them. It doesn’t matter much what the programs are about or what applications they serve. What does matter is how well they perform and how smoothly they fit with other programs in the creation of still greater programs. The programmer must seek both perfection of part and adequacy of collection. In this book the use of “program” is focused on the creation, execution, and study of programs written in a dialect of Lisp for execution on a digital computer. Using Lisp we restrict or limit not what we may program, but only the notation for our program descriptions.

**校订前**

教育者、将军、营养师、心理学家和父母都在编程。军队、学生以及某些社会则被编程。对大型问题的攻击会动用一连串程序，其中大多数是在途中才产生的。这些程序充满了看似只与手头问题相关的议题。要把编程本身当作一种智力活动来欣赏，你必须转向计算机编程；你必须阅读和编写计算机程序——大量的程序。这些程序关于什么或服务于什么应用并不太重要。真正重要的是它们运行得有多好，以及它们在创造更宏大程序时与其他程序配合得有多顺畅。程序员必须既追求部分的完美，也追求集合的充分。在本书中，“程序”一词的使用聚焦于用 Lisp 的一种方言编写、供数字计算机执行的程序的创建、执行和研究。使用 Lisp，我们限制或限定的不是我们可以编写什么程序，而只是我们描述程序所用的记法。

**校订后**

教育者、将军、营养师、心理学家和父母都在编程。军队、学生以及某些社会则被编程。解决大型问题会动用一连串程序，其中大多数是在途中才产生的。这些程序充满了看似只与手头问题相关的议题。要把编程本身当作一种智力活动来欣赏，你必须转向计算机编程；你必须阅读和编写计算机程序——大量的程序。这些程序关于什么或服务于什么应用并不太重要。真正重要的是它们运行得有多好，以及它们在创造更宏大程序时与其他程序配合得有多顺畅。程序员必须既追求部分的完美，也追求整体的适切。在本书中，“程序”一词的使用聚焦于用 Lisp 的一种方言编写、供数字计算机执行的程序的创建、执行和研究。使用 Lisp，我们限制或限定的不是我们可以编写什么程序，而只是我们描述程序所用的记法。

### Foreword:0005

**原文**

Our traffic with the subject matter of this book involves us with three foci of phenomena: the human mind, collections of computer programs, and the computer. Every computer program is a model, hatched in the mind, of a real or mental process. These processes, arising from human experience and thought, are huge in number, intricate in detail, and at any time only partially understood. They are modeled to our permanent satisfaction rarely by our computer programs. Thus even though our programs are carefully handcrafted discrete collections of symbols, mosaics of interlocking functions, they continually evolve: we change them as our perception of the model deepens, enlarges, generalizes until the model ultimately attains a metastable place within still another model with which we struggle. The source of the exhilaration associated with computer programming is the continual unfolding within the mind and on the computer of mechanisms expressed as programs and the explosion of perception they generate. If art interprets our dreams, the computer executes them in the guise of programs!

**校订前**

我们与本书主题的交涉，使我们涉及三类现象焦点：人的心智、计算机程序的集合以及计算机。每一个计算机程序都是一种模型，在头脑中孵化出来，对应一个真实过程或心智过程。这些过程源自人类经验与思想，数量庞大，细节繁复，而且在任何时候都只能被部分理解。我们的计算机程序很少能把这些过程建模到令我们永久满意的程度。因此，即使我们的程序是精心手工制作的离散符号集合、相互咬合的功能拼图，它们仍不断演化：随着我们对模型的认识加深、扩大、推广，我们会改变它们，直到模型最终在另一个我们仍在与之搏斗的模型中取得一种亚稳的位置。与计算机编程相伴的兴奋感，其来源是：以程序表达的机制在头脑中和计算机上不断展开，以及它们所引发的知觉爆发。如果艺术解释我们的梦，那么计算机则以程序为伪装执行这些梦！

**校订后**

研究本书的主题，会使我们接触到三个方面的现象：人的心智、计算机程序的集合以及计算机。每一个计算机程序都是一种模型，在头脑中孵化出来，对应一个真实过程或心智过程。这些过程源自人类经验与思想，数量庞大，细节繁复，而且在任何时候都只能被部分理解。我们的计算机程序很少能把这些过程建模到令我们永久满意的程度。因此，即使我们的程序是精心手工制作的离散符号集合、相互衔接的函数拼图，它们仍不断演化：随着我们对模型的认识加深、扩大、推广，我们会改变它们，直到模型最终在另一个我们仍在与之搏斗的模型中取得一种亚稳的位置。与计算机编程相伴的兴奋感，其来源是：以程序表达的机制在头脑中和计算机上不断展开，以及它们所引发的认识的飞跃。如果艺术解释我们的梦，那么计算机则以程序为伪装执行这些梦！

### Foreword:0006

**原文**

For all its power, the computer is a harsh taskmaster. Its programs must be correct, and what we wish to say must be said accurately in every detail. As in every other symbolic activity, we become convinced of program truth through argument. Lisp itself can be assigned a semantics (another model, by the way), and if a program’s function can be specified, say, in the predicate calculus, the proof methods of logic can be used to make an acceptable correctness argument. Unfortunately, as programs get large and complicated, as they almost always do, the adequacy, consistency, and correctness of the specifications themselves become open to doubt, so that complete formal arguments of correctness seldom accompany large programs. Since large programs grow from small ones, it is crucial that we develop an arsenal of standard program structures of whose correctness we have become sure—we call them idioms—and learn to combine them into larger structures using organizational techniques of proven value. These techniques are treated at length in this book, and understanding them is essential to participation in the Promethean enterprise called programming. More than anything else, the uncovering and mastery of powerful organizational techniques accelerates our ability to create large, significant programs. Conversely, since writing large programs is very taxing, we are stimulated to invent new methods of reducing the mass of function and detail to be fitted into large programs.

**校订前**

尽管计算机拥有强大的力量，它却是一位严厉的监工。它的程序必须正确，而我们想说的东西必须在每一个细节上都准确说出。正如在每一种其他符号活动中一样，我们通过论证来确信程序的真实性。Lisp 本身可以被赋予一种语义（顺便说一句，那是另一种模型），而如果一个程序的功能可以被规定，比如说，在谓词演算中规定，那么逻辑的证明方法就可以被用来作出可接受的正确性论证。不幸的是，随着程序变得庞大而复杂——它们几乎总是如此——规格说明本身的充分性、一致性和正确性也开始受到怀疑，因此大型程序很少附带完整的正确性形式论证。既然大型程序是从小型程序生长出来的，那么至关重要的是，我们要发展出一套标准程序结构的武库，并已确信其正确性——我们称它们为惯用法——还要学会使用已被证明有价值的组织技术，把它们组合成更大的结构。本书详细讨论了这些技术，理解它们对于参与被称为编程的普罗米修斯式事业至关重要。最重要的是，揭示并掌握强大的组织技术，会加速我们创建大型、重要程序的能力。反过来，由于编写大型程序非常费力，我们也被激励去发明新方法，以减少需要塞进大型程序中的功能和细节的数量。

**校订后**

尽管计算机拥有强大的力量，它却是一位严厉的监工。它的程序必须正确，而我们想说的东西必须在每一个细节上都准确说出。正如在每一种其他符号活动中一样，我们通过论证来确信程序的正确性。Lisp 本身可以被赋予一种语义（顺便说一句，那是另一种模型），而如果一个程序的功能可以被规定，比如说，在谓词演算中规定，那么逻辑的证明方法就可以被用来作出可接受的正确性论证。不幸的是，随着程序变得庞大而复杂——它们几乎总是如此——规格说明本身的充分性、一致性和正确性也开始受到怀疑，因此大型程序很少附带完整的正确性形式论证。既然大型程序是从小型程序生长出来的，那么至关重要的是，我们要发展出一套标准程序结构的武库，并已确信其正确性——我们称它们为惯用法——还要学会使用已被证明有价值的组织技术，把它们组合成更大的结构。本书详细讨论了这些技术，理解它们对于参与被称为编程的普罗米修斯式事业至关重要。最重要的是，揭示并掌握强大的组织技术，会加速我们创建大型、重要程序的能力。反过来，由于编写大型程序非常费力，我们也被激励去发明新方法，以减少需要塞进大型程序中的功能和细节的数量。

### Foreword:0009

**原文**

Among the programs we write, some (but never enough) perform a precise mathematical function such as sorting or finding the maximum of a sequence of numbers, determining primality, or finding the square root. We call such programs algorithms, and a great deal is known of their optimal behavior, particularly with respect to the two important parameters of execution time and data storage requirements. A programmer should acquire good algorithms and idioms. Even though some programs resist precise specifications, it is the responsibility of the programmer to estimate, and always to attempt to improve, their performance.

**校订前**

在我们编写的程序中，有一些（但从来不够多）执行精确的数学功能，例如排序或求一个数字序列的最大值、判定素性，或求平方根。我们把这样的程序称为算法，并且关于它们的最优行为已有大量了解，尤其是关于执行时间和数据存储需求这两个重要参数。程序员应当掌握好的算法和惯用法。即使有些程序难以精确规格化，程序员也有责任估计并始终尝试改进它们的性能。

**校订后**

在我们编写的程序中，有一些（但从来不够多）执行精确的数学功能，例如排序或求一个数值序列的最大值、判定素性，或求平方根。我们把这样的程序称为算法，并且关于它们的最优行为已有大量了解，尤其是关于执行时间和数据存储需求这两个重要参数。程序员应当掌握好的算法和惯用法。即使有些程序难以精确规格化，程序员也有责任估计并始终尝试改进它们的性能。

### Foreword:0011

**原文**

Lisp changes. The Scheme dialect used in this text has evolved from the original Lisp and differs from the latter in several important ways, including static scoping for variable binding and permitting functions to yield functions as values. In its semantic structure Scheme is as closely akin to Algol 60 as to early Lisps. Algol 60, never to be an active language again, lives on in the genes of Scheme and Pascal. It would be difficult to find two languages that are the communicating coin of two more different cultures than those gathered around these two languages. Pascal is for building pyramids—imposing, breathtaking, static structures built by armies pushing heavy blocks into place. Lisp is for building organisms—imposing, breathtaking, dynamic structures built by squads fitting fluctuating myriads of simpler organisms into place. The organizing principles used are the same in both cases, except for one extraordinarily important difference: The discretionary exportable functionality entrusted to the individual Lisp programmer is more than an order of magnitude greater than that to be found within Pascal enterprises. Lisp programs inflate libraries with functions whose utility transcends the application that produced them. The list, Lisp’s native data structure, is largely responsible for such growth of utility. The simple structure and natural applicability of lists are reflected in functions that are amazingly nonidiosyncratic. In Pascal the plethora of declarable data structures induces a specialization within functions that inhibits and penalizes casual cooperation. It is better to have 100 functions operate on one data structure than to have 10 functions operate on 10 data structures. As a result the pyramid must stand unchanged for a millennium; the organism must evolve or perish.

**校订前**

Lisp 会变化。本文本中使用的 Scheme 方言从最初的 Lisp 演化而来，并在若干重要方面不同于后者，包括变量绑定的静态作用域，以及允许函数产生函数作为值。在语义结构上，Scheme 与 Algol 60 的亲缘关系，正如与早期 Lisp 的亲缘关系一样密切。Algol 60，再也不会成为活跃语言，却活在 Scheme 和 Pascal 的基因中。很难找到两种语言，它们是两种文化的交流货币，而这两种文化比围绕这两种语言聚集起来的文化更加不同。Pascal 用于建造金字塔——由军队把沉重石块推到位而建成的宏伟、令人屏息的静态结构。Lisp 用于建造有机体——由小队把变化不定的无数更简单有机体装配到位而建成的宏伟、令人屏息的动态结构。两者所使用的组织原则相同，除了一个极其重要的差别：托付给单个 Lisp 程序员的自由裁量、可导出的功能，比 Pascal 事业中所能发现的要多一个数量级以上。Lisp 程序用其效用超越产生它们的应用的函数来充实库。表，Lisp 的原生数据结构，在很大程度上促成了这种效用的增长。表的简单结构和自然适用性反映在那些惊人地非特异化的函数中。在 Pascal 中，大量可声明的数据结构导致函数内部的专业化，从而抑制并惩罚随意的合作。让 100 个函数作用于一个数据结构，比让 10 个函数作用于 10 个数据结构更好。结果，金字塔必须千年不变地矗立；有机体必须演化，否则就会灭亡。

**校订后**

Lisp 会变化。本书中使用的 Scheme 方言从最初的 Lisp 演化而来，并在若干重要方面不同于后者，包括变量绑定的静态作用域，以及允许函数产生函数作为值。在语义结构上，Scheme 与 Algol 60 的亲缘关系，正如与早期 Lisp 的亲缘关系一样密切。Algol 60，再也不会成为活跃语言，却活在 Scheme 和 Pascal 的基因中。若论语言所承载的文化，很难找到比围绕这两种语言形成的文化差异更大的另一对语言。Pascal 用于建造金字塔——由军队把沉重石块推到位而建成的宏伟、令人屏息的静态结构。Lisp 用于建造有机体——由小队把变化不定的无数更简单有机体装配到位而建成的宏伟、令人屏息的动态结构。两者所使用的组织原则相同，除了一个极其重要的差别：托付给单个 Lisp 程序员的可自主决定并供外部使用的功能，比 Pascal 编程工作中所能发现的要多一个数量级以上。Lisp 程序用其效用超越产生它们的应用的函数来充实库。表，Lisp 的原生数据结构，在很大程度上促成了这种效用的增长。表的简单结构和自然适用性反映在那些具有惊人通用性的函数中。在 Pascal 中，大量可声明的数据结构导致函数的专用化，从而抑制并增加自由组合的代价。让 100 个函数作用于一个数据结构，比让 10 个函数作用于 10 个数据结构更好。结果，金字塔必须千年不变地矗立；有机体必须演化，否则就会灭亡。

### Foreword:0014

**原文**

As one would expect from its goals, artificial intelligence research generates many significant programming problems. In other programming cultures this spate of problems spawns new languages. Indeed, in any very large programming task a useful organizing principle is to control and isolate traffic within the task modules via the invention of language. These languages tend to become less primitive as one approaches the boundaries of the system where we humans interact most often. As a result, such systems contain complex language-processing functions replicated many times. Lisp has such a simple syntax and semantics that parsing can be treated as an elementary task. Thus parsing technology plays almost no role in Lisp programs, and the construction of language processors is rarely an impediment to the rate of growth and change of large Lisp systems. Finally, it is this very simplicity of syntax and semantics that is responsible for the burden and freedom borne by all Lisp programmers. No Lisp program of any size beyond a few lines can be written without being saturated with discretionary functions. Invent and fit; have fits and reinvent! We toast the Lisp programmer who pens his thoughts within nests of parentheses.

**校订前**

正如人们从其目标所预期的那样，人工智能研究产生了许多重要的编程问题。在其他编程文化中，这一连串的问题催生了新的语言。事实上，在任何非常庞大的编程任务中，一个有用的组织原则是通过发明语言来控制和隔离任务模块内部的通信。随着我们人类最频繁交互的系统边界越来越近，这些语言往往变得不那么原始。因此，这类系统包含了许多被重复多次的复杂语言处理功能。Lisp 具有如此简单的语法和语义，以至于解析可以被视为一项基本任务。因此，解析技术在 Lisp 程序中几乎不起作用，而语言处理器的构建也很少成为大型 Lisp 系统增长和变化速度的障碍。最后，正是这种语法和语义的极度简单性，造就了所有 Lisp 程序员所承担的负担与享有的自由。任何超过几行的 Lisp 程序，都不可能在不充满自由裁量函数的情况下写成。发明并适配；出问题再重新发明！我们为在括号嵌套中书写思想的 Lisp 程序员干杯。

**校订后**

正如人们从其目标所预期的那样，人工智能研究产生了许多重要的编程问题。在其他编程文化中，这一连串的问题催生了新的语言。事实上，在任何非常庞大的编程任务中，一个有用的组织原则是通过发明语言来控制和隔离任务模块内部的通信。随着我们人类最频繁交互的系统边界越来越近，这些语言往往变得不那么原始。因此，这类系统包含了许多被重复多次的复杂语言处理功能。Lisp 具有如此简单的语法和语义，以至于解析可以被视为一项基本任务。因此，解析技术在 Lisp 程序中几乎不起作用，而语言处理器的构建也很少成为大型 Lisp 系统增长和变化速度的障碍。最后，正是这种语法和语义的极度简单性，造就了所有 Lisp 程序员所承担的负担与享有的自由。任何超过几行的 Lisp 程序，都不可能在不充满自主设计的函数的情况下写成。发明并适配；出问题再重新发明！我们为在括号嵌套中书写思想的 Lisp 程序员干杯。

### Foreword:0016

**原文**

Next: Preface, Prev: Dedication, Up: Top [Contents]

**校订前**

下一节： Preface, 上一节： Dedication, 上一级： Top [目录]

**校订后**

下一节： 前言, 上一节： 献词, 上一级： 首页 [目录]

### index:0047

**原文**

1.2.2 Tree Recursion

**校订前**

1.2.2 树递归

**校订后**

1.2.2 树形递归

### index:0063

**原文**

2.2 Hierarchical Data and the Closure Property

**校订前**

2.2 层次化数据和闭包性质

**校订后**

2.2 层次化数据和闭合性质

### index:0066

**原文**

2.2.3 Sequences as Conventional Interfaces

**校订前**

2.2.3 序列作为常规接口

**校订后**

2.2.3 序列作为约定接口

### index:0067

**原文**

2.2.4 Example: A Picture Language

**校订前**

2.2.4 示例：图片语言

**校订后**

2.2.4 示例：图画语言

### index:0072

**原文**

2.3.4 Example: Huffman Encoding Trees

**校订前**

2.3.4 示例：Huffman编码树

**校订后**

2.3.4 示例：霍夫曼编码树

### Preface-1e:0001

**原文**

Structure and Interpretation of Computer Programs, 2e: Preface 1e

**校订前**

计算机程序的构造和解释，第2版：前言 1e

**校订后**

计算机程序的构造和解释，第2版：第1版前言

### Preface-1e:0002

**原文**

Next: Acknowledgments, Prev: Preface, Up: Top [Contents]

**校订前**

下一节： Acknowledgments, 上一节： Preface, 上一级： Top [目录]

**校订后**

下一节： 致谢, 上一节： 前言, 上一级： 首页 [目录]

### Preface-1e:0009

**原文**

These skills are by no means unique to computer programming. The techniques we teach and draw upon are common to all of engineering design. We control complexity by building abstractions that hide details when appropriate. We control complexity by establishing conventional interfaces that enable us to construct systems by combining standard, well-understood pieces in a “mix and match” way. We control complexity by establishing new languages for describing a design, each of which emphasizes particular aspects of the design and deemphasizes others.

**校订前**

这些技能绝非计算机编程所独有。我们所教授和借鉴的技术是所有工程设计所共有的。我们通过构建在适当时候隐藏细节的抽象来控制复杂性。我们通过建立常规接口来控制复杂性，这些接口使我们能够以“混合搭配”的方式组合标准的、已被充分理解的部件来构造系统。我们通过建立用于描述设计的新语言来控制复杂性，每种语言都强调设计的特定方面而弱化其他方面。

**校订后**

这些技能绝非计算机编程所独有。我们所教授和借鉴的技术是所有工程设计所共有的。我们通过构建在适当时候隐藏细节的抽象来控制复杂性。我们通过建立约定接口来控制复杂性，这些接口使我们能够以“混合搭配”的方式组合标准的、已被充分理解的部件来构造系统。我们通过建立用于描述设计的新语言来控制复杂性，每种语言都强调设计的特定方面而弱化其他方面。

### Preface-1e:0011

**原文**

In teaching our material we use a dialect of the programming language Lisp. We never formally teach the language, because we don’t have to. We just use it, and students pick it up in a few days. This is one great advantage of Lisp-like languages: They have very few ways of forming compound expressions, and almost no syntactic structure. All of the formal properties can be covered in an hour, like the rules of chess. After a short time we forget about syntactic details of the language (because there are none) and get on with the real issues—figuring out what we want to compute, how we will decompose problems into manageable parts, and how we will work on the parts. Another advantage of Lisp is that it supports (but does not enforce) more of the large-scale strategies for modular decomposition of programs than any other language we know. We can make procedural and data abstractions, we can use higher-order functions to capture common patterns of usage, we can model local state using assignment and data mutation, we can link parts of a program with streams and delayed evaluation, and we can easily implement embedded languages. All of this is embedded in an interactive environment with excellent support for incremental program design, construction, testing, and debugging. We thank all the generations of Lisp wizards, starting with John McCarthy, who have fashioned a fine tool of unprecedented power and elegance.

**校订前**

在教授我们的材料时，我们使用编程语言 Lisp 的一种方言。我们从不正式教授这门语言，因为我们不必这样做。我们只是使用它，学生们几天内就学会了。这是类 Lisp 语言的一大优势：它们形成复合表达式的方式非常少，而且几乎没有语法结构。所有形式属性可以在一小时内讲完，就像国际象棋规则一样。不久之后我们就忘记了语言的语法细节（因为根本没有），转而处理真正的问题——弄清楚我们想要计算什么，我们将如何把问题分解成可管理的部分，以及我们将如何处理这些部分。Lisp 的另一个优势是，它比我们所知的任何其他语言都更多地支持（但不强制）程序模块化分解的大规模策略。我们可以进行过程抽象和数据抽象，我们可以使用高阶函数来捕捉常见的使用模式，我们可以使用赋值和数据变异来模拟局部状态，我们可以用流和延迟求值来连接程序的各个部分，而且我们可以轻松实现嵌入式语言。所有这些都嵌入在一个交互式环境中，对增量式程序设计、构造、测试和调试提供了极好的支持。我们感谢一代又一代的 Lisp 奇才，从 John McCarthy 开始，他们打造了一件前所未有的强大而优雅的精良工具。

**校订后**

在教授我们的材料时，我们使用编程语言 Lisp 的一种方言。我们从不正式教授这门语言，因为我们不必这样做。我们只是使用它，学生们几天内就学会了。这是类 Lisp 语言的一大优势：它们形成复合表达式的方式非常少，而且几乎没有语法结构。所有形式属性可以在一小时内讲完，就像国际象棋规则一样。不久之后我们就忘记了语言的语法细节（因为根本没有），转而处理真正的问题——弄清楚我们想要计算什么，我们将如何把问题分解成可管理的部分，以及我们将如何处理这些部分。Lisp 的另一个优势是，它比我们所知的任何其他语言都更多地支持（但不强制）程序模块化分解的大规模策略。我们可以进行过程抽象和数据抽象，我们可以使用高阶函数来捕捉常见的使用模式，我们可以使用赋值和数据修改来模拟局部状态，我们可以用流和延迟求值来连接程序的各个部分，而且我们可以轻松实现嵌入式语言。所有这些都嵌入在一个交互式环境中，对增量式程序设计、构造、测试和调试提供了极好的支持。我们感谢一代又一代的 Lisp 奇才，从 John McCarthy 开始，他们打造了一件前所未有的强大而优雅的精良工具。

### Preface-1e:0012

**原文**

Scheme, the dialect of Lisp that we use, is an attempt to bring together the power and elegance of Lisp and Algol. From Lisp we take the metalinguistic power that derives from the simple syntax, the uniform representation of programs as data objects, and the garbage-collected heap-allocated data. From Algol we take lexical scoping and block structure, which are gifts from the pioneers of programming-language design who were on the Algol committee. We wish to cite John Reynolds and Peter Landin for their insights into the relationship of Church’s λ-calculus to the structure of programming languages. We also recognize our debt to the mathematicians who scouted out this territory decades before computers appeared on the scene. These pioneers include Alonzo Church, Barkley Rosser, Stephen Kleene, and Haskell Curry.

**校订前**

Scheme，我们所使用的 Lisp 方言，是一次将 Lisp 和 Algol 的力量与优雅结合起来的尝试。我们从 Lisp 中汲取了源自简单语法的元语言能力、程序作为数据对象的统一表示，以及垃圾回收的堆分配数据。我们从 Algol 中汲取了词法作用域和块结构，这些是编程语言设计先驱们——他们曾在 Algol 委员会中——的礼物。我们要引用 John Reynolds 和 Peter Landin，感谢他们对 Church 的 λ 演算与编程语言结构之间关系的洞见。我们也认识到我们欠那些在计算机出现之前几十年就探索了这片领域的数学家的债。这些先驱包括 Alonzo Church、Barkley Rosser、Stephen Kleene 和 Haskell Curry。

**校订后**

Scheme，我们所使用的 Lisp 方言，是一次将 Lisp 和 Algol 的力量与优雅结合起来的尝试。我们从 Lisp 中汲取了源自简单语法的元语言能力、程序作为数据对象的统一表示，以及垃圾回收的堆分配数据。我们从 Algol 中汲取了词法作用域和块结构，这些是编程语言设计先驱们——他们曾在 Algol 委员会中——的礼物。我们要特别提到 John Reynolds 和 Peter Landin，感谢他们对 Church 的 λ 演算与编程语言结构之间关系的洞见。我们也认识到我们欠那些在计算机出现之前几十年就探索了这片领域的数学家的债。这些先驱包括 Alonzo Church、Barkley Rosser、Stephen Kleene 和 Haskell Curry。

### Preface-1e:0013

**原文**

Next: Acknowledgments, Prev: Preface, Up: Top [Contents]

**校订前**

下一节： Acknowledgments, 上一节： Preface, 上一级： Top [目录]

**校订后**

下一节： 致谢, 上一节： 前言, 上一级： 首页 [目录]

### Preface:0002

**原文**

Next: Preface 1e, Prev: Foreword, Up: Top [Contents]

**校订前**

下一节： Preface 1e, 上一节： Foreword, 上一级： Top [目录]

**校订后**

下一节： 第1版前言, 上一节： 序言, 上一级： 首页 [目录]

### Preface:0011

**原文**

Next: Preface 1e, Prev: Foreword, Up: Top [Contents]

**校订前**

下一节： Preface 1e, 上一节： Foreword, 上一级： Top [目录]

**校订后**

下一节： 第1版前言, 上一节： 序言, 上一级： 首页 [目录]

### References:0002

**原文**

Next: Exercises, Prev: 5.5, Up: Top [Contents]

**校订前**

下一节： Exercises, 上一节： 5.5, 上一级： Top [目录]

**校订后**

下一节： 习题, 上一节： 5.5, 上一级： 首页 [目录]

### References:0116

**原文**

Next: Exercises, Prev: 5.5, Up: Top [Contents]

**校订前**

下一节： Exercises, 上一节： 5.5, 上一级： Top [目录]

**校订后**

下一节： 习题, 上一节： 5.5, 上一级： 首页 [目录]

### Term-Index:0002

**原文**

Next: Colophon, Prev: Figures, Up: Top [Contents]

**校订前**

下一节： Colophon, 上一节： Figures, 上一级： Top [目录]

**校订后**

下一节： 版本说明, 上一节： 插图, 上一级： 首页 [目录]

### Term-Index:0026

**原文**

agenda:

**校订前**

议程：

**校订后**

日程表：

### Term-Index:0055

**原文**

box-and-pointer notation:

**校订前**

箱指针表示法：

**校订后**

盒指针表示法：

### Term-Index:0057

**原文**

broken heart:

**校订前**

破碎的心：

**校订后**

断心：

### Term-Index:0077

**原文**

closure:

**校订前**

闭包：

**校订后**

闭合性：

### Term-Index:0079

**原文**

closure property:

**校订前**

闭包性质：

**校订后**

闭合性质：

### Term-Index:0081

**原文**

coerce:

**校订前**

强制：

**校订后**

强制转换：

### Term-Index:0082

**原文**

coercion:

**校订前**

强制：

**校订后**

强制转换：

### Term-Index:0098

**原文**

congruent modulo:

**校订前**

同余模：

**校订后**

模同余：

### Term-Index:0100

**原文**

consequent expression:

**校订前**

后件表达式：

**校订后**

结果表达式：

### Term-Index:0102

**原文**

constructors:

**校订前**

构造器：

**校订后**

构造函数：

### Term-Index:0107

**原文**

conventional interfaces:

**校订前**

常规接口：

**校订后**

约定接口：

### Term-Index:0109

**原文**

conventional interfaces:

**校订前**

常规接口：

**校订后**

约定接口：

### Term-Index:0155

**原文**

Euclidean ring:

**校订前**

欧几里得环：

**校订后**

欧几里得整环：

### Term-Index:0183

**原文**

function boxes:

**校订前**

函数盒：

**校订后**

功能盒：

### Term-Index:0196

**原文**

glitches:

**校订前**

毛刺：

**校订后**

小故障：

### Term-Index:0207

**原文**

headed list:

**校订前**

带表头表：

**校订后**

带表头的表：

### Term-Index:0242

**原文**

labels:

**校订前**

标签：

**校订后**

标号：

### Term-Index:0249

**原文**

linkage descriptor:

**校订前**

连接描述符：

**校订后**

链接描述符：

### Term-Index:0268

**原文**

mark-sweep:

**校订前**

标记-清扫：

**校订后**

标记-清除：

### Term-Index:0289

**原文**

mutators:

**校订前**

变异器：

**校订后**

修改器：

### Term-Index:0290

**原文**

mutex:

**校订前**

互斥元：

**校订后**

互斥量：

### Term-Index:0312

**原文**

obarray:

**校订前**

对象数组：

**校订后**

obarray：

### Term-Index:0316

**原文**

open-code:

**校订前**

开码：

**校订后**

开放编码：

### Term-Index:0317

**原文**

operands:

**校订前**

操作数：

**校订后**

运算对象：

### Term-Index:0349

**原文**

Preface 1e

**校订前**

第 1 版序言

**校订后**

第 1 版前言

### Term-Index:0401

**原文**

selectors:

**校订前**

选择器：

**校订后**

选择函数：

### Term-Index:0496

**原文**

Next: Colophon, Prev: Figures, Up: Top [Contents]

**校订前**

下一节： Colophon, 上一节： Figures, 上一级： Top [目录]

**校订后**

下一节： 版本说明, 上一节： 插图, 上一级： 首页 [目录]

### UTF:0002

**原文**

Next: Dedication, Prev: Top, Up: Top [Contents]

**校订前**

下一节： Dedication, 上一节： Top, 上一级： Top [目录]

**校订后**

下一节： 献词, 上一节： 首页, 上一级： 首页 [目录]

### UTF:0011

**原文**

Addendum: See also the SICP video lectures by Abelson and Sussman: at MIT CSAIL or MIT OCW.

**校订前**

附录：另见 Abelson 和 Sussman 的SICP视频讲座：在MIT CSAIL或MIT OCW。

**校订后**

补记：另见 Abelson 和 Sussman 的SICP视频讲座：在MIT CSAIL或MIT OCW。

### UTF:0014

**原文**

Next: Dedication, Prev: Top, Up: Top [Contents]

**校订前**

下一节： Dedication, 上一节： Top, 上一级： Top [目录]

**校订后**

下一节： 献词, 上一节： 首页, 上一级： 首页 [目录]

## 最终离线验证

- 39 个最终页面与逐句复核决定完全一致，从缓存及持久化修订重建也得到相同的译文。
- 2,965 个段落、1,122 个代码块、5,355 个行内代码元素、1,370 个数学公式和 87 个插图对象保留。
- 10362 个受保护片段逐项保持原样（中文页内链接按对应中文路径转换）。
- 3818 个内部链接经检查，未发现失效锚点或误指向英文页面。
- 11 项离线回归检查通过，包括原文变化、缺少逐句决定和冲突修订的拒绝检查。
