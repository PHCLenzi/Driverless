Este repositório é um controle do catvehicle via ros.

Para rodar a simulação vede-se

1- instalar ros melodic versão desktop
2- instalar catvehicle para melodic seguindo esse pdf:https://rahulbhadani.github.io/teaching/4%20-%20RunningCATVehicleSim.pdf
3- instalar o pacote criado por mim geppeto_pkg deste guithub
 3.1 - criar um pacote na area de trabalho (exp area de trabalho = catvehicle_ws. com catkin_create_pkg [nome pacote(exp: geppetto_pkg)] [dependencias]).
 3.2 - dentro do pacote adicionar a pasta "scripts"(boas práticas) e dentro de scripts colocar o nó deste repositório geppetto_node.py
 3.3 - depois de adicionar o geppeto_node.py, pelo prompt na pasta scripts criada dar o comando: {$ chmod +x geppetto_node.py }fonte = https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
 3.4 va até a pasta CMakeList.txt do pacote criado e adicione as seguintes linhas:{ catkin_install_python(PROGRAMS scripts/talker.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} }
 3.5 Pelo prompt, va até a pasta da area de trabalho catkin(exp catkin_ws) e de o comando: {$ catkin_make}
4- Rode a simulação.
  Terminal 1 
  $ cd catvehicle_ws
  $ source devel/setup.bash
  $ roslaunch catvehicle catvehicle_empty.launch

  Terminal 2 
  $ cd catvehicle_ws
  $ source devel/setup.bash
  $ gzclient

  Terminal 3 
  $ cd catvehicle_ws
  $ source devel/setup.bash
  $ roslaunch catvehicle_ws catvehicle_spawn_ampera.launch robot:=catvehicle X:=0 Y:=0 \ yaw:=0.0

  Terminal 4
  $ cd catvehicle_ws
  $ source devel/setup.bash
  $ rosrun geppetto_pkg geppetto_node.py


Como rodar a simulação

Como o geppeto_node.py funciona?
Este nó escreve uma mensagem geometry_msgs/Twist no tópico /catvehicle/cmd_vel. Esta mensagem tem 6 argumentos:linear.x ,linear.y ,linear.z , angula.x ,angula.y ,angula.z. Destes argumentos o que controla a velocidade do carro é o linear.x e o que controla a direção é o angular.z.
