package service;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class ServiceOrdenation {

    public ArrayList<Integer> getFileContent(String fileName) {
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream(fileName);
        ArrayList<Integer> list = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
            String firstLine = reader.readLine();
            int n = Integer.parseInt(firstLine);
            for (int i = 0; i < n; i++) {
                String line = reader.readLine();
                int number = Integer.parseInt(line);
                list.add(number);
            }
        } catch (Exception e) {

        }
        return list;
    }

    public ArrayList<Integer> ordenateList(ArrayList<Integer> list) {
        ArrayList<Integer> orderedList = new ArrayList<>(list);
        Collections.sort(orderedList);
        return orderedList;
    }

}
