# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
## (Converted to .py via pyside6-uic)
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
    QPalette,
    QColor,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QDoubleSpinBox,
    QLineEdit,
    QSpacerItem,
    QStatusBar,
)
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        MainWindow.setMinimumSize(QSize(1000, 650))
        MainWindow.setStyleSheet(
            """
            QMainWindow {
                background-color: #1e1e2e;
            }
            QWidget#centralwidget {
                background-color: #1e1e2e;
            }
            QGroupBox {
                background-color: #2a2a3e;
                border: 1px solid #44475a;
                border-radius: 8px;
                margin-top: 10px;
                padding: 8px;
                color: #cdd6f4;
                font-size: 13px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                color: #89b4fa;
            }
            QLabel#lbl_original, QLabel#lbl_predicted {
                background-color: #181825;
                border: 2px dashed #44475a;
                border-radius: 8px;
                color: #585b70;
                font-size: 14px;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #b4befe;
            }
            QPushButton:pressed {
                background-color: #74c7ec;
            }
            QPushButton#btn_load_model {
                background-color: #a6e3a1;
                color: #1e1e2e;
            }
            QPushButton#btn_load_model:hover {
                background-color: #cba6f7;
                color: #1e1e2e;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 13px;
            }
            QLabel#lbl_model_path {
                background-color: #181825;
                border: 1px solid #44475a;
                border-radius: 4px;
                padding: 4px 8px;
                color: #a6adc8;
                font-size: 12px;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #313244;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #89b4fa;
                width: 16px;
                height: 16px;
                margin: -5px 0;
                border-radius: 8px;
            }
            QSlider::sub-page:horizontal {
                background: #89b4fa;
                border-radius: 3px;
            }
            QDoubleSpinBox {
                background-color: #181825;
                border: 1px solid #44475a;
                border-radius: 4px;
                color: #cdd6f4;
                padding: 3px 6px;
                font-size: 12px;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                background-color: #313244;
                border: none;
                width: 18px;
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #44475a;
            }
            QStatusBar {
                background-color: #181825;
                color: #a6adc8;
                font-size: 12px;
            }
            """
        )

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ── Root vertical layout ──────────────────────────────────────────────
        self.root_vbox = QVBoxLayout(self.centralwidget)
        self.root_vbox.setContentsMargins(14, 14, 14, 10)
        self.root_vbox.setSpacing(10)

        # ── Title ─────────────────────────────────────────────────────────────
        self.lbl_title = QLabel("目标检测系统")
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.lbl_title.setFont(title_font)
        self.lbl_title.setStyleSheet("color: #cba6f7; letter-spacing: 2px;")
        self.root_vbox.addWidget(self.lbl_title)

        # ── Main content row ──────────────────────────────────────────────────
        self.content_hbox = QHBoxLayout()
        self.content_hbox.setSpacing(12)

        # ── LEFT: image panels ────────────────────────────────────────────────
        self.images_hbox = QHBoxLayout()
        self.images_hbox.setSpacing(12)

        # Original image group
        self.grp_original = QGroupBox("原始图片")
        self.grp_original.setObjectName("grp_original")
        orig_vbox = QVBoxLayout(self.grp_original)
        orig_vbox.setContentsMargins(8, 16, 8, 8)

        self.lbl_original = QLabel("请点击"图片检测"或"视频检测"载入文件")
        self.lbl_original.setObjectName("lbl_original")
        self.lbl_original.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_original.setMinimumSize(QSize(420, 380))
        self.lbl_original.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.lbl_original.setScaledContents(False)
        self.lbl_original.setWordWrap(True)
        orig_vbox.addWidget(self.lbl_original)

        # Predicted image group
        self.grp_predicted = QGroupBox("预测结果")
        self.grp_predicted.setObjectName("grp_predicted")
        pred_vbox = QVBoxLayout(self.grp_predicted)
        pred_vbox.setContentsMargins(8, 16, 8, 8)

        self.lbl_predicted = QLabel("预测结果将在此显示")
        self.lbl_predicted.setObjectName("lbl_predicted")
        self.lbl_predicted.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_predicted.setMinimumSize(QSize(420, 380))
        self.lbl_predicted.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.lbl_predicted.setScaledContents(False)
        self.lbl_predicted.setWordWrap(True)
        pred_vbox.addWidget(self.lbl_predicted)

        self.images_hbox.addWidget(self.grp_original)
        self.images_hbox.addWidget(self.grp_predicted)
        self.content_hbox.addLayout(self.images_hbox, stretch=4)

        # ── RIGHT: control panel ──────────────────────────────────────────────
        self.ctrl_vbox = QVBoxLayout()
        self.ctrl_vbox.setSpacing(12)

        # -- Model import group ------------------------------------------------
        self.grp_model = QGroupBox("模型导入")
        grp_model_vbox = QVBoxLayout(self.grp_model)
        grp_model_vbox.setSpacing(8)

        self.lbl_model_path = QLabel("未加载模型")
        self.lbl_model_path.setObjectName("lbl_model_path")
        self.lbl_model_path.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.lbl_model_path.setMinimumHeight(30)
        self.lbl_model_path.setWordWrap(True)
        grp_model_vbox.addWidget(self.lbl_model_path)

        self.btn_load_model = QPushButton("📂  导入模型")
        self.btn_load_model.setObjectName("btn_load_model")
        self.btn_load_model.setMinimumHeight(36)
        grp_model_vbox.addWidget(self.btn_load_model)

        self.ctrl_vbox.addWidget(self.grp_model)

        # -- Threshold group ---------------------------------------------------
        self.grp_thresh = QGroupBox("阈值调节")
        grp_thresh_vbox = QVBoxLayout(self.grp_thresh)
        grp_thresh_vbox.setSpacing(10)

        # IoU threshold
        iou_label_row = QHBoxLayout()
        self.lbl_iou = QLabel("IoU 阈值")
        self.spin_iou = QDoubleSpinBox()
        self.spin_iou.setRange(0.0, 1.0)
        self.spin_iou.setSingleStep(0.05)
        self.spin_iou.setValue(0.45)
        self.spin_iou.setDecimals(2)
        self.spin_iou.setFixedWidth(70)
        iou_label_row.addWidget(self.lbl_iou)
        iou_label_row.addStretch()
        iou_label_row.addWidget(self.spin_iou)
        grp_thresh_vbox.addLayout(iou_label_row)

        self.slider_iou = QSlider(Qt.Orientation.Horizontal)
        self.slider_iou.setObjectName("slider_iou")
        self.slider_iou.setRange(0, 100)
        self.slider_iou.setValue(45)
        self.slider_iou.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_iou.setTickInterval(10)
        grp_thresh_vbox.addWidget(self.slider_iou)

        # Confidence threshold
        conf_label_row = QHBoxLayout()
        self.lbl_conf = QLabel("置信度阈值")
        self.spin_conf = QDoubleSpinBox()
        self.spin_conf.setRange(0.0, 1.0)
        self.spin_conf.setSingleStep(0.05)
        self.spin_conf.setValue(0.25)
        self.spin_conf.setDecimals(2)
        self.spin_conf.setFixedWidth(70)
        conf_label_row.addWidget(self.lbl_conf)
        conf_label_row.addStretch()
        conf_label_row.addWidget(self.spin_conf)
        grp_thresh_vbox.addLayout(conf_label_row)

        self.slider_conf = QSlider(Qt.Orientation.Horizontal)
        self.slider_conf.setObjectName("slider_conf")
        self.slider_conf.setRange(0, 100)
        self.slider_conf.setValue(25)
        self.slider_conf.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_conf.setTickInterval(10)
        grp_thresh_vbox.addWidget(self.slider_conf)

        self.ctrl_vbox.addWidget(self.grp_thresh)

        # -- Detection buttons group -------------------------------------------
        self.grp_detect = QGroupBox("检测操作")
        grp_detect_vbox = QVBoxLayout(self.grp_detect)
        grp_detect_vbox.setSpacing(10)

        self.btn_image_detect = QPushButton("🖼  图片检测")
        self.btn_image_detect.setObjectName("btn_image_detect")
        self.btn_image_detect.setMinimumHeight(42)

        self.btn_video_detect = QPushButton("🎬  视频检测")
        self.btn_video_detect.setObjectName("btn_video_detect")
        self.btn_video_detect.setMinimumHeight(42)
        self.btn_video_detect.setStyleSheet(
            "QPushButton { background-color: #f38ba8; color: #1e1e2e; }"
            "QPushButton:hover { background-color: #eba0ac; }"
            "QPushButton:pressed { background-color: #e06c75; }"
        )

        grp_detect_vbox.addWidget(self.btn_image_detect)
        grp_detect_vbox.addWidget(self.btn_video_detect)

        self.ctrl_vbox.addWidget(self.grp_detect)

        # -- Info / result label -----------------------------------------------
        self.grp_info = QGroupBox("检测信息")
        grp_info_vbox = QVBoxLayout(self.grp_info)

        self.lbl_info = QLabel("— 暂无检测信息 —")
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setStyleSheet(
            "color: #a6e3a1; font-size: 12px; background: transparent;"
        )
        self.lbl_info.setMinimumHeight(80)
        grp_info_vbox.addWidget(self.lbl_info)

        self.ctrl_vbox.addWidget(self.grp_info)
        self.ctrl_vbox.addStretch()

        self.content_hbox.addLayout(self.ctrl_vbox, stretch=1)
        self.root_vbox.addLayout(self.content_hbox)

        MainWindow.setCentralWidget(self.centralwidget)

        # Status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("就绪 · Ready")

        self.retranslateUi(MainWindow)
        self._connect_signals()
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "目标检测系统", None)
        )

    # ── Internal signal wiring ────────────────────────────────────────────────
    def _connect_signals(self):
        # Keep slider and spinbox in sync — IoU
        self.slider_iou.valueChanged.connect(
            lambda v: self.spin_iou.setValue(v / 100.0)
        )
        self.spin_iou.valueChanged.connect(
            lambda v: self.slider_iou.setValue(int(v * 100))
        )

        # Keep slider and spinbox in sync — Confidence
        self.slider_conf.valueChanged.connect(
            lambda v: self.spin_conf.setValue(v / 100.0)
        )
        self.spin_conf.valueChanged.connect(
            lambda v: self.slider_conf.setValue(int(v * 100))
        )


# ── MainWindow wrapper (optional standalone run) ──────────────────────────────

class MainWindow(QMainWindow):
    """
    Thin wrapper that wires the generated UI to application logic.
    Replace / extend the slot methods below with your actual detection code.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._model = None

        # Connect buttons
        self.ui.btn_load_model.clicked.connect(self._on_load_model)
        self.ui.btn_image_detect.clicked.connect(self._on_image_detect)
        self.ui.btn_video_detect.clicked.connect(self._on_video_detect)

    # ------------------------------------------------------------------
    def _on_load_model(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "选择模型文件",
            "",
            "模型文件 (*.pt *.onnx *.weights *.pb);;所有文件 (*)",
        )
        if path:
            self._model = path
            short = path if len(path) <= 45 else "…" + path[-42:]
            self.ui.lbl_model_path.setText(short)
            self.ui.statusbar.showMessage(f"已加载模型: {path}")
            self.ui.lbl_info.setText(f"模型已加载:\n{path}")

    def _on_image_detect(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "选择图片",
            "",
            "图片文件 (*.jpg *.jpeg *.png *.bmp *.tiff *.webp);;所有文件 (*)",
        )
        if not path:
            return
        if self._model is None:
            self.ui.lbl_info.setText("⚠ 请先导入模型！")
            self.ui.statusbar.showMessage("未加载模型，请先导入模型文件")
            return

        # ---- Display original image ----
        from PySide6.QtGui import QPixmap
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            scaled = pixmap.scaled(
                self.ui.lbl_original.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.ui.lbl_original.setPixmap(scaled)

        iou  = self.ui.spin_iou.value()
        conf = self.ui.spin_conf.value()
        self.ui.statusbar.showMessage(
            f"图片检测中 — IoU: {iou:.2f}  置信度: {conf:.2f} …"
        )
        self.ui.lbl_info.setText(
            f"图片路径: {path}\nIoU: {iou:.2f}   置信度: {conf:.2f}\n\n（在此插入检测逻辑）"
        )

        # ---- TODO: run your model here and set lbl_predicted ----
        # result_pixmap = run_detection(path, self._model, iou, conf)
        # self.ui.lbl_predicted.setPixmap(result_pixmap.scaled(...))

    def _on_video_detect(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频",
            "",
            "视频文件 (*.mp4 *.avi *.mov *.mkv *.flv *.wmv);;所有文件 (*)",
        )
        if not path:
            return
        if self._model is None:
            self.ui.lbl_info.setText("⚠ 请先导入模型！")
            self.ui.statusbar.showMessage("未加载模型，请先导入模型文件")
            return

        iou  = self.ui.spin_iou.value()
        conf = self.ui.spin_conf.value()
        self.ui.statusbar.showMessage(
            f"视频检测中 — IoU: {iou:.2f}  置信度: {conf:.2f} …"
        )
        self.ui.lbl_info.setText(
            f"视频路径: {path}\nIoU: {iou:.2f}   置信度: {conf:.2f}\n\n（在此插入视频帧检测逻辑）"
        )
        # ---- TODO: run your model frame-by-frame here ----


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
