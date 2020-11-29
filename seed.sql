BEGIN;
INSERT INTO users (id, email, name) VALUES
    ('52d0ae4e-0cda-4a4f-baba-87ee880e0ddb', 'user1@example.com', 'John Doe'),
    ('6ff84d4f-fc61-4af4-8c13-707a531b31a7', 'user2@example.com', 'John Doe 2'),
    ('861503db-a55a-40a7-bb30-bade45e3515a', 'user3@example.com', 'John Doe 3'),
    ('7572c35c-a49f-4ca7-a5e4-2faad8b72861', 'user4@example.com', 'John Doe 4'),
    ('9ad7cddc-560c-4ade-8a3b-4ae8f824aba9', 'user5@example.com', 'John Doe 5'),
    ('81f05c1e-6c7f-4f5f-af8b-096fbcb794e1', 'user6@example.com', 'John Doe 6')
;

INSERT INTO presence (user_id, event_id, presence) VALUES
    ('52d0ae4e-0cda-4a4f-baba-87ee880e0ddb', '4oatu5678cld8gfh0euluj3ip3@google.com', 'present'),
    ('6ff84d4f-fc61-4af4-8c13-707a531b31a7', '4oatu5678cld8gfh0euluj3ip3@google.com', 'present'),
    ('861503db-a55a-40a7-bb30-bade45e3515a', '4oatu5678cld8gfh0euluj3ip3@google.com', 'present'),
    ('52d0ae4e-0cda-4a4f-baba-87ee880e0ddb', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'present'),
    ('6ff84d4f-fc61-4af4-8c13-707a531b31a7', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'unknown'),
    ('861503db-a55a-40a7-bb30-bade45e3515a', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'absent'),
    ('7572c35c-a49f-4ca7-a5e4-2faad8b72861', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'absent'),
    ('9ad7cddc-560c-4ade-8a3b-4ae8f824aba9', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'present'),
    ('81f05c1e-6c7f-4f5f-af8b-096fbcb794e1', '5e1ouudn8cc3sr1atbqqi3dvon@google.com', 'absent')
;
COMMIT;
