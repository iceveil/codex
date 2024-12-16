# 🚀 **代码片段管理平台**

> 一个基于 Django 的开源项目，轻松管理和分享您的代码片段。

![GitHub Repo](https://img.shields.io/badge/Django-4.x-green) ![License](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.9+-yellow)

---

## 📚 **项目简介**

代码片段管理平台提供了一种高效的方式来组织、管理和分享代码片段。无论是开发者日常积累代码，还是团队共享代码，都可以通过本平台实现。

**功能亮点**：
- 🌟 **代码盒子管理**：支持将代码片段归纳到不同的"代码盒子"中，通常一个盒子可以存放一种语言或一套类型的代码片段。
- 🔍 **代码搜索**：快速查找代码片段。
- 🛠 **语法高亮显示**：代码展示更清晰，便于阅读。
- 🤝 **用户管理**：支持用户注册、登录和代码私有化管理。
- 📤 **代码分享**：轻松生成分享链接，快速分发代码片段。

---

## 🚀 **安装与运行**

### 1️⃣ 克隆项目

```bash
git clone https://github.com/iceveil/codex.git
cd codex
```

### 2️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

### 3️⃣ 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ 启动项目

```bash
python manage.py runserver
```

项目将运行在 `http://127.0.0.1:8000/`。

---

## 📋 **使用说明**

1. 访问 **首页**，注册或登录账户。
2. 创建代码盒子，管理您的一组代码片段，支持存放单一语言或一套类型代码。
3. 新增代码片段，输入代码内容、选择代码盒子，保存即可。
4. 管理个人代码，支持编辑、删除或分享。
5. 通过搜索功能快速找到您需要的代码片段。

---

## 🤝 **贡献指南**

欢迎开发者为此项目贡献代码！请按以下步骤操作：

1. Fork 仓库
2. 创建分支 (`git checkout -b feature/your-feature`)
3. 提交更改 (`git commit -m 'Add some feature'`)
4. 推送分支 (`git push origin feature/your-feature`)
5. 提交 Pull Request

---

## 📄 **许可证**

本项目使用 [MIT 许可证](LICENSE)。

---

## 🧑‍💻 **开发者信息**

- **项目作者**：iceveil
- **GitHub**：[https://github.com/iceveil/codex](https://github.com/iceveil/codex)

---

## ⭐ **致谢**

感谢所有参与和支持本项目的开发者！如果觉得本项目对您有帮助，请给个 **Star** ⭐！

---

### 🎉 **未来计划**

- 支持代码评论和点赞功能
- 增加更多代码语言和样式主题
- 提供 API 接口，便于第三方集成