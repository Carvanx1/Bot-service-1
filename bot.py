import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token
BOT_TOKEN = "8164010363:AAEKp8In0VKfSxEncvD5PHgqUs_VGJz0pGM"

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles /start command and displays main menu."""
    user = update.effective_user
    welcome_text = (
        f"Hello {user.first_name}! 👋\n\n"
        "Welcome to the University Services Bot. Please select a category below to explore our services:"
    )
    keyboard = [
        [InlineKeyboardButton("📚 Academic Services", callback_data="academic")],
        [InlineKeyboardButton("💼 Skills, Professional, and Digital Development", callback_data="skills")],
        [InlineKeyboardButton("🎨 Design and Technology Services", callback_data="design_tech")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles category selection and displays services."""
    query = update.callback_query
    await query.answer()

    category_services = {
        "academic": [
            ("📝 Homework Assistance", "homework"),
            ("📄 Writing Research Papers and Reports", "research"),
            ("📊 Summarizing and Analyzing", "summarize"),
            ("📚 Exam Preparation Assistance", "exam_preparation"),
            ("✍️ Academic Writing Training", "writing_training"),
            ("🔍 Reviewing and Editing Academic Work", "review_editing"),
            ("📋 Creating and Analyzing Surveys", "surveys"),
            ("📅 Developing Customized Study Plans", "study_plans"),
        ],
        "skills": [
            ("📝 Writing Resumes for Students", "resume_writing"),
            ("🎯 Interview Tips for Academic/Professional Settings", "interview_tips"),
            ("💼 Academic Advising and Career Guidance", "career_guidance"),
            ("✍️ Academic Writing Training", "writing_training"),
            ("📋 Creating and Analyzing Surveys", "surveys"),
            ("🔍 Reviewing Projects and Providing Improvement Suggestions", "project_review"),
        ],
        "design_tech": [
            ("📊 Designing Presentations (PowerPoint)", "presentations"),
            ("💻 Assistance in Programming and Project Development", "programming_help"),
            ("🌐 Creating Websites or Blogs for Students", "websites"),
            ("📱 Providing Consultation on Digital Projects", "digital_projects"),
        ],
    }

    services = category_services.get(query.data, [])
    if services:
        buttons = [[InlineKeyboardButton(service[0], callback_data=service[1])] for service in services]
        buttons.append([InlineKeyboardButton("🔙 Back", callback_data="main_menu")])
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(f"Here are the services under {query.data.capitalize()}:", reply_markup=reply_markup)
    else:
        await query.edit_message_text("Invalid category selected.")

async def handle_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles service selection and displays details."""
    query = update.callback_query
    await query.answer()

    service_details = {
        "homework": (
            "📝 Homework Assistance\n\n"
            "We help you with your homework efficiently. Please provide:\n"
            "- Homework details\n"
            "- Submission deadline\n\n"
            "Options below:",
            "academic"
        ),
        "research": (
            "📄 Writing Research Papers and Reports\n\n"
            "Get professional help for writing research papers or reports. Please provide:\n"
            "- Topic details\n"
            "- Formatting requirements\n\n"
            "Options below:",
            "academic"
        ),
        "summarize": (
            "📊 Summarizing and Analyzing\n\n"
            "We help you summarize and analyze academic or research material. Please provide:\n"
            "- Documents to summarize\n"
            "- Any specific analysis requests\n\n"
            "Options below:",
            "academic"
        ),
        "exam_preparation": (
            "📚 Exam Preparation Assistance\n\n"
            "Get assistance preparing for your exams. Please provide:\n"
            "- Subjects you need help with\n"
            "- Areas of focus\n\n"
            "Options below:",
            "academic"
        ),
        "writing_training": (
            "✍️ Academic Writing Training\n\n"
            "Learn how to improve your academic writing. Please provide:\n"
            "- Writing samples\n"
            "- Desired focus areas (e.g., structure, grammar)\n\n"
            "Options below:",
            "academic"
        ),
        "review_editing": (
            "🔍 Reviewing and Editing Academic Work\n\n"
            "We help review and edit your academic papers. Please provide:\n"
            "- Paper/document to review\n"
            "- Specific areas of focus\n\n"
            "Options below:",
            "academic"
        ),
        "surveys": (
            "📋 Creating and Analyzing Surveys\n\n"
            "We can help create and analyze surveys for academic or professional purposes. Please provide:\n"
            "- Survey objectives\n"
            "- Questions you'd like included\n\n"
            "Options below:",
            "academic"
        ),
        "study_plans": (
            "📅 Developing Customized Study Plans\n\n"
            "We can help you develop a personalized study plan. Please provide:\n"
            "- Subjects or topics you are studying\n"
            "- Available study time\n\n"
            "Options below:",
            "academic"
        ),
        "resume_writing": (
            "📝 Writing Resumes for Students\n\n"
            "We help you write professional resumes. Please provide:\n"
            "- Academic and work history\n"
            "- Career goals\n\n"
            "Options below:",
            "skills"
        ),
        "interview_tips": (
            "🎯 Interview Tips for Academic/Professional Settings\n\n"
            "Get tips for interviews. Please specify:\n"
            "- Type of interview (academic/professional)\n"
            "- Areas you'd like to focus on\n\n"
            "Options below:",
            "skills"
        ),
        "career_guidance": (
            "💼 Academic Advising and Career Guidance\n\n"
            "Get guidance on academic and career paths. Please provide:\n"
            "- Your field of study\n"
            "- Career interests\n\n"
            "Options below:",
            "skills"
        ),
        "project_review": (
            "🔍 Reviewing Projects and Providing Improvement Suggestions\n\n"
            "We help review your academic or professional projects. Please provide:\n"
            "- Project details\n"
            "- Specific areas you'd like reviewed\n\n"
            "Options below:",
            "skills"
        ),
        "presentations": (
            "📊 Designing Presentations (PowerPoint)\n\n"
            "We design professional PowerPoint presentations. Please provide:\n"
            "- Topic and slides you need\n"
            "- Design preferences\n\n"
            "Options below:",
            "design_tech"
        ),
        "programming_help": (
            "💻 Assistance in Programming and Project Development\n\n"
            "We provide assistance with programming and project development. Please provide:\n"
            "- Project details\n"
            "- Programming languages involved\n\n"
            "Options below:",
            "design_tech"
        ),
        "websites": (
            "🌐 Creating Websites or Blogs for Students\n\n"
            "We assist in creating websites or blogs. Please provide:\n"
            "- Website/blog goals\n"
            "- Preferred platform (WordPress, etc.)\n\n"
            "Options below:",
            "design_tech"
        ),
        "digital_projects": (
            "📱 Providing Consultation on Digital Projects\n\n"
            "We consult on digital projects. Please provide:\n"
            "- Project goals\n"
            "- Any specific requirements\n\n"
            "Options below:",
            "design_tech"
        ),
    }

    service_info, category = service_details.get(query.data, ("Service not found", "main_menu"))
    buttons = [
        [InlineKeyboardButton("📩 Request Service", callback_data=f"request_{query.data}")],
        [InlineKeyboardButton("🔙 Back", callback_data=category)],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.edit_message_text(service_info, reply_markup=reply_markup)

async def request_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles service request."""
    query = update.callback_query
    await query.answer()

    service_request = f"Service requested: {query.data[8:]}\nUser ID: {update.effective_user.id}"
    admin_message = f"New service request received: {service_request}"

    # Notify admin (replace with actual chat ID)
    try:
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)
    except Exception as e:
        logger.error(f"Failed to notify admin: {e}")

    # Confirm to user
    await query.edit_message_text(
        "✅ Your request has been submitted successfully! You will be contacted shortly.\n\nThank you for using our services."
    )

# Main function
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_category, pattern="^(academic|skills|design_tech|main_menu)$"))
    application.add_handler(CallbackQueryHandler(handle_service, pattern="^(homework|research|summarize|exam_preparation|writing_training|review_editing|surveys|study_plans|resume_writing|interview_tips|career_guidance|project_review|presentations|programming_help|websites|digital_projects)$"))
    application.add_handler(CallbackQueryHandler(request_service, pattern="^request_"))
    
    # Start the bot
    print("Bot is running...")
    application.run_polling()