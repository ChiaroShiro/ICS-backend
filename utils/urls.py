#from django.conf.urls import url

from django.urls import re_path

from .views import SimditorImageUploadAPIView, SimditorFileUploadAPIView

urlpatterns = [
    re_path(r"^upload_image/?$", SimditorImageUploadAPIView.as_view(), name="upload_image"),
    re_path(r"^upload_file/?$", SimditorFileUploadAPIView.as_view(), name="upload_file")
]

"""
    API 说明：

        本文件定义了针对图像上传和文件上传功能的接口

"""
