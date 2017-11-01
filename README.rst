docker-gflops-alpine
===============================================================================

numpy matrix multiplication for measuring FLOPS on alpine

Build
-------------------------------------------------------------------------------

::

        docker build -f Dockerfile -t lee212/gflops .

For IBM OpenWhisk

::

        docker build -f Dockerfile.openwhisk -t lee212/gflops:openwhisk .

Run
-------------------------------------------------------------------------------


::

        docker run -it lee212/gflops <number_of_loop> <number_of_matrix>

For IBM OpenWhisk

::

        docker run -d -p 8080:8080 lee212/gflops:openwhisk

Test
-------------------------------------------------------------------------------

::

        docker run -it lee212/gflops 10 1024


For IBM OpenWhisk

::

        curl -d '{ "number_of_matrix": 1024, "number_of_loop":10 }' 'https://openwhisk.ng.bluemix.net/api/v1/namespaces/xxx/actions/gflopsopenwhisk?blocking=true' -XPOST -H 'Content-Type: application/json'

.. note::
        For asyncronous, use 'blocking=false'
