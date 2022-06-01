
import tkinter
import tkinter.messagebox

import hanoi

DEFAULT_FONT = ('Helvetica', 14)


class DiskDialog:
    """A dialog window meant to get the number of Disks per Tower for the
    Tower of Hanoi puzzle.
    """
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        
        how_many_disks_label = tkinter.Label(master=self._dialog_window,
                                             text='How many Disks per Tower do you want?',
                                             font=DEFAULT_FONT)
        
        how_many_disks_label.grid(row=0, column=0, columnspan=2,
                                  padx=10, pady=10)
        
        self.disk_entry = tkinter.Entry(master=self._dialog_window, width=20,
                                        font=DEFAULT_FONT)
        self.disk_entry.grid(row=1, column=0, columnspan=2,
                             padx=10, pady=1)
        
        button_frame = tkinter.Frame(master=self._dialog_window)
        button_frame.grid(row=2, column=0, padx=10, pady=10)
        
        set_up_button = tkinter.Button(master=button_frame, text='Set Up Game',
                                       font=DEFAULT_FONT,
                                       command=self._on_set_up_button)
        set_up_button.grid(row=0, column=0, padx=10, pady=10)
        
        exit_button = tkinter.Button(master=button_frame, text='Exit Game',
                                     font=DEFAULT_FONT,
                                     command=self._on_exit_button)
        exit_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.exited_intentionally = False  # Did the user click the exit button?
        
        # Shown when user input is invalid
        self._error_message = 'You have to enter an integer greater than or equal to 0'
        
    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
        
    def _on_set_up_button(self) -> None:
        self.num_disks_per_tower = self.disk_entry.get()
        
        try:
            self.num_disks_per_tower = int(self.num_disks_per_tower)
            if self.num_disks_per_tower <= 0:
                tkinter.messagebox.showerror('Error', self._error_message + '.')
                # We have to return None in order to prevent the self._dialog_window
                # from being destroyed.
                return None
            
        except ValueError:  # Entry was a string or a decimal, not an integer
            tkinter.messagebox.showerror('Error', self._error_message + ', not text or decimals.')
            return None
        
        self._dialog_window.destroy()
        
    def _on_exit_button(self):
        self._dialog_window.destroy()
        self.exited_intentionally = True
        
    
class HanoiWindow:
    _BACKGROUND_COLOR = '#FFF3E6'  # Light beige
    
    def __init__(self):
        self._running = True
        
        self._root_window = tkinter.Tk()
        self._root_window.title('Tower of Hanoi')
        
        self._set_up_buttons()
        
        self._hanoi_canvas = tkinter.Canvas(master=self._root_window, width=500, height=400,
                                            background=HanoiWindow._BACKGROUND_COLOR)
        
        self._move_string = tkinter.StringVar()
        self._move_string.set('No move selected.')
        move_label = tkinter.Label(master=self._root_window, textvariable=self._move_string,
                                   font=DEFAULT_FONT)
        move_label.grid(row=2, column=0, padx=5, pady=5)
        
        # Note: row here depends on the tower_button_frame's row
        self._hanoi_canvas.grid(row=3, column=0, padx=10, pady=10)
        
        self._draw_towers()
        
        # Were the Disks already drawn? (Used to ensure Disk sizes are printed correctly)
        self._disks_already_drawn = False
        
    def _set_up_buttons(self) -> None:
        """Add buttons to the top of the window."""
        button_frame = tkinter.Frame(master=self._root_window)
        button_frame.grid(row=0, column=0, padx=10, pady=10)
        
        help_button = tkinter.Button(master=button_frame, text='Help', font=DEFAULT_FONT,
                                     command=self._on_help_button)
        help_button.pack(side=tkinter.LEFT)
        
        restart_button = tkinter.Button(master=button_frame, text='Restart', font=DEFAULT_FONT,
                                        command=self._on_restart_button)
        restart_button.pack(side=tkinter.LEFT)
        
        tower_one_button = tkinter.Button(master=button_frame, text='Tower 1',
                                          font=DEFAULT_FONT, command=self._on_tower_one)
        tower_one_button.pack(side=tkinter.LEFT)
        
        tower_two_button = tkinter.Button(master=button_frame, text='Tower 2',
                                          font=DEFAULT_FONT, command=self._on_tower_two)
        tower_two_button.pack(side=tkinter.LEFT)
        
        tower_three_button = tkinter.Button(master=button_frame, text='Tower 3',
                                            font=DEFAULT_FONT, command=self._on_tower_three)
        tower_three_button.pack(side=tkinter.LEFT)
        
        self._origin = ''
        self._destination = ''
    
    def _on_tower_one(self) -> None:
        self._set_origin_and_or_destination('Tower 1')
            
    def _set_origin_and_or_destination(self, tower_str: str) -> None:
        """Set self._origin and/or self._destination to be some tower_str."""
        TOWER_DICT = {'Tower 1': self._game.tower_one, 'Tower 2': self._game.tower_two,
                      'Tower 3': self._game.tower_three}
        
        if self._origin == '':
            self._origin = tower_str
            self._move_string.set('Moving from ' + self._origin + ' into... ')
        else:
            self._destination = tower_str
        
            if self._origin != self._destination and self._destination != '':
                self._make_move(TOWER_DICT)
            else:
                self._move_string.set('Move canceled.')
            
            self._origin = ''
            self._destination = ''
    
    def _make_move(self, tower_dict: dict) -> None:
        try:
            tower_dict[self._origin].move_disk_to(tower_dict[self._destination])
        except hanoi.InvalidMoveError:
            self._move_string.set("Invalid move! You can't put a bigger Disk on top of a "
                                  + 'smaller Disk.')
            return None
        except hanoi.InvalidFirstMoveError:
            self._move_string.set('Error: you have to make your first move from Tower 1!')
            return None
        except hanoi.NoDisksError:
            self._move_string.set('Error: ' + self._origin + ' has no Disks!')
            return None
        
        self._move_string.set('Moved from ' + self._origin + ' to ' + self._destination
                              + '.')
                
        self._game.num_moves_made += 1
                
        if self._game.is_over():
            self._move_string.set('Congratulations! You solved Tower of Hanoi!\n'
                                  + 'Moves Taken: ' + str(self._game.num_moves_made) + '\n'
                                  + 'Min. # of Moves Required: ' 
                                  + str(self._game.min_moves_required))
            
        self._draw_disks()
        
    def _draw_disks(self) -> None:
        
        tower_tower_xs = {self._tower_one_x: self._game.tower_one, 
                          self._tower_two_x: self._game.tower_two,
                          self._tower_three_x: self._game.tower_three}
        
        # 'Disk_1', 'Disk_2', 'Disk_3', and so on.
        # We need underscores here because tags cannot contain whitespace.
        # These tags are used to prevent the Disk size text from overwriting itself
        # when the player makes moves.
        disk_tags = ['Disk_' + str(disk.size) for tower in tower_tower_xs.values() 
                     for disk in tower if disk != hanoi.EMPTY]
        
        if self._disks_already_drawn:
            for tag in disk_tags:
                self._hanoi_canvas.delete(tag)
        
        current_tag_index = 0     
        
        for tower_x, tower in tower_tower_xs.items():
            topmost_y = 35
            for disk in tower:
                if disk == hanoi.EMPTY:
                    # We have to increment topmost_y here in order to represent the Disks
                    # falling down as far as possible.
                    topmost_y += 15
                    continue
                else:
                    # We need to do 'tower_x + 5' here because tower_x is the x-coordinate
                    # of tower's upper-left corner.  If we did not add 5 to tower_x, the text
                    # would be in the wrong place.
                    self._hanoi_canvas.create_text(tower_x + 5, topmost_y, anchor=tkinter.W,
                                                   font=DEFAULT_FONT,
                                                   text=str(disk.size),
                                                   tag=disk_tags[current_tag_index])
                    
                    topmost_y += 15
                    current_tag_index += 1
        
        self._disks_already_drawn = True
    def _on_tower_two(self) -> None:
        self._set_origin_and_or_destination('Tower 2')
    
    def _on_tower_three(self) -> None:
        self._set_origin_and_or_destination('Tower 3')
        
    def _draw_towers(self) -> None:
        """Note: the width of each Tower is 25. The upper-left corner
        of each Tower has a y-coordinate of 25, and the upper-right corner
        a y-coordinate of 400.
        """
        TOWER_COLOR = 'white'
        self._tower_one_x = 50
        self._hanoi_canvas.create_rectangle(self._tower_one_x, 25, 75, 400, fill=TOWER_COLOR,
                                            tags='Tower 1')
        
        self._tower_two_x = 240
        self._hanoi_canvas.create_rectangle(self._tower_two_x, 25, 265, 400, fill=TOWER_COLOR,
                                            tags='Tower 2')
        
        self._tower_three_x = 425
        self._hanoi_canvas.create_rectangle(self._tower_three_x, 25, 450, 400, fill=TOWER_COLOR,
                                            tags='Tower 3')
        
    def run(self) -> None:
        """Run a session of Tower of Hanoi."""
        disk_dialog = DiskDialog()
        disk_dialog.show()
        
        if not disk_dialog.exited_intentionally:
            self._num_disks_per_tower = disk_dialog.num_disks_per_tower
            self._game = hanoi.Game(self._num_disks_per_tower)
            
            self._draw_disks()
            self._root_window.mainloop()
        
    def _on_help_button(self) -> None:
        help_message = (hanoi.HELP_MESSAGE + '\n\nThe Towers are white rectangles, and the Disks are '
                        + "numbers that represent the Disks' sizes.\n\n"
                        + "To select a Tower to move from, click on one of the 'Tower' buttons. "
                        + "Then, to select the Tower to move to, click on another one of the 'Tower' buttons."
                        + " In short, the first Tower button you click is the Tower you're moving from,"
                        + " and the second is the one you're moving to. \n\nTo cancel a move from a Tower,"
                        + " click on the button of the Tower you're moving from again.")

        tkinter.messagebox.showinfo('Welcome to the Tower of Hanoi!',
                                    help_message)
    
    def _on_restart_button(self) -> None:
        self._game = hanoi.Game(self._num_disks_per_tower)
        self._move_string.set('Restarted the game.')
        self._draw_disks()
    
    
if __name__ == '__main__':
    HanoiWindow().run()
    