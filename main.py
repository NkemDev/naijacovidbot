#bot to display information about covid_19
from telegram import *
from telegram.ext import *
from requests import *

updater =Updater(token ="********************") #telegram api
dispatcher =updater.dispatcher

def startCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id =update.effective_chat.id,
                             text ='Hello I am an automated bot created to inform you about COVId-19.Below are frequently asked question and their answers about COVID-19. You just click or type the following highlighed commands for the answers.\n\n'  +
                                    '1. /covid19 -What is COVID-19?\n'+
                                    '2. /symptoms -What are Covid-19 symptoms?\n'+
                                    '3. /difference -What is the difference between isolation and quarantine?\n'+
                                    '4. /exposure -How long does it take to develop symptoms?\n'+
                                    '5. /suspect -What do I do if I suspect I have covid-19?\n'+
                                    '6. /aftereffects -What happens to people who get Covid-19?\n'+
                                    '7. /risk -Who is at risk of severe illness from Covid-19?\n'+
                                    '8. /longterm -Does Covid-19 have long term effects?\n'+
                                    '9. /protect -How can I ensure the safety of others and myself if we do not know who is affected?\n'+
                                    '10. /status -What test should I get to know my COVID-19 status?\n'+
                                    '11. /antigen -How do I find out if I have had COVID-19 in the past?\n'+
                                    '12. /vaccine -Does COVID-19 have a vaccine?\n'+
                                    '13. /treatment -Is there treatment for COVID-19?\n' +
                                    '14./breastfeeding -Can COVID-19 be passed through breastfeeding? \n'+
                                    '15. /baby -Should a baby be allowed to make contact with and be breastfed by the mother who is infected by COVID-19?\n'+
                                    '16. /nursingmothers -Can nursing mothers be vaccinated against COVID-19?\n'+
                                    '17. /disinfection -Which disinfectants are effective against COVID-19?\n'+
                                    '18./outdoor -What are the recommended practices for when I get home from outdoor activities?\n' +
                                    '19. /foods -How should clean food items from the market for example, fruits, vegetables and packaged items?\n'+
                                    '20. /hydroxychloroquine -Is hydroxychloroquine recommended for treatment or prevention of COVID-19? \n')

def covid19Command(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2. WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.\n\n'+
                             'Click /back to contine')

def symptomsCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='The most common symptoms of COVID-19 are Fever, dry cough, body pains and fatigue\n\n'+
                             'Other symptoms that are less common and may affect some patients include:\n Loss of taste or smell, Nasal congestion, Conjunctivitis (also known as red eyes),Sore throat, Headache, Muscle or joint pain, Different types of skin rashes, Nausea or vomiting, Diarrhea, Chills or dizziness\n'+
                            'Symptoms of severe COVID-19 disease include:\n\n'+
                             'Shortness of breath,Loss of appetite, Confusion, Persistent pain or pressure in the chest, High temperature (above 38⁰C),\n\n'+
                                  'Other less common symptoms are: Irritability, Confusion, Reduced consciousness(sometimes associated with seizures), Anxiety, and DepressionSleep disorders\n\n'+
                                  'More severe and rare neurological complications such as strokes, brain inflammation, delirium and nerve damage.People of ages experience fever and/or cough associated with difficulty breathing or shortness of breath, chest pain or pressure, or loss of speech or movement should seek medical care immediately. If possible, call your healthcare provider, hotline or health facility first, so you can be directed to the right clinic.\n\n'
                             'Click /back to continue' ,parse_mode=ParseMode.HTML)

def differenceCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Both isolation and quarantine are methods of preventing the spread of COVID-19.\n\n'+
    '<b>Quarantine</b> is used for anyone who is a contact of someone infected with SARS-CoV-2 virus, which causes COVID-19, whether the infected person has symptoms or not. Quarantine means that you remain separated from others because you have been exposed to the virus and you may be infected and can be take place in a designated facility or at home. For COVID-19, this means staying in the facility or at home or 14 days.\n\n'+
                                  '<b>Isolation</b> is used for people with COVID-19 symptoms or who have tested positive for the virus. Being in isolation means being separated from other people, ideally in a medical facility where you can receive clinical care. If isolation in a medical facility is not possible and you are not in a high risk group of developing severe disease, isolation can take place at home. If you have symptoms, you should remain in isolation for at least 10 days plus an additional 3 days without symptoms. If you are infected and do not develop symptoms, you should remain in isolation for 10 days from the time you test positive.\n\n'+
                             'Click /back to contine',parse_mode=ParseMode.HTML)
def exposureCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='The time from exposure to COVID-19 to the moment when the symptoms begin to manifest is, on average, 5-6 days and can range 1-14 days. This why people who have been exposed to the virus are advised to remain at home and stay away from others, for 14 days, in order to prevent the spread of the virus, especially where testing is not easily available.\n\n' +
                                  'Click /back to contine')

def suspectCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='If you have been exposed to someone with COVID-19, you may become infected, even if you feel well. After exposure to someone who has COVID-19, do the following:\n\n'+
                            '&#8226; Call your health care provider or COVID-19 hotline to find out where and when to get a test.\n'+
                            '&#8226; Cooperate with contact-tracing procedures to stop the spread of the virus.\n'+
                            '&#8226; If testing is not available, stay home and away from others for 14 days.\n'+
                            '&#8226; While you are in quarantine, do not go to work, to school or to public places. Ask someone to bring you supplies.\n'+
                            '&#8226; Keep at least 1metre distance from others, even from family members.\n'+
                            '&#8226; Wear a medical mask to protect others, including if/when you need to seek medical care.\n'+
                            '&#8226; Clean your hands frequently.\n'+
                            '&#8226; Stay in a separate room from other family members, and if not possible, wear a medical mask.\n'+
                            '&#8226; Keep room well-ventilated.\n'+
                            '&#8226; If you share a room, place beds at least 1metre apart.\n'+
                            '&#8226; Monitor yourself for any symptoms for 14 days.\n'+
                            '&#8226; Stay positive by keeping in touch with loved ones by phone or online, and by exercising at home.\n\n'+

                                  'Click /back to contine',parse_mode=ParseMode.HTML)

def aftereffectsCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Among those who develop symptoms, most (80%) recover from the disease without needing hospital treatment. About 15% become seriously ill and require oxygen and 5% become critically ill and need intensive care. Complications leading to death may include respiratory failure, acute respiratory distress syndrome (ARDS), sepsis and septic shock, thromboembolism, and /or multi-organ failure, including injury of the heart, liver or kidneys. In rare situations, children can develop a severe inflammatory syndrome a few weeks fter infection. \n\n' +
                                  'Click /back to continue')

def riskCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='People aged 60years and above, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, obesity or cancer, are at higher risk of developing serious illness. However anyone can get sick with COVID-19 and become seriously ill or die at any age. \n\n' +
                                  'Click /back to continue')

def longtermCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Some people who have had COVID-19, whether they have needed hospitalization or not, continue to experience symptoms, including fatigue, respiratory and neurological symptoms. WHO is working with our Global Technical Network for Clinical Management of COVID-19, researchers and patient groups around the world to design and carry out studies of patients beyond the initial acute course of illness to understand the proportion of patients who have long term effects, how long they persist, and why they occur.  These studies will be used to develop further guidance for patient care. \n\n' +
                                  'Click /back to continue')

def protectCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=' Stay safe by taking some simple precautions, such as physical distancing, wearing a mask, especially when distancing cannot be maintained, keeping rooms well ventilated, avoiding crowds and close contact, regularly cleaning your hands, and coughing into a bent elbow or tissue. Check local advice where you live and work. <b>Do it all!</b> \n\n' +
                                  'Click /back to continue',parse_mode=ParseMode.HTML)

def statusCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='In most situations, a molecular test is used to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction (PCR) is the most commonly used molecular test. Samples are collected from the nose and/or throat with a swab. Molecular tests detect virus in the sample by amplifying viral genetic material to detectable levels. For this reason, a molecular test is used to confirm an active infection, usually within a few days of exposure and around the time that symptoms may begin. \n\n' +
                                  'Click /back to continue')

def antigenCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Antibody tests can tell us whether someone has had an infection in the past, even if they have not had symptoms. Also known as serological tests and usually done on a blood sample, these tests detect antibodies produced in response to an infection. In most people, antibodies start to develop after days to weeks and can indicate if a person has had past infection. Antibody tests cannot be used to diagnose COVID-19 in the early stages of infection or disease but can indicate whether or not someone has had the disease in the past. \n\n' +
                                  'Click /back to continue')

def vaccineCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>Yes.</b> The first mass vaccination programme started in early December 2020. At least 13 different vaccines (across 4 platforms) have been administered. Campaigns have started in 206 economies. The Pfizer/BioNtech Comirnaty vaccine was listed for WHO Emergency Use Listing (EUL) on 31 December 2020. The SII/Covishield and AstraZeneca/AZD1222 vaccines (developed by AstraZeneca/Oxford and manufactured by the Serum Institute of India and SK Bio respectively) were given EUL on 16 February. The Janssen/Ad26.COV 2.S developed by Johnson & Johnson, was listed for EUL on 12 March 2021. The Moderna COVID-19 vaccine (mRNA 1273) was listed for EUL on 30 April 2021 and the Sinopharm COVID-19 vaccine was listed for EUL on 7 May 2021. The Sinopharm vaccine is produced by Beijing Bio-Institute of Biological Products Co Ltd, subsidiary of China National Biotec Group (CNBG).\n'+
                                  'Once vaccines are demonstrated to be safe and efficacious, they must be approved by national regulators, manufactured to exacting standards, and distributed. WHO is working with partners around the world to help coordinate key steps in this process, including to facilitate equitable access to safe and effective COVID-19 vaccines for the billions of people who will need them.\n\n'+
                                  'Click /back to continue' ,parse_mode=ParseMode.HTML)

def treatmentCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Scientists around the world are working to find and develop treatments for COVID-19.Optimal supportive care includes oxygen for severely ill patients and those who are at risk for severe disease and more advanced respiratory support such as ventilation for patients who are critically ill.\n'+
                                'Dexamethasone is a corticosteroid that can help reduce the length of time on a ventilator and save lives of patients with severe and critical illness. Results from the WHO’s Solidarity Trial indicated that remdesivir, hydroxychloroquine, lopinavir/ritonavir and interferon regimens appear to have little or no effect on 28-day mortality or the in-hospital course of COVID-19 among hospitalized patients.\n'+
                                'Hydroxychloroquine has not been shown to offer any benefit for treatment of COVID-19.\n'+
                                'WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. WHO is coordinating efforts to develop treatments for COVID-19 and will continue to provide new information as it becomes available.\n\n'+
                                  'Click /back to continue')

def breastfeedingCommand(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Transmission of active COVID-19 (virus that can cause infection) through breast milk and breastfeeding has not been detected to date. There is no reason to avoid or stop breastfeeding.\n\n'+
                                  'Click /back to continue')

def babyCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='<b>Yes.</b> Immediate and continued skin-to-skin care, including kangaroo mother care, improves the temperature control of newborns and is associated with improved survival among newborn babies. Placing the newborn close to the mother also enables early initiation of breastfeeding which also reduces mortality. The numerous benefits of skin-to-skin contact and breastfeeding substantially outweigh the potential risks of transmission and illness associated with COVID-19.\n\n' +
                            'Click /back to continue', parse_mode=ParseMode.HTML)

def nursingmothersCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='<b>Yes,</b> women who are breastfeeding can take the vaccine when it becomes available to them. None of the currently approved vaccines use the live virus, so there is no risk of passing the virus to the baby through breast milk. There is also some evidence that, after vaccination, antibodies are found in breast milk, which may help protect the baby against COVID-19.\n\n' +
                            'Click /back to continue', parse_mode=ParseMode.HTML)

def disinfectionCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='Disinfection practices are important to reduce the potential for COVID-19 virus contamination in non-healthcare settings, such as in the home, office, schools, gyms, publicly accessible buildings, faith-based community centres, markets, transportation and business settings or restaurants. High-touch surfaces in these non-health care settings should be identified for priority disinfection such as door and window handles, kitchen and food preparation areas, counter tops, bathroom surfaces, toilets and taps, touchscreen personal devices, personal computer keyboards, and work surfaces.\n' +
                            'In non-health care settings,<b> sodium hypochlorite (bleach / chlorine)</b> may be used at a recommended concentration of 0.1% or 1,000ppm (1 part of 5% strength household bleach to 49 parts of water). Alcohol at 70-90% can also be used for surface disinfection. Surfaces must be cleaned with water and soap or a detergent first to remove dirt, followed by disinfection.  Cleaning should always start from the least soiled (cleanest) area to the most soiled (dirtiest) area in order to not spread the dirty to areas that are less soiled.\n'+
                            'All disinfectant solutions should be stored in opaque containers, in a well-ventilated, covered area that is not exposed to direct sunlight and ideally should be freshly prepared every day.\n'+
                            'In indoor spaces, routine application of disinfectants to surfaces via spraying is not recommended for COVID-19. If disinfectants are to be applied, these should be via a cloth or wipe which is soaked in the disinfectant.\n\n'+

                            'Click /back to continue', parse_mode=ParseMode.HTML)

def outdoorCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='Thorough hand hygiene: Washing hands with soap and water or using alcohol-based hand gel, should be performed before touching surfaces, items, pets, and people within the household environment. While outside, people should always follow physical distancing measures, staying at least one metre from another person; perform hand hygiene by washing hands frequently with soap and water or using alcohol-based hand rub; follow good respiratory hygiene by covering your mouth and nose with your bent elbow or tissue when coughing or sneezing; avoid touching your eyes, nose and mouth; and avoid crowded places \n\n'+

                            'Click /back to continue', parse_mode=ParseMode.HTML)

def foodsCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='There is no evidence to date of viruses that cause respiratory illnesses being transmitted via food or food packaging. Coronaviruses cannot multiply in food; they need an animal or human host to multiply.\n'+
                            'The COVID-19 virus is generally thought to be spread from person to person through respiratory droplets. Currently, there is no evidence to support transmission of the COVID-19 virus associated with food.\n'+
                            'Before preparing or eating food, it is important to always wash your hands with soap and water for at least 40-60 seconds. Regular food safety and handling guidance should be followed.\n\n'+


                            'Click /back to continue')

def hydroxychloroquineCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text='WHO does not recommend hydroxychloroquine to prevent COVID-19. This recommendation is based on six trials with more than 6000 participants who did not have COVID-19 and received hydroxychloroquine. Using hydroxychloroquine for prevention had little or no effect on preventing illness, hospitalization or death from COVID-19. Taking hydroxychloroquine to prevent COVID-19 may increase the risk of diarrhea, nausea, abdominal pain, drowsiness and headache.\n'+
                            'However, hydroxychloroquine and chloroquine are safe for use in patients with autoimmune diseases or malaria (not COVID-19).\n'+
                            'WHO also does not recommend hydroxychloroquine as a treatment for COVID-19. This recommendation is based on 30 trials with more than 10 000 COVID-19 patients. Hydroxychloroquine did not reduce mortality, the need for or duration of mechanical ventilation. Taking hydroxychloroquine to treat COVID-19 may increase the risk of heart rhythm problems, blood and lymph disorders, kidney injury, liver problems and failure.\n\n'+
                            'Click /back to continue')

dispatcher.add_handler(CommandHandler('start',startCommand))
dispatcher.add_handler(CommandHandler('back',startCommand))
dispatcher.add_handler(CommandHandler('covid19',covid19Command))
dispatcher.add_handler(CommandHandler('symptoms',symptomsCommand))
dispatcher.add_handler(CommandHandler('difference',differenceCommand))
dispatcher.add_handler(CommandHandler('exposure',exposureCommand))
dispatcher.add_handler(CommandHandler('suspect',suspectCommand))
dispatcher.add_handler(CommandHandler('aftereffects',aftereffectsCommand))
dispatcher.add_handler(CommandHandler('risk',riskCommand))
dispatcher.add_handler(CommandHandler('longterm',longtermCommand))
dispatcher.add_handler(CommandHandler('protect',protectCommand))
dispatcher.add_handler(CommandHandler('status',statusCommand))
dispatcher.add_handler(CommandHandler('antigen',antigenCommand))
dispatcher.add_handler(CommandHandler('vaccine',vaccineCommand))
dispatcher.add_handler(CommandHandler('treatment',treatmentCommand))
dispatcher.add_handler(CommandHandler('breastfeeding',breastfeedingCommand))
dispatcher.add_handler(CommandHandler('baby',babyCommand))
dispatcher.add_handler(CommandHandler('nursingmothers',nursingmothersCommand))
dispatcher.add_handler(CommandHandler('disinfection',disinfectionCommand))
dispatcher.add_handler(CommandHandler('outdoor',outdoorCommand))
dispatcher.add_handler(CommandHandler('foods',foodsCommand))
dispatcher.add_handler(CommandHandler('hydroxychloroquine',hydroxychloroquineCommand))
updater.start_polling()



