#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT

class App:

  def __init__(self, settings):
    self.settings = settings
    self.graph = ROOT.TGraph()

  def receive(self, datas):
    graph = self.graph
    for data in list(datas):
      np = graph.GetN()
      graph.SetPoint(np, float(data[0]), float(data[1]))

  def fitting(self):
    graph = self.graph
    settings = self.settings

    ROOT.gStyle.SetOptFit()
    graph.Fit(settings["fitting_option"])

