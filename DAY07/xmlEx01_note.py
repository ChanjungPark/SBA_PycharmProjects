# xmlEx01_note.py

# 첨부2.zip 파일을 압축 해제하시고, 파이참에 복사해주세요.
# https://www.w3schools.com/ 사이트 열어주세요.
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

abcd = Element('note')
abcd.attrib['no'] = '100'

SubElement(abcd, 'to').text = '홍길동'
SubElement(abcd, 'from').text = '김철수'
SubElement(abcd, 'heading').text = '잘 지내지'
SubElement(abcd, 'body').text = '밖에 비가 오네'

def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(abcd)

xmlFile = 'xmlEx_01_note.xml'

ElementTree(abcd).write(xmlFile, encoding='utf-8')

print(xmlFile + ' 파일이 생성되었습니다.')