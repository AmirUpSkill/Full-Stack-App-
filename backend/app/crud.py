from sqlalchemy.orm import Session
from . import models, schemas

def get_task(db: Session , task_id: int):
    """
    Retrieve a single task by its ID.
    
    Args:
        db (Session): The database session
        task_id (int): The ID of the task to retrieve
        
    Returns:
        Task: The task object if found, None otherwise
    """
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0 , limit: int = 100):
    """
    Retrieve a list of tasks with pagination.
    
    Args:
        db (Session): The database session
        skip (int): Number of records to skip (default: 0)
        limit (int): Maximum number of records to return (default: 100)
        
    Returns:
        List[Task]: List of task objects
    """
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session , task: schemas.TaskCreate):
    """
    Create a new task.
    
    Args:
        db (Session): The database session
        task (TaskCreate): The task data to create
        
    Returns:
        Task: The created task object
    """
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session , task_id: int , task: schemas.TaskUpdate):
    """
    Update an existing task.
    
    Args:
        db (Session): The database session
        task_id (int): The ID of the task to update
        task (TaskUpdate): The updated task data
        
    Returns:
        Task: The updated task object if found, None otherwise
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None
    db_task.title = task.title
    db_task.is_completed = task.is_completed
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    """
    Delete a task by its ID.
    
    Args:
        db (Session): The database session
        task_id (int): The ID of the task to delete
        
    Returns:
        Task: The deleted task object if found, None otherwise
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None
    db.delete(db_task)
    db.commit()
    return db_task