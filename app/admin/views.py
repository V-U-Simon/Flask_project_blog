from flask_admin.contrib.sqla import ModelView
# from flask_login import current_user
# from flask import redirect, url_for


class CustomAdminView(ModelView):
    # def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, static_folder=None, menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
    #     super().__init__(model, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type, menu_icon_value)

    def create_blueprint(self, admin):
        blueprint = super().create_blueprint(admin)
        blueprint.name = f'{blueprint.name}_admin'
        return blueprint
    
    
    def get_url(self, endpoint, **kwargs):
        if not (endpoint.startswith('.') or endpoint.startswith('admin.')):
            endpoint = endpoint.replace('.', '_admin.')
        return super().get_url(endpoint, **kwargs)

    


# class ArticleAdminView(CustomAdminView):
#     can_export = True
#     export_types = ('csv', 'xlsx')
#     column_filters = ('author_id',)
    
    


    
    
