# -*- coding: utf-8 -*-

class SbbdQueries:
    
    @staticmethod
    def getPapers(first_year=None, last_year=None):
        query = "select * from papers_paper " + \
            "join papers_tecsession on papers_paper.session_id = papers_tecsession.id " + \
            "join papers_conference on papers_tecsession.conference_id = papers_conference.id";
        if first_year is not None and last_year is not None:
            query += " where papers_conference.year between %s and %s" % (first_year, last_year);
        return query

    @staticmethod
    def getAuthors(paper_id):
        return "select coauthor_id from papers_paper_authors where paper_id = %s" % paper_id;
    
    @staticmethod
    def getAuthorsIn(author_id_list):
        return "select * from papers_author where id in %s" % author_id_list;
    
    @staticmethod
    def getAuthorsNotIn(author_id_list):
        return "select * from papers_author where id not in %s" % author_id_list;