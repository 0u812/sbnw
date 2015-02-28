cmake_minimum_required (VERSION 2.8)
project (Graphfab)

install(FILES 32x32/document-new-8.png 32x32/document-open-7.png 32x32/document-save-5.png 32x32/document-save-as-5.png 32x32/application-exit-5.png 32x32/help-about-2.png 32x32/edit-select.png 32x32/edit-node.png 32x32/view-refresh-3.png 32x32/draw-eraser-2.png 32x32/lock.png 32x32/draw-line-2.png 32x32/insert-link-2.png 32x32/homepage.png 32x32/gnome-iagno.png 32x32/system-settings.png DESTINATION icons/32x32)
if(GRAPHFAB_SPYDER_DIST)
install(FILES 32x32/document-new-8.png 32x32/document-open-7.png 32x32/document-save-5.png 32x32/document-save-as-5.png 32x32/application-exit-5.png 32x32/help-about-2.png 32x32/edit-select.png 32x32/edit-node.png 32x32/view-refresh-3.png 32x32/draw-eraser-2.png 32x32/lock.png 32x32/draw-line-2.png 32x32/insert-link-2.png 32x32/homepage.png 32x32/gnome-iagno.png 32x32/system-settings.png DESTINATION python2/spyderplugins/pyfab-assets/icons/32x32)
endif()