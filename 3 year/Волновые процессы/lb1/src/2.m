clear;
pkg load signal;

% amplitude modulation

function y = amp_mod (x, fc, fs)
  t = 0 : 1./fs : (length (x)-1)./fs;
  y = x .* cos (2.*pi.*fc.*t);
endfunction

function m = amp_demod (s, fc, fs)
  t = 0:1./fs:(length (s) - 1)./fs;
  e = s .* cos (2.*pi.*fc.*t);
  [b a] = butter (1, fc.*2./fs);
  m = filtfilt (b, a, e).*2;
endfunction


t=1; % time interval
t1=linspace(0,t,1000); % 1000 points from 0 to t

F_c=1000;
Am=2;
F_s=4000;

u_m = Am .* cos(2*pi*F_s*t1)

% modulated signal
u_am = amp_mod(u_m, F_c, F_s)


% demodulated signal
u_dem = amp_demod(u_am, F_c, F_s)

subplot(311);
plot(t1, u_m, 'k');
xlabel('time');
ylabel('amplitude');
title('message signal')

subplot(312);
plot(t1,u_am);
xlabel('time');
ylabel('amplitude');
title('modulated signal');

subplot(313);
plot(t1,u_dem);
xlabel('time');
ylabel('amplitude');
title('demodulated signal');
