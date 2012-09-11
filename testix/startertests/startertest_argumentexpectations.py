from testix import scenario
from testix import exception
from testix import expectations
from testix import argumentexpectations
from testix import fakeobject
from testix.startertests import startertestcollection
from testix.startertests.asserts import *

class StarterTestArgumentExpectations( startertestcollection.StarterTestCollection ):
	def starter_test_ArgumentEquals( self ):
		fakeObject = fakeobject.FakeObject( 'some object' )
		aScenario = scenario.Scenario() <<\
			expectations.Call( 'some object', [ 10 ], 'first' ) <<\
			expectations.Call( 'some object', [ 11 ], 'second' )
		STS_ASSERT_EQUALS( fakeObject( 10 ), 'first' )
		STS_ASSERT_THROWS_SPECIFIC_EXCEPTION( exception.ExpectationException, fakeObject, 10 )
		aScenario.end()

	def starter_test_ArgumentIsAFakeObjectWithPath( self ):
		fakeObject = fakeobject.FakeObject( 'some object' )
		anotherFakeObject = fakeobject.FakeObject( 'another fake object' )
		aScenario = scenario.Scenario() <<\
			expectations.Call( 	'some object', [ argumentexpectations.ArgumentIsAFakeObjectWithPath( 'another fake object' ) ], 
								'the result' ) <<\
			expectations.Call( 	'some object', [ argumentexpectations.ArgumentIsAFakeObjectWithPath( 'yet another' ) ], 
								'another result' )

		STS_ASSERT_EQUALS( fakeObject( anotherFakeObject ), 'the result' )
		STS_ASSERT_EQUALS( fakeObject( fakeobject.FakeObject( 'yet another' ) ), 'another result' )
		aScenario.end()

	def starter_test_IgnoreArgument( self ):
		fakeObject = fakeobject.FakeObject( 'some object' )
		aScenario = scenario.Scenario() <<\
			expectations.Call( 'some object', [ 10 ], 'first' ) <<\
			expectations.Call( 'some object', [ argumentexpectations.IgnoreArgument() ], 'second' )
		STS_ASSERT_EQUALS( fakeObject( 10 ), 'first' )
		STS_ASSERT_EQUALS( fakeObject( "this doens't matter" ), 'second' )
		aScenario.end()

	def starter_test_KeywordArguments( self ):
		fakeObject = fakeobject.FakeObject( 'some object' )
		aScenario = scenario.Scenario() <<\
			expectations.Call( 'some object', [ 10 ], 'first', kwargExpectations = { 'name': 'Lancelot' } ) <<\
			expectations.Call( 'some object', [ 11 ], 'second', kwargExpectations = { 'name': 'Galahad' } )
		STS_ASSERT_EQUALS( fakeObject( 10, name = 'Lancelot' ), 'first' )
		STS_ASSERT_THROWS_SPECIFIC_EXCEPTION( exception.ExpectationException, fakeObject, 11, name = 'not Galahad'  )
		aScenario.end()

	def starter_test_KeywordArgumentsExpected_NoneGiven( self ):
		fakeObject = fakeobject.FakeObject( 'some object' )
		aScenario = scenario.Scenario() <<\
			expectations.Call( 'some object', [ 11 ], 'result', kwargExpectations = { 'name': 'Galahad' } )
		STS_ASSERT_THROWS_SPECIFIC_EXCEPTION( exception.ExpectationException, fakeObject, 11 )
		aScenario.end()

	def starter_test_KeywordArgumentsForThrowingCall( self ):
		class MyException( Exception ): pass

		fakeObject = fakeobject.FakeObject( 'some object' )
		aScenario = scenario.Scenario() <<\
			expectations.ThrowingCall( 'some object', [ 'no kwargs will violate expectation' ], MyException, kwargExpectations = { 'name': 'Galahad' } )
		STS_ASSERT_THROWS_SPECIFIC_EXCEPTION( exception.ExpectationException, fakeObject, 'no kwargs will violate expectation' )
		aScenario.end()

		aScenario = scenario.Scenario() <<\
			expectations.ThrowingCall( 'some object', [ 11 ], MyException, kwargExpectations = { 'name': 'Galahad' } )
		STS_ASSERT_THROWS_SPECIFIC_EXCEPTION( MyException, fakeObject, 11, name = 'Galahad' )
		aScenario.end()

StarterTestArgumentExpectations()
