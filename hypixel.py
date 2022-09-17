from calendar import TextCalendar
from types import MemberDescriptorType
import requests
import random

apikeys = []

#TODO: Adding other Gamemodes to the stats
#TODO: Adding quest Class
#TODO: Adding challanges Class
#TODO: Adding petConsumables Class
#TODO: Adding all Items Class (vanityMeta, packages)
#TODO: Adding parkourCheckpointBests class
#TODO: Adding parkourCompletions
#TODO: Adding giftingMeta
#TODO: Adding leveling

def setkeys(keys : list):
    for key in keys:
        print(key)
        response = requests.get(f"https://api.hypixel.net/key?key={key}").json()
        if response["success"] == True:
            apikeys.append(key)
        else:
            raise f"The API Key {key} is invalid."

def chooseapikey():
    return random.choice(apikeys)

class Player():

    def __init__(self, uuid):
        self.UUID = uuid
        playerinfo = requests.get(f"https://api.hypixel.net/player?key={chooseapikey()}&uuid={self.UUID}").json()
        self.playerinfo = playerinfo["player"]


    @property
    def status(self):
        statusinfo = requests.get(f"https://api.hypixel.net/status?key={chooseapikey()}&uuid={self.UUID}").json()
        return statusinfo["session"]["online"]

    @property
    def Playerinfo(self):
        return self.playerinfo
    
    @property
    def uuid(self):
        uuid = self.playerinfo["uuid"]
        return uuid

    @property
    def firstLogin(self):
        firstLogin = self.playerinfo["firstLogin"]
        return firstLogin

    @property
    def lastLogin(self):
        lastLogin = self.playerinfo["lastLogin"]
        return lastLogin

    @property
    def lastLogin(self):
        lastLogin = self.playerinfo["lastLogin"]
        return lastLogin

    @property
    def lastLogout(self):
        lastLogout = self.playerinfo["lastLogout"]
        return lastLogout

    @property
    def playername(self):
        playername = self.playerinfo["playername"]
        return playername

    @property
    def displayname(self):
        displayname = self.playerinfo["displayname"]
        return displayname

    @property
    def karma(self):
        karma = self.playerinfo["karma"]
        return karma

    @property
    def networkExp(self):
        networkExp = self.playerinfo["networkExp"]
        return networkExp

    @property
    def flying(self):
        spec_always_flying = self.playerinfo["spec_always_flying"]
        return spec_always_flying

    @property
    def language(self):
        userLanguage = self.playerinfo["userLanguage"]
        return userLanguage

    @property
    def lastAdsense(self):
        lastAdsenseGenerateTime = self.playerinfo["lastAdsenseGenerateTime"]
        return lastAdsenseGenerateTime

    @property
    def lastClaimedReward(self):
        lastClaimedReward = self.playerinfo["lastClaimedReward"]
        return lastClaimedReward

    @property
    def rewardHighScore(self):
        rewardHighScore = self.playerinfo["rewardHighScore"]
        return rewardHighScore

    @property
    def totalDailyRewards(self):
        totalDailyRewards = self.playerinfo["totalDailyRewards"]
        return totalDailyRewards

    @property
    def totalRewards(self):
        totalRewards = self.playerinfo["totalRewards"]
        return totalRewards

    @property
    def rewardStreak(self):
        rewardStreak = self.playerinfo["rewardStreak"]
        return rewardStreak

    @property
    def rewardScore(self):
        rewardScore = self.playerinfo["rewardScore"]
        return rewardScore

    @property
    def grinchgifts(self):
        gifts_grinch = self.playerinfo["gifts_grinch"]
        return gifts_grinch

    @property
    def newPackageRank(self):
        newPackageRank = self.playerinfo["newPackageRank"]
        return newPackageRank

    @property
    def levelUp_VIP(self):
        levelUp_VIP = self.playerinfo["levelUp_VIP"]
        return levelUp_VIP

    @property
    def levelUp_VIP_PLUS(self):
        levelUp_VIP_PLUS = self.playerinfo["levelUp_VIP_PLUS"]
        return levelUp_VIP_PLUS

    @property
    def levelUp_MVP(self):
        levelUp_MVP = self.playerinfo["levelUp_MVP"]
        return levelUp_MVP

    @property
    def levelUp_MVP_PLUS(self):
        levelUp_MVP_PLUS = self.playerinfo["levelUp_MVP_PLUS"]
        return levelUp_MVP_PLUS

    @property
    def channel(self):
        channel = self.playerinfo["channel"]
        return channel

    @property
    def rankPlusColor(self):
        rankPlusColor = self.playerinfo["channrankPlusColorel"]
        return rankPlusColor

    @property
    def monthlyPackageRank(self):
        monthlyPackageRank = self.playerinfo["monthlyPackageRank"]
        return monthlyPackageRank

    @property
    def monthlyRankColor(self):
        monthlyRankColor = self.playerinfo["monthlyRankColor"]
        return monthlyRankColor

    @property
    def currentPet(self):
        currentPet = self.playerinfo["currentPet"]
        return currentPet

    @property
    def currentClickEffect(self):
        currentClickEffect = self.playerinfo["currentClickEffect"]
        return currentClickEffect

    @property
    def currentGadget(self):
        currentGadget = self.playerinfo["currentGadget"]
        return currentGadget

    @property
    def currentCloak(self):
        currentCloak = self.playerinfo["currentCloak"]
        return currentCloak

    @property
    def main2017Tutorial(self):
        main2017Tutorial = self.playerinfo["main2017Tutorial"]
        return main2017Tutorial

    @property
    def mostRecentGameType(self):
        mostRecentGameType = self.playerinfo["mostRecentGameType"]
        return mostRecentGameType

    @property
    def housingMeta(self):
        housingMeta = self.playerinfo["housingMeta"]
        return housingMeta

    @property
    def stats(self):
        stats = Stats(self.playerinfo["stats"])
        return stats

    @property
    def friends(self):
        friendinfo = requests.get(f"https://api.hypixel.net/friends?key={chooseapikey()}&uuid={self.UUID}").json()
        ownuuid = friendinfo["uuid"]
        friends = []
        for record in friendinfo["records"]:
            if record["uuidSender"] == ownuuid:
                friends.append(record["uuidReceiver"])
            else:
                friends.append(record["uuidSender"])
            
        return friends

    @property
    def recentgames(self):
        recentgameinfo = requests.get(f"https://api.hypixel.net/recentgames?key={chooseapikey()}&uuid={self.UUID}").json()
        return recentgameinfo["games"]

    @property
    def guild(self):
        guildData = requests.get(f"https://api.hypixel.net/guild?key={chooseapikey()}&player={self.UUID}").json()
        guild = Guild(guildData["guild"])
        return guild

    @property
    def achievements(self):
        achievementData = requests.get(f"https://api.hypixel.net/resources/achievements?key={chooseapikey()}&uuid={self.UUID}").json()
        achments = {}
        for gamemode in achievementData["achievements"]:
            achments[gamemode] = {"one_time" : [], "tiered" : []}
            for archname in achievementData["achievements"][gamemode]["one_time"]:
                achievement = Achievement(achievementData["achievements"][gamemode]["one_time"][archname])
                achments[gamemode]["one_time"].append(achievement)
            for archname in achievementData["achievements"][gamemode]["tiered"]:
            
                tiers = []
                for tier in achievementData["achievements"][gamemode]["tiered"][archname]:
                    t = AchievementTier(tier)
                    tiers.append(t)

                achievementData["achievements"][gamemode]["tiered"][archname]["tiers"] = tiers

                achievement = TieredAchievement(achievementData["achievements"][gamemode]["tiered"][archname])
                achments[gamemode]["tiered"].append(achievement)
        return achments

    @property
    def challenges(self):
        chellengeData = requests.get(f"https://api.hypixel.net/resources/challenges?key={chooseapikey()}&uuid={self.UUID}").json()
        challenges = {}
        for gamemode in chellengeData["challenges"]:
            challenges[gamemode] = []
            for challenge in chellengeData["challenges"][gamemode]:
                rewards = []
                for reward in challenge["rewards"]:
                    rew = ChallengeReward(reward)
                    rewards.append(rew)
                challenge["rewards"] = rewards
                challeng = Challenge(challenge)
                challenges[gamemode].append(challeng)
                challeng = None
        return challenges




class Stats():

    def __init__(self, data):
        self.stats = data

    @property
    def arcade(self):
        arcadeStats = ArcadeStats(self.stats["Arcade"])
        return arcadeStats

    @property
    def hungerGames(self):
        hungerGamesStats = HungerGamesStats(self.stats["Arcade"])
        return hungerGamesStats

    #TODO: Add the other game modes here

class ArcadeStats():

    def __init__(self, data):
        self.stats = data

    @property
    def coins(self):
        coins = self.stats["coins"]
        return coins

    @property
    def miniwalls_activeKit(self):
        miniwalls_activeKit = self.stats["miniwalls_activeKit"]
        return miniwalls_activeKit

    @property
    def stamp_level(self):
        stamp_level = self.stats["stamp_level"]
        return stamp_level

    @property
    def time_stamp(self):
        time_stamp = self.stats["time_stamp"]
        return time_stamp

    @property
    def arrows_hit_mini_walls(self):
        arrows_hit_mini_walls = self.stats["arrows_hit_mini_walls"]
        return arrows_hit_mini_walls

    @property
    def weekly_coins_a(self):
        weekly_coins_b = self.stats["weekly_coins_a"]
        return weekly_coins_b

    @property
    def weekly_coins_b(self):
        weekly_coins_b = self.stats["weekly_coins_b"]
        return weekly_coins_b

    @property
    def monthly_coins_a(self):
        monthly_coins_a = self.stats["monthly_coins_a"]
        return monthly_coins_a

    @property
    def monthly_coins_b(self):
        monthly_coins_b = self.stats["monthly_coins_b"]
        return monthly_coins_b

    @property
    def kills_mini_walls(self):
        kills_mini_walls = self.stats["kills_mini_walls"]
        return kills_mini_walls

    @property
    def deaths_mini_walls(self):
        deaths_mini_walls = self.stats["deaths_mini_walls"]
        return deaths_mini_walls

    @property
    def arrows_shot_mini_walls(self):
        arrows_shot_mini_walls = self.stats["arrows_shot_mini_walls"]
        return arrows_shot_mini_walls

    @property
    def wither_damage_mini_walls(self):
        wither_damage_mini_walls = self.stats["wither_damage_mini_walls"]
        return wither_damage_mini_walls

    @property
    def items_found_scuba_simulator(self):
        items_found_scuba_simulator = self.stats["items_found_scuba_simulator"]
        return items_found_scuba_simulator

    @property
    def total_points_scuba_simulator(self):
        total_points_scuba_simulator = self.stats["total_points_scuba_simulator"]
        return total_points_scuba_simulator

    @property
    def max_wave(self):
        max_wave = self.stats["max_wave"]
        return max_wave

    @property
    def probHuntSeekerWins(self):
        prop_hunt_seeker_wins_hide_and_seek = self.stats["prop_hunt_seeker_wins_hide_and_seek"]
        return prop_hunt_seeker_wins_hide_and_seek

    @property
    def seekerWins(self):
        seeker_wins_hide_and_seek = self.stats["seeker_wins_hide_and_seek"]
        return seeker_wins_hide_and_seek

    @property
    def headshots_dayone(self):
        headshots_dayone = self.stats["headshots_dayone"]
        return headshots_dayone

    @property
    def kills_dayone(self):
        kills_dayone = self.stats["kills_dayone"]
        return kills_dayone

    @property
    def basic_zombie_kills_zombies(self):
        basic_zombie_kills_zombies = self.stats["basic_zombie_kills_zombies"]
        return basic_zombie_kills_zombies

    @property
    def best_round_zombies(self):
        best_round_zombies = self.stats["best_round_zombies"]
        return best_round_zombies

    @property
    def best_round_zombies_deadend(self):
        best_round_zombies_deadend = self.stats["best_round_zombies_deadend"]
        return best_round_zombies_deadend

    @property
    def best_round_zombies_deadend_normal(self):
        best_round_zombies_deadend_normal = self.stats["best_round_zombies_deadend_normal"]
        return best_round_zombies_deadend_normal

    @property
    def bullets_hit_zombies(self):
        bullets_hit_zombies = self.stats["bullets_hit_zombies"]
        return bullets_hit_zombies

    @property
    def bullets_shot_zombies(self):
        bullets_shot_zombies = self.stats["bullets_shot_zombies"]
        return bullets_shot_zombies

    @property
    def deaths_zombies(self):
        deaths_zombies = self.stats["deaths_zombies"]
        return deaths_zombies

    @property
    def deaths_zombies_deadend(self):
        deaths_zombies_deadend = self.stats["deaths_zombies_deadend"]
        return deaths_zombies_deadend

    @property
    def deaths_zombies_deadend_normal(self):
        deaths_zombies_deadend_normal = self.stats["deaths_zombies_deadend_normal"]
        return deaths_zombies_deadend_normal

    @property
    def doors_opened_zombies(self):
        doors_opened_zombies = self.stats["doors_opened_zombies"]
        return doors_opened_zombies

    @property
    def doors_opened_zombies_deadend(self):
        doors_opened_zombies_deadend = self.stats["doors_opened_zombies_deadend"]
        return doors_opened_zombies_deadend

    @property
    def doors_opened_zombies_deadend_normal(self):
        doors_opened_zombies_deadend_normal = self.stats["doors_opened_zombies_deadend_normal"]
        return doors_opened_zombies_deadend_normal

    @property
    def empowered_zombie_kills_zombies(self):
        empowered_zombie_kills_zombies = self.stats["empowered_zombie_kills_zombies"]
        return empowered_zombie_kills_zombies

    @property
    def headshots_zombies(self):
        headshots_zombies = self.stats["headshots_zombies"]
        return headshots_zombies

    @property
    def pig_zombie_zombie_kills_zombies(self):
        pig_zombie_zombie_kills_zombies = self.stats["pig_zombie_zombie_kills_zombies"]
        return pig_zombie_zombie_kills_zombies

    @property
    def times_knocked_down_zombies(self):
        times_knocked_down_zombies = self.stats["times_knocked_down_zombies"]
        return times_knocked_down_zombies

    @property
    def times_knocked_down_zombies_deadend(self):
        times_knocked_down_zombies_deadend = self.stats["times_knocked_down_zombies_deadend"]
        return times_knocked_down_zombies_deadend

    @property
    def times_knocked_down_zombies_deadend_normal(self):
        times_knocked_down_zombies_deadend_normal = self.stats["times_knocked_down_zombies_deadend_normal"]
        return times_knocked_down_zombies_deadend_normal

    @property
    def total_rounds_survived_zombies(self):
        total_rounds_survived_zombies = self.stats["total_rounds_survived_zombies"]
        return total_rounds_survived_zombies

    @property
    def total_rounds_survived_zombies_deadend(self):
        total_rounds_survived_zombies_deadend = self.stats["total_rounds_survived_zombies_deadend"]
        return total_rounds_survived_zombies_deadend

    @property
    def total_rounds_survived_zombies_deadend_normal(self):
        total_rounds_survived_zombies_deadend_normal = self.stats["total_rounds_survived_zombies_deadend_normal"]
        return total_rounds_survived_zombies_deadend_normal

    @property
    def windows_repaired_zombies(self):
        windows_repaired_zombies = self.stats["windows_repaired_zombies"]
        return windows_repaired_zombies

    @property
    def windows_repaired_zombies_deadend(self):
        windows_repaired_zombies_deadend = self.stats["windows_repaired_zombies_deadend"]
        return windows_repaired_zombies_deadend

    @property
    def windows_repaired_zombies_deadend_normal(self):
        windows_repaired_zombies_deadend_normal = self.stats["windows_repaired_zombies_deadend_normal"]
        return windows_repaired_zombies_deadend_normal

    @property
    def wolf_zombie_kills_zombies(self):
        wolf_zombie_kills_zombies = self.stats["wolf_zombie_kills_zombies"]
        return wolf_zombie_kills_zombies

    @property
    def zombie_kills_zombies(self):
        zombie_kills_zombies = self.stats["zombie_kills_zombies"]
        return zombie_kills_zombies

    @property
    def zombie_kills_zombies_deadend(self):
        zombie_kills_zombies_deadend = self.stats["zombie_kills_zombies_deadend"]
        return zombie_kills_zombies_deadend

    @property
    def zombie_kills_zombies_deadend_normal(self):
        zombie_kills_zombies_deadend_normal = self.stats["zombie_kills_zombies_deadend_normal"]
        return zombie_kills_zombies_deadend_normal

    @property
    def deaths_oneinthequiver(self):
        deaths_oneinthequiver = self.stats["deaths_oneinthequiver"]
        return deaths_oneinthequiver

    @property
    def candy_found_halloween_simulator(self):
        candy_found_halloween_simulator = self.stats["candy_found_halloween_simulator"]
        return candy_found_halloween_simulator

    @property
    def lastTourneyAd(self):
        lastTourneyAd = self.stats["lastTourneyAd"]
        return lastTourneyAd

    @property
    def best_round_zombies_alienarcadium(self):
        best_round_zombies_alienarcadium = self.stats["best_round_zombies_alienarcadium"]
        return best_round_zombies_alienarcadium

    @property
    def best_round_zombies_alienarcadium_normal(self):
        best_round_zombies_alienarcadium_normal = self.stats["best_round_zombies_alienarcadium_normal"]
        return best_round_zombies_alienarcadium_normal

    @property
    def blob_zombie_kills_zombies(self):
        blob_zombie_kills_zombies = self.stats["blob_zombie_kills_zombies"]
        return blob_zombie_kills_zombies

    @property
    def chgluglu_zombie_kills_zombies(self):
        chgluglu_zombie_kills_zombies = self.stats["chgluglu_zombie_kills_zombies"]
        return chgluglu_zombie_kills_zombies

    @property
    def clown_zombie_kills_zombies(self):
        clown_zombie_kills_zombies = self.stats["clown_zombie_kills_zombies"]
        return clown_zombie_kills_zombies

    @property
    def deaths_zombies_alienarcadium(self):
        deaths_zombies_alienarcadium = self.stats["deaths_zombies_alienarcadium"]
        return deaths_zombies_alienarcadium

    @property
    def deaths_zombies_alienarcadium_normal(self):
        deaths_zombies_alienarcadium_normal = self.stats["deaths_zombies_alienarcadium_normal"]
        return deaths_zombies_alienarcadium_normal

    @property
    def fastest_time_10_zombies(self):
        fastest_time_10_zombies = self.stats["fastest_time_10_zombies"]
        return fastest_time_10_zombies

    @property
    def fastest_time_10_zombies_alienarcadium_normal(self):
        fastest_time_10_zombies_alienarcadium_normal = self.stats["fastest_time_10_zombies_alienarcadium_normal"]
        return fastest_time_10_zombies_alienarcadium_normal

    @property
    def fastest_time_20_zombies(self):
        fastest_time_20_zombies = self.stats["fastest_time_20_zombies"]
        return fastest_time_20_zombies

    @property
    def fastest_time_20_zombies_alienarcadium_normal(self):
        fastest_time_20_zombies_alienarcadium_normal = self.stats["fastest_time_20_zombies_alienarcadium_normal"]
        return fastest_time_20_zombies_alienarcadium_normal

    @property
    def ghast_zombie_kills_zombies(self):
        ghast_zombie_kills_zombies = self.stats["ghast_zombie_kills_zombies"]
        return ghast_zombie_kills_zombies

    @property
    def giant_zombie_kills_zombies(self):
        giant_zombie_kills_zombies = self.stats["giant_zombie_kills_zombies"]
        return giant_zombie_kills_zombies

    @property
    def iron_golem_zombie_kills_zombies(self):
        iron_golem_zombie_kills_zombies = self.stats["iron_golem_zombie_kills_zombies"]
        return iron_golem_zombie_kills_zombies

    @property
    def mega_blob_zombie_kills_zombies(self):
        mega_blob_zombie_kills_zombies = self.stats["mega_blob_zombie_kills_zombies"]
        return mega_blob_zombie_kills_zombies

    @property
    def mega_magma_zombie_kills_zombies(self):
        mega_magma_zombie_kills_zombies = self.stats["mega_magma_zombie_kills_zombies"]
        return mega_magma_zombie_kills_zombies

    @property
    def rainbow_zombie_kills_zombies(self):
        rainbow_zombie_kills_zombies = self.stats["rainbow_zombie_kills_zombies"]
        return rainbow_zombie_kills_zombies

    @property
    def sentinel_zombie_kills_zombies(self):
        sentinel_zombie_kills_zombies = self.stats["sentinel_zombie_kills_zombies"]
        return sentinel_zombie_kills_zombies

    @property
    def skeleton_zombie_kills_zombies(self):
        skeleton_zombie_kills_zombies = self.stats["skeleton_zombie_kills_zombies"]
        return skeleton_zombie_kills_zombies

    @property
    def space_blaster_zombie_kills_zombies(self):
        space_blaster_zombie_kills_zombies = self.stats["space_blaster_zombie_kills_zombies"]
        return space_blaster_zombie_kills_zombies

    @property
    def space_grunt_zombie_kills_zombies(self):
        space_grunt_zombie_kills_zombies = self.stats["space_grunt_zombie_kills_zombies"]
        return space_grunt_zombie_kills_zombies

    @property
    def times_knocked_down_zombies_alienarcadium(self):
        times_knocked_down_zombies_alienarcadium = self.stats["times_knocked_down_zombies_alienarcadium"]
        return times_knocked_down_zombies_alienarcadium

    @property
    def times_knocked_down_zombies_alienarcadium_normal(self):
        times_knocked_down_zombies_alienarcadium_normal = self.stats["times_knocked_down_zombies_alienarcadium_normal"]
        return times_knocked_down_zombies_alienarcadium_normal

    @property
    def total_rounds_survived_zombies_alienarcadium(self):
        total_rounds_survived_zombies_alienarcadium = self.stats["total_rounds_survived_zombies_alienarcadium"]
        return total_rounds_survived_zombies_alienarcadium

    @property
    def total_rounds_survived_zombies_alienarcadium_normal(self):
        total_rounds_survived_zombies_alienarcadium_normal = self.stats["total_rounds_survived_zombies_alienarcadium_normal"]
        return total_rounds_survived_zombies_alienarcadium_normal

    @property
    def windows_repaired_zombies_alienarcadium(self):
        windows_repaired_zombies_alienarcadium = self.stats["windows_repaired_zombies_alienarcadium"]
        return windows_repaired_zombies_alienarcadium

    @property
    def windows_repaired_zombies_alienarcadium_normal(self):
        windows_repaired_zombies_alienarcadium_normal = self.stats["windows_repaired_zombies_alienarcadium_normal"]
        return windows_repaired_zombies_alienarcadium_normal

    @property
    def worm_small_zombie_kills_zombies(self):
        worm_small_zombie_kills_zombies = self.stats["worm_small_zombie_kills_zombies"]
        return worm_small_zombie_kills_zombies

    @property
    def worm_zombie_kills_zombies(self):
        worm_zombie_kills_zombies = self.stats["worm_zombie_kills_zombies"]
        return worm_zombie_kills_zombies

    @property
    def zombie_kills_zombies_alienarcadium(self):
        zombie_kills_zombies_alienarcadium = self.stats["zombie_kills_zombies_alienarcadium"]
        return zombie_kills_zombies_alienarcadium

    @property
    def zombie_kills_zombies_alienarcadium_normal(self):
        zombie_kills_zombies_alienarcadium_normal = self.stats["zombie_kills_zombies_alienarcadium_normal"]
        return zombie_kills_zombies_alienarcadium_normal

    @property
    def sw_deaths(self):
        sw_deaths = self.stats["sw_deaths"]
        return sw_deaths

    @property
    def sw_kills(self):
        sw_kills = self.stats["sw_kills"]
        return sw_kills

    @property
    def sw_rebel_kills(self):
        sw_rebel_kills = self.stats["sw_rebel_kills"]
        return sw_rebel_kills

    @property
    def sw_shots_fired(self):
        sw_shots_fired = self.stats["sw_shots_fired"]
        return sw_shots_fired

    @property
    def hitw_record_q(self):
        hitw_record_q = self.stats["hitw_record_q"]
        return hitw_record_q

    @property
    def rounds_hole_in_the_wall(self):
        rounds_hole_in_the_wall = self.stats["rounds_hole_in_the_wall"]
        return rounds_hole_in_the_wall

    @property
    def best_round_zombies_badblood(self):
        best_round_zombies_badblood = self.stats["best_round_zombies_badblood"]
        return best_round_zombies_badblood

    @property
    def best_round_zombies_badblood_normal(self):
        best_round_zombies_badblood_normal = self.stats["best_round_zombies_badblood_normal"]
        return best_round_zombies_badblood_normal

    @property
    def deaths_zombies_badblood(self):
        deaths_zombies_badblood = self.stats["deaths_zombies_badblood"]
        return deaths_zombies_badblood

    @property
    def deaths_zombies_badblood_normal(self):
        deaths_zombies_badblood_normal = self.stats["deaths_zombies_badblood_normal"]
        return deaths_zombies_badblood_normal

    @property
    def family_daughter_zombie_kills_zombies(self):
        family_daughter_zombie_kills_zombies = self.stats["family_daughter_zombie_kills_zombies"]
        return family_daughter_zombie_kills_zombies

    @property
    def slime_zombie_kills_zombies(self):
        slime_zombie_kills_zombies = self.stats["slime_zombie_kills_zombies"]
        return slime_zombie_kills_zombies

    @property
    def slime_zombie_zombie_kills_zombies(self):
        slime_zombie_zombie_kills_zombies = self.stats["slime_zombie_zombie_kills_zombies"]
        return slime_zombie_zombie_kills_zombies

    @property
    def times_knocked_down_zombies_badblood(self):
        times_knocked_down_zombies_badblood = self.stats["times_knocked_down_zombies_badblood"]
        return times_knocked_down_zombies_badblood

    @property
    def times_knocked_down_zombies_badblood_normal(self):
        times_knocked_down_zombies_badblood_normal = self.stats["times_knocked_down_zombies_badblood_normal"]
        return times_knocked_down_zombies_badblood_normal

    @property
    def total_rounds_survived_zombies_badblood(self):
        total_rounds_survived_zombies_badblood = self.stats["total_rounds_survived_zombies_badblood"]
        return total_rounds_survived_zombies_badblood

    @property
    def total_rounds_survived_zombies_badblood_normal(self):
        total_rounds_survived_zombies_badblood_normal = self.stats["total_rounds_survived_zombies_badblood_normal"]
        return total_rounds_survived_zombies_badblood_normal

    @property
    def werewolf_zombie_kills_zombies(self):
        werewolf_zombie_kills_zombies = self.stats["werewolf_zombie_kills_zombies"]
        return werewolf_zombie_kills_zombies

    @property
    def windows_repaired_zombies_badblood(self):
        windows_repaired_zombies_badblood = self.stats["windows_repaired_zombies_badblood"]
        return windows_repaired_zombies_badblood

    @property
    def windows_repaired_zombies_badblood_normal(self):
        windows_repaired_zombies_badblood_normal = self.stats["windows_repaired_zombies_badblood_normal"]
        return windows_repaired_zombies_badblood_normal

    @property
    def witch_zombie_kills_zombies(self):
        witch_zombie_kills_zombies = self.stats["witch_zombie_kills_zombies"]
        return witch_zombie_kills_zombies

    @property
    def zombie_kills_zombies_badblood(self):
        zombie_kills_zombies_badblood = self.stats["zombie_kills_zombies_badblood"]
        return zombie_kills_zombies_badblood

    @property
    def zombie_kills_zombies_badblood_normal(self):
        zombie_kills_zombies_badblood_normal = self.stats["zombie_kills_zombies_badblood_normal"]
        return zombie_kills_zombies_badblood_normal

    @property
    def doors_opened_zombies_alienarcadium(self):
        doors_opened_zombies_alienarcadium = self.stats["doors_opened_zombies_alienarcadium"]
        return doors_opened_zombies_alienarcadium

    @property
    def doors_opened_zombies_alienarcadium_normal(self):
        doors_opened_zombies_alienarcadium_normal = self.stats["doors_opened_zombies_alienarcadium_normal"]
        return doors_opened_zombies_alienarcadium_normal

    @property
    def players_revived_zombies(self):
        players_revived_zombies = self.stats["players_revived_zombies"]
        return players_revived_zombies

    @property
    def players_revived_zombies_alienarcadium(self):
        players_revived_zombies_alienarcadium = self.stats["players_revived_zombies_alienarcadium"]
        return players_revived_zombies_alienarcadium

    @property
    def players_revived_zombies_alienarcadium_normal(self):
        players_revived_zombies_alienarcadium_normal = self.stats["players_revived_zombies_alienarcadium_normal"]
        return players_revived_zombies_alienarcadium_normal

    @property
    def bounty_kills_oneinthequiver(self):
        bounty_kills_oneinthequiver = self.stats["bounty_kills_oneinthequiver"]
        return bounty_kills_oneinthequiver

    @property
    def kills_oneinthequiver(self):
        kills_oneinthequiver = self.stats["kills_oneinthequiver"]
        return kills_oneinthequiver

    @property
    def wins_oneinthequiver(self):
        wins_oneinthequiver = self.stats["wins_oneinthequiver"]
        return wins_oneinthequiver

    @property
    def rounds_simon_says(self):
        rounds_simon_says = self.stats["rounds_simon_says"]
        return rounds_simon_says

    @property
    def hider_wins_hide_and_seek(self):
        hider_wins_hide_and_seek = self.stats["hider_wins_hide_and_seek"]
        return hider_wins_hide_and_seek

    @property
    def party_pooper_hider_wins_hide_and_seek(self):
        party_pooper_hider_wins_hide_and_seek = self.stats["party_pooper_hider_wins_hide_and_seek"]
        return party_pooper_hider_wins_hide_and_seek

    @property
    def party_pooper_seeker_wins_hide_and_seek(self):
        party_pooper_seeker_wins_hide_and_seek = self.stats["party_pooper_seeker_wins_hide_and_seek"]
        return party_pooper_seeker_wins_hide_and_seek

    @property
    def kicks_soccer(self):
        kicks_soccer = self.stats["kicks_soccer"]
        return kicks_soccer

    @property
    def powerkicks_soccer(self):
        powerkicks_soccer = self.stats["powerkicks_soccer"]
        return powerkicks_soccer

    @property
    def prop_hunt_hider_wins_hide_and_seek(self):
        prop_hunt_hider_wins_hide_and_seek = self.stats["prop_hunt_hider_wins_hide_and_seek"]
        return prop_hunt_hider_wins_hide_and_seek

    @property
    def hitw_record_f(self):
        hitw_record_f = self.stats["hitw_record_f"]
        return hitw_record_f

    @property
    def wins_hole_in_the_wall(self):
        wins_hole_in_the_wall = self.stats["wins_hole_in_the_wall"]
        return wins_hole_in_the_wall

    @property
    def wins_party(self):
        wins_party = self.stats["wins_party"]
        return wins_party

    @property
    def fastest_time_10_zombies_deadend_normal(self):
        fastest_time_10_zombies_deadend_normal = self.stats["fastest_time_10_zombies_deadend_normal"]
        return fastest_time_10_zombies_deadend_normal

    @property
    def fire_zombie_kills_zombies(self):
        fire_zombie_kills_zombies = self.stats["fire_zombie_kills_zombies"]
        return fire_zombie_kills_zombies

    @property
    def magma_cube_zombie_kills_zombies(self):
        magma_cube_zombie_kills_zombies = self.stats["magma_cube_zombie_kills_zombies"]
        return magma_cube_zombie_kills_zombies

    @property
    def magma_zombie_kills_zombies(self):
        magma_zombie_kills_zombies = self.stats["magma_zombie_kills_zombies"]
        return magma_zombie_kills_zombies

    @property
    def players_revived_zombies_deadend(self):
        players_revived_zombies_deadend = self.stats["players_revived_zombies_deadend"]
        return players_revived_zombies_deadend

    @property
    def players_revived_zombies_deadend_normal(self):
        players_revived_zombies_deadend_normal = self.stats["players_revived_zombies_deadend_normal"]
        return players_revived_zombies_deadend_normal

    @property
    def tnt_baby_zombie_kills_zombies(self):
        tnt_baby_zombie_kills_zombies = self.stats["tnt_baby_zombie_kills_zombies"]
        return tnt_baby_zombie_kills_zombies

    @property
    def cave_spider_zombie_kills_zombies(self):
        cave_spider_zombie_kills_zombies = self.stats["cave_spider_zombie_kills_zombies"]
        return cave_spider_zombie_kills_zombies

    @property
    def doors_opened_zombies_badblood(self):
        doors_opened_zombies_badblood = self.stats["doors_opened_zombies_badblood"]
        return doors_opened_zombies_badblood

    @property
    def doors_opened_zombies_badblood_normal(self):
        doors_opened_zombies_badblood_normal = self.stats["doors_opened_zombies_badblood_normal"]
        return doors_opened_zombies_badblood_normal

    @property
    def fastest_time_10_zombies_badblood_normal(self):
        fastest_time_10_zombies_badblood_normal = self.stats["fastest_time_10_zombies_badblood_normal"]
        return fastest_time_10_zombies_badblood_normal

    @property
    def king_slime_zombie_kills_zombies(self):
        king_slime_zombie_kills_zombies = self.stats["king_slime_zombie_kills_zombies"]
        return king_slime_zombie_kills_zombies

    @property
    def wither_skeleton_zombie_kills_zombies(self):
        wither_skeleton_zombie_kills_zombies = self.stats["wither_skeleton_zombie_kills_zombies"]
        return wither_skeleton_zombie_kills_zombies

    @property
    def wither_zombie_zombie_kills_zombies(self):
        wither_zombie_zombie_kills_zombies = self.stats["wither_zombie_zombie_kills_zombies"]
        return wither_zombie_zombie_kills_zombies

    @property
    def wolf_pet_zombie_kills_zombies(self):
        wolf_pet_zombie_kills_zombies = self.stats["wolf_pet_zombie_kills_zombies"]
        return wolf_pet_zombie_kills_zombies

    @property
    def wins_simon_says(self):
        wins_simon_says = self.stats["wins_simon_says"]
        return wins_simon_says

    @property
    def wins_halloween_simulator(self):
        wins_halloween_simulator = self.stats["wins_halloween_simulator"]
        return wins_halloween_simulator

    @property
    def anvil_spleef_best_time_party(self):
        anvil_spleef_best_time_party = self.stats["anvil_spleef_best_time_party"]
        return anvil_spleef_best_time_party

    @property
    def jigsaw_rush_best_time_party(self):
        jigsaw_rush_best_time_party = self.stats["jigsaw_rush_best_time_party"]
        return jigsaw_rush_best_time_party

    @property
    def animal_slaughter_best_score_party(self):
        animal_slaughter_best_score_party = self.stats["animal_slaughter_best_score_party"]
        return animal_slaughter_best_score_party

    @property
    def animal_slaughter_kills_party(self):
        animal_slaughter_kills_party = self.stats["animal_slaughter_kills_party"]
        return animal_slaughter_kills_party

    @property
    def animal_slaughter_round_wins_party(self):
        animal_slaughter_round_wins_party = self.stats["animal_slaughter_round_wins_party"]
        return animal_slaughter_round_wins_party

    @property
    def bombardment_best_time_party(self):
        bombardment_best_time_party = self.stats["bombardment_best_time_party"]
        return bombardment_best_time_party

    @property
    def cannon_painting_round_wins_party(self):
        cannon_painting_round_wins_party = self.stats["cannon_painting_round_wins_party"]
        return cannon_painting_round_wins_party

    @property
    def chicken_rings_best_time_party(self):
        chicken_rings_best_time_party = self.stats["chicken_rings_best_time_party"]
        return chicken_rings_best_time_party

    @property
    def chicken_rings_round_wins_party(self):
        chicken_rings_round_wins_party = self.stats["chicken_rings_round_wins_party"]
        return chicken_rings_round_wins_party

    @property
    def round_wins_party(self):
        round_wins_party = self.stats["round_wins_party"]
        return round_wins_party

    @property
    def rpg_16_kills_best_score_party(self):
        rpg_16_kills_best_score_party = self.stats["rpg_16_kills_best_score_party"]
        return rpg_16_kills_best_score_party

    @property
    def rpg_16_kills_party(self):
        rpg_16_kills_party = self.stats["rpg_16_kills_party"]
        return rpg_16_kills_party

    @property
    def rpg_16_round_wins_party(self):
        rpg_16_round_wins_party = self.stats["rpg_16_round_wins_party"]
        return rpg_16_round_wins_party

    @property
    def total_stars_party(self):
        total_stars_party = self.stats["total_stars_party"]
        return total_stars_party

    @property
    def trampolinio_round_wins_party(self):
        trampolinio_round_wins_party = self.stats["trampolinio_round_wins_party"]
        return trampolinio_round_wins_party

    @property
    def avalanche_round_wins_party(self):
        avalanche_round_wins_party = self.stats["avalanche_round_wins_party"]
        return avalanche_round_wins_party

    @property
    def high_ground_best_score_party(self):
        high_ground_best_score_party = self.stats["high_ground_best_score_party"]
        return high_ground_best_score_party

    @property
    def high_ground_total_score_party(self):
        high_ground_total_score_party = self.stats["high_ground_total_score_party"]
        return high_ground_total_score_party

    @property
    def hoe_hoe_hoe_round_wins_party(self):
        hoe_hoe_hoe_round_wins_party = self.stats["hoe_hoe_hoe_round_wins_party"]
        return hoe_hoe_hoe_round_wins_party

    @property
    def hoe_hoe_hoe_total_score_party(self):
        hoe_hoe_hoe_total_score_party = self.stats["hoe_hoe_hoe_total_score_party"]
        return hoe_hoe_hoe_total_score_party

    @property
    def shooting_range_round_wins_party(self):
        shooting_range_round_wins_party = self.stats["shooting_range_round_wins_party"]
        return shooting_range_round_wins_party

    @property
    def the_floor_is_lava_best_time_party(self):
        the_floor_is_lava_best_time_party = self.stats["the_floor_is_lava_best_time_party"]
        return the_floor_is_lava_best_time_party

    @property
    def spider_maze_best_time_party(self):
        spider_maze_best_time_party = self.stats["spider_maze_best_time_party"]
        return spider_maze_best_time_party

    @property
    def workshop_round_wins_party(self):
        workshop_round_wins_party = self.stats["workshop_round_wins_party"]
        return workshop_round_wins_party

    @property
    def jungle_jump_best_time_party(self):
        jungle_jump_best_time_party = self.stats["jungle_jump_best_time_party"]
        return jungle_jump_best_time_party

    @property
    def jungle_jump_round_wins_party(self):
        jungle_jump_round_wins_party = self.stats["jungle_jump_round_wins_party"]
        return jungle_jump_round_wins_party

    @property
    def lab_escape_best_time_party(self):
        lab_escape_best_time_party = self.stats["lab_escape_best_time_party"]
        return lab_escape_best_time_party

    @property
    def minecart_racing_best_time_party(self):
        minecart_racing_best_time_party = self.stats["minecart_racing_best_time_party"]
        return minecart_racing_best_time_party

    @property
    def minecart_racing_round_wins_party(self):
        minecart_racing_round_wins_party = self.stats["minecart_racing_round_wins_party"]
        return minecart_racing_round_wins_party

    @property
    def the_floor_is_lava_round_wins_party(self):
        the_floor_is_lava_round_wins_party = self.stats["the_floor_is_lava_round_wins_party"]
        return the_floor_is_lava_round_wins_party

    @property
    def lab_escape_round_wins_party(self):
        lab_escape_round_wins_party = self.stats["lab_escape_round_wins_party"]
        return lab_escape_round_wins_party

    @property
    def gifts_grinch_simulator_v2(self):
        gifts_grinch_simulator_v2 = self.stats["gifts_grinch_simulator_v2"]
        return gifts_grinch_simulator_v2

    @property
    def eggs_found_easter_simulator(self):
        eggs_found_easter_simulator = self.stats["eggs_found_easter_simulator"]
        return eggs_found_easter_simulator

    @property
    def fire_leapers_round_wins_party(self):
        fire_leapers_round_wins_party = self.stats["fire_leapers_round_wins_party"]
        return fire_leapers_round_wins_party

    @property
    def pig_jousting_round_wins_party(self):
        pig_jousting_round_wins_party = self.stats["pig_jousting_round_wins_party"]
        return pig_jousting_round_wins_party

    @property
    def pig_fishing_round_wins_party(self):
        pig_fishing_round_wins_party = self.stats["pig_fishing_round_wins_party"]
        return pig_fishing_round_wins_party

    @property
    def super_sheep_round_wins_party(self):
        super_sheep_round_wins_party = self.stats["super_sheep_round_wins_party"]
        return super_sheep_round_wins_party

    @property
    def dive_best_score_party(self):
        dive_best_score_party = self.stats["dive_best_score_party"]
        return dive_best_score_party

    @property
    def dive_total_score_party(self):
        dive_total_score_party = self.stats["dive_total_score_party"]
        return dive_total_score_party

    @property
    def lawn_moower_mowed_best_score_party(self):
        lawn_moower_mowed_best_score_party = self.stats["lawn_moower_mowed_best_score_party"]
        return lawn_moower_mowed_best_score_party

    @property
    def lawn_moower_mowed_total_score_party(self):
        lawn_moower_mowed_total_score_party = self.stats["lawn_moower_mowed_total_score_party"]
        return lawn_moower_mowed_total_score_party

    @property
    def packages(self):
        packages = self.stats["packages"]
        return packages

    @property
    def pixel_party_games_played(self):
        games_played = self.stats["pixel_party"]["games_played"]
        return games_played

    @property
    def pixel_party_games_played_normal(self):
        games_played_normal = self.stats["pixel_party"]["games_played_normal"]
        return games_played_normal

    @property
    def pixel_party_highest_round(self):
        highest_round = self.stats["pixel_party"]["highest_round"]
        return highest_round

    @property
    def pixel_party_rounds_completed(self):
        rounds_completed = self.stats["pixel_party"]["rounds_completed"]
        return rounds_completed

    @property
    def pixel_party_rounds_completed_normal(self):
        rounds_completed_normal = self.stats["pixel_party"]["rounds_completed_normal"]
        return rounds_completed_normal

class HungerGamesStats():

    def __init__(self, data):
        self.stats = data

    @property
    def packages(self):
        packages = self.stats["packages"]
        return packages

    @property
    def chests_opened(self):
        chests_opened = self.stats["chests_opened"]
        return chests_opened

    @property
    def damage_taken_jockey(self):
        damage_taken_jockey = self.stats["damage_taken_jockey"]
        return damage_taken_jockey

    @property
    def deaths(self):
        deaths = self.stats["deaths"]
        return deaths

    @property
    def chests_opened_jockey(self):
        chests_opened_jockey = self.stats["chests_opened_jockey"]
        return chests_opened_jockey

    @property
    def games_played_jockey(self):
        games_played_jockey = self.stats["games_played_jockey"]
        return games_played_jockey

    @property
    def damage_taken(self):
        damage_taken = self.stats["damage_taken"]
        return damage_taken

    @property
    def time_played(self):
        time_played = self.stats["time_played"]
        return time_played

    @property
    def time_played_jockey(self):
        time_played_jockey = self.stats["time_played_jockey"]
        return time_played_jockey

    @property
    def games_played(self):
        games_played = self.stats["games_played"]
        return games_played

    @property
    def damage_taken_knight(self):
        damage_taken_knight = self.stats["damage_taken_knight"]
        return damage_taken_knight

    @property
    def damage(self):
        damage = self.stats["damage"]
        return damage

    @property
    def time_played_knight(self):
        time_played_knight = self.stats["time_played_knight"]
        return time_played_knight

    @property
    def damage_knight(self):
        damage_knight = self.stats["damage_knight"]
        return damage_knight

    @property
    def games_played_knight(self):
        games_played_knight = self.stats["games_played_knight"]
        return games_played_knight

    @property
    def coins(self):
        coins = self.stats["coins"]
        return coins

    @property
    def wins_teams_normal(self):
        wins_teams_normal = self.stats["wins_teams_normal"]
        return wins_teams_normal

    @property
    def wins(self):
        wins = self.stats["wins"]
        return wins

    @property
    def wins_backup(self):
        wins_backup = self.stats["wins_backup"]
        return wins_backup

    @property
    def wins_solo_normal(self):
        wins_solo_normal = self.stats["wins_solo_normal"]
        return wins_solo_normal

    @property
    def autoarmor(self):
        autoarmor = self.stats["autoarmor"]
        return autoarmor

    @property
    def lastTourneyAd(self):
        lastTourneyAd = self.stats["lastTourneyAd"]
        return lastTourneyAd

    @property
    def exp_knight(self):
        exp_knight = self.stats["exp_knight"]
        return exp_knight

    @property
    def kills(self):
        kills = self.stats["kills"]
        return kills

    @property
    def kills_knight(self):
        kills_knight = self.stats["kills_knight"]
        return kills_knight

    @property
    def kills_solo_normal(self):
        kills_solo_normal = self.stats["kills_solo_normal"]
        return kills_solo_normal

    @property
    def potions_thrown(self):
        potions_thrown = self.stats["potions_thrown"]
        return potions_thrown

    @property
    def potions_thrown_knight(self):
        potions_thrown_knight = self.stats["potions_thrown_knight"]
        return potions_thrown_knight

class Guild():

    def __init__(self, data):
        self.guildData = data

    @classmethod
    def setID(self, id):
        self.id = id
        guildinfo = requests.get(f"https://api.hypixel.net/guild?key={chooseapikey()}&id={self.id}").json()
        self.guildData = guildinfo["guild"]

    @classmethod
    def setName(self, name):
        self.name = name
        guildinfo = requests.get(f"https://api.hypixel.net/guild?key={chooseapikey()}&name={self.name}").json()
        self.guildData = guildinfo["guild"]

    @property
    def name(self):
        name = self.guildData["name"]
        return name

    @property
    def lowerName(self):
        name_lower = self.guildData["name_lower"]
        return name_lower

    @property
    def coins(self):
        coins = self.guildData["coins"]
        return coins

    @property
    def coinsEver(self):
        coinsEver = self.guildData["coinsEver"]
        return coinsEver

    @property
    def created(self):
        created = self.guildData["created"]
        return created

    @property
    def exp(self):
        exp = self.guildData["exp"]
        return exp

    @property
    def description(self):
        description = self.guildData["description"]
        return description

    @property
    def chatMute(self):
        chatMute = self.guildData["chatMute"]
        return chatMute

    @property
    def tag(self):
        tag = self.guildData["tag"]
        return tag

    @property
    def achievements(self):
        achievements = self.guildData["achievements"]
        return achievements

    @property
    def members(self):
        members = self.guildData["members"]
        guildMembers = []
        for member in members:
            for rank in self.guildData["ranks"]:
                if rank["name"] == member["rank"]:
                    grank = GuildRank(rank)
                    member["rank"] = grank
            gmember = GuildMember(member)
            guildMembers.append(gmember)
        return guildMembers
    
    @property
    def ranks(self):
        ranks = self.guildData["ranks"]
        guildRankds = []
        for rank in ranks:
            grank = GuildRank(rank)
            guildRankds.append(grank)
        return guildRankds
        
    @property
    def preferedGames(self):
        preferredGames = self.guildData["preferredGames"]
        return preferredGames
            
    @property
    def tagColor(self):
        tagColor = self.guildData["tagColor"]
        return tagColor
                
    @property
    def guildExpByGameType(self):
        guildExpByGameType = self.guildData["guildExpByGameType"]
        return guildExpByGameType
    
    @classmethod
    def getMember(self, uuid):
        members = self.guildData["members"]
        for member in members:
            if member["uuid"] == uuid:
                return member
        return None

class GuildMember():

    def __init__(self, data):
        self.memberData = data

    @property
    def uuid(self):
        uuid = self.memberData["uuid"]
        return uuid

    @property
    def rank(self):
        rank = self.memberData["rank"]
        return rank

    @property
    def joined(self):
        joined = self.memberData["joined"]
        return joined

    @property
    def questParticipation(self):
        questParticipation = self.memberData["questParticipation"]
        return questParticipation

    @property
    def mutedTill(self):
        mutedTill = self.memberData["mutedTill"]
        return mutedTill

    @property
    def expHistory(self):
        expHistory = self.memberData["expHistory"]
        return expHistory

class GuildRank():

    def __init__(self, data):
        self.memberData = data

    @property
    def name(self):
        name = self.memberData["name"]
        return name

    @property
    def default(self):
        default = self.memberData["default"]
        return default

    @property
    def tag(self):
        tag = self.memberData["tag"]
        return tag

    @property
    def created(self):
        created = self.memberData["created"]
        return created

    @property
    def priority(self):
        priority = self.memberData["priority"]
        return priority

class Achievement():

    def __init__(self, data):
        self.achievementData = data

    @property
    def points(self):
        points = self.achievementData["points"]
        return points

    @property
    def name(self):
        name = self.achievementData["name"]
        return name

    @property
    def description(self):
        description = self.achievementData["description"]
        return description

    @property
    def gamePercentUnlocked(self):
        gamePercentUnlocked = self.achievementData["gamePercentUnlocked"]
        return gamePercentUnlocked

    @property
    def globalPercentUnlocked(self):
        globalPercentUnlocked = self.achievementData["globalPercentUnlocked"]
        return globalPercentUnlocked

class TieredAchievement():
    
    def __init__(self, data):
        self.achievementData = data

    @property
    def name(self):
        name = self.achievementData["name"]
        return name

    @property
    def description(self):
        description = self.achievementData["description"]
        return description

    @property
    def gamePercentUnlocked(self):
        gamePercentUnlocked = self.achievementData["gamePercentUnlocked"]
        return gamePercentUnlocked

    @property
    def globalPercentUnlocked(self):
        globalPercentUnlocked = self.achievementData["globalPercentUnlocked"]
        return globalPercentUnlocked

    @property
    def tiers(self):
        tiers = self.achievementData["tiers"]
        return tiers

    @property
    def legacy(self):
        legacy = self.achievementData["legacy"]
        return legacy

class AchievementTier():
    
    def __init__(self, data):
        self.achievementTierData = data

    @property
    def tier(self):
        tier = self.achievementTierData["tier"]
        return tier

    @property
    def points(self):
        points = self.achievementTierData["points"]
        return points

    @property
    def amount(self):
        amount = self.achievementTierData["amount"]
        return amount
    
    @property
    def legacy(self):
        legacy = self.achievementTierData["legacy"]
        return legacy

class Challenge():
    
    def __init__(self, data):
        self.challengeData = data

    @property
    def id(self):
        id = self.challengeData["id"]
        return id

    @property
    def name(self):
        name = self.challengeData["name"]
        return name

    @property
    def rewards(self):
        rewards = self.challengeData["rewards"]
        return rewards

class ChallengeReward():
    
    def __init__(self, data):
        self.challengeRewardData = data

    @property
    def type(self):
        type = self.challengeRewardData["type"]
        return type

    @property
    def amount(self):
        amount = self.challengeRewardData["amount"]
        return amount
