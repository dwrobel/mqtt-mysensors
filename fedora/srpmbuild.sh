#!/bin/bash
spectool -g mqtt-mysensors.spec
rpmbuild -bs --define "_sourcedir `pwd`" --define "_srcrpmdir ." --define "_specdir `pwd`" mqtt-mysensors.spec
