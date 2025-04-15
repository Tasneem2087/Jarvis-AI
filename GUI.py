        from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QStackedWidget,QWidget,QLineEdit,QGridLayout, QHBoxLayout, QPushButton,QFrame,QLabel, QSizePolicy
        from PyQt5.QtGui import Qicon, QPainter, QMovie, QColor, QTextCharFormat, QFont, QPixmap, QTextBlockFormat
        from PyQt5.QtCore import Ot, QSize, QTimer
        fron doteny Import dotenv values
        import sys
        Import os

        env_vars = dotenv_values(".env")
        Assistantname = env_vars.get("Assistantname")
        current_dir = os.getcwd() 
        old_chat_message = ""
        TempDirPath = rf"{current_dir}\Frontend\Files"
        GraphicsDirPath = rf"{current_dir}\Frontend\Graphics"

        def AnswerModifier(Answer):
            lines = Answer.split('\n')
            non_empty_lines = [line for Line in lines if line.strip()]
            modified_answer = '\n'. join(non_empty_lines)
            return modified_answer

        def QueryModifier(Query):

            new_query = Query.lower().strip()
            query_words = new_query.split()
            question_words = ["how", "what", "who", "where", "when", "why", "which", "whose", "whow", "can you", "what's", "where's", "how's"]

            if any(word + " " in new query for word in question_words):
                if query_words[-1][-1] in ['-', '?','!']:
                    new_query  = new_query[:-1] + "?"
                else:
                    new_query += "?"

            else:    
                 if query_words[-1][-1] in ['.','?','!']:
                     new_query = new_query[:-1] + "."
                 else:
                      new_query +="."
   
            return new_query.capitalize()

        def SetMicrophoneStatus(Command):
               with open(rf'{TempDirPath}\Mic.data', "w", encoding='utf-8') as file:
                      file.write(Command)
        
        def GetMicrophoneStatus():   
                with open(rf'{TempDirPath}\ Mic.data', "r", encoding='utf-8') as file:
                      Status= file.read()
                return Status
    
        def SetAssistantStatus(Status):
                with open(rf'{TempDirPath}\Status.data', "w", encoding='utf-8') as file:
                    with open(rf'{TempDirPath}\Status.data', "r", encoding='utf-8') as file: 
                        file.write(Status)

        def GetAssistantStatus():
             with open(rf'{TempDirPath} \Status.data', "r", encoding ='utf-8') as file:
                Status= file.read()
                return Status

        def MicButtonInitialed():
            SetMicrophoneStatus("False")

        def MicButtonClosed():
           SetMicrophoneStatus("True")

        def GraphicsDirectoryPath(Filename):
              Path = rf'{GraphicsDirPath}\{Filename}'
              return Path

        def TempDirectoryPath(Filename): 
            Path =rf'{TempDirPath}\{Filename}"
            return Path

        def ShowTextToScreen(Text):
            with open(rf'{TempDirPath}\Responses.data", "w", encoding=q'utf-8') as file: 
            file.write(Text)

        class ChatSection(QWidget):
    
            def_init_(self):
                super(ChatSection, self)._init_()
                layout= QVBoxLayout(self)
                layout.setContentsMargins(-10, 40, 40, 100)
                layout.setSpacing(-100)
                self.chat_text_edit = QTextEdit()
                self.chat_text_edit.setReadOnly(True)
                self.chat_text_edit.setTextInteractionFlags(Qt.NoTextinteraction)
                self.chat_text_edit.setFrameStyle(QFrame.NoFrame)
                layout.addWidget(self.chat_text_edit)
                self.setStyleSheet("background-color: black;")
                layout.setSizeConstraint(QVBoxlayout.SetDefaultConstraint)
                layout.setStretch(1, 1)
                self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
                text_color = QColor(Qt.blue)
                text_color_text = QTextCharFormat()
                text_color_text.setForeground(text_color)
                self.chat_text_edit.setCurrentCharFormat(text_color_text)
                self.gif_label =QLabel()
                self.gif_label.setStyleSheet("border: none;")
                movie =QMovie(GraphicsDirectoryPath("Jarvis.gif"))
                max gif size W 400 max gif size 278
                movie.setScaled5ize(Q5ize(max_gif size w, max_gif_size_H))
                self.gif_label.setAlignment(Qt Alignright Qt.AlignBottom)
                self.gif label.setMovie(movie) movie.start()
                Layout.addWidget(self.gif_label)
                self.Label QLabel()
                self.label.setStylesheet("color: white; font-size:16px; margin-right: 195px; border: none; margin-top: 20px;")
                self.label.setAlignment(Qt.Alignlight)
                Layout.addWidget(self.label) layout.setSpacing(-10)
                Layout.addWidget[self.gif_label)
                font QFont()
                font.setPointSize(13)
                self.chat text edit.setFont(font)
                self.timer
                QTimer(self)
                self.timer.timeout.connect(self.loadMessages)
                sell.timer.timeout.connect(self.SpeechRecogText)
                self.timer.start(5)
                self.chat_text edit.viewport().installEventFilter(self) 
                self.setStylesheet("""
                      QScrollBar:vertical{
                      border: none: 
                      background: black;
                      width: 10px;
                      margin: 0px 0px 0px 0px;
                    }

                      QScrollBar:: handle:vertical{
                      background: white;
                      min-height: 20px:
                      }

                     QScroller::add-linervercical{
                     background black;
                      subcontrol-position: bottom;
                       subcontrol -origin: margin;
                       height: 10px;
                       }

                    QscrollBar::sub-Line::vertical {
                    background: black;
                    subcontrol-position: top;
                     subcontrol-origins margin;
                     height: 10px;
                     }

                     QScrollBar::up-arrow:vertical, QScrollBar::down-arrow::vertical{
                     border: none ;
                     background: none;
                     color: none;
                     }

                    QScrollbar::add-page:vertical, QScrollBar::sub-page:vertical{
                    background: none;
                    }
                """)
            def loadMessages(self): 
                   
                   global old_chat_message 
            
            with open(TempDirectoryPath('Responses.data'),"r",encoding='utf-8') as file:
                  messages = file.read()
               
                 if None==messages:
                     pass
                 elif len(messages)<=1;
                      pass

                elif str(old_chat_message)==str(messages):
                      pass

                else:
                    self.addMessage(message = messages.color= 'White')
                    old_chat_message = messages

            def SpeechRecogText(self):
                with open(TempDirectoryPath("Status.data"), "r", encoding = "utf-8") as file:
                       messages = file.read()
                       self.Label.setText(messages)

            def load_icon(self, path, width=60, height=60):
                  pixmap = QPixmap(path)
                  new_pismap  = pixmap.scaled(width, height)
                  self.icon_label.setPixmap(new_pixmар)

            def toggle_icon(self, event = None):
              
              if self.toggled:
                    self.load_icon(GraphicsDirectoryPath("voice.png"), 60, 60)
                    MicButtonInitialed()
         
              else:
                    self.load_icon(GraphicsDirectoryPath("mic.png"), 60, 60)
                    MicButtonClosed()

              self.toggled = not self.toggled

            def addMessage(self, message, color):            
                  cursor= self.chat_text_edit.textCursor()
                  formatm = QTextCharFormat()
                  formatm = QTextBlockFormat()
                  formatm.setTopMargin(10)
                  formatm.setLeftMargin(10)
                  format.setForeground(QColor(color))
                  cursor.setCharFormat(format)
                  cursor.setBlockFormat(formatm)
                  cursor.insertText(message + "\n")
                  self.chat_text_edit.setTextCursor(cursor)

        class InitialScreen(QWidget):
            def _init_(self, parent = None):
                   super()._init_(parent)
                   desktop = QApplication.desktop()
                   screen_width = desktop.screenGeometry().width() 
                   screen_height = desktop.screenGeometry().height()
                   content_layout = QVBoxLayout()
                   content_layout.setContentsMargins(0, 0, 0, 0)
                   gif_label = QLabel()
                   movie = QMovie(GraphicsDirectoryPath("Jarvis.gif"))
                   gif_label.setMovie(movie) 
                   max_gif_size = int(screen_width/16 + 9 )
                   movie.setScaled5ize(QSize(screen_width, max_gif_size ))
                   gif_label.setAlignment(Qt.AlignCenter)
                   movie.start()
                   gif_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
                   self.icon_label = QLabel()
                   pixman = QPixmap(GraphicsDirectoryPath("Mic on.png"))
                   пеw_ріxmар = pixmap.scaled(60, 60)
                   self.icon_label.setPixmap(new_pixmap)
                   self.icon_label.setFixedSize(150,150)
                   self.icon_label.setAlignment(Qt.AlignCenter)
                   self.toggled = True
                   self.toggle_icon()
                   self.icon_label.mousePressEvent = self.toggle_icon
                   self.label = QLabel("")
                   self.label.setStyleSheet("color: white; font-size:16px; margin-bottom:0;")
                   content_layout.addWidget(gif_label, alignment = Qt.AlignCenter) 
                   content_layout.addwidget(self.Label, alignment = Qt.AlignCenter)
                   content_layout.addwidget(self.icon_label, alignment = Qt.AlignCenter)
                   content_layout.setContentsMargins(0, 0, 0, 158)
                   self.setLayout(content_layout)
                   self.setFixedHeight(screen_height)
                   self.setFixedWidth(screen_width)
                   self.setStyleSheet("background-color: black:")
                   self.timer = QTimer(self)
                   self.timer.timeout.connect(self.SpeechRecogText)
                   self.timer.start(5)

            def SpeechRecogText(self):
                  with open(TempDirectoryPath("Status.data"), "r", encoding="utf-8") as file:
                    messages = file.read()
                    self.label.setText(messages)
            
            def load_icon(self, path, width=60, height=60):
                 pixmap = QPixmap(path)
                 new_pixmap = pixmap.scaled(width, height)
                 self.icon_label.setPixmap(new_pixmap)
        
            def toggle_icon(self, event=None):
               
                if self.toggled:
                    self.load_icon(GraphicsDirectoryPath("Mic_on.png"), 60, 50)
                    MicButtonInitialed()

                else:
                    self.load_icon(GraphicsDirectoryPath ("Mic_off.png"), 60, 60)
                    MicButtonClosed()

                self.toggled = not self.toggled
            
    
        class MessageScreen(QWidget):  
        
            def _init_(self, parent =None):
                super()._init_(parent)
                screen_width = desktop.screenGeometry().width()
                screen_height = desktop.screenGeometry().height()
                layout = QVBoxLayout()
                label = QLabel("")
                layout.addwidget(chat_section)
                self.setLayout(Layout)
                self.setStyleSheet("background-color: black;")
                self.setFlatwight(screen_height)
                self.setFixedwidth(screen_width)

        class CustooTopBar(QWidget):

            def _init(self, parent, stache widget):
                super(). _init_(parent) 
                self.initUI()
                self.current_screen = None
                self.stacked_widget = stacked_widget

            def initUI(self):
                self.setFixedWeight(50)
                layout = QHBoxLayout(self)
                layout.setAlignment(Qt.AlignRight) 
                home_button = QPushButton()
                home_icon = QIcon(GraphicsDirectoryPath("Howe.png"))
                home_button.setIcon(home_icon)
                home_button.setText("Home")
                home_button.setStylesheet("height:40px; line-height:40px; background-color:white; color:black")
                message_button = QPushButton()
                message_icon = QIcon(GraphicsDirectoryPath("Chats.png"))
                message_button.setIcon(message_icon)
                message_button.setText("Chat")
                message_button.setStylesheet("height:40px; line-height:40px; background-color:white; color:black")
                minimize_button = QPushButton()
                minimize_icon = QIcon(GraphicsDirectoryPath ("Minimize2.png"))
                minimize_button.setIcon(minimize_icon)
                minimize_button.setStylesheet("background-color:white")
                minimize_button.clicked.connect(self.minimizeWindow)
                self.maximize_button = QPushButton()
                self.maximize_icon = QIcon(GraphicsDirectoryPath)("Maximize.png"))
                self.restore_icon =QIcon(GraphicsDirectoryPath("Minimize.png"))
                self.maximize_button.setIcon(self.maximize_icon)
                self.maximize_button.setFlat(True) 
                self.maximize_button.setstylesheet("background-color:white")
                self.maximize_button.clicked.connect(self.maximizeWindow)
                close_button= QPushButton()
                close_icon = QIcon(GraphicsDirectoryPath("Close.png"))
                close_button.setIcon(close_icon)
                close_button.setStyleSheet("background-color:white")
                close_button.clicked.connect(self.closeWindow)
                line_frame = QFrame()
                line_frame.setFixedHeight(1)
                line_frame.setFrameShape(QFrame.HLine)
                line_frame.setFrameShadow(QFrame.Sunken)
                line_frame.setStyleSheet("border-color: black;")
                title_label = QLabel(f"{str(Assistantname).capitalize()} AI  ")
                title_label.setStyleSheet("color: black; font-size: 18px; background-color:white") 
                home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0)) 
                message_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
                layout.addWidget(title_label) 
                layout.addStretch(1)
                layout.addwidget(home_button)
                layout.addwidget(message_button)
                layout.addStretch(1)
                layout.addwidget(minimize_button)
                layout.addwidget(self.maximize_button)
                layout.addwidget(close_button)
                layout.addwidget(line_frame)
                self.draggable = True
                self.offset  = None

        def paintEvent(self, event):
                painter = QPainter(self)
                painter.fillRect(self.rect(), Qt.white) 
                super().paintEvent(event)

        def minimizeWindow(self):
             self.parent().showMinimized()

        def maximizeWindow(self):
            if self.parent().isMaximized():
                    self.parent().showNormal() 
                    self.maximize_button.setIcon(self.maximize_icon)
            else:
                    self.parent().showMaximized() 
                    self.maximize_button.setIcon(self.restore_icon)

        def claseWindow(self):
            self.parent().close()

        def mousePressEvent(self, event):
            if self.draggable: 
                self.offset = event.pos()

        def mouseMoveEvent(self, event):
            if self.draggable and self.offset:
                 new_pos = event.globalPos() 
                 self.offset
                 self.parent().move(new_pos)

        def showMessageScreen(self):
                if self.current_screen is not None:
                    self.current_screen.hide()

                message_screen = MessageScreen(self)
                layout = self.parent().layout()
                if layout is not None:
                    layout.addWidget(message_screen)
                    self.current_screen = message_screen

        def showInitialScreen(self):
            if self.current_screen is not None:
                self.current_screen.hide()

            initial_screen = InitialScreen(self)
            layout = self.parent().layout()
            if layout is not None:
                layout.addWidget(initial_screen)
            self.current_screen = initial_screen

class MainWindow(QMainWindow):

       def _init_(self):
            super(). _init_()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.initUI()

       def initUI(self):
             desktop = QApplication.desktop()
             screen_width = desktop.screenGeometry().width()
             screen_height = desktop.screenGeometry().height()
             stacked_widget = QStackedWidget(self)
             initial_screen = InitialScreen()
             message_screen = MessageScreen()
             stacked_widget.addWidget(initial_screen)
             stacked_widget.addiWdget(message_screen) 
             self.setGeometry(0, 0, screen_width, screen_height)
             self.setStyleSheet("background-color: black;") 
             top_bar = CustomTopBar(self, stacked widget)
             self.setMenuWidget(top_bar)
             self.setCentralWidget(stacked_widget)

       def GraphicalUserInterface():
            app =QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

if __name__ == "__main__":
     GraphicalUserInterface()
            