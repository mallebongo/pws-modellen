import math
import random

import matplotlib.pyplot as plt
import time
import keyboard
import numpy as np

t = 0
dt = 180

min_min_afstandradiusmarssate = 9E50

# massa's planeten

M_zon = 1.99e30
M_aarde = 8.972e24
M_mars = 0.642e24
M_satelliet = 1000

# radius planeten

r_zon = 695700000
r_aarde = 6378000
r_mars = 3396000

# grafitatieconstante
G = 6.67E-11

# astronomische eenheid
au = 149597870700

# Marsvoor
MarsVoor = 1

# graden waarop we moeten vertrekken
gradenwaaropwemoetenvertrekken = 61.076772808280026

x_satelliet1 = 0  # in meters
y_satelliet1 = -149.56 * 10 ** 9  # in meters
vx_satelliet1 = 4800 + 29795  # in m/s
vy_satelliet1 = 0  # in m/s

x_aarde1 = 0  # in meters
y_aarde1 = -149.6 * 10 ** 9  # in meters
vx_aarde1 = 29795  # m/s
vy_aarde1 = 0  # m/s

x_mars1 = 0.228 * 10 ** 12  # in meters
y_mars1 = 0  # in meters
vx_mars1 = 0  # m/s
vy_mars1 = 23605.55697  # m/s

r_satelliet_zon = math.sqrt(x_satelliet1 ** 2 + y_satelliet1 ** 2)
r_satelliet_aarde = math.sqrt((x_satelliet1 - x_aarde1) ** 2 + (y_satelliet1 - y_aarde1) ** 2)
r_satelliet_mars = math.sqrt((x_satelliet1 - x_mars1) ** 2 + (y_satelliet1 - y_mars1) ** 2)

v_extra = 11011
schaal = 1E9
r_satelliet_mars_max = 9999999999999999999999
min_afstandradiusmarssate = 999999999999999999999

columysatelliet = []
columxsatelliet = []
columymars = []
columxmars = []
columyaarde = []
columxaarde = []
columysatellietlancering = []
columxsatellietlancering = []
columysatelliet1epos = []
columxsatelliet1epos = []
columtijd = []
columsnelheidsatelliet = []
columsatellietbuiten = []
columxmarsnalancering = []
columymarsnalancering = []

gradenvertrek = 0
marsrondjejaar = 0
max_satellietbuiten = 0
totaalextrav = 0
# de = 0

p = 0
z = 0
l = 0
i = 0
d = 0
u = 0
Q = 0
j = 0
Y = 0
q = 0
o = 0
M = 0
B = 0
J = 0
P = 0
I = 0
h = 0
H = 0
S = 0
F = 0
Z = 0
aa = 0
ab = 0
ac = 0
ad = 0
ae = 0
af = 0
ag = 0
ah = 0
ai = 0
aj = 0
ak = 0
al = 0
am = 0


def grafiekplotten():
    plt.figure(figsize=(5, 5))
    #plt.plot([columxaarde], [columyaarde], 'ro', color='blue', markersize=2.5)
    plt.plot([columxmars], [columymars], 'ro', color='red', markersize=2.5)
    plt.plot([columxmarsnalancering], [columymarsnalancering], 'ro', color='green', markersize=2.5)
    #plt.plot([columxsatelliet], [columysatelliet], 'ro', color='black', markersize=2)
    #plt.plot([columxsatelliet1epos], [columysatelliet1epos], 'ro', color='green', markersize=5)
    #plt.plot([columxsatellietlancering], [columysatellietlancering], 'ro', color='orange', markersize=6)
    plt.plot([satellietxlanceering], [satellietylanceering], 'ro', color='orange', markersize=6)
    plt.plot([aardexlanceering], [aardeylanceering], 'ro', color='purple', markersize=10)
    plt.plot([0], [0], 'ro', color='yellow', markersize=20)
    plt.axis([-500, 500, -500, 500])
    plt.show()
    plt.close()


def snelheidsgrafiekplotten():
    plt.figure(figsize=(5, 5))
    plt.plot([columtijd], [columsnelheidsatelliet], 'ro', color='black', markersize=2)
    plt.axis([-5000000, 5000000, 20000, 50000])
    plt.show()
    plt.close()


def satellietbuitengrafiek():
    plt.figure(figsize=(5, 5))
    plt.plot([columtijd], [columsatellietbuiten], 'ro', color='black', markersize=2)
    plt.axis([-50000000, 50000000, -15E6, 25E6])
    plt.show()
    plt.close()


class verplaatsing:

    def __init__(self, vxpos, vypos, Xpos, Ypos):
        self.vy = vypos
        self.vx = vxpos
        self.Ypos = Ypos
        self.Xpos = Xpos

    def deverplaasting(self):
        self.r_zon = math.sqrt(self.Xpos ** 2 + self.Ypos ** 2)
        self.a_zon = G * M_zon / (self.r_zon ** 2)
        self.ax_zon = -self.a_zon * (self.Xpos / self.r_zon)
        self.ay_zon = -self.a_zon * (self.Ypos / self.r_zon)

        self.r_mars = math.sqrt((self.Xpos - mars.Xpos) ** 2 + (self.Ypos ** 2 - mars.Ypos) ** 2)
        if self.r_mars == 0:
            self.ax_mars = 0
            self.ay_mars = 0
            pass
        else:
            self.a_mars = G * M_mars / (self.r_mars ** 2)
            self.ax_mars = -self.a_mars * ((self.Xpos - mars.Xpos) / self.r_mars)
            self.ay_mars = -self.a_mars * ((self.Ypos - mars.Ypos) / self.r_mars)

        self.r_aarde = math.sqrt((self.Xpos - aarde.Xpos) ** 2 + (self.Ypos - aarde.Ypos) ** 2)
        if self.r_aarde == 0:
            self.ax_aarde = 0
            self.ay_aarde = 0
            pass
        else:
            self.a_aarde = G * M_aarde / (self.r_aarde ** 2)
            self.ax_aarde = -self.a_aarde * ((self.Xpos - aarde.Xpos) / self.r_aarde)
            self.ay_aarde = -self.a_aarde * ((self.Ypos - aarde.Ypos) / self.r_aarde)

        self.r_satelliet = math.sqrt((self.Xpos - satelliet.Xpos) ** 2 + (self.Ypos - satelliet.Ypos) ** 2)
        if self.r_satelliet == 0:
            self.ax_satelliet = 0
            self.ay_satelliet = 0
            pass
        else:
            self.a_satelliet = G * M_satelliet / (self.r_satelliet ** 2)
            self.ax_satelliet = -self.a_satelliet * ((self.Xpos - satelliet.Xpos) / self.r_satelliet)
            self.ay_satelliet = -self.a_satelliet * ((self.Ypos - satelliet.Ypos) / self.r_satelliet)

        self.ay = self.ay_zon + self.ay_mars + self.ay_aarde
        self.ax = self.ax_zon + self.ax_mars + self.ax_aarde

        self.vy = self.vy + self.ay * dt
        self.vx = self.vx + self.ax * dt

        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)

        self.Ypos = self.Ypos + self.vy * dt
        self.Xpos = self.Xpos + self.vx * dt


aarde = verplaatsing(vx_aarde1, vy_aarde1, x_aarde1, y_aarde1)
mars = verplaatsing(vx_mars1, vy_mars1, x_mars1, y_mars1)
satelliet = verplaatsing(vx_satelliet1, vy_satelliet1, x_satelliet1, y_satelliet1)
verschillendegraden = 30
debestesnelheid = 0
debestegraden = 0

for nietwhoppa  in range(100):
    print(f'Welke zitten we: {nietwhoppa}')
    verschillendegraden += 0.1
    gradenvertrekvoordesatelliet = verschillendegraden
    for aantalkerentesten in range(5000, 6000, 10):
        print(f'huidigegraden: {verschillendegraden}')
        print(f'huidigesnelheid: {aantalkerentesten}')
        print(f'debestesnelheid:{debestesnelheid}')
        print(f'min_min_afstandradiusmarssate: {min_min_afstandradiusmarssate}')
        print(f'debeste graden: {debestegraden}')

        extrasnelheidvoordesatelliet = aantalkerentesten

        if am == 5:
            print('hij is 5 keer niet verbeterd')
            print(f'debestesnelheid: {debestesnelheid}')
            print(f'min_min_afstandradiusmarssate: {min_min_afstandradiusmarssate}')
            print(f'gradenvertrekvoordesatelliet: {gradenvertrekvoordesatelliet}')

            grafiekplotten()

        if min_afstandradiusmarssate < 0:
            min_afstandradiusmarssate = min_afstandradiusmarssate * -1

        if min_min_afstandradiusmarssate > min_afstandradiusmarssate:
            min_min_afstandradiusmarssate = min_afstandradiusmarssate
            debestesnelheid = aantalkerentesten
            debestegraden = verschillendegraden
            print(f'De nieuwe beste snelheid op dit moment is: {debestesnelheid}')
            print(f'De nieuwe minste afstand tot mars op schaal: {min_min_afstandradiusmarssate / 1E8}')
            am = 0
        else:
            am += 1

        # Marsvoor
        MarsVoor = 1

        # graden waarop we moeten vertrekken
        gradenwaaropwemoetenvertrekken = 61.076772808280026

        r_satelliet_zon = math.sqrt(x_satelliet1 ** 2 + y_satelliet1 ** 2)
        r_satelliet_aarde = math.sqrt((x_satelliet1 - x_aarde1) ** 2 + (y_satelliet1 - y_aarde1) ** 2)
        r_satelliet_mars = math.sqrt((x_satelliet1 - x_mars1) ** 2 + (y_satelliet1 - y_mars1) ** 2)

        v_extra = 11011
        r_satelliet_mars_max = 9999999999999999999999
        min_afstandradiusmarssate = 999999999999999999999
        satellietaardeverschil = 0
        satellietaardeverschilmin = 99999999999999999999

        columysatelliet = []
        columxsatelliet = []
        columymars = []
        columxmars = []
        columyaarde = []
        columxaarde = []
        columysatellietlancering = []
        columxsatellietlancering = []
        columysatelliet1epos = []
        columxsatelliet1epos = []
        columtijd = []
        columsnelheidsatelliet = []
        columsatellietbuiten = []
        columxmarsnalancering = []
        columymarsnalancering = []

        gradenvertrek = 0
        marsrondjejaar = 0
        max_satellietbuiten = 0
        totaalextrav = 0
        # de = 0

        p = 0
        z = 0
        l = 0
        i = 0
        d = 0
        u = 0
        Q = 0
        j = 0
        Y = 0
        q = 0
        o = 0
        M = 0
        B = 0
        J = 0
        P = 0
        I = 0
        h = 0
        H = 0
        S = 0
        F = 0
        Z = 0
        aa = 0
        ab = 0
        ac = 0
        ad = 0
        ae = 0
        af = 0
        ag = 0
        ah = 0
        ai = 0
        aj = 0
        ak = 0
        al = 0
        am = 0
        an = 0

        aarde = verplaatsing(vx_aarde1, vy_aarde1, x_aarde1, y_aarde1)
        mars = verplaatsing(vx_mars1, vy_mars1, x_mars1, y_mars1)
        satelliet = verplaatsing(vx_satelliet1, vy_satelliet1, x_satelliet1, y_satelliet1)

        for WOPPA in range(1000000):
            satelliet.deverplaasting()
            aarde.deverplaasting()
            mars.deverplaasting()
            if satelliet.r_aarde < r_aarde:
                print('je hebt de aarde geraakt')
                grafiekplotten()

            if satelliet.r_zon < r_zon:
                print('je hebt de zon geraakt')
                break

            if satelliet.r_mars < r_mars:
                print('je hebt mars geraakt')
                break

            r_aarde_mars = math.sqrt((aarde.Xpos - mars.Xpos) ** 2 + (aarde.Ypos - mars.Ypos) ** 2)
            dehoekniettegroot = (aarde.r_zon ** 2 + mars.r_zon ** 2 - r_aarde_mars ** 2) / (
                        2 * aarde.r_zon * mars.r_zon)

            if dehoekniettegroot > 1:
                dehoekniettegroot = 1

            if dehoekniettegroot < -1:
                dehoekniettegroot = -1

            hoekaardemars = math.acos(dehoekniettegroot)
            hoekaardemars = (hoekaardemars * 180) / math.pi

            dehoekniettegroot2 = (satelliet.r_aarde ** 2 + aarde.r_zon ** 2 - satelliet.r_zon ** 2) / (
                    2 * aarde.r_zon * satelliet.r_aarde)

            if dehoekniettegroot2 >= 1:
                dehoekniettegroot2 = 1

            if dehoekniettegroot2 <= -1:
                dehoekniettegroot2 = -1

            hoekaardesatelliet = math.acos(dehoekniettegroot2)

            hoekaardesatelliet = (hoekaardesatelliet * 180 / math.pi)

            if r_satelliet_mars < r_satelliet_mars_max and i > 0:
                r_satelliet_mars_max = r_satelliet_mars

            afstandradiusmarssate = satelliet.r_mars

            if i > 0:
                if afstandradiusmarssate < min_afstandradiusmarssate:
                    min_afstandradiusmarssate = afstandradiusmarssate

            satellietaardeverschil = aarde.v - satelliet.v
            satellietbuiten = satelliet.r_zon - aarde.r_zon

            # rondje aarde
            if aarde.vy > -20 and aarde.vy < 20 and aarde.vx > 0:
                x_aarde_checkpoint1 = aarde.Xpos
                y_aarde_checkpoint1 = aarde.Ypos
                F += 1

            if F > 30 and I == 0:
                x_aarde_checkpoint2 = aarde.Xpos
                y_aarde_checkpoint2 = aarde.Ypos
                Z = 1

            # rondje satelliet
            if satelliet.vy > -20 and satelliet.vy < 20 and satelliet.vx > 0:
                x_satelliet_checkpoint1 = satelliet.Xpos
                y_satelliet_checkpoint1 = satelliet.Ypos
                aa += 1

            if aa > 30 and I == 0:
                x_satelliet_checkpoint2 = satelliet.Xpos
                y_satelliet_checkpoint2 = satelliet.Ypos
                ab = 1

                # duratierondjemars
            if mars.vx > -20 and mars.vx < 20 and mars.vy > 0 and ak == 1:
                x_mars_checkpoint1 = mars.Xpos
                y_mars_checkpoint1 = mars.Ypos
                J += 1

            # Ligt Mars voor?
            if hoekaardemars < 0.1:
                MarsVoor = 0

            if hoekaardemars > 179.9:
                MarsVoor = 1

            if i > 0:
                satelliet.ay_aarde = 0
                satelliet.ax_aarde = 0


            if hoekaardemars > (gradenvertrekvoordesatelliet - 1.9) and hoekaardemars < (gradenvertrekvoordesatelliet + 1.9) and S == 0:
                if MarsVoor == 1 and satellietbuiten > 0:
                    if satellietaardeverschil < 1000 and satellietaardeverschil > -1000 and satellietaardeverschil < satellietaardeverschilmin:
                        satellietaardeverschilmin = satellietaardeverschil
                        print(f'satellietaardeverschilmin : {satellietaardeverschilmin}')
                        print(f'satellietbuiten : {satellietbuiten}')
                        if MarsVoor == 1 and satellietaardeverschilmin < 100 and satellietbuiten > 0:
                            xpos1 = satelliet.Xpos
                            ypos1 = satelliet.Ypos
                            S = 1
                            print(f'satellietaardeverschil : {satellietaardeverschil}')
                            print(f'aarde.v : {aarde.v / 10}')

            # if satellietbuiten > 0:




            if hoekaardemars > (gradenvertrekvoordesatelliet - 1.9) and hoekaardemars < (gradenvertrekvoordesatelliet + 1.9) and i == 0 and S == 1:
                if MarsVoor == 1 and satellietbuiten > 0:
                    if satellietaardeverschil < 1000 and satellietaardeverschil > -1000 and satellietaardeverschil < satellietaardeverschilmin:
                        satellietaardeverschilmin = satellietaardeverschil
                        print(f'satellietaardeverschilmin : {satellietaardeverschilmin}')
                        print(f'satellietbuiten : {satellietbuiten}')
                        if MarsVoor == 1 and satellietaardeverschilmin < 60 and satellietbuiten > 0:
                            extrav = extrasnelheidvoordesatelliet
                            print(f'extrav: {extrav}')
                            xpos2 = satelliet.Xpos
                            ypos2 = satelliet.Ypos

                            xverander = xpos2 - xpos1
                            yverander = ypos2 - ypos1
                            # print(f'xverander: {xverander}')

                            totverander = math.sqrt(xverander ** 2 + yverander ** 2)

                            # print(f'totverander: {totverander}')
                            # print("iets")
                            verhoudingx = xverander / totverander
                            verhoudingy = yverander / totverander

                            # print(f'verhoudingx: {verhoudingx}')
                            # print(f'verhoudingy: {verhoudingy}')

                            extravx = (extrav * verhoudingx)
                            extravy = (extrav * verhoudingy)
                            # print(f'extravy: {extravy}')
                            # print(f'extravx: {extravx}')

                            # print(f'vx_satelliet: {vx_satelliet}')
                            satelliet.vx = aarde.vx + extravx
                            satelliet.vy = aarde.vy + extravy
                            # print(f'vx_satelliet: {vx_satelliet}')
                            aardexlanceering = aarde.Xpos / schaal
                            aardeylanceering = aarde.Ypos / schaal

                            satellietxlanceering = satelliet.Xpos / schaal
                            satellietylanceering = satelliet.Ypos / schaal
                            grafiekplotten()
                            dt = 3.6

                            i += 1
                        q += 1

            if i == 1:
                an += 1
                print(an)

            if z == 0 and satelliet.r_mars < 1.1E8:
                xpos3 = mars.Xpos
                ypos3 = mars.Ypos
                z = z + 1


            v_extra2 = mars.v - 2500

            if l == 0 and satelliet.ax_mars < -0.2:
                xpos4 = mars.Xpos
                ypos4 = mars.Ypos
                xverander2 = xpos4 - xpos3
                yverander2 = ypos4 - ypos3

                totverander2 = math.sqrt(xverander2 ** 2 + yverander2 ** 2)

                verhoudingx2 = xverander2 / totverander2
                verhoudingy2 = yverander2 / totverander2

                extravx2 = v_extra2 * verhoudingx2
                extravy2 = v_extra2 * verhoudingy2

                vx_satelliet = extravx2
                vy_satelliet = extravy2

                l = l + 1

            if satelliet.r_mars < 8E8:
                j = j + 1

            if satelliet.r_mars < 1E9:
                if j < 10000:
                    dt = 10
                else:
                    dt = 360

            if i == 1 and Q == 0:
                Tijd1 = t
                Q = Q + 1

            if l == 1 and Y == 0:
                Tijd2 = t
                Reistijd_seconden = Tijd2 - Tijd1
                Reistijd_minuten = Reistijd_seconden / 60
                Reistijd_uur = Reistijd_minuten / 60
                Reistijd_dagen = Reistijd_uur / 24
                Reistijd_weken = Reistijd_dagen / 7
                Reistijd_maanden = Reistijd_dagen / 30
                Reistijd_jaren = Reistijd_dagen / 365
                Y = Y + 1
                print(Reistijd_dagen, Reistijd_maanden)

                grafiekplotten()

            if hoekaardemars < 46 and hoekaardemars > 42 and u == 1 and d == 0:
                dt = 1

            if d == 1:
                dt = 360

            t = t + dt

            # grafiek shit
            if S > 0:
                if i == 0:
                    columysatelliet1epos.insert(ad, (satelliet.Ypos / schaal))
                    columxsatelliet1epos.insert(ad, (satelliet.Xpos / schaal))
                    ad += 1
                else:
                    columysatellietlancering.insert(ac, satelliet.Ypos / schaal)
                    columxsatellietlancering.insert(ac, satelliet.Xpos / schaal)
                    ac += 1

            B += 1
            if B == 50:

                columtijd.insert(o, t)
                columsnelheidsatelliet.insert(o, satelliet.v)
                columsatellietbuiten.insert(o, satellietbuiten)
                ag += 1
                if ag == 10:
                    columxsatelliet.insert(af, satelliet.Xpos / schaal)
                    columysatelliet.insert(af, satelliet.Ypos / schaal)
                    af += 1
                    ag = 0


                if i > 0:
                    columxmarsnalancering.insert(o, mars.Xpos / schaal)
                    columymarsnalancering.insert(o, mars.Ypos / schaal)

                if I == 0:
                    columymars.insert(o, (mars.Ypos / schaal))
                    columxmars.insert(o, (mars.Xpos / schaal))

                if Z == 0:
                    columyaarde.insert(o, (aarde.Ypos / schaal))
                    columxaarde.insert(o, (aarde.Xpos / schaal))

                o += 1
                B = 0

            if keyboard.is_pressed('Up') == 1:
                print("grafiekkenren")
                print(f'hoe ver we zijn in het model {WOPPA}')
                grafiekplotten()
