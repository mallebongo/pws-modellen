import math
import matplotlib.pyplot as plt
import keyboard
import numpy as np
import csv

x_satelliet_plot3 = []
y_satelliet_plot3 = []

fieldnames1 = ["x_satelliet_plot", "y_satelliet_plot",  "columxaarde", "columyaarde", "columxmars", "columymars"]
fieldnames2 = ["columxaarde","columyaarde", "columxmars", "columymars"]

with open('data_Planeten.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames1)
    csv_writer.writeheader()

def Model50satellieten(Gradenvertrek):
    t = 0
    dt = 180

    # massa's planeten

    M_zon = 1.99e30
    M_aarde = 8.972e24
    M_mars = 0.642e24
    M_satelliet = 1000

    #radius planeten
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
    gradenwaaropwemoetenvertrekken = Gradenvertrek

    x_satelliet1 = 0  # in meters
    y_satelliet1 = -149.58 * 10 ** 9  # in meters
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

    schaal = 1E9

    columymars = []
    columxmars = []
    columyaarde = []
    columxaarde = []

    gelanceerd = 0

    i = 0
    q = 0
    I = 0
    S = 0

    x_satelliet_plot1 = []
    y_satelliet_plot1 = []
    x_satelliet_plot2 = []
    y_satelliet_plot2 = []


    def grafiekplotten():
        plt.figure(figsize=(5, 5))
        hoeveelheidsatellietenover = 0

        x_satelliet_plot1 = []
        y_satelliet_plot1 = []
        x_satelliet_plot2 = []
        y_satelliet_plot2 = []

        for i in range(aantalsatellieten):
            if satellieten[i, 5, 0] == 1:
                for Satelliet_schaal in range(27000, WOPPA, 1000):
                    x_satelliet_plot1.append(satellieten[i, 2, Satelliet_schaal] / schaal)
                    y_satelliet_plot1.append(satellieten[i, 3, Satelliet_schaal] / schaal)
                hoeveelheidsatellietenover += 1

        if satellieten[int(aantalsatellieten / 2), 5, 0] == 1:
            for Satelliet_schaal in range(0, WOPPA, 1000):
                x_satelliet_plot2.append(satellieten[int(aantalsatellieten / 2), 2, Satelliet_schaal] / schaal)
                y_satelliet_plot2.append(satellieten[int(aantalsatellieten / 2), 3, Satelliet_schaal] / schaal)
        print(f'De hoeveelheid satellieten die over blijven en worden geplot:{hoeveelheidsatellietenover}')

        plt.plot(x_satelliet_plot1, y_satelliet_plot1, color='c', markersize=2)
        plt.plot(x_satelliet_plot2, y_satelliet_plot2, color='m', markersize=2)
        plt.plot(columxaarde, columyaarde, color='b', markersize=2.5)
        plt.plot(columxmars, columymars, color='r', markersize=2.5)
        plt.plot(0, 0, color='y', markersize=20)
        plt.axis([-500, 500, -500, 500])
        plt.show()
        plt.close()


    def Opslaanwaardes_Planeten():
        with open('data_Planeten.csv','a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames1)
            Data = {
                "x_satelliet_plot": satellieten[:,2,WOPPA],
                "y_satelliet_plot": satellieten[:,3,WOPPA],
                "columxaarde":aarde.Xpos / schaal,
                "columyaarde":aarde.Ypos / schaal,
                "columxmars":mars.Ypos / schaal,
                "columymars":mars.Xpos / schaal
            }
            csv_writer.writerow(Data)

    def VerplaatsingVanSatelliet(Vx,Vy,X,Y,MinimaleAfstandTotMars,WOPPA):

        r_satelliet_mars = np.sqrt(np.square(X - mars.Xpos) + np.square(Y ** 2 - mars.Ypos))
        r_satelliet_aarde = np.sqrt(np.square(X - aarde.Xpos) + np.square(Y - aarde.Ypos))
        r_satelliet_zon = np.sqrt(np.square(X) + np.square(Y))

        for i in range(aantalsatellieten):
            if r_satelliet_aarde[i] < r_aarde and satellieten[i, 5, 0] == 1:
                print(f'je hebt de aarde geraakt. Satelliet {i},{WOPPA} heeft aarde geraakt')
                satellieten[i, 5, :] = 0

            if r_satelliet_zon[i] < r_zon and satellieten[i, 5, 0] == 1:
                print(f'je hebt de zon geraakt. Satelliet {i},{WOPPA} heeft de zon geraakt')
                satellieten[i, 5, :] = 0

            if r_satelliet_mars[i] < r_mars and satellieten[i, 5, 0] == 1:
                print(f'je hebt de mars geraakt. Satelliet {i},{WOPPA} heeft mars geraakt')
                satellieten[i, 5, :] = 2
                print('grafiekeren')
                grafiekplotten()

            if r_satelliet_mars[i] < MinimaleAfstandTotMars[i]:
                MinimaleAfstandTotMars[i] = r_satelliet_mars[i]
                if MinimaleAfstandTotMars[i] < 9E9:
                    satellieten[i, 5, :] = 2


        a_zon = G * M_zon / np.square(r_satelliet_zon)
        ax_zon = -a_zon * (X / r_satelliet_zon)
        ay_zon = -a_zon * (Y / r_satelliet_zon)

        a_mars = G * M_mars / np.square(r_satelliet_mars)
        ax_mars = -a_mars * ((X - mars.Xpos) / r_satelliet_mars)
        ay_mars = -a_mars * ((Y - mars.Ypos) / r_satelliet_mars)

        a_aarde = G * M_aarde / np.square(r_satelliet_aarde)
        ax_aarde = -a_aarde * ((X - aarde.Xpos) / r_satelliet_aarde)
        ay_aarde = -a_aarde * ((Y - aarde.Ypos) / r_satelliet_aarde)

        Ay = ay_zon + ay_mars + ay_aarde
        Ax = ax_zon + ax_mars + ax_aarde

        Vy = Vy + Ay * dt
        Vx = Vx + Ax * dt

        Y = Y + Vy * dt
        X = X + Vx * dt

        satellieten[:,0,WOPPA + 1] = Vx
        satellieten[:,1,WOPPA + 1] = Vy
        satellieten[:,2,WOPPA + 1] = X
        satellieten[:,3,WOPPA + 1] = Y
        satellieten[:,4,WOPPA + 1] = MinimaleAfstandTotMars

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


            self.ay = self.ay_zon + self.ay_mars + self.ay_aarde
            self.ax = self.ax_zon + self.ax_mars + self.ax_aarde

            self.vy = self.vy + self.ay * dt
            self.vx = self.vx + self.ax * dt

            self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)

            self.Ypos = self.Ypos + self.vy * dt
            self.Xpos = self.Xpos + self.vx * dt


    aarde = verplaatsing(vx_aarde1, vy_aarde1, x_aarde1, y_aarde1)
    mars = verplaatsing(vx_mars1, vy_mars1, x_mars1, y_mars1)

    WOPPA_range = 200000

    aantalsatellieten = 50

    satellieten = np.zeros((aantalsatellieten,6,WOPPA_range+1))

    #for i in range(int(aantalsatellieten/-2),int(aantalsatellieten/2),1):

    satellieten[:,0,0] = vx_satelliet1
    satellieten[:,1,0] = vy_satelliet1
    satellieten[:,2,0] = x_satelliet1
    satellieten[:,3,0] = y_satelliet1
    satellieten[:,4,0] = 9**99 #Grote afstand voor de eerste meting
    satellieten[:,5,:] = 1


    for WOPPA in range(WOPPA_range):

        aarde.deverplaasting()
        mars.deverplaasting()
        #VerplaatsingVanSatelliet is een functie daar moet (Vx,Vy,X,Y,Welkesatelliet we zijn, MinimaleAfstandTotMars)
        VerplaatsingVanSatelliet(satellieten[:, 0, WOPPA], satellieten[:, 1, WOPPA], satellieten[:, 2, WOPPA],
                             satellieten[:, 3, WOPPA], satellieten[:, 4, WOPPA], WOPPA)

        r_aarde_mars = math.sqrt((aarde.Xpos - mars.Xpos) ** 2 + (aarde.Ypos - mars.Ypos) ** 2)
        dehoekniettegroot = (aarde.r_zon ** 2 + mars.r_zon ** 2 - r_aarde_mars ** 2) / (
                    2 * aarde.r_zon * mars.r_zon)

        if dehoekniettegroot > 1:
            dehoekniettegroot = 1

        if dehoekniettegroot < -1:
            dehoekniettegroot = -1

        hoekaardemars = math.acos(dehoekniettegroot)
        hoekaardemars = (hoekaardemars * 180) / math.pi

        satellietbuiten = np.sqrt(satellieten[0][2][WOPPA]**2+satellieten[0][3][WOPPA]**2) - aarde.r_zon

        # Ligt Mars voor?
        if hoekaardemars < 0.1:
            MarsVoor = 0

        if hoekaardemars > 179.9:
            MarsVoor = 1

        if aarde.vx > 0 and satellieten[0, 0, WOPPA] < (aarde.vx + (aarde.vx / 5)) and satellieten[0, 0, WOPPA] > (
                aarde.vx - (aarde.vx / 5)) or aarde.vx < 0 and satellieten[0, 0, WOPPA] > (aarde.vx + (aarde.vx / 5)) and satellieten[0, 0, WOPPA] < (
                aarde.vx - (aarde.vx / 5)):
            spdcheck = 1
        else:
            spdcheck = 0


        if hoekaardemars > (gradenwaaropwemoetenvertrekken + 1.9) and hoekaardemars < (
                gradenwaaropwemoetenvertrekken + 2.1) and S == 0 and MarsVoor == 1:
            xpos1 = aarde.Xpos
            ypos1 = aarde.Ypos
            S = 1
            print("deze doet het 1")

        if hoekaardemars > (gradenwaaropwemoetenvertrekken - 1.9) and hoekaardemars < (
                gradenwaaropwemoetenvertrekken + 1.9):
            if gelanceerd == 0 and S == 1:
                if MarsVoor == 1 and satellietbuiten > 0:
                    if spdcheck == 1:
                        if satellieten[0, 1, WOPPA] < (aarde.vy + (aarde.vy / 5)) and satellieten[0, 1, WOPPA] > (
                                aarde.vy - (aarde.vy / 5)):
                            print('de satelliet word nu gelanceerd')
                            extrav = 2500

                            xpos2 = aarde.Xpos
                            ypos2 = aarde.Ypos

                            xverander = xpos2 - xpos1
                            yverander = ypos2 - ypos1

                            totverander = np.sqrt(xverander ** 2 + yverander ** 2)

                            verhoudingx = xverander / totverander
                            verhoudingy = yverander / totverander

                            extravx = (extrav * verhoudingx)
                            extravy = (extrav * verhoudingy)
                            print(extravx, extravy, verhoudingx, verhoudingy)
                            for i in range(aantalsatellieten):
                                satellieten[i][0][WOPPA + 1] = satellieten[i][0][WOPPA] + extravx * (
                                    i) / 10000 + 5700 * verhoudingx
                                satellieten[i][1][WOPPA + 1] = satellieten[i][1][WOPPA] + extravy * (
                                    i) / 10000 + 5700 * verhoudingy
                            i = 0

                            gelanceerd += 1


        q += 1
        t = t + dt


        # grafiek shit

        if WOPPA%1000 == 0:
            Opslaanwaardes_Planeten()

            columymars.append(mars.Ypos / schaal)
            columxmars.append(mars.Xpos / schaal)

            columyaarde.append(aarde.Ypos / schaal)
            columxaarde.append(aarde.Xpos / schaal)


        if keyboard.is_pressed('Up') == 1:
            print("grafiekkenren")
            print(f'hoe ver we zijn in het model {WOPPA}')
            grafiekplotten()

        if keyboard.is_pressed("Down") == 1:
            print(WOPPA)



    print(f'Minimaale afstand tot mars van elke satelliet: {satellieten[:, 4, WOPPA]}')
    for i in range(0, aantalsatellieten, 100):
        if satellieten[i, 5, 0] == 2:
            for Satelliet_schaal in range(0, WOPPA, 100):
                x_satelliet_plot3.append(satellieten[i, 2, Satelliet_schaal] / schaal)
                y_satelliet_plot3.append(satellieten[i, 3, Satelliet_schaal] / schaal)

    if keyboard.is_pressed("Down"):
        grafiekplotten()


for Graden in np.arange(26,100,1):
    print(Graden)
    Model50satellieten(Graden)


plt.figure(figsize=(5, 5))
plt.plot([x_satelliet_plot3], [y_satelliet_plot3], 'ro', color='g', markersize=2)
plt.plot([0], [0], 'ro', color='y', markersize=20)
plt.axis([-500, 500, -500, 500])
plt.show()
