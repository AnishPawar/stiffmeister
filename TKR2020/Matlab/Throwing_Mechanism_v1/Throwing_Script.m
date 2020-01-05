torque=10;

    
while torque<21.5065
    fprintf('%i\n', torque);
    sim('Throwing_Test_Final_Version');
    torque=torque+0.5;
end

