#ifndef SHAREDBUFFERTEST_H
#define SHAREDBUFFERTEST_H

#include <cppunit/extensions/HelperMacros.h>

class SharedBufferTest : public CppUnit::TestFixture
{
    CPPUNIT_TEST_SUITE(SharedBufferTest);
    CPPUNIT_TEST(testDefaultConstructor);
    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testEquals);
    CPPUNIT_TEST(testIteration);
    CPPUNIT_TEST(testCopy);
    CPPUNIT_TEST(testSwap);
    CPPUNIT_TEST(testSharing);
    CPPUNIT_TEST(testSlicing);
    CPPUNIT_TEST(testTrim);
    CPPUNIT_TEST(testTrimShared);
    CPPUNIT_TEST(testRecast);
    CPPUNIT_TEST(testAllocator);
    CPPUNIT_TEST(testAllocatorCopy);
    CPPUNIT_TEST(testCustomDeleter);
    CPPUNIT_TEST(testTransient);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp();
    void tearDown();

    // Constructors
    void testDefaultConstructor();
    void testConstructor();

    // Basic container behavior
    void testEquals();
    void testIteration();
    void testCopy();
    void testSwap();

    // Extended container behavior
    void testSharing();
    void testSlicing();
    void testTrim();
    void testTrimShared();
    void testRecast();

    // Advanced features
    void testAllocator();
    void testAllocatorCopy();
    void testCustomDeleter();
    void testTransient();

private:
    template <class Buffer>
    void testTrimImpl();
};

#endif // SHARED_BUFFER_TEST_H