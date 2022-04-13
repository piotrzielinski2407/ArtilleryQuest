from simulation import PhysicsSimulation
from terrain import Terrain
from graphic_drive import GraphicDriver
from tank import Tank
from wind_arrow import WindArrow
from barrel import Barrel

time_scale = 0.006
gravity = 9.8065
density = 1.1
default_angle = 45

simulate_env = PhysicsSimulation(time_scale, gravity, density)
terrain = Terrain()
terrain.set_up_terrain('variant1')
barrel = Barrel()
barrel.set_up_barrel(default_angle, x_position=45, y_position=35)
tank = Tank()
tank.set_up_tank(x_position=10, y_position=20)
graphics = GraphicDriver(simulate_env)
graphics.barrel = barrel
simulate_env.add_object(terrain)
simulate_env.add_object(tank)
simulate_env.add_object(barrel)

while True:
    chunks, texts = simulate_env.graphic_render_feed()
    graphics.update_screen(chunks, text_object_to_render=texts)
    simulate_env.run_time_step()




