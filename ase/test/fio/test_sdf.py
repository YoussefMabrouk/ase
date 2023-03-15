import io

from ase.io.sdf import read_sdf

DIFFICULT_BUT_VALID_SDF_V2000 = '''
     RDKit          3D

184192  0  0  0  0  0  0  0  0999 V2000
    4.9469    0.9605    0.9541 O   0  0  0  0  0  0  0  0  0  0  0  0
    5.8889    7.9815    7.1892 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.5120   13.0815   15.3326 O   0  0  0  0  0  0  0  0  0  0  0  0
    0.5700    6.0605    9.0974 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.4589    3.5533    4.6848 O   0  0  0  0  0  0  0  0  0  0  0  0
    6.3769   10.5743    3.4585 O   0  0  0  0  0  0  0  0  0  0  0  0
    2.0000   10.4887   11.6018 O   0  0  0  0  0  0  0  0  0  0  0  0
    0.0820    3.4677   12.8282 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.7251    2.2946    2.8055 N   0  0  0  0  0  0  0  0  0  0  0  0
    6.1106    9.3156    5.3378 N   0  0  0  0  0  0  0  0  0  0  0  0
    1.7337   11.7474   13.4811 N   0  0  0  0  0  0  0  0  0  0  0  0
    0.3483    4.7264   10.9488 N   0  0  0  0  0  0  0  0  0  0  0  0
    3.7595    4.4583    2.7243 N   0  0  0  0  0  0  0  0  0  0  0  0
    7.0762   11.4793    5.4191 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.6993    9.5837   13.5624 N   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6173    2.5627   10.8676 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.9276    5.0943    0.5186 N   0  0  0  0  0  0  0  0  0  0  0  0
    7.9081   12.1153    7.6247 N   0  0  0  0  0  0  0  0  0  0  0  0
    3.5312    8.9477   15.7681 N   0  0  0  0  0  0  0  0  0  0  0  0
   -1.4492    1.9267    8.6619 N   0  0  0  0  0  0  0  0  0  0  0  0
    3.5364    3.2458   -0.5546 N   0  0  0  0  0  0  0  0  0  0  0  0
    7.2993   10.2668    8.6979 N   0  0  0  0  0  0  0  0  0  0  0  0
    2.9224   10.7962   16.8412 N   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8404    3.7752    7.5888 N   0  0  0  0  0  0  0  0  0  0  0  0
    5.2860    1.2188    3.6335 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.5498    8.2398    4.5098 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.1729   12.8232   12.6531 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.9091    5.8022   11.7769 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.2288    1.3593    3.7459 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.6069    8.3803    4.3974 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.2300   12.6827   12.5407 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8520    5.6617   11.8892 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.1384    0.3735    3.2020 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.6974    7.3945    4.9414 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.3205   13.6685   13.0847 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.7615    6.6475   11.3453 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.8566    1.2188    4.4919 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.9791    8.2398    3.6515 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.6023   12.8232   11.7948 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.4797    5.8022   12.6352 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.3185    3.4445    3.4928 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.5173   10.4655    4.6505 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.1404   10.5975   12.7938 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0584    3.5765   11.6361 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.2679    5.6786    3.3648 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.5678   12.6996    4.7785 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.1909    8.3634   12.9218 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1089    1.3424   11.5081 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.5936    6.4439    2.8876 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.2421   13.4649    5.2557 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.8652    7.5981   13.3990 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7832    0.5771   11.0309 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.5798    5.7109    4.2720 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.2560   12.7319    3.8713 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.8791    8.3311   12.0146 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7971    1.3101   12.4153 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.3078    5.6800    3.3567 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.5279   12.7010    4.7866 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.1510    8.3620   12.9300 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0691    1.3410   11.5000 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.5373    4.2421    1.3873 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.2984   11.2631    6.7560 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9215    9.7999   14.8993 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8396    2.7789    9.5306 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9367    4.4359   -0.6363 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.8990   11.4569    8.7796 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.5221    9.6061   16.9229 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.4401    2.5851    7.5070 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5637    4.7687   -1.4202 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.2720   11.7897    9.5635 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.8951    9.2733   17.7068 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.8131    2.2523    6.7231 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.7167    2.2551   -1.6238 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.1190    9.2761    9.7671 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.7421   11.7869   17.9104 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6601    4.7659    6.5195 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.2222    2.5290   -2.3990 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.6135    9.5500   10.5423 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.2367   11.5130   18.6856 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1547    4.4920    5.7443 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.3967    1.4014   -1.3241 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.4390    8.4224    9.4674 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.0622   12.6406   17.6107 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.9802    5.6196    6.8192 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.6480    2.1891   -1.8436 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.1877    9.2101    9.9870 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8108   11.8529   18.1303 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.2712    4.8319    6.2997 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.9367    3.0977    0.7599 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.8990   10.1187    7.3834 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5221   10.9443   15.5267 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.4401    3.9233    8.9032 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.5686    2.0108    1.4326 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.2671    9.0318    6.7107 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8903   12.0312   14.8541 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1917    5.0102    9.5759 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.6042    7.4862   16.9467 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.4778    0.4652    7.4832 O   0  0  0  0  0  0  0  0  0  0  0  0
    5.8547    6.5558   -0.6601 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.9811   13.5768    8.8034 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.0604    6.7261   16.9055 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.0216   -0.2949    7.5244 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.3984    7.3159   -0.6189 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.4373   14.3369    8.7622 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.4474    7.0975   14.7568 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.6346    0.0765    9.6731 O   0  0  0  0  0  0  0  0  0  0  0  0
    6.0115    6.9445    1.5298 O   0  0  0  0  0  0  0  0  0  0  0  0
    4.8242   13.9655    6.6135 O   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7659    8.7484   13.2466 O   0  0  0  0  0  0  0  0  0  0  0  0
    2.8479    1.7274   11.1834 O   0  0  0  0  0  0  0  0  0  0  0  0
    7.2248    5.2936    3.0401 O   0  0  0  0  0  0  0  0  0  0  0  0
    3.6109   12.3146    5.1033 O   0  0  0  0  0  0  0  0  0  0  0  0
   -0.3245    8.0461   13.5668 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.4065    1.0251   10.8632 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.7834    5.9959    2.7199 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.0524   13.0169    5.4234 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.2313    7.8284   15.7296 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8507    0.8074    8.7003 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.2276    6.2136    0.5570 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.6081   13.2346    7.5863 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.4232    9.1301   15.5936 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5052    2.1091    8.8363 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.8820    4.9119    0.6930 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.9537   11.9329    7.4503 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8840    9.5205   14.3501 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9660    2.4995   10.0798 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.3428    4.5215    1.9365 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.4929   11.5425    6.2068 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5258   10.7913   14.1645 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.6078    3.7703   10.2655 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.9847    3.2507    2.1221 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8511   10.2717    6.0212 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0178   11.2055   12.9104 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.0998    4.1845   11.5195 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.4767    2.8365    3.3762 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.3591    9.8575    4.7671 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.9303   10.6410   12.1759 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.0123    3.6200   12.2541 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.3892    3.4010    4.1107 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.4466   10.4220    4.0326 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.6175   12.4173   12.7524 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.6995    5.3963   11.6775 C   0  0  0  0  0  0  0  0  0  0  0  0
    9.0763    1.6247    3.5342 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.7594    8.6457    4.6091 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.9375   12.6757   11.9186 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.0195    5.6547   12.5114 H   0  0  0  0  0  0  0  0  0  0  0  0
    9.3964    1.3663    4.3681 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.4394    8.3873    3.7752 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.7514   13.2753   13.8550 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.8334    6.2543   10.5749 C   0  0  0  0  0  0  0  0  0  0  0  0
    9.2103    0.7667    2.4316 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6254    7.7877    5.7117 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.1597   14.1038   13.7443 H   0  0  0  0  0  0  0  0  0  0  0  0
    5.2417    7.0828   10.6857 H   0  0  0  0  0  0  0  0  0  0  0  0
    9.6186   -0.0618    2.5423 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.2172    6.9592    5.6010 H   0  0  0  0  0  0  0  0  0  0  0  0
   -2.2922   12.9102   15.0879 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3742    5.8892    9.3420 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.7510    1.1318    1.1987 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.0847    8.1528    6.9446 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.3898   13.4958   15.8045 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.4718    6.4748    8.6254 H   0  0  0  0  0  0  0  0  0  0  0  0
    8.8487    0.5462    0.4821 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.9871    7.5672    7.6612 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6631   11.6408   15.2931 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.7451    4.6198    9.1368 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.1220    2.4012    0.9935 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.7137    9.4222    7.1498 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.2004   11.2139   16.5635 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.2824    4.1929    7.8664 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.6593    2.8281   -0.2769 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.1765    9.8491    8.4202 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.3003   11.7714   17.3013 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.3823    4.7504    7.1287 H   0  0  0  0  0  0  0  0  0  0  0  0
    7.7592    2.2706   -1.0147 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.0766    9.2916    9.1580 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6138   10.0007   16.7117 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.6958    2.9797    7.7182 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.0726    4.0413   -0.4251 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.7631   11.0623    8.5684 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.3317    9.7297   17.5554 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.4137    2.7087    6.8746 H   0  0  0  0  0  0  0  0  0  0  0  0
    6.7905    4.3123   -1.2687 H   0  0  0  0  0  0  0  0  0  0  0  0
    4.0452   11.3333    9.4120 H   0  0  0  0  0  0  0  0  0  0  0  0
  1 93  2  0
  2 94  2  0
  3 95  2  0
  4 96  2  0
  5 41  2  0
  6 42  2  0
  7 43  2  0
  8 44  2  0
  9 25  1  0
  9 41  1  0
  9 93  1  0
 10 26  1  0
 10 42  1  0
 10 94  1  0
 11 27  1  0
 11 43  1  0
 11 95  1  0
 12 28  1  0
 12 44  1  0
 12 96  1  0
 13 41  1  0
 13 45  1  0
 13 61  1  0
 14 42  1  0
 14 46  1  0
 14 62  1  0
 15 43  1  0
 15 47  1  0
 15 63  1  0
 16 44  1  0
 16 48  1  0
 16 64  1  0
 17 61  1  0
 17 65  2  0
 18 62  1  0
 18 66  2  0
 19 63  1  0
 19 67  2  0
 20 64  1  0
 20 68  2  0
 21 65  1  0
 21 73  1  0
 21 89  1  0
 22 66  1  0
 22 74  1  0
 22 90  1  0
 23 67  1  0
 23 75  1  0
 23 91  1  0
 24 68  1  0
 24 76  1  0
 24 92  1  0
 25 29  1  0
 25 33  1  0
 25 37  1  0
 26 30  1  0
 26 34  1  0
 26 38  1  0
 27 31  1  0
 27 35  1  0
 27 39  1  0
 28 32  1  0
 28 36  1  0
 28 40  1  0
 45 49  1  0
 45 53  1  0
 45 57  1  0
 46 50  1  0
 46 54  1  0
 46 58  1  0
 47 51  1  0
 47 55  1  0
 47 59  1  0
 48 52  1  0
 48 56  1  0
 48 60  1  0
 61 89  2  0
 62 90  2  0
 63 91  2  0
 64 92  2  0
 65 69  1  0
 66 70  1  0
 67 71  1  0
 68 72  1  0
 73 77  1  0
 73 81  1  0
 73 85  1  0
 74 78  1  0
 74 82  1  0
 74 86  1  0
 75 79  1  0
 75 83  1  0
 75 87  1  0
 76 80  1  0
 76 84  1  0
 76 88  1  0
 89 93  1  0
 90 94  1  0
 91 95  1  0
 92 96  1  0
 97101  1  0
 97117  1  0
 98102  1  0
 98118  1  0
 99103  1  0
 99119  1  0
100104  1  0
100120  1  0
105117  2  0
106118  2  0
107119  2  0
108120  2  0
109113  1  0
109125  1  0
110114  1  0
110126  1  0
111115  1  0
111127  1  0
112116  1  0
112128  1  0
117121  1  0
118122  1  0
119123  1  0
120124  1  0
121125  2  0
121177  1  0
122126  2  0
122178  1  0
123127  2  0
123179  1  0
124128  2  0
124180  1  0
125129  1  0
126130  1  0
127131  1  0
128132  1  0
129133  2  0
129165  1  0
130134  2  0
130166  1  0
131135  2  0
131167  1  0
132136  2  0
132168  1  0
133137  1  0
133141  1  0
134138  1  0
134142  1  0
135139  1  0
135143  1  0
136140  1  0
136144  1  0
141145  1  0
141149  2  0
142146  1  0
142150  2  0
143147  1  0
143151  2  0
144148  1  0
144152  2  0
149153  1  0
149157  1  0
150154  1  0
150158  1  0
151155  1  0
151159  1  0
152156  1  0
152160  1  0
157161  1  0
157165  2  0
158162  1  0
158166  2  0
159163  1  0
159167  2  0
160164  1  0
160168  2  0
165169  1  0
166170  1  0
167171  1  0
168172  1  0
169173  1  0
169177  2  0
170174  1  0
170178  2  0
171175  1  0
171179  2  0
172176  1  0
172180  2  0
177181  1  0
178182  1  0
179183  1  0
180184  1  0
M  END
$$$$
'''

def test_read_sdf() -> None:
    """Test SDF V2000 reader."""
    with io.StringIO(DIFFICULT_BUT_VALID_SDF_V2000) as file_obj:
        atoms = read_sdf(file_obj)

    assert len(atoms) == 184
