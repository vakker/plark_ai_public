#This script pits two rule based agents against each other and records a video
#The rule based agents used are the ones specified in the game config file

from gym_plark.envs.plark_env_sparse import PlarkEnvSparse
from agent_training import helper
from plark_game.classes.rule_based_game import create_rule_based_game

if __name__ == '__main__':

    #Env variables
    config_file_path = '/Components/plark-game/plark_game/game_config/10x10/balanced.json'
    driving_agent = 'pelican'

    random_panther_start_position = True
    random_pelican_start_position = True

    env = PlarkEnvSparse(config_file_path=config_file_path,
                         driving_agent=driving_agent,
                         random_panther_start_position=random_panther_start_position,
                         random_pelican_start_position=random_pelican_start_position)
    
    #This is the only difference to a normal environment - one has to set the game
    #to a RuleBasedGame
    env.env.activeGames[len(env.env.activeGames)-1] = create_rule_based_game(config_file_path)

    env.reset()

    reward = 0
    while True:
        _, r, done, info = env.step(None)
        reward += r
        if done:
            break
    
    print(info['status'])
    print("Reward:", reward)

    video_path = '/rule_v_rule.mp4'
    helper.make_video_plark_env(None, env, video_path, n_steps=200)
