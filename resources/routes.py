def init_routes(api):
    from resources.users_resources import UserResource, UserListResource
    from resources.homework_resources import HomeworkResource, HomeworkListResource
    from resources.teachers_resources import TeachersResource, TeachersListResource

    api.add_resource(UserResource, '/api/v1/users/<user_id>')
    api.add_resource(HomeworkResource, '/api/v1/homeworks/<homework_id>')
    api.add_resource(TeachersResource, '/api/v1/teachers/<teacher_id>')
    
    api.add_resource(UserListResource, '/api/v1/users')
    api.add_resource(HomeworkListResource, '/api/v1/homework')
    api.add_resource(TeachersListResource, '/api/v1/teachers')
    
