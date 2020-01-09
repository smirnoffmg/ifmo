pkg load signal

% Parameters
Fs = 44100;
T  = 1;
Fc = 15000;
Fm = 10;

% Low-pass filter design
[num,den] = butter(10,1.2*Fc/Fs); 

% Signals
t = 0:1/Fs:T;
x = cos(2*pi*Fm*t);
y = ammod(x,Fc,Fs);
z = amdemod(y,Fc,Fs);
w = amdemod(y,Fc,Fs,0,0,num,den); 

% Plot
figure('Name','AM Modulation');
subplot(4,1,1); plot(t,x); title('Modulating signal');
subplot(4,1,2); plot(t,y); title('Modulated signal');
subplot(4,1,3); plot(t,z); title('Demodulated signal');
subplot(4,1,4); plot(t,w); title('Demodulated signal (filtered)');

sleep(10);