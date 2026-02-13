#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# '$Id: allEditor.py,v 1.24 2011/10/21 02:52:46 cmsnow Exp $'
#
#     Copyright(c) 2009 WebCMSNow, Chih-Cheng Yuan.  All rights reserved.
#

import base64
from npmVscode import npmVscode

import json
import os
import re

ShortDesc = """A. Lorem ipsum dolor sit amet
Consectetur's "adipiscing" 'elit'
Integer molestie lorem at massa
Facilisis in pretium nisl aliquet
Nulla volutpat aliquam velit
Phasellus iaculis neque
Purus sodales ultricies
"""
LongDesc = ShortDesc + ShortDesc + ShortDesc + ShortDesc
Blog = LongDesc + LongDesc + LongDesc + LongDesc + LongDesc
ImgPath = 'https://image.webcmsb.com/images/'


class importedMod(npmVscode):
    def __init__(self, loc, linkRoot='', realMode=False):
        sRecord = {
            'MultiRecord': False,
            'RecordDesc': [
                {'Name': 'SlideType', 'Type': 'Enum', 'Option': 'All'},
                {'Name': 'title', 'Type': 'OneLiner', 'Order': 1, 'Size': '80', 'Option': 'JSON'},
                {'Name': 'colBGImage', 'Disabled': '','Option':'All'},
                {'Name': 'colBGImageWrap', 'Disabled':'', 'Option': 'All'},
                {'Name': 'code', 'Disabled':'', 'Option': 'All'},
                {'Name': 'phpFile', 'Disabled':'', 'Option': 'All'},
                {'Name': 'phpFileA', 'Disabled':'', 'Option': 'All'},
                {'Name': 'phpFileB', 'Disabled':'', 'Option': 'All'},
                {'Name': 'composerJSON', 'Disabled':'', 'Option': 'All'},
                {'Name': 'a_file', 'Disabled':'', 'Option': 'All'},
                #{'Name': 'url1', 'Type': 'OneLiner', 'Orde': 3, 'Size': '80', 'Option': 'JSON'},
                #{'Name': 'no', 'Type': 'Integer', 'Size': 3, 'Max': 200, 'Min': 0, 'Option': 'JSON'},

                {'Name': 'author', 'Type': 'OneLiner', 'Orde': 10, 'Size': '80', 'Option': 'JSON'},
                {'Name': 'date', 'Type': 'OneLiner', 'Orde': 10, 'Size': '80', 'Option': 'JSON'},
                #{'Name': 'FirstName', 'Type': 'OneLiner', 'Order': 6, 'Size': '80', 'Option': 'JSON'},
                #{'Name': 'LastName', 'Type': 'OneLiner', 'Order': 7, 'Size': '80', 'Option': 'JSON'},
                {'Name': 'summary', 'Desc': 'Content of blog', 'Order': 110, 'Type': 'tinymce','width': 800, 'height': 150,  'Option': 'JSON'},
                {'Name': 'content', 'Desc': 'Content of blog', 'Order': 115, 'Type': 'tinymce','width': 800, 'height': 350,  'Option': 'JSON'},
                {'Name': 'uimage', 'Order': 210, 'Desc': '360x300', 'Width': 360, 'Height': 300, 'Type': 'SelImage', 'Option': 'JSON'},
                {'Name': 'image', 'Order': 220, 'Desc': '200x200', 'Width': 200, 'Height': 200, 'Type': 'SelImage', 'Option': 'JSON'},
            ],
            'ModDoc': """
<h2> This module has one block per boxe<h2>
""",
            'Var': {
                'height': 600,
                'width': 1440,
                'JQueryPlugin': '',
                'Multi-GPostInc': "",
                # 'MyMethod': '6:Card,6:GCard,6:M_G0,6:M_G1,6:M_GSAP3,6:M_DA,7:ToggleOutput,7:InsertDesign,6:NPM',
                'MyMethod': '6:JSON,6:NPM',
                'insertOrder': 'top',
                'SlideType': [],
                'SlidePri': {},
                'Multi-Help': """
                <h4>An extra initial setup is required.</h4>
                <ul>
                <li>Update the website <li>
                <li>Use NPM button and click npm_install_build_clean to rebuild.</li>
                </ul>
""",
                'Multi-HeadInc': '',
                'Multi-GPostInc': "",
            },
            # contant varable, should not changed
            'VarConstant': {},
            'VarHelp': {},
            'SlideType': ['JSON','PreTag', 'EndTag', 'CodeInc','Include'],
            'SlidePri': {'JSON': 9,'CodeInc':6,'Include': 6, 'PreTag': 6, 'EndTag': 6},
            'Name': '',
        }

        initRecord = []

        initRecord += [{'SlideType': 'CodeInc','aLabel': 'for title and styleing', 'codeInc': """
#*******************************************************************************
# content between styleInc tag will be add to the before the closing head tags
#*******************************************************************************
<styleInc>
<!-- styleInc Included from _ID_ -->
 
<script>
      window.blogTitle = 'AsOne Blog';
      window.blogSubtitle = 'blog subtitle ';
</script>
<style>
#_ID_ .hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

#_ID_ .hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}

#_ID_ .hero-subtitle {
  font-size: 1.15rem;
  opacity: 0.9;
}


</style>

</styleInc>

#*******************************************************************************
# content between scriptInc tag will be add to the before the closing body tags
#*******************************************************************************
<scriptInc>
<!-- scriptInc Included from _ID_ -->

<script>

</script>

</scriptInc>

# End

?>"""}]
        dropDown=""
        for i in range(0, 5):
            sn = str(i)
            catid = 'Category ' + str(i % 3)
            if i < 3: dropDown += catid + '\n'
            initRecord += [{'SlideType': 'JSON', 'title': 'My A Message'+sn,'date': '01/2025',
                'summary': sn + ShortDesc, 'content': sn + LongDesc,'author': 'Author %s'%i,
                            'image': ImgPath + '200x200-woman1.jpg'
                            }]
        initRecord += [{'SlideType': 'Include', 'FileName':'.htaccess', 'IsText': 1, 'AbsolutePath': '','DestPath':'', 'NeedCopy': 1, 'RemoveAfterCopy': 0, 'Content': """
RewriteEngine On
RewriteBase _PagePath_
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . _PagePath_index.php [L]
"""}]

        npmVscode.__init__(self, loc, '', False, initRecord, sRecord)
        self.modGroup = ["bootstrap"]
        self.modName = 'v3_blog'
        self.modDesc = '%s ' % self.modName
        self.myModDir = 'vue3/sample/v3_blog/src/'
        self.modCat = '01_vue3'

    def print_html(self, dbWeb, html, args, data, mdata):
        # to add <div id="app"> </div>
        #args['appIdDiv'] = ''
        args['NotUsedInRootPage'] = 'Python module s_router cannot use in root page'
        return self.s_print_html(dbWeb, html, args, data, mdata)

    def pass_gvars(self, html, host,data, mydata, mydataHTML):
        return """
      <script>
      window.asoneModName = '%s';
      window.asoneId = '%s';
      window.asoneIdx = '_IDX_';
      window.asonePath = '<?php echo $PagePath;?>';
      window.asoneArea = '%s';
      window.asoneLoc = '%s';
      window.asoneData = '%s';
      </script>
<?php

if (!function_exists('findInclude')) {
   function findInclude($bdir) {
      if (!file_exists($bdir)) return;
      $files = scandir($bdir);
      $css ='';
      $js ='';
      foreach ($files as $file) {
         if (strstr($file, '.css')) {
           $css .= '<link href="'.$bdir.$file.'" rel="stylesheet" ></link>';
         }
         if (strstr($file, '.js')) {
           $js .= '<script type="module" src="'.$bdir.$file.'" ></script>';
         }
      }
      echo $css.$js;
   }
}
findInclude('./%s/ws/dist/assets/');

// for ../en-US/..
findInclude('../%s/ws/dist/assets/');
?>

""" % (self.modName, html[1]['id'], data['Area'], self.loc, base64.b64encode(bytes(json.dumps(mydata), encoding="utf-8")).decode("utf-8"), data['Area'], data['Area'])

