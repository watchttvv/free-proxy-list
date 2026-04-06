# 代理列表

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org)
[![Platform: GitHub Actions](https://img.shields.io/badge/Platform-GitHub%20Actions-blue.svg)](https://github.com/features/actions)
[![自动更新](https://img.shields.io/badge/自动更新-每小时-success.svg)]()

> 发现一个在线代理网页挺好玩，代理更新比较快，我就爬来了。代理基本都是可用的，不是那种 1 万个代理只有几个可以使用的垃圾。

数据来源：[https://tomcat1235.nyc.mn/](https://tomcat1235.nyc.mn/)

## 📋 目录

- [✨ 功能特点](#-功能特点)
- [⚡ 快速开始](#-快速开始)
- [📝 使用方法](#-使用方法)
- [🔄 自动更新](#-自动更新)
- [📦 依赖项](#-依赖项)
- [⚠️ 免责声明](#️-免责声明)

---

## ✨ 功能特点

| 功能 | 说明 |
|------|------|
| ⚡ 自动抓取 | 实时从代理源抓取最新代理列表 |
| 🔄 定时更新 | GitHub Actions 每小时自动运行 |
| 📝 标准格式 | 输出格式：`协议://ip:port [地理位置]` |
| 🌍 地理位置 | 自动解析并标注代理所在地区 |
| 📊 多协议支持 | 支持 HTTP、SOCKS5 等多种协议 |

## ⚡ 快速开始

```bash
# 克隆仓库
git clone https://github.com/watchttvv/free-proxy-list.git
cd free-proxy-list

# 安装依赖
pip install requests beautifulsoup4

# 运行脚本
python generate_proxy_list.py
```

## 📝 使用方法

### 手动运行

```bash
python generate_proxy_list.py
```

### 查看结果

代理列表保存在 `proxy.txt` 文件中，格式示例：

```
socks5://37.18.73.60:5566 [美国 加州 圣何塞]
http://123.143.162.221:6388 [韩国 首尔特别市]
socks5://35.183.59.99:5080 [加拿大 魁北克省 蒙特利尔]
```

## 🔄 自动更新

| 项目 | 说明 |
|------|------|
| 🕐 执行频率 | 每小时自动运行一次 |
| 📝 输出 | 自动提交更新的代理列表到仓库 |
| 🔄 实时性 | 确保代理信息始终保持最新 |

## 📦 依赖项

| 依赖 | 用途 |
|------|------|
| `requests` | HTTP 请求 |
| `beautifulsoup4` | HTML 解析 |

```bash
pip install requests beautifulsoup4
```

## ⚠️ 免责声明

本项目仅用于学习和研究目的，请遵守相关法律法规和网站使用条款。

---

README optimized with [Gingiris README Generator](https://gingiris.github.io/github-readme-generator/)
