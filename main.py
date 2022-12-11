from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import *
from telegram import ReplyKeyboardMarkup, Bot
import json
import os

config = json.load(open('config.json', 'r'))

TOKEN = config['api_key']
DEV = True
signup = config['signup']
refr = config['ref']
admins = config['admins']
data = []
dash_key = [['Referral Link','Referred']]
admin_key = [['Users', 'Get List']]
option_keyA = [['Buying and selling @ different platforms', 'Trading'], ['Buying and selling @ same platform', 'None']]
option_keyB = [['Binance', 'dYdX'], ['UniSwap', 'PancakeSwap']]
option_keyC = [['Decentralisation', 'Data ownership'], ['Speed', 'All of above']]
option_keyD = [['Bitcoin', 'Ethereum'], ['Solana', 'All of them']]
option_keyE = [['3.0 Wire', '3.0 University'], ['3.0 TV', 'All of the above']]

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
            update.message.reply_text(
                '''About Competition : \n🗓 Start Date : 13/12/2022 \n🗓 End Date : 18/12/2022 \n❓ No of Questions : 05 \n💰 Total Reward : $100 \n🥇 No of winners : 10\n\nActivities                                           Point\n1. Follow our Twitter page                  10P\n2. Answer the 5 Questions                25P\n3. Join our Telegram Community     25P\n4. Download the App                         50P\n5. Quiz Refferal per person               15P''')
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
            started_msg = '''Thank you for verifying, we request you to download and register on 3.0 Verse app to participate in the quiz competition further. \nClick here to download the app – https://3verse.page.link/ioaZ\n\nEnter Your Email ID linked to your 3.0 verse account'''
            text = update.message.text.lower()
            if text == '2bg48':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '2fxgd':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '5n728':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'ec6pm':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'm457d':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'w4x2m':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'yew6p':
                data['process'][user] = 'app'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            else:
                update.message.reply_text("err, try again")
        elif data["process"][user] == 'app':
            email_id = update.message.text
            if '@' in email_id:
                if ".com" in email_id:
                    data['email'][user] = email_id
                    data['process'][user] = "twitter"
                    json.dump(data, open('users.json', 'w'))
                    update.message.reply_text("Enter Your Twitter ID")
                else:
                    update.message.reply_text("Enter a Valid Email ID!")
            else:
                update.message.reply_text("Enter a Valid Email ID!")
        elif data["process"][user] == 'twitter':
            twitter_id = update.message.text
            data['process'][user] = "QUESTION1"
            data['twitter'][user] = twitter_id
            msg = "What is arbitraging??"
            reply_markup = ReplyKeyboardMarkup(option_keyA, resize_keyboard=True)
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
        user = str(update.message.chat.id)
        if data["process"][user] == "QUESTION1":
            data['marks'][user] = 0
            if answer == 'Buying and selling @ different platforms':
                data['marks'][user] = data['marks'][user] + 10
            else:
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION2"
            json.dump(data, open('users.json', 'w'))
            msg = "Which of the following are centralized exchange??"
            reply_markup = ReplyKeyboardMarkup(option_keyB, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION2":
            if answer == 'Binance':
                data['marks'][user] = data['marks'][user] + 10
            else:
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION3"
            json.dump(data, open('users.json', 'w'))
            msg = "Which one of these are not typical web3 characteristics??"
            reply_markup = ReplyKeyboardMarkup(option_keyC, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION3":
            if answer == 'All of above':
                data['marks'][user] = data['marks'][user] + 10
            else:
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION4"
            json.dump(data, open('users.json', 'w'))
            msg = "Which blockchains support smart contracts??"
            reply_markup = ReplyKeyboardMarkup(option_keyD, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION4":
            if answer == 'All of them':
                data['marks'][user] = data['marks'][user] + 10
            else:
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "QUESTION5"
            json.dump(data, open('users.json', 'w'))
            msg = "Products of 3.0 Verse?"
            reply_markup = ReplyKeyboardMarkup(option_keyE, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        elif data["process"][user] == "QUESTION5":
            if answer == 'All of the above':
                data['marks'][user] = data['marks'][user] + 10
            else:
                data['marks'][user] = data['marks'][user] + 0
            data['process'][user] = "finished"
            json.dump(data, open('users.json', 'w'))
            update.message.reply_text(f'''\n\nHurray!! 🎉 Your entry is recorded for participating in 3.0 verse Quiz competition 📝\n\nYou are currently at no. {data['total'] + 100} on Leaderboard 🎯, you may share your unique referral link with your family and friends 👥 to top the leaderboard.\n\nThe more no of people downloading the 3.0 verse app with your referral link the more is the chance of you topping the Leaderboard 🎯🎯''')
            msg3 = '''The first leaderboard would be displayed here in chat window on dd/mm/yyyy at hh:mm:ss ⏳ .Happy referring and keep topping the leaderboard 🚀🚀.'''
            update.message.reply_text(msg3)
            msg = final_msg()
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)


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
            f.write("no.,userid,username,email,twitter username,marks, referred\n")
            for u in data['users']:
                if data['process'][u] == "finished":
                    i = str(data['id'][u])
                    refrrd = 0
                    if i in data['referred']:
                        refrrd = data['referred'][i]
                    d = "{},{},{},{},{},{}\n".format(
                        i, u,data['name'][u], data['email'][u], data['twitter'][u],data['marks'][u], refrrd)
                    f.write(d)
                if data['process'][u] == "verify":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u,data['name'][u], "", "", "", refrrd)
                    f.write(d)
                if data['process'][u] == "twitter":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u,data['name'][u], data['email'][u], "","", refrrd)
                    f.write(d)
                if data['process'][u] == "email":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u,data['name'][u], "", "","", refrrd)
                    f.write(d)
            f.close()
            bot = Bot(TOKEN)
            bot.send_document(chat_id=update.message.chat.id, document=open('users.csv', 'rb'))


def link(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        msg = 'https://t.me/{}?start={}'.format(config['botname'], data['id'][user])
        reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
        update.message.reply_text(msg, reply_markup=reply_markup)


if __name__ == '__main__':
    data = json.load(open('users.json', 'r'))
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("admin", admin))
    dp.add_handler(MessageHandler(Filters.regex('^Users$'), users))
    dp.add_handler(MessageHandler(Filters.regex('^Get List$'), get_file))
    dp.add_handler(MessageHandler(Filters.regex('^Referral Link$'), link))
    dp.add_handler(MessageHandler(Filters.regex('^Buying and selling @ different platforms$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Trading$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Buying and selling @ same platform$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^None$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Binance$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^dYdX$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^UniSwap$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^PancakeSwap$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Decentralisation$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Data ownership$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Speed$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of above$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Bitcoin$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Ethereum$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Solana$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of them$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 Wire$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 University$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^3.0 TV$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^All of the above$'), questionsss))
    dp.add_handler(MessageHandler(Filters.regex('^Yes$'), extra))
    dp.add_handler(MessageHandler(Filters.regex('^Referred$'), ref))

    dp.add_handler(MessageHandler(Filters.text, extra))
    if DEV is not True:
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(webhook_url + TOKEN)
    else:
        updater.start_polling()
    print("Bot Started")
    updater.idle()
