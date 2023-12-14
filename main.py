from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import random


Config.set('graphics', 'resizable', 0)

Window.title = 'Remember'
Window.size = (480, 853)
GamRez = True
GameStatus = False
Game_cnt = 0


class ScreenMain(Screen):  # Начальный экран
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=[50],
        )

        btn_color = [10, 10, 10, 1]
        btn_txt_color = [0, 0, 0, 1]

        lbl = Label(
            text="Remember.",
            font_size="30sp",
            color=[1, 1, 1, 1],
        )
        btn_ez = Button(
            text="Легко",
            background_color=btn_color,
            size_hint=[1, 0.1],
            on_press=self.on_press_btn_ez,
            color=btn_txt_color,
        )
        btn_med = Button(
            text="Средне",
            background_color=btn_color,
            size_hint=[1, 0.1],
            on_press=self.on_press_btn_med,
            color=btn_txt_color,
        )
        btn_hard = Button(
            text="Сложно",
            background_color=btn_color,
            size_hint=[1, 0.1],
            on_press=self.on_press_btn_hard,
            color=btn_txt_color,
        )
        btn_rules = Button(
            text="Правила",
            background_color=btn_color,
            size_hint=[0.5, 0.1],
            pos_hint={'center_x': 0.5, 'top': 1},
            on_press=self.on_press_btn_rules,
            color=btn_txt_color,
        )
        boxlayout.add_widget(lbl)
        boxlayout.add_widget(btn_ez)
        boxlayout.add_widget(btn_med)
        boxlayout.add_widget(btn_hard)
        boxlayout.add_widget(btn_rules)
        self.add_widget(boxlayout)

    def on_press_btn_rules(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'rules_screen'

    def on_press_btn_ez(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_eazy_screen'

    def on_press_btn_med(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_medium_screen'

    def on_press_btn_hard(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_hard_screen'


class ScreenRules(Screen):  # Экран с правилами
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=[40]
        )

        lbl = Label(
            text="Правила\n1.На экране на некоторое время (в зависимости\nот сложности) отображается матрица, в которой\nнекоторые ячейки закрашены.\nВам нужно восстановить матрицу, нажав ЛКМ на\nместо где была закрашенная ячейка.",
            font_size="17sp"
        )

        btn_back_to_menu = Button(
            text="Вернуться в главное меню",
            color=[0, 0, 0, 1],
            background_color=[10, 10, 10, 1],
            size_hint=[1, 0.1],
            pos_hint={'center_x': 0.5, 'top': 1},
            on_press=self.on_press_btn_main_menu,
        )
        boxlayout.add_widget(lbl)
        boxlayout.add_widget(btn_back_to_menu)
        self.add_widget(boxlayout)

    def on_press_btn_main_menu(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'


class ScreenGameOver(Screen):  # Экран с правилами
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def on_enter(self, *args):
        boxlayout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=[40]
        )

        lbl = Label(
            text="Вы проиграли!",
            font_size="30sp"
        )

        lbl1 = Label(
            text="Ваш счет составил: " + str(Game_cnt),
            font_size="25sp"
        )

        btn_back_to_menu = Button(
            text="Вернуться в главное меню",
            color=[0, 0, 0, 1],
            background_color=[10, 10, 10, 1],
            size_hint=[1, 0.1],
            pos_hint={'center_x': 0.5, 'top': 1},
            on_press=self.on_press_btn_main_menu,
        )
        boxlayout.add_widget(lbl)
        boxlayout.add_widget(lbl1)
        boxlayout.add_widget(btn_back_to_menu)
        self.add_widget(boxlayout)

    def on_press_btn_main_menu(self, *args):
        global Game_cnt
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
        self.clear_widgets()
        Game_cnt = 0


class ScreenEasy(Screen):  # Легкий режим
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnt = 0

    def on_enter(self, *args):
        self.main_game()

    def main_game(self, *args):
        btn_def_col = [10, 10, 10, 1]
        btn_act_col = [2, 3, 2, 1]

        self.generation_square = []
        for i in range(0, 5):
            rand_num = random.randint(1, 9)
            self.generation_square.append(rand_num)

        self.generation_square = set(self.generation_square)
        self.check_square = []

        self.field = GridLayout(
            cols=3,
            padding=[75, 250, 75, 250],
            spacing=10,
            )

        for i in range(1, 10):
            if i in self.generation_square:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_act_col,
                    size_hint=[0.5, 0.5],
                    color=btn_act_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
            else:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_def_col,
                    size_hint=[0.5, 0.5],
                    color=btn_def_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
        self.add_widget(self.field)

        Clock.schedule_once(self.clear, 5)
        Clock.schedule_once(self.new_gen, 5)

    def new_gen(self, *args):
        field2 = GridLayout(
            cols=3,
            padding=[75, 250, 75, 250],
            spacing=10,
        )
        for j in range(1, 10):
            btn_def_col = [10, 10, 10, 1]
            self.btn = Button(
                text=str(j),
                background_color=btn_def_col,
                size_hint=[0.5, 0.5],
                color=btn_def_col,
                on_press=self.check_btn
            )
            field2.add_widget(self.btn)

        self.add_widget(field2)

    def check_btn(self, instance):
        global Game_cnt
        if int(instance.text) in self.generation_square:
            self.check_square.append(int(instance.text))
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'game_over_screen'
        self.check_square = set(self.check_square)
        self.check_square = list(self.check_square)
        c = set(self.generation_square) & set(self.check_square)
        if sum(c) == sum(self.generation_square):
            Game_cnt += 1
            self.clear()
            self.main_game()

    def activate_btn(self, instance):
        print(instance.text)

    def on_press_btn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

    def clear(self, *args):
        self.clear_widgets()


class ScreenMedium(Screen):  # Средний режим
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnt = 0

    def on_enter(self, *args):
        self.main_game()

    def main_game(self, *args):
        btn_def_col = [10, 10, 10, 1]
        btn_act_col = [2, 3, 2, 1]

        self.generation_square = []
        for i in range(0, 11):
            rand_num = random.randint(1, 16)
            self.generation_square.append(rand_num)

        self.generation_square = set(self.generation_square)
        self.check_square = []

        self.field = GridLayout(
            cols=4,
            padding=[75, 250, 75, 250],
            spacing=10,
            )

        for i in range(1, 17):
            if i in self.generation_square:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_act_col,
                    size_hint=[0.5, 0.5],
                    color=btn_act_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
            else:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_def_col,
                    size_hint=[0.5, 0.5],
                    color=btn_def_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
        self.add_widget(self.field)

        Clock.schedule_once(self.clear, 3)
        Clock.schedule_once(self.new_gen, 3)

    def new_gen(self, *args):
        field2 = GridLayout(
            cols=4,
            padding=[75, 250, 75, 250],
            spacing=10,
        )
        for j in range(1, 17):
            btn_def_col = [10, 10, 10, 1]
            self.btn = Button(
                text=str(j),
                background_color=btn_def_col,
                size_hint=[0.5, 0.5],
                color=btn_def_col,
                on_press=self.check_btn
            )
            field2.add_widget(self.btn)

        self.add_widget(field2)

    def check_btn(self, instance):
        global Game_cnt
        if int(instance.text) in self.generation_square:
            self.check_square.append(int(instance.text))
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'game_over_screen'
        self.check_square = set(self.check_square)
        self.check_square = list(self.check_square)
        c = set(self.generation_square) & set(self.check_square)
        if sum(c) == sum(self.generation_square):
            Game_cnt += 2
            self.clear()
            self.main_game()

    def activate_btn(self, instance):
        print(instance.text)

    def on_press_btn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

    def clear(self, *args):
        self.clear_widgets()


class ScreenHard(Screen):  # Тяжелый режим
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnt = 0

    def on_enter(self, *args):
        self.main_game()

    def main_game(self, *args):
        btn_def_col = [10, 10, 10, 1]
        btn_act_col = [2, 3, 2, 1]

        self.generation_square = []
        for i in range(0, 20):
            rand_num = random.randint(1, 25)
            self.generation_square.append(rand_num)

        self.generation_square = set(self.generation_square)
        self.check_square = []

        self.field = GridLayout(
            cols=5,
            padding=[50, 225, 50, 225],
            spacing=10,
            )

        for i in range(1, 26):
            if i in self.generation_square:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_act_col,
                    size_hint=[0.5, 0.5],
                    color=btn_act_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
            else:
                self.btn = Button(
                    text=str(i),
                    background_color=btn_def_col,
                    size_hint=[0.5, 0.5],
                    color=btn_def_col,
                    on_press=self.activate_btn,

                )
                self.field.add_widget(self.btn)
        self.add_widget(self.field)

        Clock.schedule_once(self.clear, 2)
        Clock.schedule_once(self.new_gen, 2)

    def new_gen(self, *args):
        field2 = GridLayout(
            cols=5,
            padding=[50, 225, 50, 225],
            spacing=10,
        )
        for j in range(1, 26):
            btn_def_col = [10, 10, 10, 1]
            self.btn = Button(
                text=str(j),
                background_color=btn_def_col,
                size_hint=[0.5, 0.5],
                color=btn_def_col,
                on_press=self.check_btn
            )
            field2.add_widget(self.btn)

        self.add_widget(field2)

    def check_btn(self, instance):
        global Game_cnt
        if int(instance.text) in self.generation_square:
            self.check_square.append(int(instance.text))
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'game_over_screen'
        self.check_square = set(self.check_square)
        self.check_square = list(self.check_square)
        c = set(self.generation_square) & set(self.check_square)
        if sum(c) == sum(self.generation_square):
            Game_cnt += 5
            self.clear()
            self.main_game()

    def activate_btn(self, instance):
        print(instance.text)

    def on_press_btn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

    def clear(self, *args):
        self.clear_widgets()


class RememberApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(ScreenRules(name='rules_screen'))
        sm.add_widget(ScreenEasy(name='game_eazy_screen'))
        sm.add_widget(ScreenGameOver(name='game_over_screen'))
        sm.add_widget(ScreenMedium(name='game_medium_screen'))
        sm.add_widget(ScreenHard(name='game_hard_screen'))

        return sm


if __name__ == "__main__":
    RememberApp().run()
