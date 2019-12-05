//camera holder

camerax = 38;
cameray=38;
cameraz=2;

camerainset = 24;
screwd=2.3;
screwh=10;
sheadd = 5;
sheadh = 3;
screwoffset = 4.07;
border = 2;
tol = 0.1;

platex = camerax+10;
platey = cameray+10;
platez = 5;

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


///////


%cube([camerax+2*border,cameray+2*border,cameraz]);
translate([-(platex-camerax-2*border)/2,-(platey-cameray-2*border)/2,0]){
    %cube([platex,platey,platez]);
    }//end translate
translate([screwoffset+border,screwoffset+border,-cameraz/2]){
    screw();
    }//end translate

translate([camerax-screwoffset+border,screwoffset+border,-cameraz/2]){
    screw();
    }//end translate

translate([screwoffset+border,cameray-screwoffset+border,-cameraz/2]){
    screw();
    }//end translate
    
translate([camerax-screwoffset+border,cameray-screwoffset+border,-cameraz/2]){
    screw();
    }//end translate
    
translate([camerax/2+border-camerainset/2,cameray/2+border-camerainset/2,-cameraz/2]){
    cube([camerainset+2*tol,camerainset+2*tol,cameraz*5]);
    }//end translate
translate([]){  
    cube([camerax/2,3,cameraz*2]);
}//end translate