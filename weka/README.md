# Weka part
These are the solutions for the weka part of the Data-Science training

## task 1
```
instances: 27
attributes: 3
```

## task 2
```
possible class values: {0<x<500,0<=x<=120,(low,medium,high,very_high)}
```

## task 3
```
-1,25,high
möglicherweise 60,120,low
```

## task 4
```
weight of -1 is impossible
Der Alterswert ist nicht sicher corrupted, da er < dem des bekanntesten ältesten Menschen ist
```

## task 5
```
97.1 %
```

## task 6
```
61
```

## task 7
```
93
```

## task 8
```
93 %
```

## task 9
```
j48 mit percentage-split,
da die Klassifikation korrekter ist
```

## task 10
```
b und c werden nicht korrekt angezeigt

ich vermute es ist 'c'
```

## task 11
```
nein, da ich mir zuvor keine Gedanken darüber gemacht habe
```

## task 12
```
80.6 %
```

## task 13
```
5,5
```

## task 14
```
Meine Vermutung ist, dass es auf Grund der Abweichung von ca. 5% keinen großen (/relevanten) Unterschied macht.
```

## task 15
```java
package weka;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
 
import weka.clusterers.SimpleKMeans;
import weka.core.Instances;
 
public class main {
 
	public static BufferedReader readDataFile(String filename) {
		BufferedReader inputReader = null;
 
		try {
			inputReader = new BufferedReader(new FileReader(filename));
		} catch (FileNotFoundException ex) {
			System.err.println("File not found: " + filename);
		}
 
		return inputReader;
	}
 
	public static void main(String[] args) throws Exception {
		SimpleKMeans kmeans = new SimpleKMeans();

		kmeans.setSeed(10);

		//important parameter to set: preserver order, number of cluster.
		kmeans.setPreserveInstancesOrder(true);
		kmeans.setNumClusters(6);

		BufferedReader datafile = readDataFile("/nfs/home/shared/Datascience_files/wekauebung/bank.arff"); 
		Instances data = new Instances(datafile);
		BufferedReader datafile_test = readDataFile("/nfs/home/shared/Datascience_files/wekauebung/bank_test.arff"); 
		Instances data_test = new Instances(datafile_test);

		kmeans.buildClusterer(data);
		System.out.println(kmeans.toString());
		
		kmeans.buildClusterer(data_test);
		System.out.println(kmeans.toString());
	}
}
```

## task 16
```
Number of iterations: 6
Within cluster sum of squared errors: 1604.7416693522332

Initial starting points (random):

Cluster 0: 25,FEMALE,RURAL,14505.3,NO,3,NO,YES,YES,NO,NO
Cluster 1: 61,FEMALE,RURAL,22942.9,YES,2,NO,YES,YES,NO,NO
Cluster 2: 54,FEMALE,INNER_CITY,31095.6,YES,2,NO,NO,YES,NO,YES
Cluster 3: 36,FEMALE,TOWN,26920.8,YES,0,NO,NO,YES,NO,NO
Cluster 4: 42,MALE,INNER_CITY,15499.9,YES,0,YES,NO,YES,YES,YES
Cluster 5: 50,MALE,TOWN,40972.9,NO,2,YES,YES,YES,YES,YES

Missing values globally replaced with mean/mode

Final cluster centroids:
                           Cluster#
Attribute      Full Data          0          1          2          3          4          5
                 (600.0)     (77.0)     (76.0)     (77.0)    (147.0)    (106.0)    (117.0)
==========================================================================================
age               42.395    37.1299    44.2763    48.3117    39.1156    39.3019    47.6667
sex               FEMALE     FEMALE     FEMALE     FEMALE     FEMALE       MALE       MALE
region        INNER_CITY INNER_CITY      RURAL INNER_CITY       TOWN INNER_CITY       TOWN
income        27524.0312 23377.7604 27772.3746 27668.4396 24047.3865    26359.8 35419.2842
married              YES         NO        YES        YES        YES        YES         NO
children               0          3          2          1          0          0          2
car                   NO         NO         NO         NO         NO        YES        YES
save_act             YES        YES        YES         NO        YES         NO        YES
current_act          YES        YES        YES        YES        YES        YES        YES
mortgage              NO         NO         NO         NO         NO        YES         NO
pep                   NO         NO         NO        YES         NO        YES        YES




kMeans
======

Number of iterations: 2
Within cluster sum of squared errors: 0.0

Initial starting points (random):

Cluster 0: 23,FEMALE,TOWN,30375.4,YES,2,NO,NO,YES,NO,NO
Cluster 1: 40,MALE,TOWN,29085.1,YES,3,YES,NO,YES,YES,NO
Cluster 2: 48,FEMALE,INNER_CITY,57546,NO,0,NO,NO,NO,NO,YES
Cluster 3: 51,FEMALE,INNER_CITY,46575.4,NO,0,YES,YES,YES,NO,NO
Cluster 4: 57,FEMALE,RURAL,50576.3,YES,0,NO,YES,NO,YES,NO

Missing values globally replaced with mean/mode

Final cluster centroids:
                           Cluster#
Attribute      Full Data          0          1          2          3          4
                   (5.0)      (1.0)      (1.0)      (1.0)      (1.0)      (1.0)
===============================================================================
age                 43.8         23         40         48         51         57
sex               FEMALE     FEMALE       MALE     FEMALE     FEMALE     FEMALE
region        INNER_CITY       TOWN       TOWN INNER_CITY INNER_CITY      RURAL
income          42831.64    30375.4    29085.1      57546    46575.4    50576.3
married              YES        YES        YES         NO         NO        YES
children               0          2          3          0          0          0
car                   NO         NO        YES         NO        YES         NO
save_act              NO         NO         NO         NO        YES        YES
current_act          YES        YES        YES         NO        YES         NO
mortgage              NO         NO        YES         NO         NO        YES
pep                   NO         NO         NO        YES         NO         NO
```

