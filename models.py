from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Table
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blog'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author_id=Column(Integer,ForeignKey('user.id'))
    author=relationship("User",back_populates='blogs')

class User(Base):
    __tablename__='user'

    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String)
    email=Column(String,unique=True)
    password=Column(String)
    blogs=relationship("Blog",back_populates='author')


# class User(Base):
#     __tablename__='user'

#     id=Column(Integer,primary_key=True,index=True)
#     user_name=Column(String,index=True)
#     password=Column(String)
#     profile=relationship("Profile",back_populates='user',uselist=False) 
#     posts=relationship("Posts",back_populates='author')

# class Profile(Base):
#     __tablename__='profile'

#     id=Column(Integer,primary_key=True,index=True)
#     first_name=Column(String)
#     last_name=Column(String)
#     user_id=Column(Integer,ForeignKey('user.id'),unique=True)
#     user=relationship("User",back_populates='profile')

# post_tag=Table(
#     "post_tag",
#     Base.metadata,
#     Column("post_id",Integer,ForeignKey("posts.id"),primary_key=True),
#     Column("tag_id",Integer,ForeignKey("tags.id"),primary_key=True)
# )

# class Post(Base): 
#     __tablename__='posts'
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String)
#     content=Column(String)
#     author_id=Column(Integer,ForeignKey('user.id'))
#     author=relationship("User",back_populates='posts')
#     tags=relationship("Tag",secondary=post_tag,back_populates="posts")

# class Tag(Base):
#     __tablename__='tags'
#     id=Column(Integer,primary_key=True,index=True)
#     tag_name=Column(String,unique=True)
#     posts=relationship("Post",secondary=post_tag,back_populates="tags")



# from .database import Base
# from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey, ARRAY, JSON
# from sqlalchemy.orm import relationship

# class User(Base):
#     __tablename__ = "users"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     first_name = Column(String)
#     middle_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     phone_number = Column(String)
#     address = Column(String)
#     dob = Column(TIMESTAMP(timezone=True))
#     weight = Column(Integer)
#     height = Column(String)
#     photo = Column(String)
#     language = Column(String)
#     user_status = Column(String, server_default='Active')
#     address_json = Column(JSON)
#     email_consent = Column(Boolean, server_default='true')
#     phone_consent = Column(Boolean, server_default='true')
#     # Relationships
#     milestones = relationship("Milestone", back_populates="user")
#     comments = relationship("Comment", back_populates="user")
#     user_milestones = relationship("UserMilestone", back_populates="user")
#     resource_links = relationship("ResourceLink", back_populates="user")
#     goals = relationship("Goal", back_populates="user")
#     goal_links = relationship("GoalLinks", back_populates="user")
#     mentor_notes = relationship("Notes", foreign_keys="[Notes.mentor_id]", back_populates="mentor")
#     user_notes = relationship("Notes", foreign_keys="[Notes.user_id]", back_populates="user")
#     user_badges = relationship("UserBadge", back_populates="user")
#     apis = relationship("API", back_populates="created_by_user")
#     children = relationship("Children", back_populates="parent")
#     file_manager = relationship("FileManager", back_populates="user")
#     form_access = relationship("FormAccess", back_populates="user")
#     created_forms = relationship("FormMetadata", back_populates="created_by_user", foreign_keys="[FormMetadata.created_by_id]")
#     updated_forms = relationship("FormMetadata", back_populates="updated_by_user", foreign_keys="[FormMetadata.updated_by_id]")
#     notifications = relationship("Notification", back_populates="user")
#     sessions = relationship("Session", back_populates="user")
#     tokens = relationship("Token", back_populates="user")
#     user_groups = relationship("UserGroup", back_populates="user")
#     user_regions = relationship("UserRegion", back_populates="user")
#     user_roles = relationship("UserRole", back_populates="user")
#     user_tags = relationship("UserTagRelation", back_populates="user")
#     parents = relationship("UserMentor", foreign_keys="[UserMentor.mentor_id]", back_populates="mentor")
#     mentors = relationship("UserMentor", foreign_keys="[UserMentor.user_id]", back_populates="user")
#     original_messages = relationship("Message", foreign_keys="[Message.original_sender_id]", back_populates="original_sender")
#     received_messages = relationship("Message", foreign_keys="[Message.receiver_id]", back_populates="receiver")
#     sent_messages = relationship("Message", foreign_keys="[Message.sender_id]", back_populates="sender")

# class Milestone(Base):
#     __tablename__ = "milestone"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     suggestions = Column(String)
#     image = Column(String)
#     resources_link = Column(String)
#     is_user_created = Column(Boolean, default=True)
#     is_not_template = Column(Boolean, default=False)
#     created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
#     sub_category_id = Column(Integer, ForeignKey('sub_category.id'), nullable=False)
#     time_interval = Column(Integer, default=0)
#     is_public = Column(Boolean, default=True)
#     # Relationships
#     user = relationship("User", back_populates="milestones")
#     category = relationship("Category", back_populates="milestones")
#     sub_category = relationship("SubCategory", back_populates="milestones")
#     resources = relationship("MilestonesResource", back_populates="milestone")
#     user_milestones = relationship("UserMilestone", back_populates="milestone")
#     goals = relationship("Goal", back_populates="milestone")
#     questions = relationship("Question", back_populates="milestone")
#     resource_links = relationship("ResourceLink", back_populates="milestone")

# class UserMilestone(Base):
#     __tablename__ = "user_milestone"
     
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     created_by_id = Column(Integer, nullable=False)
#     start_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     end_date = Column(TIMESTAMP(timezone=True), nullable=False)
#     vision = Column(String)
#     purpose = Column(String)
#     obstacle = Column(String)
#     active = Column(Boolean, default=True)
#     mentees = Column(ARRAY(Integer))
#     status = Column(Boolean, default=False)
#     mentor_notes = Column(String)
#     additional_notes = Column(String)
#     suggestions = Column(String)
#     milestone_id = Column(Integer, ForeignKey('milestone.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     parent_milestone_id = Column(Integer)
#     time_interval = Column(Integer, default=0)
#     is_template = Column(Boolean, default=False)
#     # Relationships
#     milestone = relationship("Milestone", back_populates="user_milestones")
#     user = relationship("User", back_populates="user_milestones")
#     answers = relationship("Answer", back_populates="user_milestone")
#     comments = relationship("Comment", back_populates="user_milestone")
#     resource_links = relationship("ResourceLink", back_populates="user_milestone")
#     goals = relationship("UserGoal", back_populates="user_milestone")

# class UserGoal(Base):
#     __tablename__ = "user_goal"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     created_by_id = Column(Integer, nullable=False)
#     start_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     end_date = Column(TIMESTAMP(timezone=True), nullable=False)
#     recursing_goals = Column(JSON)
#     notes = Column(String)
#     active = Column(Boolean, default=True)
#     private = Column(Boolean, default=False)
#     status = Column(Boolean, default=False)
#     goal_id = Column(Integer, ForeignKey('goal.id'), nullable=False)
#     user_milestone_id = Column(Integer, ForeignKey('user_milestone.id'), nullable=False)
#     # Relationships
#     goal = relationship("Goal", back_populates="user_goals")
#     user_milestone = relationship("UserMilestone", back_populates="goals")
#     user_goal_links = relationship("GoalLinks", back_populates="user_goal")

# class Goal(Base):
#     __tablename__ = "goal"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     value = Column(String, nullable=False)
#     description = Column(String)
#     is_user_created = Column(Boolean, default=True)
#     frequency = Column(String, nullable=False)
#     count = Column(Integer)
#     is_not_template = Column(Boolean, default=False)
#     week_days = Column(ARRAY(String))
#     month_days = Column(ARRAY(Integer))
#     created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     milestone_id = Column(Integer, ForeignKey('milestone.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="goals")
#     milestone = relationship("Milestone", back_populates="goals")
#     goal_links = relationship("GoalLinks", back_populates="goal")
#     goal_user_goals = relationship("UserGoal", back_populates="goal")

# class GoalLinks(Base):
#     __tablename__ = "goal_links"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     link = Column(String, nullable=False)
#     goal_id = Column(Integer, ForeignKey('user_goal.id'))
#     goal_template_id = Column(Integer, ForeignKey('goal.id'))
#     created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="goal_links")
#     user_goal = relationship("UserGoal", back_populates="user_goal_links")
#     goal = relationship("Goal", back_populates="goal_links")

# class ResourceLink(Base):
#     __tablename__ = "resource_link"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     link = Column(String, nullable=False)
#     milestone_id = Column(Integer, ForeignKey('user_milestone.id'))
#     milestone_template_id = Column(Integer, ForeignKey('milestone.id'))
#     created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="resource_links")
#     user_milestone = relationship("UserMilestone", back_populates="resource_links")
#     milestone = relationship("Milestone", back_populates="resource_links")

# class Comment(Base):
#     __tablename__ = "comment"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     text = Column(String, nullable=False)
#     milestone_id = Column(Integer, ForeignKey('user_milestone.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     user_milestone = relationship("UserMilestone", back_populates="comments")
#     user = relationship("User", back_populates="comments")

# class Answer(Base):
#     __tablename__ = "answer"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     answer = Column(String, nullable=False)
#     question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
#     user_milestone_id = Column(Integer, ForeignKey('user_milestone.id'), nullable=False)
#     # Relationships
#     question = relationship("Question", back_populates="answers")
#     user_milestone = relationship("UserMilestone", back_populates="answers")

# class Question(Base):
#     __tablename__ = "question"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     question = Column(String, nullable=False)
#     question_type = Column(String)
#     order = Column(Integer)
#     answer_option = Column(JSON)
#     unit_of_measurement = Column(String)
#     milestone_id = Column(Integer, ForeignKey('milestone.id'), nullable=False)
#     # Relationships
#     milestone = relationship("Milestone", back_populates="questions")
#     answers = relationship("Answer", back_populates="question")

# class Category(Base):
#     __tablename__ = "category"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     hidden = Column(Boolean, default=False)
#     is_milestone = Column(Boolean, default=True)
#     is_resources = Column(Boolean, default=False)
#     image = Column(String)
#     icon = Column(String, nullable=False)
#     color = Column(String, nullable=False)
#     sort_order = Column(Integer, default=0)
#     # Relationships
#     milestones = relationship("Milestone", back_populates="category")
#     sub_categories = relationship("SubCategory", back_populates="category")
#     resources = relationship("Resource", back_populates="category")

# class SubCategory(Base):
#     __tablename__ = "sub_category"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     is_milestone = Column(Boolean, default=True)
#     is_resources = Column(Boolean, default=False)
#     category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
#     # Relationships
#     category = relationship("Category", back_populates="sub_categories")
#     milestones = relationship("Milestone", back_populates="sub_category")
#     resources = relationship("Resource", back_populates="sub_category")

# class Resource(Base):
#     __tablename__ = "resource"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     html_code = Column(String)
#     attachment = Column(String)
#     content_type = Column(String, default="Richtext")
#     slug = Column(String, nullable=False, unique=True)
#     category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
#     sub_category_id = Column(Integer, ForeignKey('sub_category.id'), nullable=False)
#     public = Column(Boolean, default=False)
#     # Relationships
#     category = relationship("Category", back_populates="resources")
#     sub_category = relationship("SubCategory", back_populates="resources")
#     milestone_resources = relationship("MilestonesResource", back_populates="resource")
#     resource_tags = relationship("ResourceTag", back_populates="resource")

# class ResourceTag(Base):
#     __tablename__ = "resource_tag"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     resource_id = Column(Integer, ForeignKey('resource.id'), nullable=False)
#     tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)
#     # Relationships
#     resource = relationship("Resource", back_populates="resource_tags")
#     tag = relationship("Tag", back_populates="resources")
   
# class Tag(Base):
#     __tablename__="tag"
   
#     id = Column(Integer,primary_key=True,index=True)
#     created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String,nullable=False)
#     #relationships
#     resources = relationship("ResourceTag",back_populates="tag")
   
# class MilestonesResource(Base):
#     __tablename__="milestones_resource"
   
#     id = Column(Integer,primary_key=True,index=True)
#     created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     milestone_id = Column(Integer,ForeignKey('milestone.id'),nullable=False)
#     resource_id = Column(Integer,ForeignKey('resource.id'),nullable=False)
#     #relationships
#     milestone = relationship("Milestone",back_populates="resources")
#     resource = relationship("Resource",back_populates="milestone_resources")

# class Badge(Base):
#     __tablename__ = "badge"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     image = Column(String)
#     count = Column(Integer)
#     type = Column(String)
#     # Relationships
#     users = relationship("UserBadge", back_populates="badge")

# class UserBadge(Base):
#     __tablename__ = "user_badge"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     badge_id = Column(Integer, ForeignKey('badge.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="user_badges")
#     badge = relationship("Badge", back_populates="users")

# class Notes(Base):
#     __tablename__ = "notes"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     note = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     mentor_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     mentor = relationship("User", foreign_keys=[mentor_id], back_populates="mentor_notes")
#     user = relationship("User", foreign_keys=[user_id], back_populates="user_notes")

# class Event(Base):
#     __tablename__ = "event"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     created_by = Column(Integer)
#     table_name = Column(String)
#     reference_record_id = Column(Integer)
#     action = Column(String)
#     description = Column(String)
#     event_description_id = Column(Integer, ForeignKey('event_description.id'), nullable=False)
#     # Relationships
#     description = relationship("EventDescription", back_populates="events")

# class EventDescription(Base):
#     __tablename__ = "event_description"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     event_name = Column(String, unique=True)
#     description = Column(String)
#     # Relationships
#     events = relationship("Event", back_populates="description")

# class Group(Base):
#     __tablename__ = "group"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String)
#     description = Column(String, server_default='')
#     parent_id = Column(Integer, ForeignKey('group.id'))
#     is_chat = Column(Boolean, default=True)
#     # Relationships
#     parent = relationship("Group", remote_side=[id], back_populates="subgroups")
#     subgroups = relationship("Group", back_populates="parent")
#     group_permissions = relationship("GroupResourcePermission", back_populates="group")

# class GroupResourcePermission(Base):
#     __tablename__ = "group_resource_permission"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
#     resource_id = Column(Integer)
#     type = Column(String)
#     permission = Column(ARRAY(String))
#     # Relationships
#     group = relationship("Group", back_populates="group_permissions")

# class UiCustomization(Base):
#     __tablename__ = "ui_customization"
   
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String)
#     active = Column(Boolean, default=False)
#     url = Column(String)
#     top_nav_color = Column(String)
#     sidebar_color = Column(String)
#     text_size = Column(Integer)
#     top_nav_height = Column(Integer, default=48)

# class API(Base):
#     __tablename__ = "api"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     key = Column(String, unique=True, nullable=False)
#     secret = Column(String, nullable=False)
#     is_active = Column(Boolean, default=False)
#     created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     created_by_user = relationship("User", back_populates="apis")
#     api_events = relationship("ApiEvents", back_populates="api")

# class ApiEvents(Base):
#     __tablename__ = "api_events"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     api_key = Column(String, ForeignKey('api.key'), nullable=False)
#     description = Column(String, nullable=False)
#     reference_record_id = Column(String, default="")
#     # Relationships
#     api = relationship("API", back_populates="api_events")

# class UserRole(Base):
#     __tablename__ = "user_role"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="user_roles")
#     role = relationship("Role", back_populates="user_roles")

# class Role(Base):
#     __tablename__ = "role"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     permission_id = Column(Integer, default=1)
#     # Relationships
#     user_roles = relationship("UserRole", back_populates="role")
#     role_menus = relationship("RoleMenu", back_populates="role")
#     role_permissions = relationship("RolePermission", back_populates="role")

# class UserMentor(Base):
#     __tablename__ = "user_mentor"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     mentor_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     mentor = relationship("User", foreign_keys=[mentor_id], back_populates="parents")
#     user = relationship("User", foreign_keys=[user_id], back_populates="mentors")

# class Children(Base):
#     __tablename__ = "children"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     first_name = Column(String)
#     last_name = Column(String)
#     dob = Column(TIMESTAMP(timezone=True))
#     due_date = Column(TIMESTAMP(timezone=True))
#     gender = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     parent = relationship("User", back_populates="children")

# class Region(Base):
#     __tablename__ = "region"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     active = Column(Boolean, default=True)
#     private = Column(Boolean, default=False)
#     level = Column(Integer)
#     region_id = Column(Integer, ForeignKey('region.id'))
#     # Relationships
#     parent_region = relationship("Region", remote_side=[id], back_populates="regions")
#     regions = relationship("Region", back_populates="parent_region")
#     region_providers_corner = relationship("RegionProvidersCorner", back_populates="region")
#     user_regions = relationship("UserRegion", back_populates="region")

# class UserRegion(Base):
#     __tablename__ = "user_region"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     region = relationship("Region", back_populates="user_regions")
#     user = relationship("User", back_populates="user_regions")

# class Message(Base):
#     __tablename__ = "message"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     text = Column(String, nullable=False)
#     sent = Column(Boolean, default=False)
#     delivered = Column(Boolean, default=False)
#     read = Column(Boolean, default=False)
#     receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     original_sender_id = Column(Integer, ForeignKey('users.id'))
#     # Relationships
#     original_sender = relationship("User", foreign_keys=[original_sender_id], back_populates="original_messages")
#     receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_messages")
#     sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_messages")

# class Session(Base):
#     __tablename__ = "session"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     expires_at = Column(TIMESTAMP(timezone=True))
#     handle = Column(String, unique=True)
#     hashed_session_token = Column(String)
#     anti_csrf_token = Column(String)
#     public_data = Column(String)
#     private_data = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     # Relationships
#     user = relationship("User", back_populates="sessions")

# class Token(Base):
#     __tablename__ = "token"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     hashed_token = Column(String, nullable=False)
#     type = Column(String, nullable=False)
#     expires_at = Column(TIMESTAMP(timezone=True), nullable=False)
#     sent_to = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="tokens")

# class FileManager(Base):
#     __tablename__ = "file_manager"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     path = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="file_manager")

# class Menu(Base):
#     __tablename__ = "menu"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     icon = Column(String, nullable=False)
#     link = Column(String, nullable=False)
#     is_topbar_menu = Column(Boolean, default=False)
#     is_mobilenav = Column(Boolean, default=False)
#     is_hidden_sidebar = Column(Boolean, default=False)
#     sort_order = Column(Integer, default=0)
#     menu_id = Column(Integer, ForeignKey('menu.id'))
#     # Relationships
#     parent_menu = relationship("Menu", remote_side=[id], back_populates="sub_menus")
#     sub_menus = relationship("Menu", back_populates="parent_menu")
#     role_menus = relationship("RoleMenu", back_populates="menu")

# class RoleMenu(Base):
#     __tablename__ = "role_menu"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
#     menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
#     # Relationships
#     role = relationship("Role", back_populates="role_menus")
#     menu = relationship("Menu", back_populates="role_menus")

# class FormMetadata(Base):
#     __tablename__ = "form_metadata"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
#     updated_by = Column(Integer, ForeignKey('users.id'), nullable=False)
#     name = Column(String, nullable=False)
#     description = Column(String)
#     version = Column(Integer, default=0)
#     meta_json = Column(JSON)
#     response_json = Column(JSON)
#     is_complex_large_form = Column(Boolean, default=False)
#     new_table_name = Column(String)
#     is_public = Column(Boolean, default=False)
#     # Relationships
#     created_by_user = relationship("User", foreign_keys=[created_by], back_populates="created_forms")
#     updated_by_user = relationship("User", foreign_keys=[updated_by], back_populates="updated_forms")

# class PCCategory(Base):
#     __tablename__ = "pc_category"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     hidden = Column(Boolean, default=False)
#     image = Column(String)
#     icon = Column(String, nullable=False)
#     color = Column(String, nullable=False)
#     # Relationships
#     sub_categories = relationship("PCSubCategory", back_populates="category")
#     providers_corners = relationship("ProvidersCorner", back_populates="category")

# class PCSubCategory(Base):
#     __tablename__ = "pc_sub_category"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     category_id = Column(Integer, ForeignKey('pc_category.id'), nullable=False)
#     # Relationships
#     category = relationship("PCCategory", back_populates="sub_categories")
#     providers_corners = relationship("ProvidersCorner", back_populates="sub_category")

# class PCTag(Base):
#     __tablename__ = "pc_tag"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     # Relationships
#     providers_corner_tags = relationship("ProvidersCornerTag", back_populates="tag")

# class ProvidersCorner(Base):
#     __tablename__ = "providers_corner"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     html_code = Column(String)
#     attachment = Column(String)
#     content_type = Column(String, default="Richtext")
#     category_id = Column(Integer, ForeignKey('pc_category.id'), nullable=False)
#     sub_category_id = Column(Integer, ForeignKey('pc_sub_category.id'), nullable=False)
#     public = Column(Boolean, default=False)
#     slug = Column(String, server_default="")
#     # Relationships
#     category = relationship("PCCategory", back_populates="providers_corners")
#     sub_category = relationship("PCSubCategory", back_populates="providers_corners")
#     provider_corner_tags = relationship("ProvidersCornerTag", back_populates="providers_corner")
#     region_providers_corners = relationship("RegionProvidersCorner", back_populates="providers_corner")

# class RegionProvidersCorner(Base):
#     __tablename__ = "region_providers_corner"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
#     provider_id = Column(Integer, ForeignKey('providers_corner.id'), nullable=False)
#     # Relationships
#     providers_corner = relationship("ProvidersCorner", back_populates="region_providers_corners")
#     region = relationship("Region", back_populates="region_providers_corner")

# class Notification(Base):
#     __tablename__ = "notification"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     message = Column(String, nullable=False)
#     is_read = Column(Boolean, default=False)
#     # Relationships
#     user = relationship("User", back_populates="notifications")

# class Configuration(Base):
#     __tablename__ = "configuration"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     value = Column(String, nullable=False)

# class QueryConfig(Base):
#     __tablename__ = "query_config"
    
#     id = Column(String, primary_key=True, default=text('uuid_generate_v4()'))
#     config = Column(JSON, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     created_by = Column(String, nullable=False)
#     name = Column(String, nullable=False)

# class JwtConfig(Base):
#     __tablename__ = "jwt_config"
    
#     id = Column(String, primary_key=True, default=text('uuid_generate_v4()'))
#     unique_id = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     expires = Column(Boolean, default=False)
#     created_by = Column(Integer, nullable=False)

# class UserTag(Base):
#     __tablename__ = "user_tag"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     name = Column(String, nullable=False)
#     description = Column(String)
#     # Relationships
#     user_tag_relations = relationship("UserTagRelation", back_populates="user_tag")

# class UserTagRelation(Base):
#     __tablename__ = "user_tag_relation"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     user_tag_id = Column(Integer, ForeignKey('user_tag.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="user_tags")
#     user_tag = relationship("UserTag", back_populates="user_tag_relations")

# class Feedback(Base):
#     __tablename__ = "feedback"
    
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, nullable=False)
#     message = Column(String, nullable=False)
#     is_reviewed = Column(Boolean, default=False)
#     comments = Column(String)

# class Announcement(Base):
#     __tablename__ = "announcement"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     display_message = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     link = Column(String, nullable=False)
#     is_public = Column(Boolean, default=False)
#     type = Column(String, nullable=False)
#     start_date = Column(TIMESTAMP(timezone=True), nullable=False)
#     end_date = Column(TIMESTAMP(timezone=True), nullable=False)

# class RolePermission(Base):
#     __tablename__ = "role_permission"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     resource = Column(String, nullable=False)
#     permission = Column(ARRAY(String))
#     role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
#     # Relationships
#     role = relationship("Role", back_populates="role_permissions")

# class Report(Base):
#     __tablename__ = "report"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     slug = Column(String, unique=True, nullable=False)
#     query = Column(String, nullable=False)
#     is_public = Column(Boolean, default=False)
#     is_logged_in = Column(Boolean, default=False)

# class FormMetaHistory(Base):
#     __tablename__ = "form_meta_history"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     form_id = Column(Integer, nullable=False)
#     form_version = Column(Integer, nullable=False)
#     form_meta_json = Column(JSON, nullable=False)

# class FormMetadatum(Base):
#     __tablename__ = "form_metadatum"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))

# class FormAccess(Base):
#     __tablename__ = "form_access"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     form_id = Column(Integer, nullable=False)
#     form_version = Column(Integer, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     permission = Column(ARRAY(String))
#     # Relationships
#     user = relationship("User", back_populates="form_access")

# class UserGroup(Base):
#     __tablename__ = "user_group"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
#     # Relationships
#     user = relationship("User", back_populates="user_groups")
#     group = relationship("Group", back_populates="user_groups")

# class ProvidersCornerTag(Base):
#     __tablename__ = "providers_corner_tag"
    
#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))
#     providers_corner_id = Column(Integer, ForeignKey('providers_corner.id'), nullable=False)
#     tag_id = Column(Integer, ForeignKey('pc_tag.id'), nullable=False)
#     # Relationships
#     providers_corner = relationship("ProvidersCorner", back_populates="provider_corner_tags")
#     tag = relationship("PCTag", back_populates="providers_corner_tags")