#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class ProxyListScraper:
    def __init__(self):
        self.url = "https://tomcat1235.nyc.mn/proxy_list"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def scrape_proxy_list(self):
        """抓取代理列表"""
        try:
            print(f"正在抓取代理列表: {self.url}")
            response = requests.get(self.url, headers=self.headers, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 查找包含代理数据的表格
            table = soup.find('table')
            if not table:
                print("未找到代理数据表格")
                return []
            
            proxies = []
            rows = table.find_all('tr')[1:]  # 跳过表头
            
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 4:  # 需要至少4列：协议、IP、端口、位置
                    protocol = cells[0].text.strip()
                    ip = cells[1].text.strip()
                    port = cells[2].text.strip()
                    location = cells[3].text.strip() if len(cells) > 3 else "未知"
                    
                    # 清理位置信息中的多余文本
                    location = location.replace('复制', '').replace('已复制', '').replace('已', '').strip()
                    # 移除多余的空行、换行符和多余的空格
                    location = ' '.join(location.split())
                    
                    if protocol and ip and port:
                        # 使用标准代理格式：协议://ip:port [地址位置]
                        proxy = f"{protocol}://{ip}:{port} [{location}]"
                        proxies.append(proxy)
            
            print(f"成功抓取到 {len(proxies)} 个代理")
            return proxies
            
        except requests.RequestException as e:
            print(f"网络请求错误: {e}")
            return []
        except Exception as e:
            print(f"抓取错误: {e}")
            return []
    
    def save_to_file(self, proxies, filename: str='proxy.txt') -> bool:
        """保存代理列表到文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # 写入时间戳
                f.write(f"# 代理列表更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"# 总计: {len(proxies)} 个代理\n\n")
                
                # 写入代理列表 (标准格式：协议://ip:port [地址位置])
                for proxy in proxies:
                    f.write(f"{proxy}\n")
            
            print(f"代理列表已保存到 {filename}")
            return True
            
        except Exception as e:
            print(f"保存文件错误: {e}")
            return False

def main() -> None:
    """主函数"""
    scraper = ProxyListScraper()
    
    # 抓取代理列表
    proxies = scraper.scrape_proxy_list()
    
    if proxies:
        # 保存到文件
        scraper.save_to_file(proxies)
        print("代理列表抓取完成！")
    else:
        print("未能获取到代理数据")

if __name__ == "__main__":
    main()
