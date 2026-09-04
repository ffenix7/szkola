-- Tabela: typy_posilkow
CREATE TABLE typy_posilkow (
    id_typu INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(50) UNIQUE
);

-- Tabela: typy_alergii
CREATE TABLE typy_alergii (
    id_alergii INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100) UNIQUE
);

-- Tabela: uczniowie
CREATE TABLE uczniowie (
    id_ucznia INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    klasa VARCHAR(10),
    id_alergii INT NULL,
    FOREIGN KEY (id_alergii) REFERENCES typy_alergii(id_alergii)
);

-- Tabela: posilki
CREATE TABLE posilki (
    id_posilku INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100),
    id_typu INT,
    wegetarianski BOOLEAN,
    kalorie INT,
    FOREIGN KEY (id_typu) REFERENCES typy_posilkow(id_typu)
);

-- Tabela: zamowienia
CREATE TABLE zamowienia (
    id_zamowienia INT AUTO_INCREMENT PRIMARY KEY,
    id_ucznia INT,
    id_posilku INT,
    data DATE,
    FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia),
    FOREIGN KEY (id_posilku) REFERENCES posilki(id_posilku)
);


-- Typy posiłków
INSERT INTO typy_posilkow (id_typu, nazwa) VALUES (1, 'śniadanie');
INSERT INTO typy_posilkow (id_typu, nazwa) VALUES (2, 'obiad');
INSERT INTO typy_posilkow (id_typu, nazwa) VALUES (3, 'podwieczorek');

-- Typy alergii
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (1, 'orzechy');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (2, 'laktoza');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (3, 'gluten');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (4, 'jajka');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (5, 'soja');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (6, 'ryby');
INSERT INTO typy_alergii (id_alergii, nazwa) VALUES (7, 'seler');

-- Uczniowie
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (1, 'Oliwier', 'Kramer', '1B', 6);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (2, 'Kacper', 'Salawa', '3A', 4);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (3, 'Juliusz', 'Magier', '3C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (4, 'Arkadiusz', 'Drewicz', '2B', 4);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (5, 'Rafał', 'Masny', '2B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (6, 'Aleksander', 'Madura', '2B', 2);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (7, 'Franciszek', 'Chromy', '3C', 5);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (8, 'Mariusz', 'Tomaszuk', '1B', 2);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (9, 'Janina', 'Matulka', '2B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (10, 'Malwina', 'Broszkiewicz', '2A', 4);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (11, 'Mateusz', 'Mały', '1B', 7);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (12, 'Julita', 'Kurant', '1B', 4);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (13, 'Cyprian', 'Matla', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (14, 'Apolonia', 'Roszkiewicz', '3A', 1);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (15, 'Roksana', 'Gryta', '1C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (16, 'Anna Maria', 'Łapacz', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (17, 'Ada', 'Wojtunik', '1C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (18, 'Jędrzej', 'Kunc', '2B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (19, 'Leon', 'Matela', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (20, 'Jędrzej', 'Pupek', '3A', 5);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (21, 'Eryk', 'Boba', '3C', 7);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (22, 'Robert', 'Słupik', '1B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (23, 'Mikołaj', 'Jantos', '3A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (24, 'Dawid', 'Andziak', '3C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (25, 'Alan', 'Herda', '2B', 2);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (26, 'Grzegorz', 'Flisek', '1A', 7);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (27, 'Szymon', 'Wielgos', '1C', 6);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (28, 'Jan', 'Wojtczuk', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (29, 'Sonia', 'Maron', '3B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (30, 'Hubert', 'Olszyna', '3A', 5);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (31, 'Monika', 'Fiedorczuk', '1A', 7);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (32, 'Dawid', 'Pieczarka', '2B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (33, 'Jędrzej', 'Czura', '1C', 2);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (34, 'Karina', 'Łuszczyk', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (35, 'Dawid', 'Glonek', '3B', 2);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (36, 'Róża', 'Wichłacz', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (37, 'Julita', 'Kalota', '2A', 3);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (38, 'Olaf', 'Nowrot', '2C', 5);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (39, 'Marcin', 'Katana', '2C', 7);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (40, 'Tymoteusz', 'Kloska', '1C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (41, 'Aleks', 'Pajda', '3B', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (42, 'Ksawery', 'Hadam', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (43, 'Róża', 'Tabisz', '1B', 6);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (44, 'Gabriel', 'Plaskota', '3A', 1);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (45, 'Sandra', 'Sadowy', '2B', 1);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (46, 'Jędrzej', 'Dydo', '2A', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (47, 'Olgierd', 'Jarosik', '1C', NULL);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (48, 'Daniel', 'Szwałek', '2B', 4);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (49, 'Marcel', 'Zbroszczyk', '3B', 1);
INSERT INTO uczniowie (id_ucznia, imie, nazwisko, klasa, id_alergii) VALUES (50, 'Natasza', 'Maraszek', '1B', NULL);

-- Posiłki
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (1, 'Kanapka z serem karta', 1, TRUE, 381);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (2, 'Kanapka z serem dyrektor', 1, TRUE, 321);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (3, 'Kanapka z serem we', 1, TRUE, 366);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (4, 'Kanapka z serem moneta', 1, TRUE, 374);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (5, 'Kanapka z serem smutek', 1, TRUE, 382);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (6, 'Owsianka z owocami jakość', 1, TRUE, 313);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (7, 'Owsianka z owocami zbiór', 1, TRUE, 280);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (8, 'Owsianka z owocami zachowywać się', 1, TRUE, 286);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (9, 'Owsianka z owocami kara', 1, TRUE, 309);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (10, 'Owsianka z owocami dostać', 1, TRUE, 302);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (11, 'Jajecznica z chlebem czytać', 1, FALSE, 403);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (12, 'Jajecznica z chlebem podawać', 1, FALSE, 351);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (13, 'Jajecznica z chlebem który', 1, FALSE, 413);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (14, 'Jajecznica z chlebem żywy', 1, FALSE, 402);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (15, 'Jajecznica z chlebem niski', 1, FALSE, 413);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (16, 'Zupa pomidorowa składnik', 2, TRUE, 270);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (17, 'Zupa pomidorowa 10', 2, TRUE, 216);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (18, 'Zupa pomidorowa dialekt', 2, TRUE, 218);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (19, 'Zupa pomidorowa forma', 2, TRUE, 276);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (20, 'Zupa pomidorowa dziś', 2, TRUE, 229);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (21, 'Kotlet schabowy z ziemniakami napój', 2, FALSE, 568);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (22, 'Kotlet schabowy z ziemniakami zajmować', 2, FALSE, 567);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (23, 'Kotlet schabowy z ziemniakami lekarstwo', 2, FALSE, 557);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (24, 'Kotlet schabowy z ziemniakami znowu', 2, FALSE, 623);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (25, 'Kotlet schabowy z ziemniakami wiadomość', 2, FALSE, 596);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (26, 'Spaghetti wegetariańskie wysoki', 2, TRUE, 470);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (27, 'Spaghetti wegetariańskie rolnik', 2, TRUE, 535);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (28, 'Spaghetti wegetariańskie różowy', 2, TRUE, 499);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (29, 'Spaghetti wegetariańskie chociaż', 2, TRUE, 484);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (30, 'Spaghetti wegetariańskie wiele', 2, TRUE, 483);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (31, 'Jogurt naturalny badać', 3, TRUE, 170);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (32, 'Jogurt naturalny obcy', 3, TRUE, 165);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (33, 'Jogurt naturalny kolega', 3, TRUE, 134);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (34, 'Jogurt naturalny narkotyk', 3, TRUE, 224);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (35, 'Jogurt naturalny oś', 3, TRUE, 187);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (36, 'Owocowa sałatka zaufanie', 3, TRUE, 155);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (37, 'Owocowa sałatka rolnik', 3, TRUE, 100);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (38, 'Owocowa sałatka wrażenie', 3, TRUE, 124);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (39, 'Owocowa sałatka chłopiec', 3, TRUE, 107);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (40, 'Owocowa sałatka pojedynczy', 3, TRUE, 150);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (41, 'Pudding czekoladowy Grecja', 3, TRUE, 222);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (42, 'Pudding czekoladowy okazja', 3, TRUE, 183);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (43, 'Pudding czekoladowy znać', 3, TRUE, 169);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (44, 'Pudding czekoladowy 80', 3, TRUE, 187);
INSERT INTO posilki (id_posilku, nazwa, id_typu, wegetarianski, kalorie) VALUES (45, 'Pudding czekoladowy w czasie', 3, TRUE, 174);

-- Zamówienia
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (1, 15, 32, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (2, 50, 11, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (3, 34, 29, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (4, 39, 34, '2025-06-03');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (5, 4, 44, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (6, 32, 33, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (7, 6, 25, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (8, 12, 34, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (9, 8, 1, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (10, 48, 35, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (11, 17, 3, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (12, 49, 8, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (13, 24, 37, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (14, 18, 8, '2025-06-06');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (15, 11, 13, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (16, 32, 14, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (17, 8, 40, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (18, 50, 40, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (19, 33, 24, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (20, 36, 4, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (21, 25, 44, '2025-06-06');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (22, 40, 45, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (23, 9, 34, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (24, 11, 45, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (25, 39, 29, '2025-06-03');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (26, 38, 25, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (27, 35, 37, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (28, 10, 40, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (29, 19, 18, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (30, 1, 44, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (31, 45, 8, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (32, 37, 27, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (33, 22, 31, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (34, 1, 24, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (35, 6, 17, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (36, 25, 26, '2025-06-03');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (37, 22, 23, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (38, 29, 4, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (39, 22, 33, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (40, 33, 33, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (41, 28, 20, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (42, 24, 1, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (43, 33, 24, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (44, 28, 36, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (45, 28, 3, '2025-06-06');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (46, 43, 11, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (47, 49, 28, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (48, 45, 12, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (49, 25, 22, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (50, 30, 7, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (51, 45, 43, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (52, 28, 9, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (53, 2, 42, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (54, 28, 13, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (55, 44, 20, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (56, 25, 3, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (57, 1, 39, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (58, 49, 11, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (59, 5, 9, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (60, 12, 25, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (61, 8, 27, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (62, 49, 18, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (63, 38, 39, '2025-06-06');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (64, 26, 21, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (65, 50, 21, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (66, 31, 31, '2025-06-03');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (67, 30, 9, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (68, 18, 18, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (69, 9, 41, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (70, 35, 18, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (71, 33, 7, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (72, 35, 3, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (73, 28, 42, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (74, 45, 20, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (75, 1, 31, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (76, 25, 43, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (77, 40, 3, '2025-06-02');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (78, 28, 20, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (79, 12, 43, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (80, 36, 28, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (81, 32, 4, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (82, 31, 19, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (83, 22, 36, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (84, 28, 5, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (85, 12, 44, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (86, 45, 29, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (87, 32, 4, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (88, 13, 21, '2025-06-04');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (89, 50, 39, '2025-06-07');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (90, 42, 26, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (91, 11, 39, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (92, 28, 6, '2025-06-03');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (93, 13, 16, '2025-06-05');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (94, 34, 24, '2025-06-10');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (95, 35, 43, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (96, 26, 34, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (97, 23, 8, '2025-06-08');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (98, 15, 33, '2025-06-01');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (99, 45, 33, '2025-06-09');
INSERT INTO zamowienia (id_zamowienia, id_ucznia, id_posilku, data) VALUES (100, 49, 9, '2025-06-06');
