%1
clear();

figure('name','Acuracy_train');
x1 = linspace(0,10,11);y1 = [0,0.0041, 0.0071,0.0118,0.0158,0.0221,0.0244,0.0289,0.0349,0.0470,0.0572];
plot(x1,y1,'LineWidth',2);hold on;
x2 = linspace(0,10,11);y2 = [0,0.2916,0.7398, 0.8967, 0.9522,0.9794,0.9878, 0.9937,0.9963, 0.9974, 0.9973];
plot(x2,y2,'LineWidth',2);
xlabel('epoch(s)');ylabel('accuracy');title('TrainACC');%if out of index clear title;
legend('NoPrtrain','Pretrain','location','East');
saveas(gcf, ['ACC_train.png'], 'png');

clear();

%2
figure('name','Loss_train');
x1 = linspace(0,10,11);y1 = [0,5.5882862003004155 ,5.289145985848777 ,5.181993451708661 ,5.103186022790336 ,5.017972073058482 ,4.939698416029775 ,4.875766745719085 ,4.755256452354327 ,4.618581710957825 ,4.433459503008949 ];
plot(x1,y1,'LineWidth',2);hold on;
x2 = linspace(0,10,11);y2 = [0,3.187225727763298 ,0.9298709284345855 ,0.3639439005397392 ,0.17397367374601908 ,0.08551854082549719 ,0.052850920114161225 ,0.02823993581217258 ,0.01723000085189909 ,0.010358199974876959 ,0.012274898983874818];
plot(x2,y2,'LineWidth',2);
xlabel('epoch(s)');ylabel('loss');title('TrainLoss');%if out of index clear title;
legend('NoPrtrain','Pretrain','location','East');
saveas(gcf, ['Loss_train.png'], 'png');

clear();

%3
figure('name','Acuracy_test');
x1 = linspace(0,10,11);y1 = [0,0,1,1,1,2,2,3,3,5,6];
plot(x1,y1,'LineWidth',2);hold on;
x2 = linspace(0,10,11);y2 = [0,53,71,75,85,86,88,89,89,90,90];
plot(x2,y2,'LineWidth',2);
xlabel('epoch(s)');ylabel('accuracy');title('TestACC');%if out of index clear title;
legend('NoPrtrain','Pretrain','location','East');
saveas(gcf, ['ACC_test.png'], 'png');