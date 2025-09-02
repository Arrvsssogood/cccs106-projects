# hello_flet.py
# CCCS 106 - Week 2 Lab Exercise
# First Flet GUI Application
# Student: Harvey Lloyd V. Palacios

import flet as ft
from datetime import datetime
import re  # Input validation

def main(page: ft.Page):
    # Page configuration
    page.title = "CCCS 106 - Hello Flet"
    page.window.width = 1000
    page.window.height = 1000
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Title with styling
    title = ft.Text(
        "CCCS 106: Hello Flet Application",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLUE_700
    )
    
    # Student information (update with your details)
    student_info = ft.Column([
        ft.Text("Student Information:", size=18, weight=ft.FontWeight.BOLD),
        ft.Text("Name: Harvey Lloyd V. Palacios", size=14),
        ft.Text("Student ID: 23100286", size=14),
        ft.Text("Program: BSCS", size=14),
        ft.Text(f"Date: {datetime.now().strftime('%B %d, %Y')}", size=14),
    ])
    
    # Interactive name input
    name_input = ft.TextField(
        label="Enter your name",
        width=300,
        border_color=ft.Colors.BLUE_300
    )
    
    # Output text for greetings
    greeting_text = ft.Text(
        "",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREEN_700
    )
    
    # Button functions
    def say_hello(e):
        if name_input.value:
            # Check for invalid characters using regex: Allow letters, spaces, numbers, period, apostrophe, hyphen
            if re.search(r'[^a-zA-Z0-9\s\.\'-]', name_input.value):  # Regex checks for invalid characters
                greeting_text.value = "Error: Name contains invalid characters!"
                greeting_text.color = ft.Colors.RED  # Set text color to red
            else:
                greeting_text.value = f"Hello, {name_input.value}! Welcome to Flet GUI development!"
                greeting_text.color = ft.Colors.GREEN_700  # Set text color to green
        else:
            greeting_text.value = "Please enter your name first!"
            greeting_text.color = ft.Colors.RED  # Set text color to red
        page.update()
    
    def clear_all(e):
        name_input.value = ""
        greeting_text.value = ""
        page.update()
    
    def show_info(e):
        info_text = (
            "This is a Flet 0.28.3 application built for CCCS 106.\n"
            "Flet allows you to create beautiful GUI applications using Python!\n"
            f"Current time: {datetime.now().strftime('%I:%M:%S %p')}"
        )
        
        # Create dialog
        dialog = ft.AlertDialog(
            title=ft.Text("Application Information"),
            content=ft.Text(info_text),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_dialog(dialog))
            ]
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    
    def close_dialog(dialog):
        dialog.open = False
        page.update()
    
    # Buttons with styling
    hello_button = ft.ElevatedButton(
        "Say Hello",
        on_click=say_hello,
        width=120,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE
    )
    
    clear_button = ft.ElevatedButton(
        "Clear",
        on_click=clear_all,
        width=120,
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE
    )
    
    info_button = ft.ElevatedButton(
        "App Info",
        on_click=show_info,
        width=120,
        bgcolor=ft.Colors.GREEN_600,
        color=ft.Colors.WHITE
    )
    
    # Layout using containers and columns
    page.add(
        ft.Container(
            content=ft.Column([
                title,
                ft.Divider(height=20),
                student_info,
                ft.Divider(height=20),
                ft.Text("Interactive Section:", size=16, weight=ft.FontWeight.BOLD),
                name_input,
                ft.Row(
                    [hello_button, clear_button, info_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Divider(height=10),
                greeting_text,
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10),
            padding=20
        )
    )

# Run the application
if __name__ == "__main__":
    ft.app(target=main)
