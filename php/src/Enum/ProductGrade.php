<?php

declare(strict_types=1);

namespace App\Enum;

enum ProductGrade: string
{
    case APlus = 'A+';
    case AB = 'AB';
    case A = 'A';
    case B = 'B';
    case C = 'C';
    case D = 'D';
    case NONE = 'NONE';
}