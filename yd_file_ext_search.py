#!/usr/bin/env python
import glob
import os
from yd_console import YDConsole
from yd_error_handling import YDErrorHandling
from enum import Enum

class YDDepth(Enum):
    HEAVY = 1
    LIGHT = 0

class YDFileExtensionSearch:

    def __init__ ( self, root_directory, log_depth:YDDepth ):
        self.root_directory = root_directory

        if self.root_directory:
            self.app_bundle_dir = self.return_app_bundle()

        self.exec_path = str()
        self.log_level = log_depth
        self.general_settings = ['CFBundleName', 'CFBundleExecutable', 'CFBundleIdentifier', 'MinimumOSVersion',
                                 'UILaunchStoryboardName']
        self.wildcard_searches = ['account', 'key', 'api', 'secret']
        self.directory_extensions = ['framework','bundle'] #'storyboardc'
        self.file_extensions_light = ['json','cert','crt','html','js','cer','pub','txt']
        self.file_extensions_deep = ['plist','strings']
        self.target_permissions = ['framework','bundle','storyboardc']

        if self.log_level == YDDepth.HEAVY:
            self.list_files()
            self.list_frameworks()
            self.inspect_info_plist()
        else:
            self.inspect_info_plist()


    def __str__ ( self ):
        return "Log level " + str(self.log_level)

    def return_app_bundle( self ):
        plist_hunt= os.path.join(self.root_directory + '/*.app')
        for i in glob.glob(plist_hunt):
            YDConsole.single_label_and_value('Found app bundle name', os.path.basename(i))
            return i
        YDErrorHandling.exit_on_usage('no app bundle name found')

    def get_executable_path( self ):
        return("/file/path")

    def list_files(self):

        extension_final = self.file_extensions_light
        if self.log_level == YDDepth.HEAVY:
            extension_final =  self.file_extensions_light + self.file_extensions_deep

        for i in extension_final:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for f in files:
                    if f.endswith(i):
                        YDConsole.single_value_subheading(os.path.join(root, f))
        return None

    def list_frameworks(self):
        for i in self.directory_extensions:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for d in dirs:
                    if d.endswith(i):
                        YDConsole.single_value_subheading(d)

        return None


    def inspect_info_plist(self):
        target_infoplist = self.app_bundle_dir + '/Info.plist'
        if os.path.isfile(target_infoplist) == True:
            YDConsole.banner('Searching: ' + target_infoplist)

        try:
            import plistlib
        except ImportError:
            return None

        with open(target_infoplist, 'rb') as f:
            pl = plistlib.load(f)

        temp_permission_dict,temp_settings_dict,temp_wildcards_dict  = {},{},{}  # avoid mix up of data when printing

        for key, value in pl.items():

            if key in self.general_settings:
                temp_settings_dict[key] = value
                if key == 'CFBundleExecutable':
                    self.exec_path = os.path.join(self.app_bundle_dir + '/' + value)
                    YDConsole.single_value_subheading(f'found exec file: {value}')

            if key.startswith('NS'):
                temp_permission_dict[key] = value

            for i in self.wildcard_searches:
                if i.lower() in key.lower():
                    temp_wildcards_dict[key] = value

        if len(temp_settings_dict) > 0:
            self.print_dict_from_plist('settings',temp_settings_dict)

        if len(temp_permission_dict) > 0:
            self.print_dict_from_plist('user permissions', temp_permission_dict)
        else:
            YDConsole.single_label_and_value('user permissions','none found')

        if len(temp_wildcards_dict) > 0:
            self.print_dict_from_plist('wildcards in plist', temp_wildcards_dict)
        return None

    def print_dict_from_plist(self, title: str, findings: dict):
        YDConsole.banner(title)
        for k, v in findings.items():
            YDConsole.single_label_and_value(k, v)

        return None