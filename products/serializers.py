from  rest_framework import serializers

from .models import Product, Category, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title','file')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title', 'description', 'avatar', 'categories','files','url')





      