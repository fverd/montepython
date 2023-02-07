info.to_change={'inv_M_wdm_keV':'$M_{wdm}^{-1}$','log10sigmaovermass':'$\log_{10}{\sigma / m}$'}
#info.to_plot=['M_wdm','\log_10} \sigma/M']

info.to_plot=['$M_{wdm}^{-1}$','$\log_{10}{\sigma / m}$']
info.ticksize=8
info.ticknumber=5
info.linesize=1.5

info.force_limits = {'$M_{wdm}^{-1}$':[0.1,0.4]}

#Following values reccomended by plot_files/example.plot
info.posterior_smoothing=0
info.interpolation_smoothing = 2
info.gaussian_smoothing = 0.35