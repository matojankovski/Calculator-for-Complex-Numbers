# Calculator-for-Complex-Numbers
Complex Number Calculator without complex library

ComplexLogic.py - contains operations of Complex Calculator. 
RLC module is not finished and needs to improve code logic. Basic complex calculator logic is functional.

ComplexNumber.py - contain class ComplexNumber that ComplexLogic.py is using. Parsing and basic operations are included there. Currently contains also RLC module
that is still bit clumsy. Idea is to create new class RLC that will deal only with impedance calculation - issue with polar form of C and L elements. By definition they
have +-90 degree phasor.

test_ComplexLogic.py - contains test cases for ComplexLogic and ComplexNumber. 
