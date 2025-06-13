<?php

namespace App\Entity;

use App\Enum\ProductCondition;
use App\Enum\ProductGrade;
use App\Repository\ProductRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: ProductRepository::class)]
class Product
{
    #[ORM\Id]
    #[ORM\GeneratedValue(strategy: 'IDENTITY')]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\ManyToOne]
    #[ORM\JoinColumn(nullable: false)]
    private ?Category $category = null;

    #[ORM\Column(enumType: ProductGrade::class)]
    private ?ProductGrade $grade = null;

    #[ORM\Column(nullable: false)]
    private ?int $storage = null;

    #[ORM\Column(nullable: false, enumType: ProductCondition::class)]
    private ?ProductCondition $condition = null;

    #[ORM\Column(nullable: false)]
    private ?float $price = null;

    #[ORM\ManyToOne]
    #[ORM\JoinColumn(nullable: false)]
    private ?Model $model = null;

    #[ORM\Column(nullable: true)]
    private ?string $color = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getCategory(): ?Category
    {
        return $this->category;
    }

    public function setCategory(?Category $category): static
    {
        $this->category = $category;

        return $this;
    }

    public function getGrade(): ?ProductGrade
    {
        return $this->grade;
    }

    public function setGrade(ProductGrade $grade): static
    {
        $this->grade = $grade;

        return $this;
    }

    public function getStorage(): ?int
    {
        return $this->storage;
    }

    public function setStorage(int $storage): static
    {
        $this->storage = $storage;

        return $this;
    }

    public function getCondition(): ?ProductCondition
    {
        return $this->condition;
    }

    public function setCondition(ProductCondition $condition): static
    {
        $this->condition = $condition;

        return $this;
    }

    public function getPrice(): ?float
    {
        return $this->price;
    }

    public function setPrice(float $price): static
    {
        $this->price = $price;

        return $this;
    }

    public function getModel(): ?Model
    {
        return $this->model;
    }

    public function setModel(?Model $model): static
    {
        $this->model = $model;

        return $this;
    }

    public function getColor(): ?string
    {
        return $this->color;
    }

    public function setColor(?string $color): self
    {
        $this->color = $color;

        return $this;
    }
}
