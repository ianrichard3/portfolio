package com.parcial.pruebaTp.support;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Point2D {
    private double x;
    private double y;


    public static double distanceBetweenPoints(Point2D p1, Point2D p2) {

        double xDist = (p2.x - p1.x);
        double yDist = (p2.y - p1.y);

        double distance = Math.sqrt(Math.pow(xDist, 2) + Math.pow(yDist, 2));

        return distance;
    }
}
