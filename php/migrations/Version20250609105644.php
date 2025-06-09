<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20250609105644 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            CREATE SEQUENCE brand_id_seq INCREMENT BY 1 MINVALUE 1 START 1
        SQL);
        $this->addSql(<<<'SQL'
            CREATE SEQUENCE category_id_seq INCREMENT BY 1 MINVALUE 1 START 1
        SQL);
        $this->addSql(<<<'SQL'
            CREATE SEQUENCE model_id_seq INCREMENT BY 1 MINVALUE 1 START 1
        SQL);
        $this->addSql(<<<'SQL'
            CREATE SEQUENCE product_id_seq INCREMENT BY 1 MINVALUE 1 START 1
        SQL);
        $this->addSql(<<<'SQL'
            CREATE TABLE brand (id INT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY(id))
        SQL);
        $this->addSql(<<<'SQL'
            CREATE UNIQUE INDEX UNIQ_1C52F9585E237E06 ON brand (name)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE TABLE category (id INT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY(id))
        SQL);
        $this->addSql(<<<'SQL'
            CREATE UNIQUE INDEX UNIQ_64C19C15E237E06 ON category (name)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE TABLE model (id INT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY(id))
        SQL);
        $this->addSql(<<<'SQL'
            CREATE UNIQUE INDEX UNIQ_D79572D95E237E06 ON model (name)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE TABLE product (id INT NOT NULL, category_id INT NOT NULL, brand_id INT NOT NULL, model_id INT NOT NULL, grade VARCHAR(255) NOT NULL, storage INT NOT NULL, condition VARCHAR(255) NOT NULL, price INT NOT NULL, PRIMARY KEY(id))
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX IDX_D34A04AD12469DE2 ON product (category_id)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX IDX_D34A04AD44F5D008 ON product (brand_id)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX IDX_D34A04AD7975B7E7 ON product (model_id)
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product ADD CONSTRAINT FK_D34A04AD12469DE2 FOREIGN KEY (category_id) REFERENCES category (id) NOT DEFERRABLE INITIALLY IMMEDIATE
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product ADD CONSTRAINT FK_D34A04AD44F5D008 FOREIGN KEY (brand_id) REFERENCES brand (id) NOT DEFERRABLE INITIALLY IMMEDIATE
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product ADD CONSTRAINT FK_D34A04AD7975B7E7 FOREIGN KEY (model_id) REFERENCES model (id) NOT DEFERRABLE INITIALLY IMMEDIATE
        SQL);
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            DROP SEQUENCE brand_id_seq CASCADE
        SQL);
        $this->addSql(<<<'SQL'
            DROP SEQUENCE category_id_seq CASCADE
        SQL);
        $this->addSql(<<<'SQL'
            DROP SEQUENCE model_id_seq CASCADE
        SQL);
        $this->addSql(<<<'SQL'
            DROP SEQUENCE product_id_seq CASCADE
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product DROP CONSTRAINT FK_D34A04AD12469DE2
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product DROP CONSTRAINT FK_D34A04AD44F5D008
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product DROP CONSTRAINT FK_D34A04AD7975B7E7
        SQL);
        $this->addSql(<<<'SQL'
            DROP TABLE brand
        SQL);
        $this->addSql(<<<'SQL'
            DROP TABLE category
        SQL);
        $this->addSql(<<<'SQL'
            DROP TABLE model
        SQL);
        $this->addSql(<<<'SQL'
            DROP TABLE product
        SQL);
    }
}
