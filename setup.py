from setuptools import find_packages, setup

setup(name='portuguese_bert',
      packages=find_packages(),
      install_requires=[
        'pytorch-transformers==1.1.0', 'seqeval==0.0.12', 'jsonlines==1.2.0',
        'scikit-learn',
        'pytorch_crf @ git+https://github.com/kmkurn/pytorch-crf.git@4cd79bc8af55fb0f34a2a39b2e38f0e71c208fd4#egg=pytorch_crf'
      ]
)
