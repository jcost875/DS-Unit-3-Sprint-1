"""Basic Unit Tests for Lambdata package"""

from random import randint
import pytest
import lambdata as ld
from lambdata.oop_examples import SocialMediaUser, Animal


# Testing __init__ in lambdata


def test_increment_int():
    """Making sure increment works for integers"""
    x0 = 0
    y0 = ld.increment(x0)
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1)
    assert y1 == 101


def test_increment_float():
    """Making sure increment works for floats"""    
    x0 = 10.5
    y0 = ld.increment(x0)
    assert y0 == 11.5


def test_increment_neg_int():
    """Making sure increment works for negative integers"""
    x0 = -1
    y0 = ld.increment(x0)
    assert y0 == 0


def test_increment_neg_float():
    """Making sure increment works for negative floats"""
    x0 = -1.5
    y0 = ld.increment(x0)
    assert y0 == -0.5


def test_colors():
    """Testing that COLORS contains correct items"""
    assert 'Cyan' in ld.COLORS
    assert 'Mauve' in ld.COLORS
    assert 'Blue' in ld.COLORS
    assert 'Brown' not in ld.COLORS
    assert 'Yellow' not in ld.COLORS


def test_number_colors():
    """Testing the number of elements in colors"""
    assert len(ld.COLORS) == 4


# Testing OOP_examples
user1 = ld.oop_examples.SocialMediaUser(name='Nick', location='Arizona')
user2 = ld.oop_examples.SocialMediaUser(
    name='Carl', location='Costa Rica', upvotes=250)

animal1 = ld.oop_examples.Animal(name='Parrot', weight=2)
animal2 = ld.oop_examples.Animal(name='Wolf', weight=150)

def test_SMU_constructor():
    """Testing that SMU constructor works properly"""
    # Testing name
    assert user1.name.lower() == 'nick'
    assert user2.name.lower() == 'carl'
    # Testing location
    assert user1.location.lower() == 'arizona'
    assert user2.location.lower() == 'costa rica'
    # Testing upvotes
    assert user1.upvotes == 0    # Checks default
    assert user2.upvotes == 250  # Checks assignment


def test_unpopular():
    """Testing to make sure 0 upvotes is unpopular"""
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()


def test_popular():
    """Testing to make sure 250 upvotes is popular"""
    assert isinstance(user2.is_popular(), bool)
    assert user2.is_popular()


def test_SMU_constructor_types():
    """Testing types"""
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)

def test_Animal_constructor():
    """Testing that Animal constructor and types work properly"""
    # Testing constructor
    assert animal1.name.upper() == 'PARROT'
    assert animal2.name.upper() == 'WOLF'
    # Testing types
    assert isinstance(animal1.name, str)
    assert isinstance(animal1.weight, int)
    assert isinstance(animal2.name, str)
    assert isinstance(animal2.weight, int)