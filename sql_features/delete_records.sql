-- Delete any score rows that truly have no score recorded
-- (after updates, these would have status = 'Missing')
DELETE FROM scores
WHERE score IS NULL;
