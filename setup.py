from setuptools import setup

setup(
    name='vcf2gwas',
    version='0.8.9',
    description="Python API for comprehensive GWAS analysis using GEMMA",
    license="GNUv3",
    author="Frank Vogt, Ellen Schofield",
    url='https://github.com/tottlefields/vcf2gwas.git',
    packages=['vcf2gwas'],
    package_dir={'vcf2gwas': 'vcf2gwas'},
    package_data={'vcf2gwas': ['*.yml', 'input/example.*', 'GFF_files/GFF*', 'README.*', 'LIC*']},
    keywords='vcf2gwas',
    classifiers=['Programming Language :: Python :: 3.9']
)
