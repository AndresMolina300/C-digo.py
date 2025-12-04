import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    Lx, Ly = 1.0, 1.0    
    Nx, Ny = 100, 100     
    dx = Lx / Nx          
    dy = Ly / Ny         
    alpha = 0.01         

    dt = 0.25 * min(dx, dy)**2 / alpha 
    Nt = 100             

    u = np.zeros((Nx, Ny)) 

    cento_medios=(Nx//10)//2  
    cx, cy = Nx//2, Ny//2     

    fig, ax = plt.subplots()  

    img = ax.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot', vmin=0, vmax=100)

    cbar = plt.colorbar(img, ax=ax, label='Temperatura')

    ax.set_title("Difusión de calor en 2D")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ani = animation.FuncAnimation(fig, update, frames=Nt, interval=50, blit=False, fargs=(u,Nx,Ny,cento_medios,cx,cy,dx,dy,alpha,dt,img,ax,fig,Nt))

    plt.show()
    
def update(frame,u,Nx,Ny,cento_medios,cx,cy,dx,dy,alpha,dt,img,ax,fig,Nt):
    u[cx-cento_medios:cx+cento_medios, cy-cento_medios:cy+cento_medios] = 100.0
    
    u_new = u.copy()
    
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            u_new[i,j] = u[i,j] + alpha * dt * (
                (u[i+1,j] - 2*u[i,j] + u[i-1,j]) / dx**2 +  
                (u[i,j+1] - 2*u[i,j] + u[i,j-1]) / dy**2    
            )
            
    u_new[0, :] = u_new[1, :]       
    u_new[-1, :] = u_new[-2, :]    
    u_new[:, 0] = u_new[:, 1]       
    u_new[:, -1] = u_new[:, -2]     

    u[:,:] = u_new
    
    img.set_array(u)
    
    ax.set_title(f"Difusión de calor - paso {frame}")
    
    if frame>=Nt-1:
        plt.close(fig)
        
    return [img]

if __name__ == "__main__":

    main()
