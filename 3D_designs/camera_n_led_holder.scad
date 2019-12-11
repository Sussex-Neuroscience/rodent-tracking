//camera holder

camerax = 38;
cameray=38;
cameraz=2;

camerainset = 24;
camerainseth = 14;//17;//22;
screwd=2.3;
screwh=10;
sheadd = 3.8;
sheadh = 3;
screwoffset = 4.07;
border = 2;
tol = 0.1;

platex = camerax+18;
platey = cameray+10;
platez = 5;

pilarx = 17;
pilary = 7;

ledd = 5;

$fn=30;
fn1 = 30;
fn2 = 30;
///// modules ////////

module screw(diam1=screwd+2*tol,h1=screwh,diam2=sheadd+2*tol,h2=sheadh+0.5,fn1=fn1,fn2=fn2){
    translate([0,0,h1/2]){
        cylinder(d=diam1,h=h1,center=true,$fn=fn1);
    }//end translate
    translate([0,0,h2/2]){
        cylinder(d=diam2,h=h2,center=true,$fn=fn2);
    }//end translate
    
    }//end module
/////

module grid(){
            for (i = [0:9]) {
            translate([i*(7.85+2),0,0]){
                cylinder(d=2.1,h=80);
            }//end translate
        }//end for

    
    }//end grid
///////
module camera_holder(){
difference(){
    union(){
        cube([camerax+2*border,cameray+2*border,cameraz]);
    
        translate([-(platex-camerax-2*border)/2,-(platey-cameray-2*border)/2,0]){
            cube([platex,platey,platez]);
        translate([0,0,-camerainseth+2]){
            cube([pilarx,pilary,camerainseth]);
            }//end translate
        translate([0,platey-pilary,-camerainseth+2]){
            cube([pilarx,pilary,camerainseth]);
            }//end translate
        translate([platex-pilarx,platey-pilary,-camerainseth+2]){
            cube([pilarx,pilary,camerainseth]);
            }//end translate
        translate([platex-pilarx,0,-camerainseth+2]){
            cube([pilarx,pilary,camerainseth]);
            }//end translate
        }//end translate
    }//end union
    
    union(){
        translate([screwoffset+border+1,screwoffset+border+1,-cameraz/2]){
            screw();
            }//end translate

        translate([camerax-screwoffset+border-1,screwoffset+border+1,-cameraz/2]){
            screw();
            }//end translate

        translate([screwoffset+border+1,cameray-screwoffset+border-1,-cameraz/2]){
            screw();
            }//end translate
    
        translate([camerax-screwoffset+border-1,cameray-screwoffset+border-1,-cameraz/2]){
            screw();
            }//end translate
    
        translate([camerax/2+border-camerainset/2,cameray/2+border-camerainset/2,-cameraz/2]){
            cube([camerainset+2*tol,camerainset+2*tol,camerainseth]);
            }//end translate

        translate([camerax/2-10,5.5,+cameraz]){  
            cube([camerax/2,3,cameraz*2]);
        }//end translate

        translate([-3.5,60,-11.5]){
            rotate([90,0,0]){
                grid();
            }//end rotate
        }//end translate

        }//end union
    }//end difference
}//end module
/////

module led_holder(){
    difference(){

        cube([14,10,5]);

        translate([7,5,-1]){
            cylinder(d=ledd+2*tol,h=10);
        }//end translate

    }//end difference
}//end module

//camera_holder();
difference(){

translate([-2,2,-0.5]){
led_holder();
}//end translate
rotate([-90,0,0]){
grid();
}

}