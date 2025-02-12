from gym.envs.mujoco.mujoco_env import MujocoEnv
# ^^^^^ so that user gets the correct error
# message if mujoco is not installed correctly

# Base class
from gym.envs.mujoco.base_env import BaseEnv

# Walker2d
from gym.envs.mujoco.walker2d import Walker2dEnv
#from gym.envs.mujoco.walker2d_v0 import Walker2dEnvV0
from gym.envs.mujoco.walker2d_forward import Walker2dForwardEnv
from gym.envs.mujoco.walker2d_backward import Walker2dBackwardEnv
from gym.envs.mujoco.walker2d_balance import Walker2dBalanceEnv
from gym.envs.mujoco.walker2d_jump import Walker2dJumpEnv
from gym.envs.mujoco.walker2d_crawl import Walker2dCrawlEnv
from gym.envs.mujoco.walker2d_patrol import Walker2dPatrolEnv
from gym.envs.mujoco.walker2d_hurdle_v0 import Walker2dHurdleEnvV0
from gym.envs.mujoco.walker2d_hurdle import Walker2dHurdleEnv
from gym.envs.mujoco.walker2d_obstacle_course import Walker2dObstacleCourseEnv

# Jaco
from gym.envs.mujoco.jaco import JacoEnv
from gym.envs.mujoco.jaco_pick import JacoPickEnv
from gym.envs.mujoco.jaco_catch import JacoCatchEnv
from gym.envs.mujoco.jaco_toss import JacoTossEnv
from gym.envs.mujoco.jaco_hit import JacoHitEnv
from gym.envs.mujoco.jaco_keep_pick import JacoKeepPickEnv
from gym.envs.mujoco.jaco_keep_catch import JacoKeepCatchEnv
from gym.envs.mujoco.jaco_serve import JacoServeEnv

# HalfCheetahEnv
from gym.envs.mujoco.half_cheetah import HalfCheetahEnv
from gym.envs.mujoco.half_cheetah_hurdle import HalfCheetahEnv_Hurdle
from gym.envs.mujoco.half_cheetah_hurdle_v2 import HalfCheetahEnv_Hurdle_v2
from gym.envs.mujoco.half_cheetah_hurdle_v3 import HalfCheetahEnv_Hurdle_v3

from gym.envs.mujoco.hopper_v3_hurdle import HopperEnv as Hopper_hurdle_v3_Env

from gym.envs.mujoco.ant_v3 import AntEnv