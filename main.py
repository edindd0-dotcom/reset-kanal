const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

client.on('ready', () => {
    console.log(`${client.user.tag} aktif! :rocket:`);
});

client.on('messageCreate', async (message) => {
    if (message.content === '.silkanal') {
        if (!message.member.permissions.has('Administrator')) {
            return message.reply('yönetici yetkin yok! :no_entry_sign:');
        }

        try {
            const channels = message.guild.channels.cache;
            for (const channel of channels.values()) {
                await channel.delete();
            }
            const newChannel = await message.guild.channels.create({ name: 'islem-tamam' });
            newChannel.send('bütün kanallar silindi. :white_check_mark:');
        } catch (err) {
            console.error(err);
        }
    }
});

client.login(process.env.TOKEN);
