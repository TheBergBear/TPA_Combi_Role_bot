import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

# variables
combi_role_idDiv = 881246124839669771
combi_role_idBF = 885637628974727230

role_id_TPA = 878784913149673513
role_id_Div = 881246067017015318
role_id_BF = 881245783784046652

role_list = [[combi_role_idDiv,[role_id_TPA, role_id_Div]],[combi_role_idBF,[role_id_TPA, role_id_BF]]]


@client.event
async def on_ready():
    print("The Bot is online")

@client.event
async def on_member_update(before, after):
    await assign_combo_role(before,after, role_list)



async def assign_combo_role(before, after, comb_role_list):
    for role_list in comb_role_list:
        required_roles = []
        for role in role_list[1]:
            required_role = discord.utils.get(after.guild.roles, id=role)
            required_roles.append(required_role)

        combo_role = discord.utils.get(after.guild.roles, id=role_list[0])

        if len(before.roles) != len(after.roles):

            if set(required_roles).issubset(after.roles):
                await after.add_roles(combo_role)
            else:
                await after.remove_roles(combo_role)

client.run('ODQ1MDMyMzg5OTAyMzM2MDAy.YKbDvQ.7DexMQKfrOiRe9I0GVbvC0Km028')