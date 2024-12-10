from utils.api import serializers

class CreateEditWebsiteConfigSerializer(serializers.Serializer):
    website_base_url = serializers.CharField(max_length=128)
    website_name = serializers.CharField(max_length=64)
    website_name_shortcut = serializers.CharField(max_length=64)
    website_footer = serializers.CharField(max_length=1024 * 1024)
    allow_register = serializers.BooleanField()
    submission_list_show_all = serializers.BooleanField()


class JudgeServerHeartbeatSerializer(serializers.Serializer):
    hostname = serializers.CharField(max_length=128)
    judger_version = serializers.CharField(max_length=32)
    cpu_core = serializers.IntegerField(min_value=1)
    memory = serializers.FloatField(min_value=0, max_value=100)
    cpu = serializers.FloatField(min_value=0, max_value=100)
    action = serializers.ChoiceField(choices=("heartbeat", ))
    service_url = serializers.CharField(max_length=256)
