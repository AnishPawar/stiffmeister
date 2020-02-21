i=8; %use for custon run in while loop
project_len =0.55;

plane_x = 10;
plane_y = 10;

thrower_x = 0.11;
thrower_y = 0.075;

thrower_p_x = 1.06;
thrower_p_y = 0.5;

contact_damping = 70;
contact_stiffness = 500;

contact_stiffness_wood = 10000;
contact_damping_wood = 400;

k_fric_throw = 0.34;
s_fric_throw = 0.344;

k_fric_plane = 0.6;
s_fric_plane = 0.6;

shagai_mass = 660;
height_mm = 155;

piston_force = 32; %5.3 bars
theta = 12.4;
sim('Shagai_Throwing');

%plot3(shagai_x.data, shagai_y.data, shagai_z.data)

%for more awesomeness type from cmd 
%matlab -nosplash -nodesktop -r "run ('path_to_file')";

%theta increment
{
while theta>13
    fprintf('%i\n', theta);
    sim('Shagai_Throwing');
    theta=theta-0.2;
end
}

%shagai mass and theta increment
%{
while shagai_mass<751
    theta=11;
    while theta<13.6                                                  
        fprintf('%i\n', theta);
        fprintf('%i\n', shagai_mass);
        sim('Shagai_Throwing');
        theta=theta+0.5;
        end
    shagai_mass=shagai_mass+50;
end
%}