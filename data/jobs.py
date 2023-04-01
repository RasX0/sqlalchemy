import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))

    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    user = orm.relationship('User')

    def __repr__(self):
        return "%s %s %s" % (
            self.team_leader, self.job, self.work_size)
    # title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)
    # is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    #
    # user_id = sqlalchemy.Column(sqlalchemy.Integer,
    #                             sqlalchemy.ForeignKey("users.id"))
    # user = orm.relationship('User')
