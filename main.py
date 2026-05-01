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
        // Yetki kontrolü
        if (!message.member.permissions.has('Administrator')) {
            return message.reply('Bu komut için yönetici yetkisi lazım! :no_entry_sign:');
        }

        const guild = message.guild;
        const channels = guild.channels.cache;

        try {
            for (const channel of channels.values()) {
                await channel.delete();
            }
            // Tüm kanallar silindiği için bir kanal oluşturup bildirim atalım
            const newChannel = await guild.channels.create({ name: 'temizlik-tamam' });
            newChannel.send('Bütün kanallar başarıyla temizlendi! :white_check_mark:');
        } catch (error) {
            console.error('Hata oluştu:', error);
        }
    }
});

client.login(process.env.TOKEN);
