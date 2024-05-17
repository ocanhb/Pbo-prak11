# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:01:54 2024

@author: ocanh
"""

def honorific(cls):
    class HonorificCls(cls):
        def full_name(self):
            return f"Full Name: Mr. {super().full_name()} NIM: {self.nim}"

    return HonorificCls

@honorific
class Person:
    def __init__(self, nama_lengkap, nim):
        self.nama_lengkap = nama_lengkap
        self.nim = nim

    def full_name(self):
        return f"{self.nama_lengkap}"

# Penggunaan
nama_lengkap = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")

person = Person(nama_lengkap, nim)
print(person.full_name())
