# Generated by Django 4.2.3 on 2023-09-27 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import workspace.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('assigned_by', models.ForeignKey(help_text='Select the user who is assigning the task.', on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to=settings.AUTH_USER_MODEL, verbose_name='Assigned By')),
                ('assigned_to', models.ForeignKey(help_text='Select the user to whom the task is being assigned.', on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(help_text='Insert label name', max_length=50, verbose_name='Label name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('soft_delete', models.BooleanField(default=False, verbose_name='Soft delete')),
                ('name', models.CharField(help_text='Enter the name of the project', max_length=200, verbose_name='Project name')),
                ('description', models.TextField(blank=True, help_text='Enter a description for the project.', null=True)),
                ('deadline', models.DateTimeField(blank=True, help_text='The date and time when the project deadline.', null=True, verbose_name='Deadline')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('soft_delete', models.BooleanField(default=False, verbose_name='Soft delete')),
                ('name', models.CharField(help_text='Enter the name of the workspace.', max_length=255, verbose_name='Workspace name')),
                ('description', models.TextField(blank=True, help_text='Enter a description for the workspace', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='workspace/images', validators=[workspace.validators.validate_file_size])),
            ],
            options={
                'verbose_name': 'Workspace',
                'verbose_name_plural': 'Workspaces',
            },
        ),
        migrations.CreateModel(
            name='WorkspaceMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('access_level', models.IntegerField(choices=[(1, 'Member'), (2, 'Admin')], default=1)),
                ('member', models.ForeignKey(help_text='Users who are members of this workspace.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace', to='workspace.workspace', verbose_name='Workspace')),
            ],
            options={
                'unique_together': {('workspace', 'member', 'access_level')},
            },
        ),
        migrations.AddField(
            model_name='workspace',
            name='member',
            field=models.ManyToManyField(through='workspace.WorkspaceMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('soft_delete', models.BooleanField(default=False, verbose_name='Soft delete')),
                ('title', models.CharField(help_text='Enter the title of the task.', max_length=250, verbose_name='Title')),
                ('description', models.TextField(help_text='Provide a detailed description of the task.', verbose_name='Description')),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('suspend', 'Suspended'), ('done', 'Done')], default='todo', help_text="The current status of the task.          Choose from 'To Do', 'Doing', 'Suspended', or 'Done'.", max_length=20, verbose_name='Status')),
                ('start_date', models.DateTimeField(auto_now_add=True, help_text='The date and time when the task was created.', verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, help_text='The date and time when the task was completed.', null=True, verbose_name='End Date')),
                ('due_date', models.DateTimeField(blank=True, help_text='The date and time by which the task should be completed.', null=True, verbose_name='Due Date')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', help_text="The priority level of the task.            Choose from 'Low', 'Medium', or 'High'.", max_length=20, verbose_name='Priority')),
                ('assigned_by', models.ManyToManyField(help_text='Select the users who are assigning the task.', related_name='assignment_given', through='workspace.Assignment', to=settings.AUTH_USER_MODEL, verbose_name='Assigned By')),
                ('assigned_to', models.ManyToManyField(help_text='Select the users to whom the task is being assigned.', related_name='assignment_received', through='workspace.Assignment', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
                ('project', models.ForeignKey(help_text='The project to which this task belongs.', on_delete=django.db.models.deletion.CASCADE, to='workspace.project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('member', models.ForeignKey(help_text='Users who are members of this workspace.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='workspace.project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(through='workspace.ProjectMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='workspace',
            field=models.ForeignKey(help_text='Select the workspace this project belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='workspace.workspace'),
        ),
        migrations.CreateModel(
            name='LabeledTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('label', models.ForeignKey(help_text='Label to use', on_delete=django.db.models.deletion.CASCADE, related_name='label', to='workspace.label', verbose_name='Label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.task', verbose_name='Task to label')),
            ],
            options={
                'unique_together': {('label', 'task')},
            },
        ),
        migrations.AddField(
            model_name='label',
            name='task',
            field=models.ManyToManyField(through='workspace.LabeledTask', to='workspace.task'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('soft_delete', models.BooleanField(default=False, verbose_name='Soft delete')),
                ('text', models.TextField(help_text='Write comment', verbose_name='Comment text')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.task', verbose_name='Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='task',
            field=models.ForeignKey(help_text='Select the task that is being assigned.', on_delete=django.db.models.deletion.CASCADE, to='workspace.task', verbose_name='Task'),
        ),
    ]
