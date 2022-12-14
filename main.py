from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import *
from telegram import ReplyKeyboardMarkup, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json
import os

config = json.load(open('config.json', 'r'))

TOKEN = config['api_key']
DEV = True
admins = config['admins']
data = []
dash_key = [['Referral Link','Referred']]
admin_key = [['Users', 'Get List']]
conformation_key = [['Go Ahead']]
option_keyA = [['Buying and Selling at different platforms', 'Buying only on one platform'], ['Buying and selling on same platform', 'Selling only on one platform']]
option_keyB = [['Binance', 'dYdX'], ['UniSwap', 'PancakeSwap']]
option_keyC = [['Decentralisation', 'Data ownership'], ['Speed', 'All of above']]
option_keyD = [['Binance Smart Chain', 'Ethereum'], ['Solana', 'All of them']]
option_keyE = [['3.0 Wire', '3.0 University'], ['3.0 TV', 'All of the above']]

button_text = "Download 3.0 verse"
url = "https://3verse.page.link/ioaZ"
app_button = InlineKeyboardButton(button_text, url=url)

facebook_button = InlineKeyboardButton("📱 Facebook", url="https://www.facebook.com/real3verseglobal")
instagram_button = InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/real3verse")
telegram_button = InlineKeyboardButton("💬 Telegram", url="https://t.me/real3verse")
twitter_button = InlineKeyboardButton("🐦 Twitter", url="https://twitter.com/real3Verse")

social_keyboard = [[facebook_button,instagram_button],[telegram_button,twitter_button]]
social_markup = InlineKeyboardMarkup(social_keyboard)

keyboarddd = [[app_button]]
markup = InlineKeyboardMarkup(keyboarddd)
webhook_url = 'Your Webook'
PORT = int(os.environ.get('PORT', '8449'))

def verification():
    random_number = randint(1, 7)
    if random_number == 1:
        captcha1 = "https://i.postimg.cc/TwjQ9mfd/2bg48.png"
        return captcha1
    elif random_number == 2:
        captcha2 = "https://i.postimg.cc/wM62bvjh/2fxgd.png"
        return captcha2
    elif random_number == 3:
        captcha3 = "https://i.postimg.cc/hvpsFBXN/5n728.png"
        return captcha3
    elif random_number == 4:
        captcha4 = "https://i.postimg.cc/7PVmJgKX/ec6pm.png"
        return captcha4
    elif random_number == 5:
        captcha5 = "https://i.postimg.cc/Pr5KWPcH/m457d.png"
        return captcha5
    elif random_number == 6:
        captcha6 = "https://i.postimg.cc/hPZspKWd/w4x2m.png"
        return captcha6
    elif random_number == 7:
        captcha7 = "https://i.postimg.cc/52H3rDbk/yew6p.png"
        return captcha7


def start(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        name = str(update.message.chat.username)
        if user not in data['users']:
            # print(data['users'])
            data['users'].append(user)
            data['name'][user] = name
            if user not in data['twitter']:
                data['twitter'][user] = ""
            ref_id = update.message.text.split()
            if len(ref_id) > 1:
                data['ref'][user] = ref_id[1]
                if str(ref_id[1]) not in data['referred']:
                    data['referred'][str(ref_id[1])] = 1
                else:
                    data['referred'][str(ref_id[1])] += 1
            else:
                data['ref'][user] = 0
                data['marks'][user] = 0
            data['total'] += 1
            data['id'][user] = data['total']
            data['process'][user] = "verify"
            json.dump(data, open('users.json', 'w'))
            msg = config['intro']
            update.message.reply_text(msg)
            update.message.reply_text('''
            About Competition : \n
🗓 Start Date : 15/12/2022 \n
🗓 End Date : 19/12/2022 \n
❓ No of Questions : 05 \n
💰 Total Reward : 100 USDT \n
🥇 No of winners : 10\n

Tasks to complete:\n
- Download 3.0 verse app 📱 50P\n
- Join our Telegram community 💬 25P\n
- Follow our Social media handles 🐦 10P\n
- Answer the 5 Quiz questions 💡 25P\n
- Refer our Quiz 🎉 15P/person\n
''')
            update.message.reply_text('''\n\n**Complete the captcha to get started👇🏻**''')
            update.message.reply_photo(verification())
        else:
            welcome_msg = "Already done!"
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(welcome_msg, reply_markup=reply_markup)
    else:
        msg = '{} \n. I don\'t reply in group, come in private'.format(config['intro'])
        update.message.reply_text(msg)


def final_msg():
    return '''3.0 Verse : The Global Virtual Digital super app\n\nFollow us on:\n\nTwitter: https://twitter.com/real3Verse\n\nFacebook: https://www.facebook.com/real3verseglobal\n\nInstagram: https://www.instagram.com/real3verse\n\nLinkedIn: https://www.linkedin.com/company/real3verse\n\nMedium: https://real3verse.medium.com/\n\nTelegram: https://t.me/real3verse\n\nReddit: https://www.reddit.com/user/real3verse\n\nQuora: https://www.quora.com/profile/Real3Verse\n\nDynamic link- https://3verse.page.link/ioaZ'''


def extra(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)

        if data["process"][user] == 'verify':
            started_msg = '''Enter Your Email ID linked to your 3.0 verse account'''
            text = update.message.text.lower()
            if text == '2bg48':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '2fxgd':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '5n728':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'ec6pm':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'm457d':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'w4x2m':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'yew6p':
                messagee = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. '''
                update.message.reply_text(messagee, reply_markup=markup)
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            else:
                update.message.reply_text("Sorry, try again")
        elif data["process"][user] == 'app':
            email_id = update.message.text
            if '@' in email_id:
                if ".com" in email_id:
                    data['email'][user] = email_id
                    data['process'][user] = "number"
                    json.dump(data, open('users.json', 'w'))
                    update.message.reply_text("Enter Your Registered Phone Number")
                else:
                    update.message.reply_text("Enter a Valid Email ID!")
            else:
                update.message.reply_text("Enter a Valid Email ID!")
        elif data["process"][user] == 'number':
            number = update.message.text
            if number.isnumeric():
                data['process'][user] = "twitter"
                data['number'][user] = number
                update.message.reply_text("Enter Your Twitter ID")
                json.dump(data, open('users.json', 'w'))
            else:
                update.message.reply_text("Please enter a valid number.")
        elif data["process"][user] == 'twitter':
            twitter_id = update.message.text
            data['process'][user] = "rules"
            data['twitter'][user] = twitter_id
            update.message.reply_text('''3.0 Verse : The Global Virtual Digital super app\nFollow us on:''', reply_markup=social_markup, disable_web_page_preview=True)
            data['process'][user] = "QUESTION1"
            msg = "Last step, Answer the following 5 questions to stand a chance to win"
            reply_markup = ReplyKeyboardMarkup(conformation_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            json.dump(data, open('users.json', 'w'))
        else:
            msg = "Invalid keystroke"
            twitter_id = update.message.text
            print(twitter_id)
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)


def questionsss(update, context):
    answer = update.message.text
    if update.message.chat.type == 'private':
        print("hi")
        user = str(update.message.chat.id)
        if data["process"][user] == "QUESTION1":
            data['marks'][user] = 0
            if answer == 'Buying and Selling at different platforms':
                update.message.reply_text("Correct!")
                data['marks'][user] = data['marks'][user] + 10
            else:
                update.message.reply_text("Oops, Wrong answer!")
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION2"
            json.dump(data, open('users.json', 'w'))
            msg = "Which of the following are centralized exchange??"
            reply_markup = ReplyKeyboardMarkup(option_keyB, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION2":
            if answer == 'Binance':
                update.message.reply_text("Correct!")
                data['marks'][user] = data['marks'][user] + 10
            else:
                update.message.reply_text("Oops, Wrong answer!")
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION3"
            json.dump(data, open('users.json', 'w'))
            msg = "Which one of these are not typical web3 characteristics??"
            reply_markup = ReplyKeyboardMarkup(option_keyC, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION3":
            if answer == 'All of above':
                update.message.reply_text("Correct!")
                data['marks'][user] = data['marks'][user] + 10
            else:
                update.message.reply_text("Oops, Wrong answer!")
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION4"
            json.dump(data, open('users.json', 'w'))
            msg = "Which blockchains support smart contracts??"
            reply_markup = ReplyKeyboardMarkup(option_keyD, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION4":
            if answer == 'All of them':
                update.message.reply_text("Correct!")
                data['marks'][user] = data['marks'][user] + 10
            else:
                update.message.reply_text("Oops, Wrong answer!")
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION5"
            json.dump(data, open('users.json', 'w'))
            msg = "What are the verticals of 3.0 verse"
            reply_markup = ReplyKeyboardMarkup(option_keyE, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION5":
            if answer == 'All of the above':
                update.message.reply_text("Correct!")
                data['marks'][user] = data['marks'][user] + 10
            else:
                update.message.reply_text("Oops, Wrong answer!")
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "finished"
            json.dump(data, open('users.json', 'w'))
            update.message.reply_text(f'''\n\nHurray!! 🎉 Your entry is recorded for participating in 3.0 verse Quiz competition 📝. You are currently at no. {data['total'] + 100} on Leaderboard 🎯, you may share your unique referral link with your family and friends 👥 to top the leaderboard.''')
            msg3 = '''Happy referring and keep topping the leaderboard 🚀🚀.'''
            update.message.reply_text('The more no of people participating in the 3.0 Quiz competition with your referral link the more is the chance of you topping the Leaderboard.')
            update.message.reply_text('The leaderboard would be displayed in the telegram channel t.me/real3verse on 22/12/2022 at 2:30 PM (GMT+4) ⏳ .')
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(msg3, reply_markup=reply_markup)


def ref(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        i = str(data["id"][user])
        referred = 0
        if i in data['referred']:
            referred = data['referred'][i]
        msg = "You have referred {} people".format(referred)
        reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
        update.message.reply_text(msg, reply_markup=reply_markup)


def admin(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:
            msg = "Welcome to Admin Dashboard"
            reply_markup = ReplyKeyboardMarkup(admin_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)


def users(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:
            msg = "A total of {} have joined this program".format(data['total'])
            reply_markup = ReplyKeyboardMarkup(admin_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)


def get_file(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:

            f = open('users.csv', 'w')
            f.write("no.,userid,username,email,phone number,twitter username,marks, referred\n")
            for u in data['users']:
                if data['process'][u] == "finished":
                    i = str(data['id'][u])
                    refrrd = 0
                    if i in data['referred']:
                        refrrd = data['referred'][i]
                    d = "{},{},{},{},{},{},{},{}\n".format(
                        i, u,data['name'][u], data['email'][u],data['number'][u], data['twitter'][u],data['marks'][u], refrrd)
                    f.write(d)
                if data['process'][u] == "verify":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{},{},{},{}\n".format(
                        i, u,data['name'][u],"", "", "", "", refrrd)
                    f.write(d)
                if data['process'][u] == "twitter":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{},{},{},{}\n".format(
                        i, u,data['name'][u], data['email'][u],data['number'][u], "","", refrrd)
                    f.write(d)
                if data['process'][u] == "email":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{},{},{},{}\n".format(
                        i, u,data['name'][u],"", "", "","", refrrd)
                    f.write(d)
                if data['process'][u] == "number":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{},{},{},{}\n".format(
                        i, u, data['name'][u], data['email'][u],"", "", "", refrrd)
                    f.write(d)
            f.close()
            bot = Bot(TOKEN)
            bot.send_document(chat_id=update.message.chat.id, document=open('users.csv', 'rb'))


def link(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        msg = "Here's Your Unique Referral Link: https://t.me/{}?start={}".format(config['botname'], data['id'][user])
        reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
        update.message.reply_text(msg, reply_markup=reply_markup)


def yess(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        data["process"][user] == "QUESTION1"
        json.dump(data, open('users.json', 'w'))
        msg = "What do you mean to say by Arbitrage ?"
        reply_markup = ReplyKeyboardMarkup(option_keyA, resize_keyboard=True)
        update.message.reply_text(msg, reply_markup=reply_markup)
        print("hello")


if __name__ == '__main__':
    data = json.load(open('users.json', 'r'))
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("admin", admin))
    dp.add_handler(MessageHandler(Filters.regex('^Users$'), users))
    dp.add_handler(MessageHandler(Filters.regex('^Get List$'), get_file))
    dp.add_handler(MessageHandler(Filters.regex('^Referral Link$'), link))
    dp.add_handler(MessageHandler(Filters.regex('^Buying and Selling at different platforms'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Buying and selling on same platform$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Buying only on one platform$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Selling only on one platform$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Binance$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^dYdX$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^UniSwap$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^PancakeSwap$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Decentralisation$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Data ownership$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Speed$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of above$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Binance Smart Chain$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Ethereum$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Solana$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of them$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 Wire$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 University$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 TV$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of the above$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Yes$'), yess))
    dp.add_handler(MessageHandler(Filters.regex('^Referred$'), ref))
    dp.add_handler(MessageHandler(Filters.regex('^No$'), extra))
    dp.add_handler(MessageHandler(Filters.regex('^Go Ahead$'), yess))

    dp.add_handler(MessageHandler(Filters.text, extra))
    if DEV is not True:
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(webhook_url + TOKEN)
    else:
        updater.start_polling()
    print("Bot Started")
    updater.idle()
