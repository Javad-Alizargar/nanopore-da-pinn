"""Publication figures drawn only from corrected revision outputs."""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'outputs/revision'
OUT = DATA / 'figures'
sys.path.insert(0,str(ROOT / 'src'))
from pnp_da_pinn.config import load_config
from pnp_da_pinn.grid import make_grid
from pnp_da_pinn.baseline import PnpSolution
from pnp_da_pinn.conservative import physical_current

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                     'savefig.dpi':300,'font.family':'DejaVu Sans'})


def save(fig,name):
    fig.savefig(OUT / (name+'.png'),dpi=300)
    fig.savefig(OUT / (name+'.pdf'))
    plt.close(fig)


def field(ax,r,z,values,title,cmap='viridis'):
    im=ax.pcolormesh(z,r,values,shading='auto',cmap=cmap)
    ax.set(xlabel='z/L',ylabel='r/R',title=title)
    plt.colorbar(im,ax=ax,pad=.02)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    ref=np.load(DATA/'reference.npz')
    pred=np.load(DATA/'data_assimilated_42.npz')
    r,z=ref['r'],ref['z']
    stats=pd.read_csv(DATA/'surrogate_runs.csv')
    grids=pd.read_csv(DATA/'grid_refinement.csv')
    sweep=pd.read_csv(DATA/'parameter_sweep.csv')
    fig,ax=plt.subplots(2,3,figsize=(11.5,6.4),layout='constrained')
    a=ax[0,0]
    a.add_patch(Rectangle((0,.15),1,.7,facecolor='#e8f4f5',edgecolor='black'))
    a.plot([0,1],[.85,.85],color='#b4443a',lw=3)
    a.plot([0,1],[.15,.15],color='#b4443a',lw=3)
    a.annotate('',xy=(.9,.5),xytext=(.1,.5),arrowprops={'arrowstyle':'->','lw':2})
    a.text(.5,.95,'Charged wall',ha='center')
    a.text(.5,.65,'R = 5 nm     L = 30 nm',ha='center')
    a.text(.05,.35,'50 mV',ha='left')
    a.text(.95,.35,'0 mV',ha='right')
    a.set(xlim=(-.05,1.05),ylim=(0,1.1),title='A  Cylindrical pore')
    a.axis('off')
    field(ax[0,1],r,z,ref['c_plus']-1,'B  Conservative reference: cation excess')
    indices=pred['training_indices']
    rr,zz=np.meshgrid(r,z,indexing='ij')
    ax[0,2].scatter(zz.ravel()[indices],rr.ravel()[indices],s=3,color='#27866e')
    ax[0,2].set(xlabel='z/L',ylabel='r/R',title='C  500 numerical anchors')
    ax[1,0].axis('off')
    ax[1,0].set_title('D  Exact reservoir constraints')
    ax[1,0].text(.03,.8,r'$\psi_\theta=\psi_{app}(1-z)+z(1-z)N_\psi$',fontsize=12)
    ax[1,0].text(.03,.59,r'$c_{\pm,\theta}=\exp[z(1-z)N_\pm]$',fontsize=12)
    ax[1,0].text(.03,.34,'PNP residuals + axis/wall conditions\n+ field and charge assimilation',linespacing=1.7)
    field(ax[1,1],r,z,pred['c_plus']-1,'E  DA-PINN: cation excess')
    a=ax[1,2]
    a.axis('off')
    a.set_title('F  Independent diagnostics')
    a.text(.03,.8,'Equilibrium and Ohmic tests\nTolerance and field refinement\nHeld-out nodes and paired seeds\nCharge and current errors\nTraining and inference timing',va='top',linespacing=1.9)
    save(fig,'Figure_1_workflow')
    fig,axes=plt.subplots(2,2,figsize=(10,6.4),layout='constrained')
    for a,key,title in zip(axes.ravel(),['psi','c_plus','c_minus','charge'],
                           ['A  Potential','B  Cation concentration','C  Anion concentration','D  Net charge density']):
        values=ref[key] if key!='charge' else ref['c_plus']-ref['c_minus']
        field(a,r,z,values,title)
    save(fig,'Figure_2_reference_fields')
    fig,axes=plt.subplots(1,3,figsize=(11.5,3.3),layout='constrained')
    axes[0].plot(grids.nr,grids.current_pA,'o-',color='#327d86')
    axes[0].ticklabel_format(style='plain',useOffset=False,axis='y')
    axes[0].set(xlabel='Radial nodes',ylabel='Mean current (pA)',title='A  Current refinement')
    for col,label in [('psi_relative_to_finest','Potential'),('c_plus_relative_to_finest','Cation'),('charge_relative_to_finest','Charge')]:
        axes[1].semilogy(grids.nr[:-1],grids[col][:-1],'o-',label=label)
    axes[1].set(xlabel='Radial nodes',ylabel='Relative error vs 41 x 121',title='B  Field refinement')
    axes[1].legend(fontsize=8)
    tol=pd.read_csv(DATA/'tolerance_study.csv')
    axes[2].loglog(tol.tolerance[:-1],tol.charge_relative_to_tight[:-1],'o-',color='#a65143')
    axes[2].set(xlabel='Requested fixed-point tolerance',ylabel='Charge error vs tight solve',title='C  Tolerance sensitivity')
    save(fig,'Figure_3_grid_refinement')
    fig,axes=plt.subplots(2,3,figsize=(11.5,6.2),layout='constrained')
    for i,key in enumerate(['psi','c_plus','charge']):
        a=ref[key] if key!='charge' else ref['c_plus']-ref['c_minus']
        b=pred[key] if key!='charge' else pred['c_plus']-pred['c_minus']
        field(axes[0,i],r,z,b,['A  DA-PINN potential','B  DA-PINN cation','C  DA-PINN charge'][i])
        field(axes[1,i],r,z,np.abs(a-b),['D  Absolute potential error','E  Absolute cation error','F  Absolute charge error'][i],'magma')
    save(fig,'Figure_4_surrogate_errors')
    fig,axes=plt.subplots(2,2,figsize=(10,6.4),layout='constrained')
    iv=sweep[sweep['case'].str.startswith('voltage')].sort_values('voltage_mV')
    axes[0,0].plot(iv.voltage_mV,iv.current_pA,'o-',color='#327d86')
    axes[0,0].set(xlabel='Voltage (mV)',ylabel='Current (pA)',title='A  SG/FV current-voltage sweep')
    charge=sweep[sweep['case'].str.startswith('charge')].sort_values('wall_charge',ascending=False)
    axes[0,1].plot(-charge.wall_charge,charge.wall_cation-1,'o-',color='#27866e')
    axes[0,1].set(xlabel=r'$|q_w|$',ylabel='Near-wall cation excess',title='B  SG/FV charge sweep')
    salt=sweep[sweep['case'].str.startswith('salt')]
    axes[1,0].semilogx(salt.bulk,salt.wall_cation-1,'o-',color='#a65143')
    axes[1,0].set(xlabel=r'Bulk concentration (mol m$^{-3}$)',ylabel='Near-wall cation excess',title='C  SG/FV salt sweep')
    radius=sweep[sweep['case'].str.startswith('radius')]
    axes[1,1].plot(radius.radius_nm,radius.current_pA,'o-',color='#6f5b92')
    axes[1,1].set(xlabel='Radius (nm)',ylabel='Current (pA)',title='D  SG/FV radius sweep')
    save(fig,'Figure_5_surface_response')
    fig,axes=plt.subplots(1,3,figsize=(11.5,3.7),layout='constrained')
    modes=['physics_only','data_assimilated','wall_adaptive']
    labels=['Physics\nonly','Data\nassisted','Wall\nadaptive']
    for a,col,title in zip(axes,['c_plus_heldout_rel_l2','charge_heldout_rel_l2','current_rel_l2'],
                           ['A  Held-out cation error','B  Held-out charge error','C  Current-profile error']):
        for seed in sorted(stats.seed.unique()):
            y=[stats[(stats.seed==seed)&(stats['mode']==mode)][col].iloc[0] for mode in modes]
            a.plot(range(3),y,'o-',alpha=.65,label=f'Seed {seed}')
        a.set_xticks(range(3),labels)
        a.set(ylabel='Relative L2 error',title=title,yscale='log')
    axes[0].legend(fontsize=8)
    save(fig,'Figure_6_ablation')


if __name__=='__main__':
    main()
