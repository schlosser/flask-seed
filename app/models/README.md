# `/app/models`

[Mongoengine][mongoengine] model definitions live here.

- `User.py` is an example model.
- `__init__.py` imports all of the models for easy importing from elsewhere:
    
    ```python
    from app.models import User
    ```

[mongoengine]: http://docs.mongoengine.org/