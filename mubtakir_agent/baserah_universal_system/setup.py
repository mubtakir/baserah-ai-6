#!/usr/bin/env python3
"""
Setup script for Baserah Universal System

👨‍💻 المطور: باسل يحيى عبدالله
🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
📅 تاريخ الإنشاء: 2025
🌟 النظام: Baserah Universal System - نظام ثوري نقي
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="baserah-universal-system",
    version="1.0.0",
    author="باسل يحيى عبدالله (Basil Yahya Abdullah)",
    author_email="basil.yahya.abdullah@example.com",
    description="نظام Baserah الثوري المتكامل - Revolutionary Universal System",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/basil-yahya-abdullah/baserah-universal-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Religion",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ],
        "full": [
            "sympy>=1.9.0",
            "pillow>=8.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "baserah-cli=user_interfaces.cli_interface:main",
            "baserah-web=user_interfaces.web_interface:main",
            "baserah-api=user_interfaces.api_interface:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.yaml", "*.yml"],
        "ref": ["*"],
        "documentation": ["*"],
    },
    keywords=[
        "artificial intelligence",
        "mathematics", 
        "arabic language",
        "quran analysis",
        "revolutionary theories",
        "basil theories",
        "zero duality theory",
        "perpendicular opposites theory", 
        "filament theory",
        "sigmoid functions",
        "linear equations",
        "pure mathematics",
        "islamic studies",
        "arabic lexicon",
        "morphological analysis",
        "semantic analysis",
        "intelligent agent",
        "mathematical engine",
        "dream interpretation",
        "content generation",
        "code generation",
        "revolutionary system",
        "baserah methodology"
    ],
    project_urls={
        "Bug Reports": "https://github.com/basil-yahya-abdullah/baserah-universal-system/issues",
        "Source": "https://github.com/basil-yahya-abdullah/baserah-universal-system",
        "Documentation": "https://baserah-universal-system.readthedocs.io/",
    },
)
