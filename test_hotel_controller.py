'''
Test suite for hotels
'''

import unittest
from hotel import Hotel
from customer import Customer


class TestHotel (unittest.TestCase):

    '''
    Class for testing hotel methods
    '''

    db = None
    controller = None

    def test_sets_hotel_information(self):
        '''
        test if the create method correctly creates a new hotel
        '''
        hotel_name = 'Marriott'
        hotel_id = 3
        hotel = Hotel()

        hotel.set_id(hotel_id)
        hotel.set_name(hotel_name)

        self.assertEqual(hotel_id, hotel.get_id())
        self.assertEqual(hotel_name, hotel.get_name())

    def test_reserves_room(self):
        '''
        Test if a room is reserve correctly
        '''
        hotel_name = 'Marriott'
        hotel_id = 2
        hotel = Hotel(hotel_id=hotel_id, name=hotel_name)
        customer = Customer(1, 'John Smith')

        reservation = hotel.reserve_room(customer)

        self.assertEqual(hotel_id, reservation.get_hotel())
        self.assertEqual(1, reservation.get_customer())

    def test_reserves_room(self):
        '''
        Test if a room is reserve correctly
        '''
        hotel_name = 'Marriott'
        hotel_id = 2  # Cambia el ID esperado a un valor incorrecto
        hotel = Hotel(hotel_id=hotel_id, name=hotel_name)
        customer = Customer(1, 'John Smith')

        reservation = hotel.reserve_room(customer)

        # Ahora esperamos un error porque el ID del hotel no es el esperado
        self.assertNotEqual(hotel_id, reservation.get_hotel())


if __name__ == '__main__':
    unittest.main()
