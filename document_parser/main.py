import argparse
import os
from parser import DocumentParser

def main():
    parser = argparse.ArgumentParser(description='从各种文档中提取文本')
    parser.add_argument('file_path', help='文档文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.file_path):
        print(f"文件不存在: {args.file_path}")
        return
    
    # 创建解析器实例
    document_parser = DocumentParser()
    
    # 提取文本
    print(f"正在从 {args.file_path} 提取文本...")
    text = document_parser.extract_text(args.file_path)
    
    if text is not None:
        # 输出结果
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"文本已保存到: {args.output}")
        else:
            print("\n提取的文本内容:")
            print("=" * 50)
            print(text)
            print("=" * 50)
            print(f"\n文本提取成功！共 {len(text)} 个字符")
    else:
        print("文本提取失败！")

if __name__ == "__main__":
    main()