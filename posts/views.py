from .models import Post
from rest_framework import viewsets, permissions, serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     return self.request.user.posts.all()
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
