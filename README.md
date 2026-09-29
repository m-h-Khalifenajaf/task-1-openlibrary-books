# OpenLibrary Books

This project uses the OpenLibrary API to retrieve information about 50 books based on a topic entered by the user, filter books published after 2000, and save the results in a CSV file.

## Features

* Ask the user to enter a book topic
* Retrieve information about 50 books related to the entered topic
* Filter books published after 2000
* Convert list values into readable text
* Save the results in a CSV file named based on the entered topic

## Requirements

* Python 3
* requests

## Installation

Install the required library:

```bash
pip install requests
```

## Usage

Run the following command:

```bash
python task_1_openlibrary_books.py
```

Then enter a topic when prompted:

```text
Enter a topic: Python
```

## Output

The program creates a CSV file based on the entered topic.

For example, if the entered topic is:

```text
Python
```

the output file will be:

```text
Books about Python.csv
```

The CSV file contains information about books related to the entered topic that were published after 2000.

## API

This project uses the OpenLibrary Search API.

---

# کتاب‌های OpenLibrary

این پروژه با استفاده از API سایت OpenLibrary، بر اساس موضوعی که کاربر وارد می‌کند اطلاعات ۵۰ کتاب را دریافت می‌کند، کتاب‌هایی که سال انتشار آن‌ها بعد از ۲۰۰۰ است را فیلتر می‌کند و اطلاعات نهایی را در یک فایل CSV ذخیره می‌کند.

## امکانات

* دریافت موضوع کتاب از کاربر
* دریافت اطلاعات ۵۰ کتاب مرتبط با موضوع واردشده
* فیلتر کردن کتاب‌های منتشرشده بعد از سال ۲۰۰۰
* تبدیل مقادیر لیستی به متن قابل خواندن
* ذخیره نتایج در یک فایل CSV که نام آن بر اساس موضوع واردشده تعیین می‌شود

## پیش‌نیازها

* Python 3
* کتابخانه `requests`

## نصب

برای اجرای برنامه ابتدا کتابخانه موردنیاز را با دستور زیر نصب کنید:

```bash
pip install requests
```

## نحوه اجرا

برای اجرای برنامه دستور زیر را در ترمینال اجرا کنید:

```bash
python task_1_openlibrary_books.py
```

سپس موضوع موردنظر خود را وارد کنید:

```text
Enter a topic: Python
```

## خروجی

برنامه یک فایل CSV ایجاد می‌کند که نام آن بر اساس موضوع واردشده تعیین می‌شود.

برای مثال، اگر موضوع واردشده:

```text
Python
```

باشد، فایل خروجی به صورت زیر خواهد بود:

```text
Books about Python.csv
```

این فایل شامل اطلاعات کتاب‌های مرتبط با موضوع واردشده است که سال انتشار آن‌ها بعد از ۲۰۰۰ بوده است.

## ای‌پی‌آی‌ها

در این پروژه از Search API سایت OpenLibrary برای دریافت اطلاعات کتاب‌ها استفاده شده است.
