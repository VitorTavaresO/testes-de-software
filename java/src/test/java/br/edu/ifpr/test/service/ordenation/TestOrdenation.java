package br.edu.ifpr.test.service.ordenation;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.io.InputStream;
import java.util.ArrayList;

import org.junit.jupiter.api.Test;

import service.ServiceOrdenation;

public class TestOrdenation {
    @Test
    public void mustReadFile() {

        // GIVEN

        String fileName = "case01.txt";
        ArrayList<Integer> expectedInput = new ArrayList<>();
        expectedInput.add(4);
        expectedInput.add(12);
        expectedInput.add(9);
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream(fileName);
        assertNotNull(inputStream, "Input stream should not be null");

        // WHEN

        ServiceOrdenation serviceOrdenation = new ServiceOrdenation();
        ArrayList<Integer> fileContent = serviceOrdenation.getFileContent(fileName);
        System.out.println(fileContent);

        // THEN
        assertEquals(expectedInput, fileContent);

    }

    @Test
    public void mustReadDisordelyPrintOrdered() {

        // GIVEN

        String fileName = "case01.txt";
        String expectedInput = "4,12,9";
        String expectedOutput = "4,9,12";
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream(fileName);
        assertNotNull(inputStream, "Input stream should not be null");

        // WHEN

        ServiceOrdenation serviceOrdenation = new ServiceOrdenation();
        ArrayList<Integer> list = serviceOrdenation.getFileContent(fileName);
        ArrayList<Integer> orderedList = serviceOrdenation.ordenateList(list);

        // THEN

    }

    @Test
    public void mustOrderArrayList() {

        // GIVEN

        String fileName = "case01.txt";
        ArrayList<Integer> expectedOutput = new ArrayList<>();
        expectedOutput.add(4);
        expectedOutput.add(9);
        expectedOutput.add(12);
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream(fileName);
        assertNotNull(inputStream, "Input stream should not be null");

        // WHEN

        ServiceOrdenation serviceOrdenation = new ServiceOrdenation();
        ArrayList<Integer> list = serviceOrdenation.getFileContent(fileName);
        ArrayList<Integer> orderedList = serviceOrdenation.ordenateList(list);

        // THEN
        assertEquals(expectedOutput, orderedList);
        System.out.println(orderedList);

    }
}
