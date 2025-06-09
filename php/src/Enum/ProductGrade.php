<?php

declare(strict_types=1);

namespace App\Enum;

enum ProductGrade: string
{
    case APlus = 'A+';
    case A = 'A';
    case B = 'B';
    case C = 'C';
}