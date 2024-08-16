-- Use the lms database
USE lms;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS borrowed_books;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS authors;

-- Create the authors table
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key for authors
    name VARCHAR(255) NOT NULL,
    birth_year INT,  -- Field for the author's birth year
    biography TEXT
);

-- Create the books table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,  -- Foreign key referring to authors table
    isbn VARCHAR(20) NOT NULL UNIQUE,  -- ISBN should be unique
    publication_date DATE,
    availability BOOLEAN DEFAULT TRUE,  -- Using TRUE instead of 1 for boolean
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE  -- Unique library ID for each user
);

-- Create the borrowed_books table
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Insert sample data into authors
INSERT INTO authors (name, birth_year, biography) VALUES
('J.K. Rowling', 1965, 'British author, best known for the Harry Potter series.'),
('George Orwell', 1903, 'English novelist and essayist, known for Animal Farm and 1984.');

-- Insert sample data into books
INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES
('Harry Potter and the Philosopher\'s Stone', 1, '9780747532743', '1997-06-26', TRUE),
('1984', 2, '9780451524935', '1949-06-08', TRUE);

-- Insert sample data into users
INSERT INTO users (name, library_id) VALUES
('Alice Smith', 'LIB001'),
('Bob Jones', 'LIB002');

-- Insert sample data into borrowed_books
INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES
(1, 1, '2024-08-15'),
(2, 2, '2024-08-15');

-- Update authors table
UPDATE authors
SET name = 'Updated Author Name', 
    biography = 'Updated biography here', 
    birth_year = 1980
WHERE author_id = 1;

-- Describe authors table to see the updated schema
DESCRIBE authors;
