import os

# 该脚本用来将多个文档合并为一个文档

def merge_md_files(input_dir, output_file):
    # 获取目录下所有md文件并按文件名排序
    md_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.md')])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for md_file in md_files:
            # 跳过最终合并文件自身
            if md_file == os.path.basename(output_file):
                continue
                
            file_path = os.path.join(input_dir, md_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read().strip()  # 去除头尾空行
                    outfile.write(content + '\n\n')  # 文件间保留两个空行
                print(f'成功合并: {md_file}')
            except Exception as e:
                print(f'错误处理 {md_file}: {str(e)}')

if __name__ == '__main__':
    input_directory = None  # 需要修改为实际目录
    output_filename = 'merged_dataset.md'
    merge_md_files(input_directory, output_filename)
    print(f'合并完成，生成文件: {output_filename}')
