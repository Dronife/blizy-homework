<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20250610103451 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            ALTER TABLE category ADD brand_id INT NOT NULL
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE category ADD CONSTRAINT FK_64C19C144F5D008 FOREIGN KEY (brand_id) REFERENCES brand (id) NOT DEFERRABLE INITIALLY IMMEDIATE
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX IDX_64C19C144F5D008 ON category (brand_id)
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product DROP CONSTRAINT fk_d34a04ad44f5d008
        SQL);
        $this->addSql(<<<'SQL'
            DROP INDEX idx_d34a04ad44f5d008
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product DROP brand_id
        SQL);
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            CREATE SCHEMA public
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE category DROP CONSTRAINT FK_64C19C144F5D008
        SQL);
        $this->addSql(<<<'SQL'
            DROP INDEX IDX_64C19C144F5D008
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE category DROP brand_id
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product ADD brand_id INT NOT NULL
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE product ADD CONSTRAINT fk_d34a04ad44f5d008 FOREIGN KEY (brand_id) REFERENCES brand (id) NOT DEFERRABLE INITIALLY IMMEDIATE
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX idx_d34a04ad44f5d008 ON product (brand_id)
        SQL);
    }
}
