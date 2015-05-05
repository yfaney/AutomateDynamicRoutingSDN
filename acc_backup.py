#!/usr/bin/python           # This is py file
#!/usr/bin/python           # This is py file
# Copyright (c) Younghwan Jang, 2014-2015
# You can copy, reuse, modify whatever you want but...
# I want you to specify where it is from.(It is not by force, but a recommendation)

import subprocess, httplib, urllib2, json, time

MAX_BPS = 100 * 1024 * 1024

def get_throughput(switch_no, port_no):
	p = subprocess.Popen(["ifstat", "-b", "-i", "s"+str(switch_no)+"-"+"eth"+str(port_no), "0.1", "1"], stdout=subprocess.PIPE)
	out, err = p.communicate()
	token = out.split()
	ret = [int(float(token[5].strip())), int(float(token[6].strip()))]
	return ret

def list_if_name():
	p = subprocess.Popen(["./getIfList.sh"], stdout=subprocess.PIPE)
	out, err = p.communicate()
	token = out.split()
	list = []
	for i in token:
		if "ovs" in i: continue
		if "-" in i: list.append(i)

	return list

def parse_switch_if(if_name):
	if if_name.startswith("s") and "-" in if_name:
		token = if_name.split("-")
		switch_no = int(token[0][1])
		port_no = int(token[1][3])
		return [switch_no, port_no]
	else: return ["error", "Ohh!"]

def set_cost(src_sw, src_port, dst_sw, dst_port, cost):
	data = {'src' : '00:00:00:00:00:00:00:'+"{:02x}".format(src_sw), 'outPort' : src_port, 'dst' : '00:00:00:00:00:00:00:'+"{:02x}".format(dst_sw), 'inPort' : dst_port, 'cost' : cost}
	headers = {'Content-type':'application/json', 'Accept':'topocosts/json'}
	url = 'http://localhost:8080/wm/ccbalancer/topocosts/json'
	r = requests.post(url, data=json.dumps(data), headers=headers)
	return

def get_cost_json(src_sw, src_port, dst_sw, dst_port, cost):
	data = {'src' : '00:00:00:00:00:00:00:'+"{:02x}".format(src_sw), 'outPort' : src_port, 'dst' : '00:00:00:00:00:00:00:'+"{:02x}".format(dst_sw), 'inPort' : dst_port, 'cost' : cost}
	return json.dumps(data)

def get_links():
	j = urllib2.urlopen('http://localhost:8080/wm/topology/links/json')
	j_obj_list = json.load(j)
	list = []
	for j_obj in j_obj_list:
		src_sw = int(j_obj['src-switch'][-2:],16)
		src_port = int(j_obj['src-port'])
		dst_sw = int(j_obj['dst-switch'][-2:],16)
		dst_port = int(j_obj['dst-port'])
		list.append([src_sw,src_port,dst_sw,dst_port])

	return list

def find_link(links, src_sw, src_port):
	for link in links:
		if link[0] == src_sw and link[1] == src_port:return link

	return [0,0,0,0]

def get_cost(in_band, out_band):
	return int(max(in_band, out_band, 1))

links = get_links()
iflist = list_if_name()

while True:
	costJson = "["
	for link in links:
		#[switch_no, port_no] = parse_switch_if(ifobj)
		[switch_no, port_no] = [link[0], link[1]]
		thp = get_throughput(switch_no, port_no)
		#print "switch"+ str(switch_no) + "/port" + str(port_no) + "(in/out): " + str(thp[0]) + "/" + str(thp[1]) + "cost : " + str(get_cost(thp[0], thp[1]))
		costJson = costJson + get_cost_json(link[0], link[1], link[2], link[3], get_cost(thp[0], thp[1])) + ","

	costJson = costJson[:-1] + "]"
	print costJson
	time.sleep(1)

print parse_switch_if("s5-eth0")
