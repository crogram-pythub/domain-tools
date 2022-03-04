#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Domain Tools'''

from tkinter import *

import whois

from utils.functions import set_window_center
from utils.tkAsyncEvent import AsyncEvent


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('域名查询工具 Domain Tools')
        set_window_center(self, 400, 300)

        # Variable Classes in tkinter
        self.domain_server = StringVar()
        self.domain_add_date = StringVar()
        self.domain_exp_date = StringVar()
        self.domain_reg_name = StringVar()
        self.domain_org = StringVar()
        self.domain_state = StringVar()
        self.domain_city = StringVar()
        self.domain_country = StringVar()
        self.domain_dnssec = StringVar()

        # AsyncEvent
        self.async_executor = AsyncEvent(self)

        self.load_view()

        self.mainloop()

    def get_domain_info(self, _=None):
        '''get domain information'''
        # print('get_domain_info')
        d = self.domain_entry.get()
        # domain = whois.whois(d)
        self.async_executor.submit(whois.whois, d).then(self.set_domain_info)

    def set_domain_info(self, domain):
        # print('set_domain_info')

        self.domain_server.set(domain.whois_server)
        self.domain_add_date.set(domain.creation_date)
        self.domain_exp_date.set(domain.expiration_date)
        self.domain_reg_name.set(domain.name)
        self.domain_org.set(domain.org)
        self.domain_state.set(domain.state)
        self.domain_city.set(domain.city)
        self.domain_country.set(domain.country)
        self.domain_dnssec.set(domain.dnssec)

    def load_view(self):
        '''window view widget'''
        # Creating label for each information
        # name using widget Label
        Label(self, text="Website URL : ").grid(row=0, sticky=W)
        Label(self, text="Server Name :").grid(row=3, sticky=W)
        Label(self, text="Expiration date :").grid(row=4, sticky=W)
        Label(self, text="Register name :").grid(row=5, sticky=W)
        Label(self, text="Origination :").grid(row=6, sticky=W)
        Label(self, text="State :").grid(row=7, sticky=W)
        Label(self, text="City :").grid(row=8, sticky=W)
        Label(self, text="Country :").grid(row=9, sticky=W)

        # Creating label for class variable
        # name using widget Entry
        Label(self, text="", textvariable=self.domain_server).grid(row=3,
                                                                   column=1,
                                                                   sticky=W)
        Label(self, text="", textvariable=self.domain_exp_date).grid(row=4,
                                                                     column=1,
                                                                     sticky=W)
        Label(self, text="", textvariable=self.domain_reg_name).grid(row=5,
                                                                     column=1,
                                                                     sticky=W)
        Label(self, text="", textvariable=self.domain_org).grid(row=6,
                                                                column=1,
                                                                sticky=W)
        Label(self, text="", textvariable=self.domain_state).grid(row=7,
                                                                  column=1,
                                                                  sticky=W)
        Label(self, text="", textvariable=self.domain_city).grid(row=8,
                                                                 column=1,
                                                                 sticky=W)
        Label(self, text="", textvariable=self.domain_country).grid(row=9,
                                                                    column=1,
                                                                    sticky=W)

        self.domain_entry = Entry(self)
        self.domain_entry.bind('<Return>', self.get_domain_info)
        self.domain_entry.grid(row=0, column=1)

        # creating a button using the widget
        # Button that will call the submit function
        b = Button(self,
                   text="查询",
                   command=self.get_domain_info,
                   bd=0,
                   padx=10,
                   pady=2)
        b.grid(
            row=0,
            column=2,
            columnspan=2,
            rowspan=2,
            padx=5,
            pady=5,
        )


if __name__ == '__main__':
    App()
