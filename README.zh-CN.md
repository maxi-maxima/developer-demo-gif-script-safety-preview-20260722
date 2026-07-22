# Developer Demo GIF Script Safety Preview

## 解决的痛点
开发者发布开源项目时常录终端 GIF，脚本里可能不小心包含 token、.env 或危险命令。

## 为什么现在值得做
AI/开发者工具项目越来越依赖短视频和 GIF 演示传播，录制前安全预览能减少泄露。

## 安装与运行
无需第三方依赖。

```bash
python developer_demo_gif_script_safety_preview.py --help
python developer_demo_gif_script_safety_preview.py --json examples/demo.sh
```

## 示例
```bash
python developer_demo_gif_script_safety_preview.py examples/demo.sh
# safe_to_record=False findings=2 storyboard_steps=3
```

## 自检
```bash
python test_developer_demo_gif_script_safety_preview.py
```

## 路线图
- 输出 asciinema 章节文件
- 增加终端宽度可读性评分
- 自动生成脱敏后的演示脚本

## 许可证
MIT
