import os
from typing import Optional

class DocumentParser:
    def extract_text(self, file_path: str) -> Optional[str]:
        """从文档中提取文本
        
        Args:
            file_path: 文档文件路径
            
        Returns:
            提取的文本内容，如果无法解析则返回None
        """
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.txt':
            return self._extract_from_txt(file_path)
        elif file_extension == '.pdf':
            return self._extract_from_pdf(file_path)
        elif file_extension == '.docx':
            return self._extract_from_docx(file_path)
        else:
            print(f"不支持的文件格式: {file_extension}")
            return None
    
    def _extract_from_txt(self, file_path: str) -> Optional[str]:
        """从txt文件中提取文本"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # 尝试使用其他编码
            try:
                with open(file_path, 'r', encoding='gbk') as file:
                    return file.read()
            except Exception as e:
                print(f"读取TXT文件时出错: {e}")
                return None
        except Exception as e:
            print(f"读取TXT文件时出错: {e}")
            return None
    
    def _extract_from_pdf(self, file_path: str) -> Optional[str]:
        """从PDF文件中提取文本"""
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except Exception as e:
            print(f"读取PDF文件时出错: {e}")
            return None
    
    def _extract_from_docx(self, file_path: str) -> Optional[str]:
        """从Word文档中提取文本"""
        try:
            from docx import Document
            doc = Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            print(f"读取Word文档时出错: {e}")
            return None