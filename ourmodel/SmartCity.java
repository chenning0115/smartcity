package smartcity;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.functions.SGDText.Count;
import weka.classifiers.trees.RandomForest;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.OptionHandler;
import weka.core.Utils;
import weka.core.converters.CSVLoader;
import weka.core.converters.ConverterUtils.DataSource;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.NumericToNominal;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Vector;

import com.vividsolutions.jts.triangulate.VoronoiDiagramBuilder;

import data.LRInstances;

public class SmartCity {
	
	
	public static void printinstancesmetadata(Instances data)
	{
		for(int i =0;i<data.numAttributes();i++)
		 {
			 System.out.println(data.attribute(i).name()+" "+data.attribute(i).typeToString(data.attribute(i)));
		 }
		System.out.println("len="+data.size());
	}
	
	public static int getmaxindex(double[] values)
	{
		double max = values[0];
		int maxindex = 0;
		for(int i=1;i<values.length;i++)
		{
			if(values[i]>max)
			{
				max = values[i];
				maxindex = i;
			}
		}
		return maxindex;
	}
	public static void printarray(double[] arr)
	{
		for(int i=0;i<arr.length;i++)
		{
			System.out.print(i+",");
		}
		System.out.println();
	}
	public static void printarray2(double[][] arr){
		for(int i=0;i<arr.length;i++)
		{
			for(int j =0;i<arr[i].length;j++)
			{
				System.out.print(j+",");
			}
			System.out.println();
		}
	}
	public static void printins_10(Instances inss)
	{
		for(int k=0;k<10;k++)
		{
			Instance ins = inss.get(k);
			for (int i=0;i<ins.numAttributes();i++)
			{
				System.out.println(ins.attribute(i).name()+","+ins.value(i));
			}
		}
		
	}
	public static void main(String[] args)
	{
		try{
			String trainpath = "/Users/chenning/Desktop/data/smc_std_traindata_jicha.csv";
			CSVLoader loader = new CSVLoader();
		    loader.setSource(new File(trainpath));
		    Instances traindata = loader.getDataSet();
			//Instances traindata = DataSource.read(trainpath);
			//System.out.println("sucessfully load from "+trainpath+" length = "+traindata.size()+" attrlength = "+traindata.numAttributes());
			printinstancesmetadata(traindata);
			 Filter numtonomial = new NumericToNominal();
			 String[] filter_options = new String[2];
			 filter_options[0] = "-R";                                    // "range"
			 filter_options[1] = "8";  
	         numtonomial.setInputFormat(traindata);
			 numtonomial.setOptions(filter_options);
			 Instances newtraindata = Filter.useFilter(traindata, numtonomial);
			 newtraindata.setClassIndex(7);
			 printinstancesmetadata(newtraindata);
			 //printins_10(traindata);
			 System.out.println(newtraindata.classAttribute().name());
			RandomForest randomforest = new RandomForest();
			randomforest.buildClassifier(newtraindata);
			
			String predpath = "/Users/chenning/Desktop/data/jicha_all.csv";
			//String predpath = "/Users/chenning/Desktop/data/smc_std_traindata_jicha.csv";
			String respath = "/Users/chenning/Desktop/data/result1.csv";
			PrintWriter writer = new PrintWriter(new OutputStreamWriter(new FileOutputStream(new File(respath))));
		    loader.setSource(new File(predpath));
		    Instances preddata_1 = loader.getDataSet();
		    Instances preddata = Filter.useFilter(preddata_1, numtonomial);
		    preddata.setClassIndex(7);
		    printinstancesmetadata(preddata);
		    //printins_10(preddata);
		    int count = preddata.size();
		    ArrayList<String> list = new ArrayList<>(); 
		    for(int i=0;i<count;i++)
		    { 
		    	Instance instance = preddata.get(i);
		    	double temp = randomforest.classifyInstance(instance);
		    	//int c = getmaxindex(temp);
		    	String c = instance.classAttribute().value((int)temp);
		    	list.add(c);
		    	if(instance.classValue()>0) System.out.println(i+" r="+instance.classAttribute().value((int)instance.classValue())+" c="+c);
		    	//printarray(temp);
		    	writer.println(i+","+c);
		    	writer.flush();
		    }
		   writer.flush();
		   writer.close();
		    System.out.println("ok");
		    
		}catch(Exception e)
		{
			e.printStackTrace();
		}
		
		
	}

}
