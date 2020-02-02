/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.youtube_width = 640;
    config.youtube_height = 360;
    config.youtube_responsive = true;
    config.youtube_related = false;
    config.youtube_older = false;
    config.youtube_disabled_fields = ['txtWidth', 'txtHeight'];


};
