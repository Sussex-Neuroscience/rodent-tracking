//camera holder

tol = 0.1;

IRledarrayd = 54;
IRledarrayh = 12.5;//12.41

basex = IRledarrayd+2*tol+5;
basey = IRledarrayd+2*tol+5;
basez = IRledarrayh+7;




$fn=50;

///// modules ////////



module grid(){
            for (i = [0:9]) {
            translate([i*(7.83+2),0,0]){
                cylinder(d=2.1+tol,h=80);
                translate([0,-5,40]){
                cube([2.1+tol,10,80],center=true);    
                }//end translate
            }//end translate
        }//end for

    
    }//end grid
///////


module ircamholder(){
difference(){    
    translate([0,0,-5]){
        cube([basex,basey,basez]);

        }//end translate
                translate([basex/4+5,-1,-6]){
            cube([20,basey+2,15]);
    }//end translate
    
    translate([(basex)/2,(basey)/2,7]){//5 was the original height
            cylinder(d=IRledarrayd+2*tol+1,h=IRledarrayh);
            }//end translate
            
    translate([(basex)/2,(basey)/2,-basez/2]){
        
        cylinder(d=(IRledarrayd+2*tol)-2,h=IRledarrayh+5);
        
        
        
        translate([0,0,-5]){
            cylinder(d=14,h=30);
            }//end translate
    }//end translate

    
}//end difference    

}//end module
difference(){
translate([4.8,1,2]){
ircamholder();
    }//end translate


translate([0,80,0]){
rotate([90,0,0]){
grid();
}
}
}