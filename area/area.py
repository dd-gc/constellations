#!/usr/bin/env python

# Copyright 2026 Golden Communications LLC.  Mason, Ohio
# MIT License

from math import pi, sin


def get_constdict(boundary_filename):
    constdict = {}

    with open(boundary_filename, 'r') as fi:
        for line in fi.readlines():
            fields = line.split()
            constname = fields[2]
            if constname not in constdict:
                constdict[constname] = []
            ra = float(fields[0]) * pi / 12.0
            dec = float(fields[1]) * pi / 180.0
            constdict[constname].append((ra, dec))

    return constdict


def integrate_constpoints(constpoints):
    A = 0.0

    for i in range(1, len(constpoints)):
        ra1, dec1 = constpoints[i-1]
        ra2, dec2 = constpoints[i]
        if dec1 == dec2:
            if abs(ra1 - ra2) > pi:
                if ra1 > ra2:
                    ra1 -= 2 * pi
                else:
                    ra2 -= 2 * pi
            A += sin(dec1) * (ra2 - ra1)
        elif ra1 == ra2:
            pass
        else:
            raise ValueError('Invalid path')

    return A


if __name__ == '__main__':

    boundary_filename = '../VI_49/constbnd.dat'

    constdict = get_constdict(boundary_filename)
    areadict = {}

    for constname in constdict.keys():
        constpoints = constdict[constname]
        A = integrate_constpoints(constpoints)
        if constname == 'Oct' or constname == 'UMi':
            A += 2 * pi
        areadict[constname] = A

    areadict['Ser'] = areadict.pop('Ser1') + areadict.pop('Ser2')

    L = sorted([(area, name) for (name, area) in areadict.items()], reverse=True)

    A_total = 0.0

    for i, (A, name) in enumerate(L):
        print(f'{i+1:2}  {name} {A:21.18f} {A/4/pi:21.18f}')
        A_total += A

    print('='*51)
    print(f'Total   {A_total:21.18f} {A_total/4/pi:21.18f}')
