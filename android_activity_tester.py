import os
from xml.dom.minidom import parseString
import argparse

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--manifest', 
                        dest="manifest",
                        required=True,
                        metavar="FILE", 
    					type=lambda x: is_valid_file(parser, x),
                        help='Path to the AndroidManifest.xml file')    
    parser.add_argument('-p', '--package', 
                        dest="package",
                        required=True,
                        help='Package name, e.g.: com.twitter.android')    
    args = parser.parse_args()
    return args

def get_activities_dictionary(manifest_file_path):
    data = ''
    with open(manifest_file_path,'r') as f:
        data = f.read()
    dom = parseString(data)
    activities = dom.getElementsByTagName('activity')
    activities_dictionary = {}
    for activity in activities:
        activity_name = activity.toxml().split('android:name="')[1].split('"')[0]
        activities_dictionary[activity_name] = 'android:exported="true"' in activity.toxml() or '<intent-filter>' in activity.toxml()
    return activities_dictionary

def get_adb_formatted_activity(activity_name, package_name):
    if package_name in activity_name:
        return '.' + activity_name.split(package_name + '.')[1]
    else:
        return activity_name

if __name__ == '__main__':
    args = get_parsed_args()
    dict = get_activities_dictionary(args.manifest)

    print('\n=================== Exported =================== ')
    for entry in dict:
        if dict[entry] == True:
            print(entry)

    print('\n=================== Not Exported ===================')
    for entry in dict:
        if dict[entry] == False:
            print(entry)

    print('\n=================== ADB Test ===================')
    for entry in dict:
        if dict[entry] == True:
            os.system('adb shell am start -n ' + args.package + '/' + get_adb_formatted_activity(entry, args.package))
            input("Press Enter to continue...")