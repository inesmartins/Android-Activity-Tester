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
        activity_xml = activity.toxml()
        export_explicit = 'android:exported="true"' in activity_xml
        export_implicit = 'android:exported="false"' not in activity_xml and '<intent-filter>' in activity_xml
        activity_name = activity_xml.split('android:name="')[1].split('"')[0]
        if export_explicit or export_implicit:
            activities_dictionary[activity_name] = True
        else:
            activities_dictionary[activity_name] = False
    return activities_dictionary

def get_adb_formatted_activity(activity_name, package_name):
    if package_name in activity_name:
        return '.' + activity_name.split(package_name + '.')[1]
    else:
        return activity_name

if __name__ == '__main__':
    args = get_parsed_args()
    dict = get_activities_dictionary(args.manifest)

    print('\n=================== Explicitly/Implicitly Exported Activities =================== ')
    for entry in dict:
        if dict[entry] == True:
            print(entry)

    print('\n=================== Non-Exported Activities ===================')
    for entry in dict:
        if dict[entry] == False:
            print(entry)

    print('\n=================== Launch Exported Activities with ADB ===================')
    for entry in dict:
        if dict[entry] == True:
            os.system('adb shell am start -n ' + args.package + '/' + get_adb_formatted_activity(entry, args.package))
            input("Press Enter to continue...")

    print('\n=================== Launch Non-Exported Activities with ADB Root ===================')
    os.system('adb root')
    for entry in dict:
        if dict[entry] == False:
            os.system('adb shell am start -n ' + args.package + '/' + get_adb_formatted_activity(entry, args.package))
            input("Press Enter to continue...")