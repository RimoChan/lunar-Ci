# 【lunar-Ci】今日诸事不宜！

你是否有过这样的经历，明明合并代码之前通过了所有测试，但是上线之后服务就炸了？

这是因为你的测试不够全面。在Librian幼女娱乐中心<sub>(这是个公司)</sub>，合并代码之前得先检查黄历，如果黄历说诸事不宜，那就不能合并。


## 使用方法

你只需要为你的GitHub仓库新建一个Action，设置为在收到PR的时候安装`lunar_test`并进行单元测试，之后所有的PR就都会自动测试啦。

Action的参考代码长这样——

```yaml
name: CI
on:
  push:
    branches: [ slave ]
  pull_request:
    branches: [ slave ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2.2.2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install lunar_test
      - name: lunar_test
        run: python -m unittest lunar_test
```

对了，虽然这是一个Python仓库，但这个Action和仓库语言没有关系，大家都可以用。


## 本地测试

你也可以使用lunar_test来测试你的本地代码，也只要先`pip install lunar_test`，然后在测试脚本里加上——

```sh
python -m unittest lunar_test
```

这样就好了，测试代码从来没有这么方便！
