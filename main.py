import sys
import random

string vtipy[] = {"Ztratit manželku je pro muže obvykle velmi těžké. Někteří by mohli říct až nemožné.", "Když vidím čokoládu, slyším v hlavě dva hlasy. Ten první říká: 'Musíš sníst tu čokoládu.' Ten druhý hlas říká: 'Slyšelas dobře. Sněz tu čokoládu.' "}


def main():
    print "Generátor Vtipů --- Jozef Nagy v. 1.0\n"
    print "-------------------------------------\n\n"

    for x in range(10):
        print vtipy[random.randint(1, 11)]
