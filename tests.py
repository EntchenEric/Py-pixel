import hypixel

hypixel.setkeys(["60f7a5cd-1f78-4917-9347-62f431be6f5c"])

dennis = hypixel.Player("992daae1-237b-4459-bb82-b26332c9fbd9")

guild = dennis.guild

for member in guild.members:
    gmember = hypixel.Player(member.uuid)
    print(gmember.displayname)
    print(member.rank.name)