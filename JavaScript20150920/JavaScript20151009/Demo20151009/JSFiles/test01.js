

function myFunction()
{
x=document.getElementById("demo");  // 找到元素
x.innerHTML="Hello JavaScript!";    // 改变内容
}

function testFun()
{
y=document.getElementById("demo");  // 找到元素
y.innerHTML="点击按钮事件";
// document.getElementById("demo").innerHTML="点击按钮事件"；
}

function modifyTagName()
{
x=document.getElementById("tag1");  // 找到元素
x.innerHTML="点击按钮2，修改标签文本";    // 改变内容
}

function modifyTagName2()
{
y=document.getElementById("tag1");  // 找到元素
y.innerHTML="点击按钮1，更新标签文本";
// document.getElementById("demo").innerHTML="点击按钮事件"；
}

