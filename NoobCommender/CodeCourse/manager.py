from django.contrib.auth.base_user import BaseUserManager
#create your manager here ... 

class UserManager(BaseUserManager):
    use_in_migration = True
    
    def _create_user(self,username):
        pass