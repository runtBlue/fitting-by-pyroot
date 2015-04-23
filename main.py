#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------
# はじめに
# -------------------------------------

# 目的
#   指定したデータを、１次関数近似でフィッテイングして、結果を表示させる

from app import App

# -------------------------------------
# Configurations
# -------------------------------------

settings = {
  # "canvas" : {
  #   "width" : 400,
  #   "height" : 400,
  #   "position_x" : 400,
  #   "position_y" : 400,
  # },
  # フィッテイングオプション
  "fitting_option" : "pol1",
  # "save_image": "saved-image02.png",
}

# -------------------------------------
# Main logic
# -------------------------------------

raw_datas = ["1 2", "3 4"]
datas = [x.split() for x in raw_datas]
app = App(settings)
app.receive(datas)
app.fitting()
