from PySide2 import QtCore, QtWidgets


class MainWindowUI(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.status_bar = None
        self.action_file_exit = None
        self.action_file_save = None
        self.action_file_save_as = None
        self.action_file_open = None
        self.action_file_save_as_image = None
        self.tree_widget = None
        self.add_splitter_button = None
        self.delete_splitter_button = None
        self.set_description_button = None
        self.description_edit = None
        self.splitter_type_combo = None
        self.fiber_length_spin = None
        self.setup()

    def setup(self):
        self.main_window.setWindowTitle('GPlanner')
        self.main_window.resize(800, 600)
        self.setup_menu_bar()
        self.setup_status_bar()
        self.setup_central_widget()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def setup_menu_bar(self):
        menu_bar = QtWidgets.QMenuBar(self.main_window)
        menu_file = QtWidgets.QMenu('&File', menu_bar)
        self.action_file_exit = QtWidgets.QAction('&Exit', self.main_window)
        self.action_file_save = QtWidgets.QAction('&Save', self.main_window)
        self.action_file_open = QtWidgets.QAction('&Open', self.main_window)
        self.action_file_save_as = QtWidgets.QAction('Save &as', self.main_window)
        self.action_file_save_as_image = QtWidgets.QAction('Save as &image', self.main_window)
        menu_file.addAction(self.action_file_save)
        menu_file.addAction(self.action_file_save_as)
        menu_file.addAction(self.action_file_save_as_image)
        menu_file.addAction(self.action_file_open)
        menu_file.addAction(self.action_file_exit)
        menu_bar.addAction(menu_file.menuAction())
        self.main_window.setMenuBar(menu_bar)

    def setup_status_bar(self):
        self.status_bar = QtWidgets.QStatusBar(self.main_window)
        self.main_window.setStatusBar(self.status_bar)

    def setup_central_widget(self):
        central_widget = QtWidgets.QWidget(self.main_window)
        self.tree_widget = QtWidgets.QTreeWidget(central_widget)
        self.tree_widget.setHeaderLabels(('Type', 'Signal attenuation', 'Fiber length', 'Free connectors', 'Description'))

        main_layout = QtWidgets.QVBoxLayout(central_widget)

        controls_layout = QtWidgets.QGridLayout()
        equipment_type_label = QtWidgets.QLabel('Equipment type', central_widget)
        fiber_length_label = QtWidgets.QLabel('Fiber length(km)', central_widget)
        description_label = QtWidgets.QLabel('Description', central_widget)
        self.splitter_type_combo = QtWidgets.QComboBox(central_widget)
        self.fiber_length_spin = QtWidgets.QDoubleSpinBox(central_widget)
        self.add_splitter_button = QtWidgets.QPushButton('Add Equipment', central_widget)
        self.delete_splitter_button = QtWidgets.QPushButton('Delete Equipment', central_widget)
        self.set_description_button = QtWidgets.QPushButton('Set description')
        self.description_edit = QtWidgets.QLineEdit()
        self.description_edit.setClearButtonEnabled(True)

        controls_layout.addWidget(equipment_type_label, 0, 0, 1, 1)
        controls_layout.addWidget(fiber_length_label, 1, 0, 1, 1)
        controls_layout.addWidget(self.splitter_type_combo, 0, 1, 1, 1)
        controls_layout.addWidget(self.fiber_length_spin, 1, 1, 1, 1)
        controls_layout.addWidget(self.add_splitter_button, 0, 2, 1, 1)
        controls_layout.addWidget(self.delete_splitter_button, 1, 2, 1, 1)
        controls_layout.addWidget(description_label, 2, 0, 1, 1)
        controls_layout.addWidget(self.description_edit, 2, 1, 1, 1)
        controls_layout.addWidget(self.set_description_button, 2, 2, 1, 1)

        main_layout.addWidget(self.tree_widget)
        main_layout.addLayout(controls_layout)

        self.main_window.setCentralWidget(central_widget)
