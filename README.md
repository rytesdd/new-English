# New English

This repository contains English learning materials and resources.

## Document Parser Feature

This project includes a document parser that can extract text from various file formats including:
- Plain text files (.txt)
- PDF documents (.pdf)
- Microsoft Word documents (.docx)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installing

1. Clone the repository
2. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```

## Usage

Run the document parser with:
```
python3 document_parser/main.py <file_path> [-o output_file]
```

### Example

```
# 直接输出到控制台
python3 document_parser/main.py sample.pdf

# 保存到文件
python3 document_parser/main.py sample.pdf -o extracted_text.txt
```

## Authors

* **rytesdd** - *Initial work* 

## License

This project is licensed under the MIT License.