//   Request-reply client in C++
//   Connects REQ socket to tcp://localhost:5559
//   Sends "Hello" to server, expects "World" back
//
// Olivier Chamoux <olivier.chamoux@fr.thalesgroup.com>

#include "zhelpers.hpp"

int main(int argc, char *argv[])
{
    zmq::context_t context(1);

    zmq::socket_t requester(context, ZMQ_REQ);
    requester.connect("tcp://localhost:5559");

    for (int request = 0; request < 20; request++)
    {

        s_send(requester, "Hello from client 2");
        // s_send (requester, "Berna");
        std::string string = s_recv(requester);

        std::cout << "Received reply " << request
                  << " [" << string << "]" << std::endl;
    }
}
