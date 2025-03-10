import pdftotext
import argparse

COLUMN_WIDTH = 64

class Page:
    def __init__(self, page_string, skip='skip this line', bulletpoint_format=True, bullet='', merge_lines=True, width=COLUMN_WIDTH):
        '''
        skip: 如果页面中包含该字符串（或多个字符串），则跳过对应行，例如页面标签 " / 10"
        '''
        self.page_string = page_string
        self.lines = self.page_string.replace('  ', '').split('\n')
        self.parsed = self.lines
        self.skip = skip
        self.bulletpoint_format = bulletpoint_format
        self.bullet = bullet
        self.merge_lines = merge_lines
        self.width = width

    def makeTitle(self):
        self.title = '\n##### ' + self.lines[0]
        temp = self.lines
        temp[0] = self.title
        self.parsed = temp
        return self

    def parsePage(self):
        string = ''
        for line in self.parsed:
            not_skipped = True
            new_line = True
            is_list_item = False

            if line == '':
                not_skipped = False

            if isinstance(self.skip, list):
                for skipping_item in self.skip:
                    if skipping_item in line:
                        not_skipped = False
            else:
                if self.skip in line:
                    not_skipped = False

            if not_skipped:
                curr_line = Line(line.replace('↵', ''), self.bullet)
                temp = line
                if self.bulletpoint_format:
                    try:
                        if (temp.lstrip(' ')[0] == self.bullet) or (temp.lstrip(' ')[1] == self.bullet) or (temp.lstrip(' ')[1] == '.'):
                            is_list_item = True
                            curr_line.makeListItem()
                        elif (len(line) < self.width) and self.merge_lines:
                            new_line = False
                    except IndexError:
                        if (len(line) < self.width) and self.merge_lines:
                            new_line = False

                    curr_line = curr_line.parsed

                    if new_line:
                        string += '\n' + curr_line + ' '
                    else:
                        string += curr_line + ' '
                else:
                    string += '\n' + line + ' '
        self.parsed = string
        return self

class Line:
    def __init__(self, line_string, bullet):
        self.line_string = line_string
        self.parsed = line_string
        self.bullet = bullet

    def makeListItem(self):
        self.parsed = self.parsed.replace(self.bullet, '- ')
        return self

class PDF:
    def __init__(self, file, pw='', skip='skip this line', manual=False, bulletpoint_format=True, outfile='output.txt', bullet='- ', merge_lines=False, width=COLUMN_WIDTH):
        self.file = file
        self.pw = pw
        with open(file, "rb") as f:
            if self.pw != '':
                pdf = pdftotext.PDF(f, self.pw)
            else:
                pdf = pdftotext.PDF(f)
        self.pdf = pdf
        self.n_pages = len(pdf)
        self.manual = manual
        self.bulletpoint_format = bulletpoint_format
        self.skip = skip
        self.outfile = outfile
        self.bullet = bullet
        self.merge_lines = merge_lines
        self.width = width

    def parsePDF(self):
        if not self.manual:
            with open(self.outfile, 'w') as output:
                for page in self.pdf:
                    output.write('\n')
                    cur_page = Page(page, self.skip, bulletpoint_format=self.bulletpoint_format, bullet=self.bullet, merge_lines=self.merge_lines, width=self.width)
                    cur_page = cur_page.makeTitle()
                    cur_page = cur_page.parsePage()
                    print(cur_page.parsed)
                    for parsed_line in cur_page.parsed:
                        output.write(parsed_line)
        else:
            for i, page in enumerate(self.pdf):
                with open(self.outfile, 'w') as output:
                    satisfied = False
                    while not satisfied:
                        print('\n------------processing page %i / %i------------\n' % (i+1, self.n_pages))
                        skip = str(input('skip lines containing the following (separate multiple with ";"), default "skip this line": ') or 'skip this line')
                        skip = skip.split(';')
                        merge_lines = input('merge broken lines? (T: yes -> form paragraphs, default / F: no, leave as they exist in the pdf): ') or 'T'
                        merge_lines = False if merge_lines == 'F' else True
                        bulletpoint_format = input('modify format (T: bulletpoint_format, default / F: original document): ') or 'T'
                        if bulletpoint_format == 'T':
                            bulletpoint_format = True
                            bullet = str(input('identifier for bullet point: ') or '- ')
                        else:
                            bulletpoint_format = False
                            bullet = '- '
                        width = int(input('merge lines shorter than (max no. of characters): ') or 64)
                        cur_page = Page(page, skip, bulletpoint_format, bullet, merge_lines, width)
                        cur_page = cur_page.makeTitle()
                        cur_page = cur_page.parsePage()
                        print('\n ------------OUTPUT------------')
                        print(cur_page.parsed)
                        print('\n--------------------------------\n')
                        ok = input('satisfied? (y/n):')
                        if ok == 'y':
                            output.write('\n')
                            for parsed_line in cur_page.parsed:
                                output.write(parsed_line)
                            print('ok, start with the next page!')
                            satisfied = True
                        else:
                            print('\nRedo current page.')

def main():
    parser = argparse.ArgumentParser(description='使用 pdftotext 解析 PDF，并进行自定义格式化输出')
    parser.add_argument('filename', help='待处理的 PDF 文件路径')
    parser.add_argument('-p', '--password', default='', help='PDF 文件密码（如果有）')
    parser.add_argument('-o', '--outfile', default='output.txt', help='输出文本文件名 (默认 output.txt)')
    parser.add_argument('-m', '--manual', action='store_true', help='手动模式：逐页交互设置参数')
    parser.add_argument('--width', type=int, default=COLUMN_WIDTH, help='合并长度小于该值的行 (默认 64)')
    parser.add_argument('--skip', default='skip this line', help='跳过包含此字符串的行（多个字符串用分号分隔） (默认 "skip this line")')
    parser.add_argument('--merge_lines', type=lambda x: x.lower() in ['true', 't', 'yes', '1'], default=True, help='是否合并断开的行 (默认 True)')
    parser.add_argument('--bulletpoint_format', type=lambda x: x.lower() in ['true', 't', 'yes', '1'], default=True, help='是否使用 bullet point 格式化 (默认 True)')
    parser.add_argument('--bullet', default='- ', help='bullet point 标识符 (默认 "- ")')
    
    args = parser.parse_args()
    
    # 如果传入的 skip 参数中包含分号，则转换为列表，否则保持字符串
    skip_value = args.skip.split(';') if ';' in args.skip else args.skip

    pdf_obj = PDF(
        file=args.filename,
        pw=args.password,
        skip=skip_value,
        manual=args.manual,
        bulletpoint_format=args.bulletpoint_format,
        outfile=args.outfile,
        bullet=args.bullet,
        merge_lines=args.merge_lines,
        width=args.width
    )
    pdf_obj.parsePDF()

if __name__ == "__main__":
    main()
