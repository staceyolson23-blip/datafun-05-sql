-- 1) If a score is NULL, mark status as 'Missing'
UPDATE scores
SET status = 'Missing'
WHERE score IS NULL;

-- 2) If a score exists but status is NULL, mark as 'Recorded'
UPDATE scores
SET status = 'Recorded'
WHERE score IS NOT NULL
  AND (status IS NULL OR TRIM(status) = '');

-- 3) Floor very low Formative scores after reassessment to 2.0
UPDATE scores
SET score = 2.0
WHERE score IS NOT NULL
  AND score < 2.0
  AND assessment_id LIKE 'FA_%';
