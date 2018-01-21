# Generated by Django 2.0.1 on 2018-01-20 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_remove_document_summary_top_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentSummary',
            fields=[
                ('document_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crawler.Document')),
                ('sentences_n', models.IntegerField()),
                ('text_rank', models.TextField()),
                ('word_count', models.TextField()),
                ('word_tfidf', models.TextField()),
                ('summary_text', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Sentiment_list',
            new_name='SentimentList',
        ),
        migrations.RemoveField(
            model_name='document_summary',
            name='document_id',
        ),
        migrations.DeleteModel(
            name='Document_summary',
        ),
    ]