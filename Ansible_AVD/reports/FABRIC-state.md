# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |
| ----------- | ------------------ | ------------------ | ------------------- |
| 361 | 305 | 24 | 32 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| leaf1 | 62 | 58 | 0 | 4 | - | Hardware |
| leaf2 | 62 | 58 | 0 | 4 | - | Hardware |
| leaf3 | 62 | 51 | 7 | 4 | BGP, Connectivity, Interfaces, Routing | Hardware |
| leaf4 | 63 | 52 | 7 | 4 | BGP, Connectivity, Interfaces, Routing | Hardware |
| spine1 | 28 | 24 | 0 | 4 | - | Hardware |
| spine2 | 28 | 24 | 0 | 4 | - | Hardware |
| spine3 | 28 | 24 | 0 | 4 | - | Hardware |
| spine4 | 28 | 14 | 10 | 4 | BGP, Connectivity, Interfaces | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 68 | 60 | 8 | 0 |
| Connectivity | 104 | 94 | 10 | 0 |
| Hardware | 32 | 0 | 0 | 32 |
| Interfaces | 89 | 85 | 4 | 0 |
| MLAG | 4 | 4 | 0 | 0 |
| Routing | 48 | 46 | 2 | 0 |
| System | 16 | 16 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 128 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | FAIL | AFI: evpn Peer: 192.168.101.14 - Incorrect session state - Expected: Established Actual: Active |
| 133 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.22) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.22 - Incorrect session state - Expected: Established Actual: Idle |
| 139 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet5 | FAIL | Port: Ethernet6 Neighbor: spine4.atd.lab Neighbor Port: Ethernet5 - No LLDP neighbors |
| 147 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | FAIL | Host: 192.168.101.14 Source: 192.168.101.3 VRF: default - Packet loss detected - Transmitted: 1 Received: 0 |
| 151 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.23) - Destination: spine4 Ethernet5 (IP: 192.168.103.22) | FAIL | Ping command 'ping vrf default 192.168.103.22 source 192.168.103.23 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 161 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet5 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |
| 179 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | FAIL | The following route(s) are missing from the routing table of VRF default: 192.168.101.14 |
| 190 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | FAIL | AFI: evpn Peer: 192.168.101.14 - Incorrect session state - Expected: Established Actual: Active |
| 195 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.30) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.30 - Incorrect session state - Expected: Established Actual: Idle |
| 201 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet6 | FAIL | Port: Ethernet6 Neighbor: spine4.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 209 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | FAIL | Host: 192.168.101.14 Source: 192.168.101.4 VRF: default - Packet loss detected - Transmitted: 1 Received: 0 |
| 213 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.31) - Destination: spine4 Ethernet6 (IP: 192.168.103.30) | FAIL | Ping command 'ping vrf default 192.168.103.30 source 192.168.103.31 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 223 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet6 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |
| 242 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | FAIL | The following route(s) are missing from the routing table of VRF default: 192.168.101.14 |
| 336 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | FAIL | AFI: evpn Peer: 192.168.101.3 - Incorrect session state - Expected: Established Actual: Active |
| 337 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | FAIL | AFI: evpn Peer: 192.168.101.4 - Incorrect session state - Expected: Established Actual: Active |
| 340 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.23) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.23 - Incorrect session state - Expected: Established Actual: Idle |
| 341 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.31) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.31 - Incorrect session state - Expected: Established Actual: Idle |
| 344 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet6 | FAIL | Port: Ethernet5 Neighbor: leaf3.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 345 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet6 | FAIL | Port: Ethernet6 Neighbor: leaf4.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 348 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.22) - Destination: leaf3 Ethernet6 (IP: 192.168.103.23) | FAIL | Ping command 'ping vrf default 192.168.103.23 source 192.168.103.22 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 349 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.30) - Destination: leaf4 Ethernet6 (IP: 192.168.103.31) | FAIL | Ping command 'ping vrf default 192.168.103.31 source 192.168.103.30 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 356 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet6 = 'up' | FAIL | Ethernet5 - Status mismatch - Expected: up/up, Actual: down/down |
| 357 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet6 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |

## All Test Results

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 1 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 2 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 3 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 4 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | PASS | - |
| 5 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 10.255.251.1) | PASS | - |
| 6 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.0) | PASS | - |
| 7 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.2) | PASS | - |
| 8 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.4) | PASS | - |
| 9 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.6) | PASS | - |
| 10 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf2 Ethernet1 | PASS | - |
| 11 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf2 Ethernet2 | PASS | - |
| 12 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet3 | PASS | - |
| 13 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet3 | PASS | - |
| 14 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet3 | PASS | - |
| 15 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet3 | PASS | - |
| 16 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 17 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 18 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 19 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 20 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 21 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 22 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 23 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | PASS | - |
| 24 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.1) - Destination: spine1 Ethernet3 (IP: 192.168.103.0) | PASS | - |
| 25 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.3) - Destination: spine2 Ethernet3 (IP: 192.168.103.2) | PASS | - |
| 26 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.5) - Destination: spine3 Ethernet3 (IP: 192.168.103.4) | PASS | - |
| 27 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.7) - Destination: spine4 Ethernet3 (IP: 192.168.103.6) | PASS | - |
| 28 | leaf1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 29 | leaf1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 30 | leaf1 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 31 | leaf1 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 32 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf2_Ethernet1 = 'up' | PASS | - |
| 33 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf2_Ethernet2 = 'up' | PASS | - |
| 34 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet3 = 'up' | PASS | - |
| 35 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet3 = 'up' | PASS | - |
| 36 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet3 = 'up' | PASS | - |
| 37 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet3 = 'up' | PASS | - |
| 38 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host1_Ethernet1 = 'up' | PASS | - |
| 39 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 40 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 41 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf2_Port-Channel1 = 'up' | PASS | - |
| 42 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host1 = 'up' | PASS | - |
| 43 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 44 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 45 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 46 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 47 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 48 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 49 | leaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 50 | leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 51 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 52 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 53 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 54 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 55 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | PASS | - |
| 56 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 57 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 58 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 59 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 60 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 61 | leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 62 | leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 63 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 64 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 65 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 66 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | PASS | - |
| 67 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 10.255.251.0) | PASS | - |
| 68 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.8) | PASS | - |
| 69 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.10) | PASS | - |
| 70 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.12) | PASS | - |
| 71 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.14) | PASS | - |
| 72 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf1 Ethernet1 | PASS | - |
| 73 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf1 Ethernet2 | PASS | - |
| 74 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet4 | PASS | - |
| 75 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet4 | PASS | - |
| 76 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet4 | PASS | - |
| 77 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet4 | PASS | - |
| 78 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 79 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 80 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 81 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 82 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 83 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 84 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 85 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | PASS | - |
| 86 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.9) - Destination: spine1 Ethernet4 (IP: 192.168.103.8) | PASS | - |
| 87 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.11) - Destination: spine2 Ethernet4 (IP: 192.168.103.10) | PASS | - |
| 88 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.13) - Destination: spine3 Ethernet4 (IP: 192.168.103.12) | PASS | - |
| 89 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.15) - Destination: spine4 Ethernet4 (IP: 192.168.103.14) | PASS | - |
| 90 | leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 91 | leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 92 | leaf2 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 93 | leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 94 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf1_Ethernet1 = 'up' | PASS | - |
| 95 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf1_Ethernet2 = 'up' | PASS | - |
| 96 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet4 = 'up' | PASS | - |
| 97 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet4 = 'up' | PASS | - |
| 98 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet4 = 'up' | PASS | - |
| 99 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet4 = 'up' | PASS | - |
| 100 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host1_Ethernet2 = 'up' | PASS | - |
| 101 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 102 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 103 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf1_Port-Channel1 = 'up' | PASS | - |
| 104 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host1 = 'up' | PASS | - |
| 105 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 106 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 107 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 108 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 109 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 110 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 111 | leaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 112 | leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 113 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 114 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 115 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 116 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 117 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | PASS | - |
| 118 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 119 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 120 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 121 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 122 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 123 | leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 124 | leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 125 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 126 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 127 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 128 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | FAIL | AFI: evpn Peer: 192.168.101.14 - Incorrect session state - Expected: Established Actual: Active |
| 129 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 10.255.251.5) | PASS | - |
| 130 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.16) | PASS | - |
| 131 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.18) | PASS | - |
| 132 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.20) | PASS | - |
| 133 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.22) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.22 - Incorrect session state - Expected: Established Actual: Idle |
| 134 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf4 Ethernet1 | PASS | - |
| 135 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf4 Ethernet2 | PASS | - |
| 136 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet5 | PASS | - |
| 137 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet5 | PASS | - |
| 138 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet5 | PASS | - |
| 139 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet5 | FAIL | Port: Ethernet6 Neighbor: spine4.atd.lab Neighbor Port: Ethernet5 - No LLDP neighbors |
| 140 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 141 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 142 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 143 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 144 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 145 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 146 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 147 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | FAIL | Host: 192.168.101.14 Source: 192.168.101.3 VRF: default - Packet loss detected - Transmitted: 1 Received: 0 |
| 148 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.17) - Destination: spine1 Ethernet5 (IP: 192.168.103.16) | PASS | - |
| 149 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.19) - Destination: spine2 Ethernet5 (IP: 192.168.103.18) | PASS | - |
| 150 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.21) - Destination: spine3 Ethernet5 (IP: 192.168.103.20) | PASS | - |
| 151 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.23) - Destination: spine4 Ethernet5 (IP: 192.168.103.22) | FAIL | Ping command 'ping vrf default 192.168.103.22 source 192.168.103.23 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 152 | leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 153 | leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 154 | leaf3 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 155 | leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 156 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf4_Ethernet1 = 'up' | PASS | - |
| 157 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf4_Ethernet2 = 'up' | PASS | - |
| 158 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet5 = 'up' | PASS | - |
| 159 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet5 = 'up' | PASS | - |
| 160 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet5 = 'up' | PASS | - |
| 161 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet5 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |
| 162 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host3_Ethernet1 = 'up' | PASS | - |
| 163 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 164 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 165 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf4_Port-Channel1 = 'up' | PASS | - |
| 166 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host3 = 'up' | PASS | - |
| 167 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 168 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 169 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 170 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 171 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 172 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 173 | leaf3 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 174 | leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 175 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 176 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 177 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 178 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 179 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | FAIL | The following route(s) are missing from the routing table of VRF default: 192.168.101.14 |
| 180 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 181 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 182 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 183 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 184 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 185 | leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 186 | leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 187 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 188 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 189 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 190 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine4 (IP: 192.168.101.14) | FAIL | AFI: evpn Peer: 192.168.101.14 - Incorrect session state - Expected: Established Actual: Active |
| 191 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 10.255.251.4) | PASS | - |
| 192 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.24) | PASS | - |
| 193 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.26) | PASS | - |
| 194 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.28) | PASS | - |
| 195 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine4 (IP: 192.168.103.30) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.30 - Incorrect session state - Expected: Established Actual: Idle |
| 196 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf3 Ethernet1 | PASS | - |
| 197 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf3 Ethernet2 | PASS | - |
| 198 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet6 | PASS | - |
| 199 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet6 | PASS | - |
| 200 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet6 | PASS | - |
| 201 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: spine4 Ethernet6 | FAIL | Port: Ethernet6 Neighbor: spine4.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 202 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 203 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 204 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 205 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 206 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 207 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 208 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 209 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine4 Loopback0 (IP: 192.168.101.14) | FAIL | Host: 192.168.101.14 Source: 192.168.101.4 VRF: default - Packet loss detected - Transmitted: 1 Received: 0 |
| 210 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.25) - Destination: spine1 Ethernet6 (IP: 192.168.103.24) | PASS | - |
| 211 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.27) - Destination: spine2 Ethernet6 (IP: 192.168.103.26) | PASS | - |
| 212 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.29) - Destination: spine3 Ethernet6 (IP: 192.168.103.28) | PASS | - |
| 213 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.31) - Destination: spine4 Ethernet6 (IP: 192.168.103.30) | FAIL | Ping command 'ping vrf default 192.168.103.30 source 192.168.103.31 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 214 | leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 215 | leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 216 | leaf4 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 217 | leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 218 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf3_Ethernet1 = 'up' | PASS | - |
| 219 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf3_Ethernet2 = 'up' | PASS | - |
| 220 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet6 = 'up' | PASS | - |
| 221 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet6 = 'up' | PASS | - |
| 222 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet6 = 'up' | PASS | - |
| 223 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_spine4_Ethernet6 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |
| 224 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host3_Ethernet2 = 'up' | PASS | - |
| 225 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet9 = 'up' | PASS | - |
| 226 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 227 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 228 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf3_Port-Channel1 = 'up' | PASS | - |
| 229 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host3 = 'up' | PASS | - |
| 230 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 231 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 232 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 233 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 234 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 235 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 236 | leaf4 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 237 | leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 238 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 239 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 240 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 241 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 242 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.14 - Peer: spine4 | FAIL | The following route(s) are missing from the routing table of VRF default: 192.168.101.14 |
| 243 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 244 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 245 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 246 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 247 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 248 | leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 249 | leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 250 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 251 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 252 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 253 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 254 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.1) | PASS | - |
| 255 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.9) | PASS | - |
| 256 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.17) | PASS | - |
| 257 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.25) | PASS | - |
| 258 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet3 | PASS | - |
| 259 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet3 | PASS | - |
| 260 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet3 | PASS | - |
| 261 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet3 | PASS | - |
| 262 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.0) - Destination: leaf1 Ethernet3 (IP: 192.168.103.1) | PASS | - |
| 263 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.8) - Destination: leaf2 Ethernet3 (IP: 192.168.103.9) | PASS | - |
| 264 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.16) - Destination: leaf3 Ethernet3 (IP: 192.168.103.17) | PASS | - |
| 265 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.24) - Destination: leaf4 Ethernet3 (IP: 192.168.103.25) | PASS | - |
| 266 | spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 267 | spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 268 | spine1 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 269 | spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 270 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet3 = 'up' | PASS | - |
| 271 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet3 = 'up' | PASS | - |
| 272 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet3 = 'up' | PASS | - |
| 273 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet3 = 'up' | PASS | - |
| 274 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 275 | spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 276 | spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 277 | spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 278 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 279 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 280 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 281 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 282 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.3) | PASS | - |
| 283 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.11) | PASS | - |
| 284 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.19) | PASS | - |
| 285 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.27) | PASS | - |
| 286 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet4 | PASS | - |
| 287 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet4 | PASS | - |
| 288 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet4 | PASS | - |
| 289 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet4 | PASS | - |
| 290 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.2) - Destination: leaf1 Ethernet4 (IP: 192.168.103.3) | PASS | - |
| 291 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.10) - Destination: leaf2 Ethernet4 (IP: 192.168.103.11) | PASS | - |
| 292 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.18) - Destination: leaf3 Ethernet4 (IP: 192.168.103.19) | PASS | - |
| 293 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.26) - Destination: leaf4 Ethernet4 (IP: 192.168.103.27) | PASS | - |
| 294 | spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 295 | spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 296 | spine2 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 297 | spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 298 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet4 = 'up' | PASS | - |
| 299 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet4 = 'up' | PASS | - |
| 300 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet4 = 'up' | PASS | - |
| 301 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet4 = 'up' | PASS | - |
| 302 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 303 | spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 304 | spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 305 | spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 306 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 307 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 308 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 309 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 310 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.5) | PASS | - |
| 311 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.13) | PASS | - |
| 312 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.21) | PASS | - |
| 313 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.29) | PASS | - |
| 314 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet5 | PASS | - |
| 315 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet5 | PASS | - |
| 316 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet5 | PASS | - |
| 317 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet5 | PASS | - |
| 318 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.4) - Destination: leaf1 Ethernet5 (IP: 192.168.103.5) | PASS | - |
| 319 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.12) - Destination: leaf2 Ethernet5 (IP: 192.168.103.13) | PASS | - |
| 320 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.20) - Destination: leaf3 Ethernet5 (IP: 192.168.103.21) | PASS | - |
| 321 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.28) - Destination: leaf4 Ethernet5 (IP: 192.168.103.29) | PASS | - |
| 322 | spine3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 323 | spine3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 324 | spine3 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 325 | spine3 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 326 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet5 = 'up' | PASS | - |
| 327 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet5 = 'up' | PASS | - |
| 328 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet5 = 'up' | PASS | - |
| 329 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet5 = 'up' | PASS | - |
| 330 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 331 | spine3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 332 | spine3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 333 | spine3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 334 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 335 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 336 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | FAIL | AFI: evpn Peer: 192.168.101.3 - Incorrect session state - Expected: Established Actual: Active |
| 337 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | FAIL | AFI: evpn Peer: 192.168.101.4 - Incorrect session state - Expected: Established Actual: Active |
| 338 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.7) | PASS | - |
| 339 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.15) | PASS | - |
| 340 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.23) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.23 - Incorrect session state - Expected: Established Actual: Idle |
| 341 | spine4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.31) | FAIL | AFI: ipv4 SAFI: unicast VRF: default Peer: 192.168.103.31 - Incorrect session state - Expected: Established Actual: Idle |
| 342 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet6 | PASS | - |
| 343 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet6 | PASS | - |
| 344 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet6 | FAIL | Port: Ethernet5 Neighbor: leaf3.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 345 | spine4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet6 | FAIL | Port: Ethernet6 Neighbor: leaf4.atd.lab Neighbor Port: Ethernet6 - No LLDP neighbors |
| 346 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.6) - Destination: leaf1 Ethernet6 (IP: 192.168.103.7) | PASS | - |
| 347 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.14) - Destination: leaf2 Ethernet6 (IP: 192.168.103.15) | PASS | - |
| 348 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.22) - Destination: leaf3 Ethernet6 (IP: 192.168.103.23) | FAIL | Ping command 'ping vrf default 192.168.103.23 source 192.168.103.22 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 349 | spine4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.30) - Destination: leaf4 Ethernet6 (IP: 192.168.103.31) | FAIL | Ping command 'ping vrf default 192.168.103.31 source 192.168.103.30 size 100 repeat 1' failed with an unexpected message: 'ping: bind: Cannot assign requested address' |
| 350 | spine4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 351 | spine4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 352 | spine4 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 353 | spine4 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 354 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet6 = 'up' | PASS | - |
| 355 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet6 = 'up' | PASS | - |
| 356 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet6 = 'up' | FAIL | Ethernet5 - Status mismatch - Expected: up/up, Actual: down/down |
| 357 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet6 = 'up' | FAIL | Ethernet6 - Status mismatch - Expected: up/up, Actual: down/down |
| 358 | spine4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 359 | spine4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 360 | spine4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 361 | spine4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
