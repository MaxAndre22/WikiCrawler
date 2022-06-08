export function getAverageDifferentWordsPerPage() {
    const sqlQuery = `SELECT AVG(words_body)
                      FROM article_stats;`
}

export function getAverageDifferentWordsPerSubTitle() {
    const sqlQuery = `SELECT AVG(words_subtitles)
                      FROM article_stats;`
}

export function getAverageDifferentWordsPerTitle() {
    const sqlQuery = `SELECT AVG(words_titles)
                      FROM article_stats;`
}

export function getAverageImagesWithAlt() {
    const sqlQuery = `SELECT AVG(images_w_alt)
                      FROM article_stats;`
}

SELECT account_no, 
        COUNT(*) transaction_count
   FROM transactions
  GROUP BY account_no
  ORDER BY COUNT(*) DESC
  LIMIT 1000

export function getAverageReferencesUsage() {
    const sqlQuery = `SELECT AVG(count)
                      FROM reference;`
}

export function getAverageReferencesWithActiveLinks() {
    const sqlQuery = `SELECT COUNT
                      FROM reference
                      WHERE has_link=true;`
}

export function getAverageReferencesWithLinks() {

}

export function getMostCommonWords() {

}
