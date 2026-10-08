#!/usr/bin/env python3
"""V12: rebuild a metadata-only EPUB spine map. Never writes novel body text."""
import argparse
import csv
import hashlib
import re
from pathlib import Path
from posixpath import dirname, join, normpath
from zipfile import ZipFile
from lxml import etree, html

NUMERIC = re.compile(r'^第\s*([0-9０-９]+)\s*章')
CHINESE = re.compile(r'^第([一二三四五六七八九十百千]+)章')
DIGITS = str.maketrans('０１２３４５６７８９','0123456789')
EXPECTED = {
    '晚明': ('a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082', 571),
    '铁血残明': ('9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf', 532),
}

def chinese_number(s):
    digits=dict(zip('零一二三四五六七八九',range(10)))
    out=0; part=0
    for c in s:
        if c in digits: part=digits[c]
        elif c=='十':out+=(part or 1)*10; part=0
        elif c=='百':out+=(part or 1)*100; part=0
        elif c=='千':out+=(part or 1)*1000; part=0
    return out+part

def text_node(el):
    return re.sub(r'\s+',' ',''.join(el.itertext())).strip()

def title_from(dom):
    nodes=dom.xpath('//body//*[local-name()="h1" or local-name()="h2" or local-name()="h3" or local-name()="h4"]')
    nodes+=dom.xpath('//*[local-name()="title"]')
    return next((x for el in nodes if (x:=text_node(el))), '')

def build(book, path):
    dig=hashlib.sha256(path.read_bytes()).hexdigest()
    expected,count=EXPECTED[book]
    if dig!=expected:raise ValueError(f'Unexpected EPUB SHA256 for {book}: {dig}')
    rows=[]; volume=0; ordinal=0
    with ZipFile(path) as z:
        if z.testzip():raise ValueError('Bad EPUB ZIP CRC')
        meta=etree.fromstring(z.read('META-INF/container.xml'))
        opfs=meta.xpath('//*[local-name()="rootfile"]/@full-path')
        if len(opfs)!=1:raise ValueError('Unexpected container rootfile count')
        opf=opfs[0]
        src=etree.fromstring(z.read(opf))
        manifest={m.get('id'):m for m in src.xpath('//*[local-name()="manifest"]/*')}
        spine=src.xpath('//*[local-name()="spine"]/*')
        for i,item in enumerate(spine):
            idref=item.get('idref'); file=manifest.get(idref)
            if file is None:raise ValueError(f'Unresolved spine {i} idref {idref}')
            internal=normpath(join(dirname(opf),file.get('href').split('#')[0]))
            body=z.read(internal)
            dom=html.fromstring(body)
            title=title_from(dom)
            all_body=dom.xpath('//body')
            text=text_node(all_body[0]) if all_body else ''
            m=NUMERIC.match(title)
            c=CHINESE.match(title) if m is None else None
            n=int(m.group(1).translate(DIGITS)) if m else (chinese_number(c.group(1)) if c else None)
            typ='numbered_chapter' if n is not None else 'front_or_appendix_review'
            if book=='晚明' and i<12 and typ=='numbered_chapter':typ='supplemental_reference'
            if book=='晚明' and c is not None:typ='global_numbered_chapter'
            if book=='晚明' and i in (11,63,118,169,286,503):typ='volume_separator'
            if n is not None and '未完待续' in text and len(text)<100:typ='incomplete_placeholder'
            if (book=='铁血残明' and title=='引子') or (book=='晚明' and title=='可有可无的序'):typ='prologue'
            if not text and n is None:typ='image_or_empty'
            if typ=='volume_separator':volume+=1
            if typ in ('numbered_chapter','global_numbered_chapter'):ordinal+=1; narrative_ordinal=ordinal
            else:narrative_ordinal=''
            rows.append({'spine_index':i, 'idref':idref, 'epub_path':internal, 'title':title[:100],
              'chapter_number':n or '', 'type':typ, 'body_characters':len(text), 'file_bytes':len(body),
              'file_sha256':hashlib.sha256(body).hexdigest(), 'linear':item.get('linear') or 'unspecified',
              'volume_ordinal':volume if book=='晚明' and volume else '', 'narrative_ordinal':narrative_ordinal})
    if ordinal!=count:raise ValueError(f'{book}: chapter count {ordinal} expected {count}')
    return rows

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--wanming', type=Path, required=True, help='Source EPUB file')
    parser.add_argument('--tiexue', type=Path, required=True, help='Source EPUB file')
    parser.add_argument('--output', type=Path, default=Path('research/epub_audit'))
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    for book,path in [('晚明',args.wanming),('铁血残明',args.tiexue)]:
        rows=build(book,path)
        outfile=args.output / f'{book}_spine.csv'
        with outfile.open('w',newline='',encoding='utf-8-sig') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        print(f'{book}: {len(rows)} spine items, {EXPECTED[book][1]} narrative chapters; wrote {outfile}')

if __name__=='__main__':main()
