from urllib.request import urlretrieve
from os import path
from zipfile import ZipFile
import tarfile


def download(name, url, write_dir='data'):
    urlretrieve(url, path.join(write_dir, name))
    print('downloaded {}'.format(name))
    if (url.endswith('tar.gz')):
        tar = tarfile.open(path.join(write_dir, name), 'r:gz')
        tar.extractall()
        tar.close()
        print('extracted {}'.format(name))
    elif (url.endswith('zip')):
        with ZipFile(path.join(write_dir, name), 'r') as f:
            f.extractall(path.join(write_dir, path.splitext(name)[0]))
        print('extracted {}'.format(name))

        
if __name__ == '__main__':
    resources = [('word2vec-wiki.zip', 'http://vectors.nlpl.eu/repository/11/6.zip'),
                ('glove-wiki.zip', 'http://vectors.nlpl.eu/repository/11/8.zip'),
                ('fasttext-wiki.zip', 'http://vectors.nlpl.eu/repository/11/10.zip'),
                ('bpeemb.tar.gz', 'https://nlp.h-its.org/bpemb/en/en.wiki.bpe.vs100000.d300.w2v.txt.tar.gz')]
    for resource_name, url in resources:
        download(resource_name, url)