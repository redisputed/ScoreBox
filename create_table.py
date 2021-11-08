#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE team (
            team_id SERIAL PRIMARY KEY,
            team_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE player (
            player_id SERIAL PRIMARY KEY,
            player_name VARCHAR(255) NOT NULL,
            birth_date DATE NOT NULL,
            birth_country VARCHAR(255),
            birth_state VARCHAR(255),
            birth_city VARCHAR(255),
            name_first VARCHAR(255),
            name_last VARCHAR(255),
            weight SMALLINT,
            height SMALLINT,
            bats CHAR(1),
            throws CHAR(1),
            debut DATE,
            finalGame DATE
        )
        """,
        """
        CREATE TABLE game (
            game_id SERIAL PRIMARY KEY,
            game_date DATE NOT NULL,
            site CHAR(1) NOT NULL,
            home_id INT NOT NULL REFERENCES team (team_id),
            visitor_id INT NOT NULL REFERENCES team (team_id),
            winner_id INT NOT NULL REFERENCES team (team_id),
            loser_id INT NOT NULL REFERENCES team (team_id)
        )
        """,
        """
        CREATE TABLE boxscore (
            boxscore_id SERIAL PRIMARY KEY,
            player_id INT NOT NULL REFERENCES player (player_id),
            team_id INT NOT NULL REFERENCES team (team_id),
            game_id INT NOT NULL REFERENCES game (game_id),
            batting_order INT NOT NULL,
            at_bats INT NOT NULL,
            runs INT NOT NULL,
            hits INT NOT NULL,
            rbi INT NOT NULL,
            single INT NOT NULL,
            double INT NOT NULL,
            triple INT NOT NULL,
            home_run INT NOT NULL,
            strike_out INT NOT NULL,
            base_on_balls INT NOT NULL,
            sac_fly INT NOT NULL,
            stolen_base INT NOT NULL
        )
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
