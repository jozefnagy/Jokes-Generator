# coding=utf-8
import sys
import random

vtipy = ["Ztratit manželku je pro muže obvykle velmi těžké. Někteří by mohli říct až nemožné.", "Když vidím čokoládu, slyším v hlavě dva hlasy. Ten první říká: 'Musíš sníst tu čokoládu.' Ten druhý hlas říká: 'Slyšelas dobře. Sněz tu čokoládu.' ", "Moje žena vaří tak hrozně, že se zpravidla vzdáváme díky Bohu i po jídle.", "Proč není svatba dvou zadnicových půlek dobrý nápad? Protože jdou od sebe kvůli každému prdu.",
         "Rád bych zakoupil nový bumerang. A taky bych potřeboval poradit, jak vyhodit ten starý.", "Věda nám dala letadla, nebetyčné mrakodrapy… Ale jen náboženství dokáže tyhle dvě věci spojit.", "Můj nedostatek elektrikářských znalostí pro mnoho lidí často představuje šok..", "Kdo je sakra Rorschach, a proč namaloval tolik obrázků mojí matky?!", "Co dostanete, když zkřížíte řečnickou otázku s vtipem?", "Říká se, že za prachy si štěstí nekoupíš. Ale každá teorie by se měla otestovat."]


def main():
    print("Generátor Vtipů --- Jozef Nagy v. 1.0\n")
    print("-------------------------------------\n\n")

    # 1, nejmenší číslo generace (Neměnit), Druhé číslo změnit pouze v případě zvýšení počtu vtipů (Číslo by mělo být o 1 větší než celkový počet vtipů(řádek 4))
    print(vtipy[random.randint(1, 11)])
